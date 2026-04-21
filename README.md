# VoiceClone 🎙️

AI Voice Cloning and Real-time Text-to-Speech using XTTS v2.

## 🚀 Overview
This repository provides a simple interface for voice cloning and real-time speech generation.

## 📁 Project Structure
- **`app.py`**: Used for model training and initial setup.
- **`voice.py`**: Used for real-time text input to be given to the model for speech generation.

## 🛠️ Requirements
To install the necessary dependencies, run:
```bash
pip install -r requirements.txt
```

## 🎙️ Usage

### 1. Model Training / Setup
Run `app.py` to initialize or train the model:
```bash
python app.py
```

### 2. Real-time TTS
Run `voice.py` to convert text to speech in real-time:
```bash
python voice.py
```

## 📋 Features
- High-quality voice cloning (XTTS v2)
- Multi-language support (Hindi, English, Spanish, etc.)
- Interactive real-time mode
- Fast inference with model persistence

## 🎧 Audio Samples
Listen to a sample of the generated voice:
- [Generated Speech (Hindi)](output-51.wav)
