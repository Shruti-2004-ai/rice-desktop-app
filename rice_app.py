
import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

# Load the trained model
model = load_model("rice_type_classifier.h5")

# Define class names (must match model's output)
class_names = ['Basmati', 'Jasmine', 'Arborio', 'Brown', 'Other']

# --- UI CONFIG ---
st.set_page_config(page_title="Rice Type Classifier", layout="centered")

# --- SIDEBAR ---
st.sidebar.title("🍚 Rice Classifier App")
st.sidebar.info("Upload a rice grain image or use a sample to predict its type.")
st.sidebar.markdown("""
**👨‍🔬 Features:**
- Rice type prediction  
- Confidence score  
- Sample test  
- User feedback logging
""")

# --- MAIN TITLE ---
st.title("🌾 Rice Type Classification Using Machine Learning")

st.markdown("""
This AI-powered app classifies rice grain images into five categories using a trained deep learning model.
""")

# --- ABOUT RICE TYPES ---
with st.expander("📘 About Rice Types"):
    st.markdown("""
- **Basmati**: Long grain, aromatic  
- **Jasmine**: Fragrant, softer grain  
- **Arborio**: Short and starchy, used in risotto  
- **Brown**: Whole grain rice  
- **Other**: Any type not covered above  
""")

# --- FILE UPLOAD ---
uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])
use_sample = st.checkbox("🖼️ Use sample image instead")

if use_sample:
    sample_path = "samplecrop (1).jpg"
    if not os.path.exists(sample_path):
        st.error("Sample image not found.")
    else:
        uploaded_file = sample_path

if uploaded_file:
    # Load and display image
    if isinstance(uploaded_file, str):
        image = Image.open(uploaded_file).convert("RGB")
    else:
        image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Input Image", use_column_width=True)

    # Preprocess
    image = image.resize((224, 224))
    img_array = np.expand_dims(np.array(image) / 255.0, axis=0)

    # Predict
    prediction = model.predict(img_array)
    predicted_index = int(np.argmax(prediction))
    predicted_label = class_names[predicted_index]
    confidence = float(np.max(prediction)) * 100

    # Output results
    st.subheader("🔍 Prediction")
    st.success(f"**Predicted:** {predicted_label}")
    st.write(f"📊 Confidence: `{confidence:.2f}%`")
    st.progress(int(confidence))

    # --- Rating Feedback ---
    rating = st.slider("⭐ How accurate is this prediction?", 0, 5, 3)
    st.write(f"✅ You rated it: `{rating}/5`")

    # --- Logging Feedback ---
    feedback_file = "user_feedback.csv"
    with open(feedback_file, "a") as f:
        f.write(f"{predicted_label},{confidence:.2f},{rating}\n")

    st.info("📝 Feedback saved. Thank you!")
