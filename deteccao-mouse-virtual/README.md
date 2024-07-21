# Projeto Mouse Virtual

Este projeto utiliza o poder do OpenCV, MediaPipe e PyAutoGUI para criar um mouse virtual que pode ser controlado com gestos das mãos capturados pela webcam. É uma maneira inovadora de interagir com o seu computador sem a necessidade de um mouse físico.

## Recursos

- **Reconhecimento de Gestos das Mãos:** Utiliza MediaPipe para detectar gestos das mãos em tempo real.
- **Movimento e Clique do Mouse:** Transforma movimentos das mãos em movimentos do cursor do mouse e interpreta gestos como cliques do mouse.

## Funcionalidade de Clique

### Distância para Clique

Para detectar um clique, o sistema usa a posição do dedo indicador e do polegar. Abaixo está a explicação sobre como a distância entre esses dois pontos é usada para determinar se um clique deve ser registrado:

- **Distância de Clique:** O sistema considera que um clique ocorre quando a posição y do dedo indicador está próxima à posição y do polegar. O valor de proximidade atualmente considerado para um clique é de 20 pixels.
- **Distância para Mover o Cursor:** Se a posição y do dedo indicador e do polegar não estiver dentro da faixa de 20 pixels, mas a diferença entre eles for menor que 100 pixels, o cursor do mouse é movido para a posição do dedo indicador. Se a diferença for maior que 100 pixels, o cursor não se moverá.

Esses valores podem ser ajustados conforme necessário para melhorar a sensibilidade do clique e a precisão do controle do cursor.


## Pré-requisitos

- Python 3.6 ou superior
- OpenCV
- MediaPipe
- PyAutoGUI

## Instalação

1. Clone o repositório para a sua máquina local.
2. Certifique-se de que você tem o Python instalado. Caso contrário, faça o download e instale a partir de [python.org](https://www.python.org/).
3. Instale as bibliotecas necessárias usando pip:

```bash
pip install opencv-python mediapipe pyautogui

## Thiago Vieira