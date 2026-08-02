from ultralytics import YOLO

if __name__ == '__main__':
    # Khởi tạo mô hình YOLOv8n tiền huấn luyện (pretrained)
    model = YOLO('yolov8n.pt')

    # Bắt đầu quá trình huấn luyện
    results = model.train(
        data='data.yaml',       # Đường dẫn tới file khai báo dữ liệu
        epochs=50,              # Số lượt huấn luyện
        imgsz=640,              # Kích thước ảnh đầu vào
        batch=16,               # Kích thước batch
        device='cpu',           # Chạy trên CPU (đổi thành 0 nếu dùng GPU NVIDIA)
        name='yolov8n_custom'   # Tên thư mục lưu kết quả
    )

    print("HUẤN LUYỆN HOÀN TẤT!")
    print("Mô hình tốt nhất đã được lưu tại: runs/detect/yolov8n_custom/weights/best.pt")
