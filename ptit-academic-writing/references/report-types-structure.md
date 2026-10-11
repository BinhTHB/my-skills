# Cấu trúc Báo cáo Học thuật PTIT (Khung Mô-đun Phi Hardcode)

Tài liệu này cung cấp các khung cấu trúc chuẩn hóa nhưng **hoàn toàn linh hoạt (không hardcode)** cho từng loại hình văn bản học thuật tại Học viện Công nghệ Bưu chính Viễn thông (PTIT). Số lượng chương, tên mục và các khối thủ tục phải thích ứng theo đề tài và yêu cầu cụ thể của giảng viên.


> **Khung mẫu tương ứng:** Khung A và B dùng `assets/template_btl.docx` (có thể thêm chương bằng `append`). Khung D dùng `assets/template_do_an.docx`. Khung C dùng `assets/template_tieu_luan.docx`. Thông số trình bày xem `ptit-standards.md`.
---

## 1. Nguyên tắc Cấu trúc Phi Hardcode (Dynamic Modular Rules)

1. **Không có một khung số chương cố định cho mọi báo cáo:**
   - Đề tài đơn giản hoặc bài tập lập trình môn học: **3 chương** là tối ưu, tránh kéo dài lê thê.
   - Đề tài dữ liệu, trực quan hóa, AI hoặc hệ thống đầy đủ: **4 chương** (Tổng quan $\rightarrow$ Thiết kế $\rightarrow$ Cài đặt $\rightarrow$ Thực nghiệm & Đánh giá).
   - Tiểu luận môn học (KNTLVB, PPLNCKH, Triết học, Pháp luật...): Chia theo **3 Phần lớn (Mở đầu – Nội dung – Kết luận)** hoặc các mục La Mã (I, II, III), không bắt buộc gọi là "Chương".
   - Đồ án chuyên ngành / Khóa luận tốt nghiệp: **4 đến 5 chương** với đầy đủ các trang thủ tục pháp lý học viện.

2. **Quy tắc cho Danh mục Bảng biểu & Danh mục Hình vẽ:**
   - **Chỉ thêm khi có từ 2 bảng biểu hoặc 2 hình vẽ trở lên** trong toàn bộ báo cáo.
   - Nếu bài viết chỉ có 1 hình hoặc không có hình vẽ/bảng biểu nào, **loại bỏ hoàn toàn** trang Danh mục này để tránh trang in bị rỗng.

3. **Lời cảm ơn vs Lời cam đoan:**
   - **BTL & Tiểu luận môn học:** Sử dụng *Lời cảm ơn* (xưng "em" chân thành, cảm ơn Thầy/Cô giảng dạy).
   - **Đồ án chuyên ngành & Khóa luận tốt nghiệp:** Bắt buộc có *Lời cam đoan* (cam kết tính trung thực, không sao chép trái phép) trước, sau đó mới đến *Lời cảm ơn*.

---

## 2. Các Khung Cấu trúc Chuẩn theo Loại hình

### Khung A: Bài tập lớn (BTL) 3 Chương (Môn Lập trình, CSDL, Mạng, Ứng dụng)
- **TRANG BÌA CHUẨN PTIT**
- **LỜI CẢM ƠN** (1 trang)
- **DANH MỤC TỪ VIẾT TẮT** (1 trang, Bảng 0.1)
- **MỤC LỤC** (Tab chấm dẫn Dotted Leader, Hyperlink)
- **PHẦN MỞ ĐẦU:**
  1. Tính cấp thiết của đề tài
  2. Mục tiêu và phạm vi
  3. Phương pháp tiếp cận và công cụ thực thi
  4. Bố cục báo cáo
- **CHƯƠNG 1: KHẢO SÁT BÀI TOÁN VÀ CƠ SỞ LÝ THUYẾT:** Nghiệp vụ thực tế, lý thuyết nền tảng, công nghệ sử dụng.
- **CHƯƠNG 2: PHÂN TÍCH YÊU CẦU VÀ THIẾT KẾ HỆ THỐNG:** Yêu cầu chức năng, biểu đồ ca sử dụng (Use Case), thiết kế CSDL (ERD/Schema), thiết kế kiến trúc.
- **CHƯƠNG 3: HIỆN THỰC HÓA, THỰC NGHIỆM VÀ ĐÁNH GIÁ:** Cài đặt mã nguồn, giao diện chương trình, kịch bản kiểm thử, đánh giá kết quả đạt được.
- **KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN:** Kết quả hoàn thành, các hạn chế còn tồn đọng, hướng nâng cấp.
- **TÀI LIỆU THAM KHẢO** (Chuẩn IEEE)

---

