# 🖥️ Rice Classifier - Desktop App Version

This repository contains an offline, standalone `.exe` version of the Rice Type Classifier powered by a deep learning model trained on rice grain images.

No Python installation is required — just double-click the executable and use the app in your browser.

---

## 🍚 App Features

- 📷 Upload image of a rice grain
- 🤖 Predict rice type using trained `.h5` model
- 📊 Confidence score of prediction
- ⭐ Rate the prediction
- 🖥️ Fully offline — runs locally as a standalone app

---

## 📁 Project Structure

```
RiceApp_StandaloneBuilder/
├── rice_app.py                # Streamlit app code
├── rice_type_classifier.h5    # Pre-trained model
├── samplecrop (1).jpg         # Sample test image (optional)
├── build_exe.bat              # Script to create .exe
├── requirements.txt           # (For devs) list of packages
└── dist/
    └── rice_app.exe           # Final Windows executable (generated)
```

---

## 🚀 How to Build `.exe` (Developers Only)

> This step is for developers. End users can skip it and use the `.exe` directly.

### 🧱 1. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 📦 2. Install Requirements

```bash
pip install -r requirements.txt
```

Or manually install:
```
streamlit tensorflow-cpu pillow numpy pyinstaller
```

### 🛠 3. Run the Build Script

```bash
build_exe.bat
```

You’ll get `rice_app.exe` in the `dist/` folder.

---

## 🏃 How to Run

Double-click:
```
dist\rice_app.exe
```

The app will open in your default browser at:
```
http://localhost:8501
```

✅ You don’t need Python or any setup on the end user’s machine.

---

## 🛡 Notes

- The `.exe` file includes all Python dependencies and the ML model.
- If antivirus flags it, mark as safe or sign it.
- Ideal for demo, research, and offline ML classification.

---

## 👤 Author

Developed by Shruti Gupta 
GitHub: [@Shruti-2004-ai([https://github.com/yourusername](https://github.com/Shruti-2004-ai/rice-desktop-app))

---
