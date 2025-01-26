import cv2
import threading
from rmn import RMN
import time

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)  # Largura da câmera 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)  # Altura da câmera  full hd

m = RMN()

emotion_colors = {
    "angry": (0, 0, 255),
    "disgust": (0, 128, 0),
    "fear": (255, 0, 255),
    "happy": (147, 20, 255),
    "sad": (255, 0, 0),
    "surprise": (255, 255, 0),
    "neutral": (255, 255, 255),
}

frame = None
results = []
lock = threading.Lock()
stop_processing = False  # Variável para parar a thread


def process_frame():
    """Thread para processar emoções."""
    global frame, results, stop_processing
    while not stop_processing:
        if frame is not None:
            with lock:
                processed_frame = frame.copy()
            results = m.detect_emotion_for_single_frame(processed_frame)


# Iniciar a thread para processamento
thread = threading.Thread(target=process_frame, daemon=True)
thread.start()

# Configurar a janela para forçar tela cheia
cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    with lock:
        local_results = results.copy()

    for result in local_results:
        x, y, x2, y2 = result['xmin'], result['ymin'], result['xmax'], result['ymax']
        emotion = result['emo_label'].lower()
        color = emotion_colors.get(emotion, (0, 255, 255))
        cv2.rectangle(frame, (x, y), (x2, y2), color, 2)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow('Frame', frame)

    # Encerrar ao pressionar a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        stop_processing = True  # Indica para a thread parar
        break

cap.release()
cv2.destroyAllWindows()

# Aguarda a thread terminar antes de encerrar
thread.join()
