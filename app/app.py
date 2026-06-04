import cv2 
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("./model/emotion_model.h5")

# Load face detector
face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default (1).xml"
)

# Emotion labels
emotions = [
    "Angry",
    "Disgust",
    "Fear",
    "Happy",
    "Sad",
    "Surprise",
    "Neutral"
]

# Open Webcam
cap = cv2.VideoCapture(0)



while True:

    ret, frame = cap.read()

    if not ret:
        print("Failed to access camera")
        break


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        # draw rectangle
        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (255, 0, 0),
            2
        )

        # Extract face
        roi = gray[y:y+h,x:x+w]

        try:
            roi = cv2.resize(roi, (48, 48))

            roi = roi.astype("float32") / 255.0

            roi = np.expand_dims(roi, axis=0)
            roi = np.expand_dims(roi, axis=-1)

            predction = model.predict(roi,verbose=0)

            emotion_index = np.argmax(predction)
            emotion = emotions[emotion_index]

            confidence = np.max(predction) * 100

            cv2.putText(
                frame,
                f"{emotion} ({confidence:.1f}%)",
                (x,y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0,255,0),
                2
            )
        except Exception as e:
            print("Prediction Error:", e)


    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()