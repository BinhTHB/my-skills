# Cấu trúc Khung Báo cáo Chi tiết Theo Chuyên ngành PTIT

Tài liệu này cung cấp khung cấu trúc (skeleton outline) chuẩn mực của PTIT cho 4 nhóm đề tài kỹ thuật phổ biến.

---

## 1. Cấu trúc Khối Thủ tục Chung (Front Matter)

Áp dụng cho mọi loại báo cáo học thuật:
1. **Trang Bìa chính** (Có khung hoa văn và biểu trưng PTIT).
2. **Trang Bìa phụ** (Trang lót bên trong).
3. **Lời cam đoan** (Cam kết tính trung thực, không sao chép trái phép).
4. **Lời cảm ơn** (Cảm ơn giảng viên hướng dẫn, bộ môn và nhà trường).
5. **Bảng phân công nhiệm vụ** (Bắt buộc với bài tập nhóm: Họ tên, MSV, Công việc phụ trách, Tỷ lệ % hoàn thành).
6. **Mục lục** (Đề mục tự động cập nhật đến cấp 3: 1.1.1).
7. **Danh mục thuật ngữ và từ viết tắt** (Bảng 3 cột: Viết tắt, Cụm từ gốc tiếng Anh, Ý nghĩa tiếng Việt; xếp theo A-Z).
8. **Danh mục bảng biểu** (Số bảng, Tên bảng, Trang).
9. **Danh mục hình vẽ và đồ thị** (Số hình, Tên hình, Trang).

---

## 2. Nhóm Đề tài 1: Khai phá & Trực quan hóa Dữ liệu (Data Analytics & Visualization)

Phù hợp các môn: *Trực quan hóa dữ liệu, Khoa học dữ liệu, Khai phá dữ liệu, Cơ sở dữ liệu lớn*.

### MỞ ĐẦU
- **1. Tính cấp thiết của đề tài:** Bối cảnh thị trường/nghiệp vụ, nhu cầu nắm bắt thông tin qua trực quan hóa.
- **2. Mục tiêu nghiên cứu:** Xây dựng luồng thu thập (ETL/ELT), làm sạch và bảng điều khiển tương tác (Interactive Dashboard).
- **3. Đối tượng và phạm vi nghiên cứu:** Nguồn dữ liệu (E-commerce, Bất động sản, Thời tiết, Y tế...), giới hạn không gian/thời gian.
- **4. Phương pháp tiếp cận và công cụ:** Python (Pandas, Polars, Playwright), Power BI / Streamlit / Dash, Database (PostgreSQL/DuckDB).
- **5. Bố cục báo cáo:** Tóm lược nội dung 4 chương.

### CHƯƠNG 1: TỔNG QUAN BÀI TOÁN VÀ CƠ SỞ LÝ THUYẾT
- **1.1 Bối cảnh miền dữ liệu nghiên cứu:** Đặc thù dữ liệu, chỉ số kinh doanh quan trọng (KPIs, Price Index, Demand).
- **1.2 Cơ sở lý thuyết về quy trình xử lý dữ liệu:** Kiến trúc đường ống ETL/ELT, chuẩn hóa và xử lý missing/outlier.
- **1.3 Các nguyên lý trực quan hóa dữ liệu khoa học:** Nguyên tắc Edward Tufte, lựa chọn loại đồ thị (Distribution, Correlation, Composition, Geospatial), thiết kế bảng màu và Cognitive Load.
- **1.4 Khảo sát các giải pháp và công trình liên quan:** Đánh giá ưu nhược điểm của các hệ thống hiện hữu.

