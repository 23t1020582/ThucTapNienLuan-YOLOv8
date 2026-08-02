#  Hệ Thống Nhận Diện Vật Dụng Cá Nhân Và Mệnh Giá Tiền Tự Động

> **Thực tập Niên luận**  
> **Đề tài:** Xây dựng ứng dụng phân loại vật dụng cá nhân thiết yếu hỗ trợ sinh hoạt độc lập cho người khiếm thị dựa trên mô hình **YOLOv8n** trên nền tảng **Streamlit**.
>
> **Tác giả:** Phạm Quang Tuân - 23T1020582

---

# 📌 Giới thiệu

Đây là hệ thống hỗ trợ người khiếm thị nhận diện vật dụng cá nhân và mệnh giá tiền Việt Nam bằng mô hình **YOLOv8n** kết hợp giao diện **Streamlit**.

Hệ thống hoạt động theo thời gian thực thông qua webcam và cung cấp kết quả bằng hình ảnh cùng thông báo bằng giọng nói.

---

# Chức năng

## Nhận diện vật dụng cá nhân

- Bottle
- Mobile Phone
- Keys
- Wallet

##  Nhận diện mệnh giá tiền

- 50.000 VNĐ
- 500.000 VNĐ

---

#  Kết quả thực nghiệm

| Chỉ số | Giá trị |
|---------|---------|
| mAP@0.5 | **90.4%** |
| Precision | **89.2%** |
| Recall | **87.3%** |
| Inference Time | **45.20 ms** |
| FPS (CPU) | **22.1 FPS** |
| Model Size | **6.2 MB** |

---

#  Công nghệ sử dụng

- Python
- YOLOv8n
- Ultralytics
- OpenCV
- Streamlit
- NumPy
- PyTorch

---

#  Cấu trúc thư mục

```text
ThucTapNienLuan-YOLOv8/
│
├── app.py
├── train.py
├── val.py
├── predict.py
├── benchmark.py
├── data.yaml
├── requirements.txt
├── README.md
│
├── dataset/
│   ├── train/
│   ├── valid/
│   └── test/
│
└── weights/
    └── best.pt
```

---

# ⚙️ Cài đặt

## 1. Clone project

```bash
git clone https://github.com/23t1020582/ThucTapNienLuan-YOLOv8.git

cd ThucTapNienLuan-YOLOv8
```

---

## 2. Tạo môi trường ảo

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

---

# 📁 Chuẩn bị Dataset

Giải nén file **dataset.zip** vào thư mục gốc của dự án.

```
dataset/
├── train/
├── valid/
└── test/
```

Trong đó

- Train: **350 ảnh**
- Validation: **100 ảnh**
- Test: **50 ảnh**

---

# 🎯 Huấn luyện mô hình

```bash
python train.py
```

---

# 📈 Đánh giá mô hình

```bash
python val.py
```

---

# 🖼 Thử nghiệm dự đoán

```bash
python predict.py
```

---

#  Benchmark

```bash
python benchmark.py
```

---

#  Chạy ứng dụng

```bash
streamlit run app.py
```

Sau khi chạy, trình duyệt sẽ tự mở tại

```
http://localhost:8501
```

---

#  Demo

> Thêm ảnh hoặc GIF demo của hệ thống tại đây.

```
demo/demo.gif
```

---

#  Dataset

Tập dữ liệu gồm **500 ảnh**, chia thành:

| Tập dữ liệu | Số lượng |
|-------------|----------|
| Train | 350 |
| Validation | 100 |
| Test | 50 |

---

#  Tác giả

**Phạm Quang Tuân**

Đại học Khoa học Huế

---

# 📄 Giấy phép

Dự án được phát triển phục vụ mục đích học tập và nghiên cứu.
