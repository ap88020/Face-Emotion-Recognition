# 😊 MoodLens-AI

<div align="center">

# 😊 Emotion Detection AI

### AI-Powered Facial Emotion Recognition using Deep Learning, TensorFlow, OpenCV & Streamlit

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-DeepLearning-orange?style=for-the-badge\&logo=tensorflow)
![OpenCV](https://img.shields.io/badge/OpenCV-ComputerVision-green?style=for-the-badge\&logo=opencv)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red?style=for-the-badge\&logo=streamlit)

</div>

---

## 🚀 Overview

Emotion Detection AI is a Deep Learning based Computer Vision project capable of detecting human emotions from facial images.

The system uses a Convolutional Neural Network (CNN) trained on the FER2013 dataset and provides an interactive Streamlit interface for real-time emotion analysis.

### ✨ Features

* 📸 Upload Image Detection
* 📷 Camera Capture Detection
* 😀 Facial Emotion Recognition
* 🎯 Confidence Score Prediction
* 📊 Emotion Ranking Visualization
* 🧠 Deep Learning Powered
* ⚡ Fast Streamlit Interface
* 👤 Automatic Face Detection

---

## 📸 Project Screenshots

### Home Page

> Add your screenshot here

```markdown
![Home](screenshot/image.png)
![Home](screenshot/image1.png)
```

### Prediction Result

> Add your screenshot here

```markdown
![Prediction](screenshot/image1.png)
```

---

## 🎭 Supported Emotions

| Emotion     |
| ----------- |
| 😠 Angry    |
| 🤢 Disgust  |
| 😨 Fear     |
| 😊 Happy    |
| 😢 Sad      |
| 😲 Surprise |
| 😐 Neutral  |

---

## 🏗️ Project Structure

```text
FACE-DETECTION
│
├── app/
│   └── Core detection scripts
│
├── UI/
│   └── Streamlit Web Application
│
├── model/
│   ├── emotion_model.h5
│   └── trained model files
│
├── notebook/
│   └── Training notebook
│
├── ComputerVision_Cascade/
│   └── Haar Cascade XML
│
├── screenshot/
│   └── Project screenshots
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🧠 Deep Learning Architecture

```text
Input (48x48x1)

↓ Conv2D (32 Filters)
↓ MaxPooling

↓ Conv2D (64 Filters)
↓ MaxPooling

↓ Conv2D (128 Filters)
↓ MaxPooling

↓ Flatten

↓ Dense (512 Neurons)

↓ Dropout (0.5)

↓ Dense (7 Classes)

Output → Emotion Prediction
```

---

## ⚙️ Technologies Used

### 🔥 Deep Learning

* TensorFlow
* Keras
* CNN (Convolutional Neural Network)

### 👁️ Computer Vision

* OpenCV
* Haar Cascade Face Detection

### 🎨 Frontend

* Streamlit

### 📊 Data Processing

* NumPy
* Pillow (PIL)

### 📈 Visualization

* Matplotlib

---

## 📂 Dataset

This project uses the FER2013 (Facial Emotion Recognition) Dataset.

Download Dataset:

https://www.kaggle.com/datasets/msambare/fer2013

Dataset is not included in this repository.

After downloading:

```text
data/
├── train/
└── test/
```

---

## 🔧 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/MoodLens-AI.git

cd MoodLens-AI
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Environment

Windows

```bash
env\Scripts\activate
```

Linux / Mac

```bash
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run UI/ui.py
```

Application will start at:

```text
http://localhost:8501
```

---

## 🎯 How It Works

1. Upload an image or capture from camera
2. OpenCV detects faces
3. Face is converted to grayscale
4. Image resized to 48x48
5. CNN model predicts emotion
6. Emotion label and confidence score displayed
7. Results visualized in Streamlit UI

---

## 📊 Example Output

```text
Happy (92.3%)

Emotion Ranking:

Happy      92.3%
Neutral     4.1%
Surprise    1.8%
Sad         0.9%
Fear        0.5%
Angry       0.3%
Disgust     0.1%
```

---

## 🌟 Future Improvements

* 🎥 Real-Time Webcam Streaming
* 📊 Emotion Analytics Dashboard
* 📈 Emotion Trends Visualization
* ☁️ Cloud Deployment
* 📱 Mobile Responsive Interface
* 🤖 Multiple Face Tracking

---

## 👨‍💻 Author

### Akash Patel

Passionate about:

* Artificial Intelligence
* Deep Learning
* Computer Vision
* Generative AI
* Machine Learning

---

## ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork this project

📢 Share your feedback

---

<div align="center">

### 🚀 Teaching Machines to Understand Human Emotions

Made with ❤️ using Deep Learning

</div>
