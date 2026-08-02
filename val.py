from ultralytics import YOLO

if __name__ == '__main__':
    # Load trọng số đã huấn luyện tốt nhất
    model = YOLO('weights/best.pt')

    # Tiến hành đánh giá mô hình trên tập validation/test
    metrics = model.val(
        data='data.yaml',
        split='val',            # Hoặc 'test' tùy tập bạn muốn đánh giá
        imgsz=640,
        batch=16,
        device='cpu'
    )

    # In các chỉ số hiệu năng chính ra màn hình
    print("\n" + "="*40)
    print("--- KẾT QUẢ ĐÁNH GIÁ MÔ HÌNH ---")
    print(f"Precision (Độ chính xác): {metrics.results_dict['metrics/precision(B)']:.4f}")
    print(f"Recall (Độ phủ):          {metrics.results_dict['metrics/recall(B)']:.4f}")
    print(f"mAP@0.5:                  {metrics.results_dict['metrics/mAP50(B)']:.4f}")
    print(f"mAP@0.5:0.95:             {metrics.results_dict['metrics/mAP50-95(B)']:.4f}")
    print("="*40)
