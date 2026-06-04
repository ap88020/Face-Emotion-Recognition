import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="Emotion Detection AI",
    page_icon="😊",
    layout="wide"
)

# ==================================
# CUSTOM CSS
# ==================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #4CAF50;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: gray;
    margin-bottom: 25px;
}

</style>
""", unsafe_allow_html=True)

# ==================================
# HEADER
# ==================================

st.markdown(
    "<div class='title'>😊 Emotion Detection AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Upload an image or use your camera for real-time emotion analysis</div>",
    unsafe_allow_html=True
)

# ==================================
# LOAD MODEL
# ==================================

@st.cache_resource
def load_emotion_model():
    return load_model("../model/emotion_model.h5")

try:
    model = load_emotion_model()
except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()

# ==================================
# LOAD FACE DETECTOR
# ==================================

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

if face_cascade.empty():
    st.error("Failed to load Haar Cascade.")
    st.stop()

# ==================================
# EMOTION LABELS
# ==================================

emotions = [
    "Angry",
    "Disgust",
    "Fear",
    "Happy",
    "Sad",
    "Surprise",
    "Neutral"
]

# ==================================
# MODE SELECTION
# ==================================

st.markdown("### Choose Input Source")

mode = st.radio(
    "",
    ["📸 Upload Image", "🎥 Camera Capture"],
    horizontal=True
)

uploaded_file = None

if mode == "📸 Upload Image":

    uploaded_file = st.file_uploader(
        "Upload Image",
        type=["jpg", "jpeg", "png"]
    )

elif mode == "🎥 Camera Capture":

    uploaded_file = st.camera_input(
        "Take a Picture"
    )

# ==================================
# IMAGE PROCESSING
# ==================================

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    image_np = np.array(image)

    image_bgr = cv2.cvtColor(
        image_np,
        cv2.COLOR_RGB2BGR
    )

    gray = cv2.cvtColor(
        image_bgr,
        cv2.COLOR_BGR2GRAY
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    if len(faces) == 0:

        st.warning("⚠️ No face detected in image.")

        st.image(
            image,
            use_container_width=True
        )

    else:

        all_predictions = []

        for (x, y, w, h) in faces:

            roi = gray[y:y+h, x:x+w]

            roi = cv2.resize(
                roi,
                (48, 48)
            )

            roi = roi.astype("float32") / 255.0

            roi = np.expand_dims(
                roi,
                axis=0
            )

            roi = np.expand_dims(
                roi,
                axis=-1
            )

            prediction = model.predict(
                roi,
                verbose=0
            )

            emotion_index = np.argmax(prediction)

            emotion = emotions[emotion_index]

            confidence = float(
                np.max(prediction) * 100
            )

            all_predictions.append(
                prediction[0]
            )

            # Draw Face Rectangle
            cv2.rectangle(
                image_bgr,
                (x, y),
                (x+w, y+h),
                (0, 255, 0),
                2
            )

            # Draw Label
            cv2.putText(
                image_bgr,
                f"{emotion} ({confidence:.1f}%)",
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        col1, col2 = st.columns([2, 1])

        # ==========================
        # IMAGE COLUMN
        # ==========================

        with col1:

            st.image(
                cv2.cvtColor(
                    image_bgr,
                    cv2.COLOR_BGR2RGB
                ),
                use_container_width=True
            )

        # ==========================
        # RESULT COLUMN
        # ==========================

        with col2:

            st.subheader("🎯 Prediction Result")

            top_prediction = all_predictions[0]

            emotion_index = np.argmax(
                top_prediction
            )

            emotion = emotions[
                emotion_index
            ]

            confidence = (
                np.max(top_prediction)
                * 100
            )

            st.success(
                f"{emotion}"
            )

            st.metric(
                "Confidence",
                f"{confidence:.2f}%"
            )

            st.divider()

            st.subheader(
                "📊 Emotion Ranking"
            )

            sorted_idx = np.argsort(
                top_prediction
            )[::-1]

            for idx in sorted_idx:

                score = (
                    top_prediction[idx]
                    * 100
                )

                st.write(
                    f"**{emotions[idx]}**"
                )

                st.progress(
                    int(score)
                )

                st.caption(
                    f"{score:.2f}%"
                )