### CHƯƠNG 2: THIẾT KẾ HỆ THỐNG VÀ KIẾN TRÚC DỮ LIỆU
- **2.1 Phân tích yêu cầu hệ thống:** Yêu cầu thu thập, biến đổi, lưu trữ và truy vấn phân tích trực quan.
- **2.2 Thiết kế kiến trúc tổng thể (Architecture Pipeline):** Tầng thu thập -> Tầng lưu trữ thô (Data Lake/Staging) -> Tầng tinh chế (Data Warehouse/Parquet) -> Tầng phục vụ trực quan.
- **2.3 Thiết kế mô hình dữ liệu (Data Modeling):** Lược đồ sao (Star Schema) / Snowflake Schema, bảng Fact, bảng Dimension, từ điển dữ liệu (Data Dictionary).
- **2.4 Thiết kế hệ thống chỉ số phân tích và biểu đồ:** Ma trận câu hỏi nghiệp vụ -> Chỉ số tương ứng -> Dạng biểu đồ trực quan hóa tối ưu.

### CHƯƠNG 3: HIỆN THỰC HÓA ĐƯỜNG ỐNG DỮ LIỆU (DATA PIPELINE)
- **3.1 Thu thập và tiền xử lý dữ liệu (Data Ingestion & Cleaning):** 
  - Kỹ thuật Crawler / Scraping / Gọi API đối tác.
  - Xử lý trùng lặp (Deduplication), chuẩn hóa đơn vị đo lường, phân giải kiểu dữ liệu.
  - Xử lý giá trị khuyết thiếu (Imputation) và giá trị ngoại lai (Outlier detection qua IQR/Z-score).
- **3.2 Xây dựng kho lưu trữ và trích xuất đặc trưng:** Cấu hình Partitioning, Parquet/Delta Lake, tạo cột phái sinh (Feature Engineering).
- **3.3 Tự động hóa và điều phối đường ống (Pipeline Automation):** Script điều phối, log kiểm soát chất lượng dữ liệu (Data Validation).

### CHƯƠNG 4: THỰC NGHIỆM TRỰC QUAN HÓA VÀ ĐÁNH GIÁ THỊ TRƯỜNG
- **4.1 Xây dựng ứng dụng trực quan hóa tương tác (Dashboard UI):** Bố cục giao diện, bộ lọc đa chiều (Slicers/Filters), tương tác drill-down.
- **4.2 Phân tích kết quả thực nghiệm và Insight dữ liệu:**
  - Phân tích phân phối và xu hướng giá.
  - Phân tích tương quan giữa các thông số kỹ thuật và giá cả.
  - Phân tích phân khúc thị trường và thị phần thương hiệu.
- **4.3 Đánh giá hiệu năng hệ thống:** Tốc độ load dữ liệu, thời gian phản hồi biểu đồ, khối lượng bản ghi xử lý.

### KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN
- **Kết luận:** Tổng kết các kết quả định lượng đạt được, đối chiếu mục tiêu ban đầu.
- **Hạn chế:** Giới hạn về nguồn thu thập, tính thời gian thực, độ trễ scraping.
- **Hướng phát triển:** Tích hợp mô hình dự báo học máy (Machine Learning Forecasting), mở rộng đa nguồn dữ liệu thời gian thực.

---

## 3. Nhóm Đề tài 2: Phát triển Hệ thống & Phần mềm (Software & Web/App System)

Phù hợp các môn: *Công nghệ phần mềm, Phát triển ứng dụng Web/Mobile, Hệ thống phân tán, Đồ án ngành CNTT*.

### CHƯƠNG 1: TỔNG QUAN BÀI TOÁN VÀ CÔNG NGHỆ NỀN TẢNG
- **1.1 Bối cảnh và bài toán thực tế cần giải quyết.**
- **1.2 Khảo sát các hệ thống tương tự trên thị trường.**
- **1.3 Các công nghệ và framework áp dụng:** Backend (NestJS, FastAPI, Spring Boot), Frontend (Next.js, Flutter), Database (PostgreSQL, Redis), Hạ tầng (Docker, K8s).

