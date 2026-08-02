from ultralytics import YOLO

def main():
 
    model = YOLO('weights/best.pt')


    metrics = model.val(data='data.yaml', split='test')
    
    print(f"mAP@0.5: {metrics.box.map50:.3f}")
    print(f"mAP@0.5:0.95: {metrics.box.map:.3f}")

if __name__ == '__main__':
    main()