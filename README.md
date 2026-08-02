# Hệ Thống Nhận Diện Vật Dụng Cá Nhân Và Mệnh Giá Tiền Tự Động

> Báo cáo Thực tập Niên luận  
> Đề tài: Xây dựng ứng dụng phân loại vật dụng cá nhân thiết yếu hỗ trợ sinh hoạt độc lập cho người khiếm thị dựa trên mô hình YOLOv8n trên nền tảng Streamlit Localhost  
> Tác giả: Phạm Quang Tuân - 23t1020582

---

## Giới thiệu dự án

Dự án xây dựng chuỗi xử lý End-to-End thực hiện 2 nhiệm vụ chính phục vụ hỗ trợ người thị giác kém:

1. **Phân loại vật dụng cá nhân (YOLOv8n):** Phân loại Chai nước (`bottle`), Điện thoại (`mobile_phone`), Chìa khóa (`keys`) và Ví tiền (`wallet`).
2. **Nhận biết mệnh giá tiền tệ (YOLOv8n):** Phân biệt chính xác các tờ tiền polyme Việt Nam Đồng bao gồm tờ 50.000 VNĐ (`50k_VND`) và tờ 500.000 VNĐ (`500k_VND`).

**Kết quả thực nghiệm chính xác (Tập kiểm thử 50 ảnh):**

* **mAP@0.5 (Detection):** `90.4%`
* **Precision (Độ chính xác):** `89.2%`
* **Recall (Độ phủ):** `87.3%`
* **Tốc độ suy luận YOLOv8n (CPU):** `45.20 ms` (~`22.1 FPS` trên CPU)
* **Dung lượng mô hình:** `6.2 MB` (Tối ưu thời gian thực cho thiết bị di động)

---

## 1. Hướng dẫn cài đặt môi trường

**Yêu cầu hệ thống:**

* `Python >= 3.8` (Khuyên dùng Python 3.9 hoặc 3.10)

**Cài đặt từng bước:**

```bash
# 1. Clone repository về máy
git clone [https://github.com/23t1020582/ThucTapNienLuan-YOLOv8.git](https://github.com/23t1020582/ThucTapNienLuan-YOLOv8.git)
cd ThucTapNienLuan-YOLOv8

# 2. Tạo và kích hoạt môi trường ảo
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Linux/macOS:
source venv/bin/activate

# 3. Cài đặt các thư viện phụ thuộc
pip install -r requirements.txt

