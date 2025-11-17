import subprocess
import re
import platform
import time

def run_cmd(cmd):
    """Chạy lệnh hệ thống và trả về output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            return result.stdout
        else:
            print(f"[LỖI] Lệnh '{cmd}' thất bại.")
            return None
    except subprocess.TimeoutExpired:
        print(f"[LỖI] Lệnh '{cmd}' timeout.")
        return None

def get_network_interfaces_subprocess():
    """Lấy danh sách card mạng và địa chỉ IP"""
    system = platform.system()
    print("=== DANH SÁCH CARD MẠNG ===")
    
    if system == "Windows":
        output = run_cmd("ipconfig /all")
        if not output:
            return
        # Parse IP, MAC, interface name
        sections = re.split(r'\n\s*\n', output)
        for section in sections:
            if "adapter" in section.lower() or "card" in section.lower():
                name_match = re.search(r'^[A-Za-z0-9\s.-]+', section, re.MULTILINE)
                if name_match:
                    name = name_match.group().strip()
                    print(f"\n--- Interface: {name} ---")
                    ipv4_match = re.search(r'IPv4 Address[.\s:]*([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', section)
                    if ipv4_match:
                        print(f"  IPv4: {ipv4_match.group(1)}")
                    mac_match = re.search(r'Physical Address[.\s:]*([0-9A-Fa-f:-]{17})', section)
                    if mac_match:
                        print(f"  MAC: {mac_match.group(1)}")

    elif system in ("Linux", "Darwin"):  # Darwin là macOS
        output = run_cmd("ifconfig")
        if not output:
            return
        # Tách theo interface name
        interfaces = re.split(r'\n(?=\w)', output)
        for iface in interfaces:
            name_match = re.match(r'^(\w+):', iface)
            if name_match:
                name = name_match.group(1)
                print(f"\n--- Interface: {name} ---")
                ipv4_match = re.search(r'inet ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', iface)
                if ipv4_match:
                    print(f"  IPv4: {ipv4_match.group(1)}")
                mac_match = re.search(r'ether ([0-9a-f:]{17})', iface)
                if mac_match:
                    print(f"  MAC: {mac_match.group(1)}")

def get_gateway_subprocess():
    """Lấy gateway mặc định"""
    system = platform.system()
    print("\n=== GATEWAY MẶC ĐỊNH ===")
    
    if system == "Windows":
        output = run_cmd("route print")
        if not output:
            return
        for line in output.splitlines():
            if "0.0.0.0" in line and "0.0.0.0" in line.split():
                gateway = line.split()[2]
                print(f"Gateway: {gateway}")
                break
    elif system in ("Linux", "Darwin"):
        output = run_cmd("ip route")
        if not output:
            return
        for line in output.splitlines():
            if "default via" in line:
                gateway = line.split()[2]
                print(f"Gateway: {gateway}")
                break

def get_public_ip_subprocess():
    """Lấy IP công khai bằng curl hoặc requests (nếu có)"""
    print("\n=== IP CÔNG KHAI ===")
    try:
        import requests
        response = requests.get('https://httpbin.org/ip', timeout=5)
        ip = response.json()['origin']
        print(f"Public IP: {ip}")
    except ImportError:
        # Dùng curl nếu có
        output = run_cmd("curl -s https://httpbin.org/ip")
        if output:
            match = re.search(r'"origin": "([^"]+)"', output)
            if match:
                print(f"Public IP: {match.group(1)}")
    except Exception:
        print("Không thể lấy IP công khai.")

def get_active_connections_subprocess():
    """Lấy các kết nối mạng đang mở"""
    system = platform.system()
    print("\n=== KẾT NỐI MẠNG ĐANG MỞ ===")
    
    if system == "Windows":
        output = run_cmd("netstat -an")
    elif system in ("Linux", "Darwin"):
        output = run_cmd("netstat -an")
    else:
        print("Hệ điều hành không hỗ trợ.")
        return

    if not output:
        return

    for line in output.splitlines():
        if "ESTABLISHED" in line:
            parts = line.split()
            if len(parts) >= 5:
                local = parts[3]
                remote = parts[4]
                print(f"  {local} -> {remote}")

def get_bandwidth_linux():
    """Tính băng thông (chỉ Linux hỗ trợ /proc/net/dev)"""
    if platform.system() != "Linux":
        print("\n=== BĂNG THÔNG (chỉ hỗ trợ Linux) ===")
        print("Chỉ hỗ trợ trên Linux.")
        return

    print("\n=== BĂNG THÔNG (ước lượng trong 1s) ===")
    def get_bytes():
        with open('/proc/net/dev', 'r') as f:
            lines = f.readlines()
        for line in lines[2:]:
            if 'eth0' in line or 'wlan0' in line or 'enp' in line or 'wlp' in line:
                fields = line.split()
                rx_bytes = int(fields[1])
                tx_bytes = int(fields[9])
                return rx_bytes, tx_bytes
        return 0, 0

    rx1, tx1 = get_bytes()
    time.sleep(1)
    rx2, tx2 = get_bytes()

    rx_speed = (rx2 - rx1) / 1024 / 1024  # MB/s
    tx_speed = (tx2 - tx1) / 1024 / 1024  # MB/s

    print(f"Download: {rx_speed:.2f} MB/s")
    print(f"Upload: {tx_speed:.2f} MB/s")

def main():
    print("=== SCRIPT LẤY THÔNG TIN MẠNG BẰNG SUBPROCESS ===")
    get_network_interfaces_subprocess()
    get_gateway_subprocess()
    get_public_ip_subprocess()
    get_active_connections_subprocess()
    get_bandwidth_linux()

if __name__ == "__main__":
    main()