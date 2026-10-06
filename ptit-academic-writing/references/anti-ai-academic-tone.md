# Sổ tay Văn phong Sinh viên Thực tế & Kỹ thuật Tạo Văn phong Tự nhiên (Student Academic Tone)

Tài liệu này định hướng cách viết bài **đúng tầm sinh viên đại học (năm 3, năm 4 PTIT)**: chân thực, tập trung vào kỹ thuật thực hành, chấp nhận các hạn chế và "sạn tự nhiên" của một đồ án môn học, tuyệt đối không viết đao to búa lớn như bài báo của giáo sư hoặc bài dịch máy hoàn hảo của AI.

---

## 1. Định vị Văn phong: Đúng Tầm Sinh viên Đại học

### A. Giữ đúng bản chất đồ án môn học / BTL
- **Tập trung vào những gì sinh viên thực sự làm được:** Viết code gì, dùng thư viện nào, gặp lỗi gì trong quá trình chạy, sửa lỗi thế nào, kết quả biểu đồ ra sao.
- **Tránh văn phong "thao túng ngôn từ":** Không dùng các từ hoa mỹ, triết lý hoặc bao quát toàn cầu (như *"cuộc cách mạng công nghiệp 4.0", "chuyển đổi số toàn diện nhân loại"*).
- **Môi trường thực nghiệm thực tế:** Nêu rõ cấu hình máy tính cá nhân thử nghiệm (ví dụ: *CPU Core i5, 16GB RAM, GPU RTX 3050 hoặc chạy trên Google Colab Free*), dung lượng dữ liệu thực tế (vài nghìn đến vài trăm nghìn dòng, không bịa là "Big Data hàng tỷ bản ghi").

### B. Chấp nhận và tạo "Sạn Cố ý / Tính Tự nhiên" (Authentic Imperfections)
1. **Lối hành văn trực diện, mộc mạc:** Diễn đạt theo tư duy người làm kỹ thuật trực tiếp:
   - *Ví dụ tự nhiên:* "Trong quá trình cào dữ liệu từ Shopee, hệ thống thường bị chặn bởi mã CAPTCHA và lỗi giới hạn tần suất (Rate Limit). Để khắc phục tạm thời trong phạm vi bài tập lớn, nhóm thiết lập khoảng nghỉ ngẫu nhiên (random sleep) từ 2 đến 5 giây giữa các lượt gửi yêu cầu HTTP."
2. **Thành thật về giới hạn và lỗi tồn đọng:** Sinh viên làm đồ án luôn có giới hạn thời gian và kiến thức:
   - *Ví dụ tự nhiên:* "Do hạn chế về tài nguyên máy tính cá nhân, nhóm chưa thể huấn luyện mô hình trên toàn bộ tập dữ liệu 1 triệu mẫu mà chỉ lấy mẫu ngẫu nhiên (sample) 50.000 bản ghi để chạy thử nghiệm."
3. **Cấu trúc câu phong phú nhưng không cầu toàn:** Không ép mọi đoạn văn phải có đủ 4 tầng triết học; chỉ cần nói rõ: *Mục đích là gì $\rightarrow$ Dùng công cụ gì $\rightarrow$ Kết quả ra sao $\rightarrow$ Nhận xét ngắn gọn.*

---

## 2. Bảng Chuyển đổi: Từ "AI Giáo Sư" sang "Sinh Viên Làm Thật"

| AI Viết Quá Đạt / Quá Hoàn Hảo (Cần Tránh) | Sinh Viên PTIT Viết Thực Tế (Khuyến Nghị) |
| :--- | :--- |
| *Nghiên cứu này đề xuất một kiến trúc phân tán đột phá nhằm tối ưu hóa triệt để hiệu năng xử lý luồng dữ liệu thời gian thực...* | *Bài tập lớn này xây dựng một hệ thống thu thập và hiển thị dữ liệu giá laptop từ các sàn thương mại điện tử bằng Python và Streamlit.* |
| *Mô hình đạt độ chính xác tiệm cận tuyệt đối, mở ra tiềm năng ứng dụng sâu rộng trong mọi lĩnh vực của nền kinh tế...* | *Mô hình đạt độ chính xác khoảng 86.5% trên tập kiểm thử, đủ đáp ứng yêu cầu phân loại cơ bản trong phạm vi môn học.* |
| *Qua quá trình phân tích đa chiều với các thuật toán tối tân, chúng ta có thể khẳng định chắc chắn rằng...* | *Dựa vào biểu đồ phân phối ở Hình 3.2, có thể thấy đa số các dòng laptop tầm trung tập trung ở mức giá từ 15 đến 20 triệu đồng.* |
| *Hệ thống sở hữu khả năng chịu lỗi tối thượng và khả năng mở rộng vô hạn...* | *Hệ thống hoạt động ổn định trên môi trường máy cục bộ (localhost) khi xử lý đồng thời khoảng 5 đến 10 truy vấn.* |

---

## 3. Nguyên tắc Giữ Thể thức Chuẩn nhưng Nội dung Đời thực

- **Về Thể thức (Hình thức):** Phải làm cực kỳ chuẩn (Bìa có khung + Logo, căn lề 3-2-2-1.5, Times New Roman 13pt, caption bảng biểu ở trên, caption hình ở dưới) vì giảng viên chấm hình thức rất nghiêm.
- **Về Nội dung (Hành văn):** Giữ giọng điệu nghiêm túc, khách quan (không xưng *mình/em/tôi* trong phần kỹ thuật), nhưng câu chữ gãy gọn, thực tế, đúng tâm thế sinh viên đang báo cáo kết quả thực hành.
