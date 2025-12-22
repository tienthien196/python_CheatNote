# import PyPDF2

thuc_an = ["a", "b", "c"]

print(a:=",".join(thuc_an))
print(a.split(","))

def lay_10_trang_dau(ten_file_pdf):
    """
    Hàm lấy và in ra nội dung của 10 trang đầu tiên của một file PDF.

    Args:
        ten_file_pdf (str): Đường dẫn đến file PDF.
    """
    try:
        with open(ten_file_pdf, 'rb') as file_pdf: # Mở file ở chế độ đọc nhị phân
            doc_reader = PyPDF2.PdfReader(file_pdf)

            so_trang = len(doc_reader.pages)
            print(f"Số trang trong file PDF: {so_trang}\n")

            so_trang_muon_doc = min(10, so_trang) # Lấy tối đa 10 trang hoặc số trang có nếu ít hơn 10

            for i in range(so_trang_muon_doc):
                trang = doc_reader.pages[i]
                noi_dung_trang = trang.extract_text()

                print(f"--- Nội dung trang {i+1} ---")
                print(noi_dung_trang)
                print("\n" + "="*50 + "\n") # Dấu phân cách giữa các trang

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {ten_file_pdf}")
    except PyPDF2.PdfReadError:
        print("Lỗi: Không thể đọc file PDF. Có thể file bị lỗi hoặc được bảo vệ mật khẩu.")
    except Exception as e:
        print(f"Đã xảy ra lỗi không mong muốn: {e}")

# --- Sử dụng hàm ---
# Thay 'duong_dan_den_file.pdf' bằng đường dẫn thực tế đến file PDF của bạn
# ten_file = r"E:\DATA\test_project\___.pdf"
# lay_10_trang_dau(ten_file)