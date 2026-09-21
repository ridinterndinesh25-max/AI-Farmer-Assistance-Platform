from pathlib import Path

import numpy as np
import tensorflow as tf


# Project ke main folder me saved model
BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = BASE_DIR / "disease_model.keras"

# Ye order train_model.py ke output se match hona chahiye
CLASS_NAMES = [
    "Potato_Early_Blight",
    "Potato_Healthy",
    "Potato_Late_Blight",
    "Tomato_Healthy",
    "Tomato_Late_Blight",
    "Tomato___Early_blight",
]

def get_model():
    return tf.keras.models.load_model(MODEL_PATH)


def predict_disease(image_path):
    image = tf.keras.utils.load_img(
        image_path,
        target_size=(224, 224)
    )

    image_array = tf.keras.utils.img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)

    model = get_model()
    predictions = model.predict(image_array, verbose=0)[0]

    predicted_index = int(np.argmax(predictions))
    disease_name = CLASS_NAMES[predicted_index]
    confidence = round(float(predictions[predicted_index]) * 100, 2)

    return disease_name, confidence

# Disease ke according treatment recommendation

TREATMENT_GUIDE = {
    "Potato_Early_Blight": {
        "disease": "Potato Early Blight",
        "status": "Disease detected",
        "treatment": [
            "Affected leaves ko remove karke dispose karein.",
            "Plants ke beech proper spacing rakhein.",
            "Leaves ko lambe samay tak geela rehne se bachayein."
        ],
        "medicine": "Potato Early Blight ke liye approved fungicide ki zarurat ho sakti hai.",
        "warning": "Fungicide ka selection aur dose product label aur local agricultural expert ke according karein."
    },

    "Potato_Late_Blight": {
        "disease": "Potato Late Blight",
        "status": "Disease detected",
        "treatment": [
            "Affected plants ko jaldi identify karein.",
            "Infected plant material ko field se remove karein.",
            "Crop ko monitor karein, kyunki disease tezi se fail sakti hai."
        ],
        "medicine": "Potato Late Blight ke liye locally approved fungicide ki recommendation lein.",
        "warning": "Disease confirm karne ke baad hi suitable fungicide aur dose decide karein."
    },

    "Tomato___Early_blight": {
        "disease": "Tomato Early Blight",
        "status": "Disease detected",
        "treatment": [
            "Affected leaves ko remove karein.",
            "Plants ke beech proper spacing rakhein.",
            "Leaves par unnecessary water spraying se bachein."
        ],
        "medicine": "Tomato Early Blight ke liye approved fungicide ki zarurat ho sakti hai.",
        "warning": "Product label par di gayi dose, PPE aur harvest interval follow karein."
    },

    "Tomato_Late_Blight": {
        "disease": "Tomato Late Blight",
        "status": "Disease detected",
        "treatment": [
            "Affected plants ko isolate karein.",
            "Infected leaves aur fruits ko remove karein.",
            "Disease ko jaldi control karne ke liye local agricultural expert se salah lein."
        ],
        "medicine": "Tomato Late Blight ke liye locally approved fungicide ki recommendation lein.",
        "warning": "AI prediction ke basis par bina confirmation pesticide spray na karein."
    },

    "Potato_Healthy": {
        "disease": "Potato Healthy",
        "status": "Healthy",
        "treatment": [
            "Crop ki regular monitoring karein.",
            "Balanced fertilizer aur proper irrigation maintain karein."
        ],
        "medicine": "Is prediction ke basis par disease-control medicine ki zarurat nahi hai."
    },

    "Tomato_Healthy": {
        "disease": "Tomato Healthy",
        "status": "Healthy",
        "treatment": [
            "Crop ki regular monitoring karein.",
            "Proper irrigation aur balanced nutrition maintain karein."
        ],
        "medicine": "Is prediction ke basis par disease-control medicine ki zarurat nahi hai."
    }
}


def get_treatment(disease_name):
    """
    Predicted disease ke according treatment guide return karta hai.
    """

    return TREATMENT_GUIDE.get(
        disease_name,
        {
            "disease": disease_name,
            "status": "Unknown",
            "treatment": [
                "Disease ki expert se confirmation karwayein."
            ],
            "medicine": "Abhi medicine recommendation available nahi hai.",
            "warning": "Bina disease confirm kiye pesticide spray na karein."
        }
    )