### CHƯƠNG 2: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG
- **2.1 Phân tích yêu cầu chức năng (Use Case Diagram & Specs).**
- **2.2 Phân tích yêu cầu phi chức năng (Bảo mật, Tính sẵn sàng, Hiệu năng, Mở rộng).**
- **2.3 Thiết kế kiến trúc phần mềm:** Microservices / Clean Architecture / MVC, Sơ đồ khối kiến trúc hệ thống.
- **2.4 Thiết kế Cơ sở dữ liệu:** Sơ đồ ERD, thiết kế chi tiết bảng và ràng buộc khóa.
- **2.5 Thiết kế giao diện (Wireframe / Figma Mockup) và API Contract (RESTful / GraphQL).**

### CHƯƠNG 3: HIỆN THỰC HÓA VÀ CÀI ĐẶT HỆ THỐNG
- **3.1 Cài đặt môi trường và cấu hình hạ tầng triển khai.**
- **3.2 Hiện thực hóa các mô-đun nghiệp vụ lõi (Core Business Logic).**
- **3.3 Xây dựng cơ chế xác thực, ủy quyền (JWT, OAuth2, RBAC) và bảo mật.**
- **3.4 Hiện thực hóa giao diện người dùng và tích hợp API.**

### CHƯƠNG 4: THỰC NGHIỆM, ĐÁNH GIÁ VÀ KIỂM THỬ HỆ THỐNG
- **4.1 Kịch bản kiểm thử chức năng (Unit Test, Integration Test, E2E Test).**
- **4.2 Kiểm thử hiệu năng và tải (Load Testing qua k6 / Locust / JMeter).**
- **4.3 Trình diễn các chức năng hoàn thiện của hệ thống (Demo Screenshots & Walkthrough).**

---

## 4. Nhóm Đề tài 3: Nghiên cứu Trí tuệ Nhân tạo & Thuật toán (AI / ML / DL / NLP)

### CHƯƠNG 1: TỔNG QUAN BÀI TOÁN VÀ CƠ SỞ LÝ THUYẾT AI
- **1.1 Giới thiệu bài toán học máy/học sâu.**
- **1.2 Cơ sở toán học và lý thuyết mô hình:** Công thức tối ưu, hàm mất mát (Loss Function), kiến trúc mạng nơ-ron (Transformer, CNN, LSTM, v.v.).
- **1.3 Tổng quan các nghiên cứu liên quan (Literature Review & SOTA).**

### CHƯƠNG 2: THIẾT KẾ PHƯƠNG PHÁP VÀ MÔ HÌNH ĐỀ XUẤT
- **2.1 Xây dựng và thu thập tập dữ liệu (Dataset Pipeline).**
- **2.2 Kỹ thuật tiền xử lý và trích xuất đặc trưng (Feature Extraction / Tokenization / Augmentation).**
- **2.3 Kiến trúc mô hình đề xuất (Proposed Architecture / Model Pipeline).**
- **2.4 Thiết lập chiến lược huấn luyện (Training Strategy, Loss, Optimizer, Hyperparameters).**

### CHƯƠNG 3: HUẤN LUYỆN VÀ TỐI ƯU HÓA MÔ HÌNH
- **3.1 Môi trường huấn luyện phần cứng và tham số thực thi.**
- **3.2 Tiến trình huấn luyện (Training Curves: Train Loss vs Val Loss).**
- **3.3 Các kỹ thuật tối ưu hóa áp dụng (Regularization, Early Stopping, Fine-tuning, Quantization).**

### CHƯƠNG 4: THỰC NGHIỆM VÀ ĐÁNH GIÁ ĐỊNH LƯỢNG
- **4.1 Độ đo đánh giá (Evaluation Metrics):** Accuracy, Precision, Recall, F1-Score, BLEU, ROUGE, Latency (ms).
- **4.2 So sánh đối sánh với các mô hình Baseline (Benchmark Comparison Table).**
- **4.3 Phân tích lỗi (Ablation Study & Error Analysis).**
- **4.4 Đóng gói và tích hợp mô hình vào ứng dụng thực tế (Inference Pipeline / API Service).**
