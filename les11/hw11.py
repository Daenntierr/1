import cv2
import torch
from PIL import Image
import numpy as np

def load_model():
    # Завантаження попередньо натренованої моделі YOLOv5
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    return model

def detect_patterns(model, image_path):
    # Використання моделі для детекції об'єктів
    results = model(image_path)
    detections = results.pandas().xyxy[0]  # Отримуємо результати як DataFrame
    return detections

def overlay_image(base_image, overlay_image_path, coords):
    # Накладання зображення на базове зображення
    overlay = Image.open(overlay_image_path).convert("RGBA")
    base = Image.fromarray(cv2.cvtColor(base_image, cv2.COLOR_BGR2RGB)).convert("RGBA")

    for _, row in coords.iterrows():
        x1, y1, x2, y2 = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
        overlay_resized = overlay.resize((x2 - x1, y2 - y1))
        base.paste(overlay_resized, (x1, y1), overlay_resized)

    return cv2.cvtColor(np.array(base), cv2.COLOR_RGB2BGR)

if __name__ == "__main__":
    # Вхідні дані
    base_image_path = "path_to_base_image.jpg"  # Початкове зображення
    overlay_image_path = "path_to_overlay_image.png"  # Зображення для накладання
    output_image_path = "output_image.jpg"  # Результуюче зображення

    # Завантаження моделі
    model = load_model()

    # Детекція патернів
    detections = detect_patterns(model, base_image_path)

    # Фільтрація для 2 патернів
    filtered_detections = detections.head(2)  # Беремо перші два знайдені об'єкти

    # Завантаження зображення
    base_image = cv2.imread(base_image_path)

    # Накладання зображень
    result_image = overlay_image(base_image, overlay_image_path, filtered_detections)

    # Збереження результату
    cv2.imwrite(output_image_path, result_image)
    print(f"Результуюче зображення збережено в {output_image_path}")