import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

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

    def predict_image(self, image_path):
        imagem = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        imagem = imagem / 255.0
        imagem = cv2.resize(imagem, (150, 40))
        imagem = np.expand_dims(imagem, axis=-1)

        previsao = self.model.predict(np.array([imagem]))

        resultado = self.decode_predictions(previsao)[0]

        return resultado

if __name__ == "__main__":
    # Defina os paths e variáveis de ambiente
    MODEL_PATH = os.getenv("MODEL_PATH", "/Users/alertrack/Documents/Captcha-Bot/")
    IMAGE_PATH = os.getenv("IMAGE_PATH", "/Users/alertrack/Documents/Captcha-Bot/dataset/archive/1a1SZ.jpg")
    CHAR_POOL = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Crie uma instância da classe CaptchaModel
    modelo_captcha = CaptchaModel(MODEL_PATH, CHAR_POOL)

    # Faça a previsão na imagem
    resultado = modelo_captcha.predict_image(IMAGE_PATH)

    # Exiba o resultado
    print("Resultado:", resultado)
