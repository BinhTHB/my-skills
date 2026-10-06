---
name: ptit-academic-writing
description: Kỹ năng soạn thảo báo cáo Bài tập lớn, Tiểu luận, Đồ án ngành và Khóa luận PTIT với thể thức chuẩn chỉnh 100% (trang bìa, căn lề, IEEE), nhưng nội dung hành văn tự nhiên đúng tầm sinh viên đại học (chân thực, tập trung thực hành, có sạn tự nhiên, không đao to búa lớn).
license: MIT
metadata:
  category: "academic-writing"
  tags: "PTIT, Academic Writing, Report, Student Level, Realistic, Word DOCX"
---

# Kỹ năng Soạn thảo Báo cáo Học thuật PTIT (Tầm Sinh viên Thực tế)

Kỹ năng này đảm bảo sự cân bằng hoàn hảo giữa:
1. **Hình thức & Thể thức:** Chuẩn xác 100% theo quy chế văn bản PTIT (khung hoa văn, Logo, căn lề, Header/Footer, trích dẫn IEEE, bảng biểu/hình vẽ).
2. **Nội dung & Văn phong:** Đúng tầm sinh viên đại học năm 3, năm 4 làm đồ án thực tế: mộc mạc, trực diện vào mã nguồn và dữ liệu thực, chấp nhận các hạn chế và "sạn tự nhiên" của bài tập lớn, không hoa mỹ kiểu bài báo quốc tế hay văn phong AI hoàn hảo.

---

## 1. Bản đồ Tham chiếu Tài liệu (Reference Index)

| Tác vụ / Nghiệp vụ | Tài liệu Tham chiếu |
| :--- | :--- |
| **Quy chuẩn Thể thức & Trang in PTIT** (Căn lề, cỡ chữ 13pt, trang bìa hoa văn, Logo, Caption) | `references/ptit-standards.md` |
| **Văn phong Sinh viên & Sạn Tự nhiên** (Cách viết chân thực, tránh văn phong AI giáo sư, tả lỗi thật) | `references/anti-ai-academic-tone.md` |
| **Khung Cấu trúc Báo cáo theo Đề tài** (BTL Dữ liệu, Đồ án Web/App, Nghiên cứu AI/Thuật toán) | `references/report-types-structure.md` |
| **Cẩm nang Trích dẫn Chuẩn IEEE** (Quy tắc đánh số [1], [2]... khớp nội văn) | `references/ieee-citation-guide.md` |
| **Kịch bản Tự động Xuất DOCX** (Code Python `python-docx` tạo file Word chuẩn ngay lập tức) | `references/docx-generator-script.md` |

---

## 2. Các Nguyên tắc Soạn thảo Cốt lõi

### A. Hình thức Chuẩn chỉnh (Nghiêm ngặt)
- Trang bìa có khung viền hoa văn (`assets/Khung.png`) và Logo PTIT (`assets/Logo.png`).
- Căn lề: Trái 3.0–3.5 cm (đóng gáy), Phải 1.5–2.0 cm, Trên/Dưới 2.0–2.5 cm.
- Phông chữ Times New Roman 13 pt (hoặc 14 pt), giãn dòng 1.3–1.5 lines.
- Đánh số trang: Chữ số La Mã (`i, ii...`) cho phần đầu; Số Arab (`1, 2...`) từ Mở đầu đến hết.
- Caption: Tiêu đề Bảng ở **TRÊN**, tiêu đề Hình ở **DƯỚI**.

### B. Nội dung Đúng Tầm Sinh viên Đại học (Chân thực & Tự nhiên)
- **Tập trung vào giải pháp thực hành:** Mô tả cụ thể đã dùng thư viện gì (Pandas, BeautifulSoup, Express, Flutter...), viết hàm xử lý nào, gặp khó khăn gì khi triển khai và đã xử lý ra sao.
- **Tránh từ ngữ đao to búa lớn:** Không dùng các cụm từ sáo rỗng như *"cuộc cách mạng công nghiệp 4.0", "giải pháp tối thượng", "đột phá vượt bậc"*.
- **Số liệu & Môi trường thực tế:** Báo cáo trên môi trường máy cá nhân thực tế (Laptop Core i5/i7, 8GB-16GB RAM), dữ liệu vài nghìn đến vài chục nghìn dòng, thời gian xử lý thực tế vài giây đến vài phút.
- **Thừa nhận hạn chế một cách trung thực:** Nêu rõ những điểm đồ án chưa làm được (ví dụ: giao diện còn đơn giản, chưa xử lý được dữ liệu realtime quy mô lớn, thuật toán chỉ chạy trên tập mẫu nhỏ).

---

## 3. Quy trình 5 Bước Xuất Báo cáo

1. **Lập dàn ý (Outline):** Phân chia đề tài thành Mở đầu, 4 Chương kỹ thuật và Kết luận theo `references/report-types-structure.md`.
2. **Viết nội dung kỹ thuật:** Viết theo giọng văn sinh viên thực tế tại `references/anti-ai-academic-tone.md`.
3. **Chèn Hình vẽ, Bảng biểu & Mã nguồn:** Bổ sung ảnh chụp màn hình chạy thử, biểu đồ thực nghiệm, bảng dữ liệu mẫu có đánh số chương.
4. **Gắn mã trích dẫn IEEE:** Thêm các nguồn tài liệu tham khảo chính thống bằng mã `[1]`, `[2]`...
5. **Xuất file Word DOCX:** Chạy script `ptit_docx_builder.py` để đóng gói file báo cáo hoàn chỉnh nộp giảng viên.