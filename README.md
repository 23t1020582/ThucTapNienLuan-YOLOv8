
# Hệ Thống Nhận Diện Vật Dụng Cá Nhân & Mệnh Giá Tiền Hỗ Trợ Người Thị Giác Kém

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-realtime.svg)](https://github.com/ultralytics/ultralytics)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI%20App-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/Academic-Thesis%20Report-green.svg)]()

> **Báo cáo Thực tập Niên luận**  
> **Đề tài:** Xây dựng ứng dụng phân loại vật dụng cá nhân thiết yếu hỗ trợ sinh hoạt độc lập cho người khiếm thị dựa trên mô hình YOLOv8n trên nền tảng Streamlit Localhost  
> **Tác giả:** [Họ và Tên Sinh Viên] - [Mã Số Sinh Viên]  
> **Khoa/Trường:** Công nghệ Thông tin  
> **Repository:** [ThucTapNienLuan-YOLOv8](https://github.com/23t1020582/ThucTapNienLuan-YOLOv8)

---

## 📌 1. Giới thiệu tổng quan

Dự án xây dựng một giải pháp thị giác máy tính **End-to-End** hỗ trợ người thị giác kém/khiếm thị trong việc nhận biết các vật dụng sinh hoạt hàng ngày và phân biệt các mệnh giá tiền Việt Nam Đồng (VND). 

Hệ thống sử dụng kiến trúc mô hình **YOLOv8n (Nano)** – phiên bản siêu nhẹ được tối ưu hóa cho các thiết bị nhúng và thiết bị di động có cấu hình phần cứng hạn chế, đảm bảo tốc độ phản hồi thời gian thực (Real-time).

```mermaid
graph LR
    A[Input: Ảnh / Camera] --> B[Tiền xử lý Ảnh]
    B --> C[Mô hình YOLOv8n Trained]
    C --> D[Phát hiện Bounding Box & Class]
    D --> E[Xuất Kết quả / Web UI Streamlit]

# Cấu trúc thư mục dự án

```text
ThucTapNienLuan-YOLOv8/
├── dataset/                  # Tập dữ liệu ảnh (500 ảnh: Train/Valid/Test)
│   ├── train/                # Ảnh & Nhãn huấn luyện (70% - 350 ảnh)
│   ├── valid/                # Ảnh & Nhãn kiểm định (20% - 100 ảnh)
│   └── test/                 # Ảnh & Nhãn kiểm thử (10% - 50 ảnh)
├── weights/
│   └── best.pt               # Trọng số YOLOv8n đã huấn luyện tốt nhất (mAP50 = 0.904)
├── data.yaml                 # File cấu hình đường dẫn và 6 lớp đối tượng
├── train.py                  # Script huấn luyện mô hình YOLOv8n
├── val.py                    # Script đánh giá các chỉ số mAP@0.5, Precision, Recall
├── predict.py                # Script nhận diện & xuất kết quả dự đoán hình ảnh
├── app.py                    # Ứng dụng Web UI giao diện Streamlit tương tác trực quan
├── requirements.txt          # Danh sách các thư viện phụ thuộc
└── README.md                 # Báo cáo và tài liệu hướng dẫn sử dụng
---

💻 1. Hướng dẫn cài đặt môi trường
Yêu cầu hệ thống:
Python: >= 3.8 (Khuyên dùng Python 3.9 hoặc 3.10)

Cài đặt từng bước:
Bash
# 1. Clone repository về máy
git clone [https://github.com/23t1020582/ThucTapNienLuan-YOLOv8.git](https://github.com/23t1020582/ThucTapNienLuan-YOLOv8.git)
cd ThucTapNienLuan-YOLOv8

# 2. Tạo và kích hoạt môi trường ảo (Virtual Environment)
python -m venv venv

# Trên Windows:
venv\Scripts\activate
# Trên Linux/macOS:
source venv/bin/activate

# 3. Cài đặt các thư viện phụ thuộc
pip install -r requirements.txt

