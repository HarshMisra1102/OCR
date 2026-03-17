import cv2

def detect_edges(image):
    edges = cv2.Canny(image, 75, 200)
    return edges