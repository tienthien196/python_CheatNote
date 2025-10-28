#!/usr/bin/env python3
import os
import sys
import socket
import datetime
import time
import psutil
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from collections import deque

# Cấu hình
LOG_FILE = "networkinfo.log"
DATA_FILE = "network_data.json"
PING_HOST = "8.8.8.8"
PING_PORT = 53
PING_TIMEOUT = 3
UPDATE_DELAY = 1  # giây

# Dữ liệu sẽ được lưu theo thời gian
network_history = []
bandwidth_history = deque(maxlen=60)  # Giữ 60s gần nhất

def ping():
    try:
        socket.setdefaulttimeout(PING_TIMEOUT)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((PING_HOST, PING_PORT))
        s.close()
        return True
    except (OSError, socket.timeout):
        return False

def load_history():
    global network_history, bandwidth_history
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
                network_history = data.get("network", [])
                # bandwidth_history không load lại để tránh quá tải
        except Exception as e:
            print(f"[!] Lỗi khi tải lịch sử: {e}")

def save_history():
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump({"network": network_history}, f, indent=2, default=str)
    except Exception as e:
        print(f"[!] Lỗi khi lưu lịch sử: {e}")

def log_event(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
    print(message)

def plot_uptime():
    if not network_history:
        print("[!] Không có dữ liệu để vẽ biểu đồ.")
        return

    times = [datetime.datetime.fromisoformat(item["time"]) for item in network_history]
    statuses = [1 if item["status"] == "up" else 0 for item in network_history]

    plt.figure(figsize=(12, 4))
    plt.step(times, statuses, where='post', color='green', linewidth=2)
    plt.fill_between(times, statuses, step='post', color='lightgreen', alpha=0.5)
    plt.ylim(-0.1, 1.1)
    plt.yticks([0, 1], ["Offline", "Online"])
    plt.title("Trạng thái kết nối Internet")
    plt.xlabel("Thời gian")
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.show()

def plot_bandwidth():
    if len(bandwidth_history) < 2:
        print("[!] Chưa đủ dữ liệu băng thông để vẽ.")
        return

    times = [item["time"] for item in bandwidth_history]
    upload = [item["upload_speed"] for item in bandwidth_history]
    download = [item["download_speed"] for item in bandwidth_history]

    plt.figure(figsize=(12, 5))
    plt.plot(times, download, label="Download", color="blue", marker='o', markersize=3)
    plt.plot(times, upload, label="Upload", color="orange", marker='o', markersize=3)
    plt.title("Tốc độ mạng theo thời gian (Bytes/s)")
    plt.xlabel("Thời gian")
    plt.ylabel("Tốc độ (Bytes/s)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.show()

def main():
    load_history()
    log_event("🟢 Bắt đầu giám sát mạng...")

    # Kiểm tra kết nối ban đầu
    last_status = "up" if ping() else "down"
    if last_status == "down":
        down_time = datetime.datetime.now()
        log_event("🔴 Mất kết nối ban đầu.")

    io = psutil.net_io_counters()
    bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv

    try:
        while True:
            current_time = datetime.datetime.now()
            is_up = ping()

            # Ghi nhận thay đổi trạng thái
            if is_up and last_status == "down":
                downtime_duration = current_time - down_time
                log_event(f"🟢 Kết nối khôi phục! Mất mạng trong {downtime_duration}")
                network_history.append({
                    "time": current_time.isoformat(),
                    "status": "up",
                    "downtime_seconds": downtime_duration.total_seconds()
                })
                last_status = "up"
                save_history()

            elif not is_up and last_status == "up":
                down_time = current_time
                log_event("🔴 Mất kết nối!")
                network_history.append({
                    "time": current_time.isoformat(),
                    "status": "down"
                })
                last_status = "down"
                save_history()

            # Cập nhật băng thông
            io2 = psutil.net_io_counters()
            us = (io2.bytes_sent - bytes_sent) / UPDATE_DELAY
            ds = (io2.bytes_recv - bytes_recv) / UPDATE_DELAY
            bandwidth_history.append({
                "time": current_time,
                "upload_speed": us,
                "download_speed": ds
            })
            bytes_sent, bytes_recv = io2.bytes_sent, io2.bytes_recv

            time.sleep(UPDATE_DELAY)

    except KeyboardInterrupt:
        print("\n[?] Nhấn Ctrl+C lần nữa để vẽ biểu đồ và thoát.")
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\n[+] Đang vẽ biểu đồ...")
            plot_uptime()
            plot_bandwidth()
            log_event("⏹️  Dừng giám sát.")
            save_history()
            sys.exit(0)

if __name__ == "__main__":
    main()