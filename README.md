# Captcha Bot

Este é um projeto que consiste em uma aplicação para reconhecimento de caracteres em captchas utilizando uma rede neural convolucional (CNN) treinada.

## Conteúdo
+ Dataset
+ Aplicativo
+ Treinamento do Modelo
+ Como Usar
+ Build em Docker

## Dataset

O dataset utilizado para treinar o modelo está disponível [Aqui](https://www.kaggle.com/datasets/parsasam/captcha-dataset). Ele contém uma variedade de imagens de captchas com caracteres alfanuméricos.

## Aplicativo
O aplicativo consiste em uma API onde é possível enviar uma imagem em formato base64 para ser processada pelo modelo de reconhecimento de caracteres. O resultado retornado pela API é a string contendo os caracteres reconhecidos.

## Treinamento do Modelo
O notebook generate_model/train_model.ipynb contém o código utilizado para treinar o modelo de reconhecimento de caracteres. Este modelo utiliza uma arquitetura de rede neural convolucional (CNN) para processar as imagens do dataset e reconhecer os caracteres.

## Como Usar
Para usar o aplicativo, é necessário enviar uma imagem codificada em base64 para a API. O resultado será a string contendo os caracteres reconhecidos no captcha.

#### Exemplo de Uso:
```
import requests
import base64

with open("captcha_image.jpg", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

response = requests.post('http://localhost:8080/predict', json={'image': encoded_image})

print(response.json())
```

## Build em Docker
Para buildar e rodar a aplicação em um contêiner Docker, siga os passos abaixo:

Certifique-se de ter o Docker instalado em sua máquina.
No terminal, navegue até o diretório raiz do projeto.
Execute o seguinte comando para buildar a imagem Docker:

```
docker build -t captcha-bot .

docker run -p 8080:8080 captcha-bot
```

Isso irá rodar a aplicação na porta 8080 do seu localhost. Agora você pode enviar imagens codificadas em base64 para a API e receber o resultado do reconhecimento de caracteres.

Com estas instruções, você será capaz de usar e rodar o projeto de reconhecimento de caracteres em captchas. Se precisar de mais informações ou tiver dúvidas, não hesite em entrar em contato.