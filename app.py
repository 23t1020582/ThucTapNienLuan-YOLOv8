import cv2
import streamlit as st
import pyttsx3
from ultralytics import YOLO

st.title("Ứng dụng Nhận diện Vật dụng Cá nhân cho Người Khiếm thị")

# Load mô hình
@st.cache_resource
def load_model():
    return YOLO('weights/best.pt')

model = load_model()

# Khởi tạo bộ phát âm thanh Text-to-Speech
engine = pyttsx3.init()

run = st.checkbox('Mở Camera')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    ret, frame = camera.read()
    if not ret:
        st.write("Không thể kết nối Webcam!")
        break
    
    # Dự đoán bằng YOLOv8n
    results = model.predict(frame, conf=0.5)
    annotated_frame = results[0].plot()
    
    # Phát âm thanh tên vật thể nhận diện được
    for r in results:
        for c in r.boxes.cls:
            class_name = model.names[int(c)]
            engine.say(f"Phát hiện {class_name}")
            engine.runAndWait()

    # Hiển thị lên giao diện Streamlit
    FRAME_WINDOW.image(cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB))
else:
    camera.release()