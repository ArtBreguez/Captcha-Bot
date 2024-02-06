import os
import cv2
import numpy as np
import base64
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model

app = Flask(__name__)

class CaptchaModel:
    def __init__(self, model_path, char_pool):
        self.model = load_model(model_path)
        self.char_pool = char_pool

    def decode_predictions(self, predictions):
        decoded_strings = []
        for pred in predictions:
            char_indices = np.argmax(pred, axis=-1)
            decoded_string = ''.join([self.char_pool[i] for i in char_indices])
            decoded_strings.append(decoded_string)
        return decoded_strings

    def predict_image(self, base64_image):
        image_data = base64.b64decode(base64_image)
        nparr = np.frombuffer(image_data, np.uint8)
        imagem = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
        imagem = imagem / 255.0  # Normalização
        imagem = cv2.resize(imagem, (150, 40))
        imagem = np.expand_dims(imagem, axis=-1)

        previsao = self.model.predict(np.array([imagem]))

        resultado = self.decode_predictions(previsao)[0]

        return resultado

MODEL_PATH = 'model'
CHAR_POOL = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

modelo_captcha = CaptchaModel(MODEL_PATH, CHAR_POOL)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    base64_image = data.get('image')
    if base64_image:
        try:
            resultado = modelo_captcha.predict_image(base64_image)
            return jsonify({'prediction': resultado}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Image not provided'}), 400

if __name__ == '__main__':
    app.run(debug=False)
