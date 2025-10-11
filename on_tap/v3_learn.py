#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
decode_full_ajaxData.py
Hỗ trợ:
- Đọc từ stdin (dán tay) HOẶC từ file
- Xử lý ajaxData = { ... };
- Trích xuất đáp án theo thứ tự RESPONSE0, RESPONSE1, ...
"""

import re
import json
import html
import pathlib
import sys
import xml.etree.ElementTree as ET

# --- Cấu hình ---
READ_FROM_FILE = True
JSON_FILE = r"E:\1_test_Src\src\python\python_cheat\on_tap\v2.json"

def decode_unicode_escape(text: str) -> str:
    """Giải mã \\u003c -> <, xử lý cả \\u2019 -> ' """
    try:
        return text.encode('utf-8').decode('unicode_escape').replace('\r\n', '\n')
    except:
        return text.replace('\r\n', '\n')

def extract_answers_from_xml(xml_content: str):
    """
    Trích xuất đáp án từ XML QTI, giữ nguyên thứ tự theo responseDeclaration
    Trả về list: ["đáp án 0", "đáp án 1", ...]
    Mỗi đáp án có thể là "A / B / C" nếu có nhiều giá trị
    """
    try:
        # Gỡ bỏ khai báo XML nếu cần (ElementTree không thích có nhiều root)
        if xml_content.lstrip().startswith('<?xml'):
            # Tìm thẻ root đầu tiên
            start = xml_content.find('<assessmentItem')
            if start == -1:
                start = xml_content.find('<')
            xml_content = xml_content[start:]

        root = ET.fromstring(xml_content)
        answers = []

        # Namespace (nếu có)
        ns = {'qti': 'http://www.imsglobal.org/xsd/imsqti_v2p2'}

        # Tìm tất cả responseDeclaration theo thứ tự
        for resp_decl in root.findall('.//qti:responseDeclaration', ns):
            identifier = resp_decl.get('identifier', '')
            correct_resp = resp_decl.find('.//qti:correctResponse', ns)
            if correct_resp is None:
                answers.append("(no answer)")
                continue

            values = []
            for val in correct_resp.findall('.//qti:value', ns):
                text = val.text or ''
                clean_text = html.unescape(text.strip())
                values.append(clean_text)

            if values:
                answers.append(" / ".join(values))
            else:
                answers.append("(empty)")

        return answers

    except ET.ParseError as e:
        print(f"⚠️ Lỗi parse XML: {e}")
        # Fallback: dùng regex (ít tin cậy)
        answers = []
        cr_blocks = re.findall(r'<responseDeclaration[^>]*>.*?<correctResponse>(.*?)</correctResponse>', xml_content, re.S)
        for block in cr_blocks:
            values = re.findall(r'<value>(.*?)</value>', block, re.S)
            clean_vals = [html.unescape(v.strip()) for v in values]
            answers.append(" / ".join(clean_vals) if clean_vals else "(empty)")
        return answers

def main():
    if READ_FROM_FILE:
        print(f"📂 Đọc từ file: {JSON_FILE}")
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            raw = f.read().strip()
    else:
        print("📌 Dán đoạn ajaxData = { ... }; vào, kết thúc bằng Ctrl+D (Linux/Mac) hoặc Ctrl+Z (Win):")
        raw = sys.stdin.read().strip()

    # Loại bỏ ajaxData = ... ; nếu có
    if raw.startswith('ajaxData'):
        raw = re.sub(r'^\s*ajaxData\s*=\s*', '', raw)
        raw = re.sub(r';\s*$', '', raw)

    data = json.loads(raw)

    for key, xml_raw in data.items():
        if not key.endswith('.xml'):
            continue

        xml_clean = decode_unicode_escape(xml_raw)
        out_file = pathlib.Path(key)
        out_file.write_text(xml_clean, encoding='utf-8')
        print(f"\n✅ Đã lưu XML → {out_file}")

        answers = extract_answers_from_xml(xml_clean)
        print(f"📋 Đáp án ({len(answers)} câu) trong {key}:")
        for idx, ans in enumerate(answers):
            print(f"  {idx:>2}. {ans}")

if __name__ == '__main__':
    main()