### Khung B: Bài tập lớn (BTL) 4 Chương (Môn Trực quan hóa dữ liệu, Khoa học dữ liệu, AI)
- **TRANG BÌA CHUẨN PTIT**
- **LỜI CẢM ƠN**
- **DANH MỤC THUẬT NGỮ VÀ TỪ VIẾT TẮT**
- **MỤC LỤC**
- **DANH MỤC BẢNG BIỂU & HÌNH VẼ** (Nếu có từ 2 bảng/hình trở lên)
- **PHẦN MỞ ĐẦU:** Tính cấp thiết, mục tiêu, đối tượng dữ liệu, công cụ phân tích, bố cục.
- **CHƯƠNG 1: TỔNG QUAN BÀI TOÁN VÀ CƠ SỞ LÝ THUYẾT:** Khảo sát bài toán thị trường, lý thuyết ETL, nguyên tắc trực quan hóa dữ liệu.
- **CHƯƠNG 2: PHÂN TÍCH VÀ THIẾT KẾ ĐƯỜNG ỐNG DỮ LIỆU:** Sơ đồ pipeline, cấu trúc từ điển dữ liệu (Data Dictionary), tiêu chí làm sạch.
- **CHƯƠNG 3: HIỆN THỰC HÓA ĐƯỜNG ỐNG THU THẬP VÀ XỬ LÝ:** Code cào dữ liệu (Scraping/API), làm sạch dữ liệu khuyết/ngoại lai, ghép nối dữ liệu (pd.merge).
- **CHƯƠNG 4: THỰC NGHIỆM TRỰC QUAN HÓA VÀ ĐÁNH GIÁ THỊ TRƯỜNG:** Trả lời bộ câu hỏi phân tích, biểu đồ trực quan (Dashboard/Charts), nhận xét insight.
- **KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN:** Kết quả định lượng, hạn chế máy cá nhân, hướng mở rộng.
- **TÀI LIỆU THAM KHẢO** (Chuẩn IEEE)

---

### Khung C: Tiểu luận Môn học (3 Phần lớn - Không chia chương)
- **TRANG BÌA CHUẨN PTIT** (Ghi rõ: TIỂU LUẬN HỌC PHẦN...)
- **MỤC LỤC**
- **PHẦN 1: MỞ ĐẦU / ĐẶT VẤN ĐỀ:**
  - 1.1 Lý do chọn đề tài / Bối cảnh
  - 1.2 Mục tiêu nghiên cứu
  - 1.3 Đối tượng và phạm vi nghiên cứu
  - 1.4 Phương pháp nghiên cứu
- **PHẦN 2: NỘI DUNG NGHIÊN CỨU:**
  - 2.1 Cơ sở lý luận / Khung lý thuyết của vấn đề
  - 2.2 Thực trạng vấn đề nghiên cứu trong thực tiễn
  - 2.3 Phân tích nguyên nhân và đánh giá ưu/nhược điểm
  - 2.4 Đề xuất giải pháp, bài học kinh nghiệm hoặc kiến nghị
- **PHẦN 3: KẾT LUẬN:** Tóm tắt toàn bộ phát hiện nghiên cứu, ý nghĩa thực tiễn.
- **TÀI LIỆU THAM KHẢO** (Chuẩn IEEE)

---

### Khung D: Đồ án Chuyên ngành & Khóa luận Tốt nghiệp (4 - 5 Chương)
- **TRANG BÌA CHÍNH (Bìa cứng hoa văn chìm)**
- **TRANG BÌA PHỤ (Bìa lót)**
- **PHIẾU GIAO NHIỆM VỤ ĐỒ ÁN / KHÓA LUẬN**
- **LỜI CAM ĐOAN** (Cam kết tính trung thực của tác giả)
- **LỜI CẢM ƠN**
- **BẢN NHẬN XÉT CỦA GIẢNG VIÊN HƯỚNG DẪN**
- **BẢN NHẬN XÉT CỦA CÁN BỘ CHẤM PHẢN BIỆN**
- **TÓM TẮT ĐỒ ÁN (ABSTRACT TIẾNG VIỆT & TIẾNG ANH)**
- **MỤC LỤC**
- **DANH MỤC THUẬT NGỮ VÀ TỪ VIẾT TẮT**
- **DANH MỤC BẢNG BIỂU**
- **DANH MỤC HÌNH VẼ**
- **CÁC CHƯƠNG KỸ THUẬT (4 hoặc 5 chương theo chuyên đề)**
- **KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN**
- **TÀI LIỆU THAM KHẢO** (IEEE)
- **PHỤ LỤC** (Mã nguồn quan trọng, bảng số liệu chi tiết)