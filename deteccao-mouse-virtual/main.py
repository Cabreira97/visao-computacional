import cv2
import mediapipe as mp
import pyautogui

# Inicialização dos objetos necessários
captura = cv2.VideoCapture(0)
detector_maos = mp.solutions.hands.Hands()
utilitarios_desenho = mp.solutions.drawing_utils
largura_tela, altura_tela = pyautogui.size()

contador_clicks = 0  # Inicializa o contador de cliques

# Função para processar o quadro e detectar mãos
def processar_quadro(quadro):
    quadro = cv2.flip(quadro, 1)
    quadro_rgb = cv2.cvtColor(quadro, cv2.COLOR_BGR2RGB)
    resultado = detector_maos.process(quadro_rgb)
    return resultado, quadro

# Função para desenhar landmarks da mão
def desenhar_landmarks(quadro, maos):
    if maos:
        for mao in maos:
            utilitarios_desenho.draw_landmarks(quadro, mao)
    return quadro

# Função para obter as coordenadas dos landmarks
def obter_posicoes_landmarks(mao, largura_quadro, altura_quadro):
    landmarks = mao.landmark
    posicoes = [(int(landmark.x * largura_quadro), int(landmark.y * altura_quadro)) for landmark in landmarks]
    return posicoes

# Função para mover o cursor e clicar com base na posição dos dedos
def controlar_cursor_e_clicar(pos_indicador, pos_polegar):
    global contador_clicks  # Usa a variável global para o contador de cliques
    indicador_x, indicador_y = pos_indicador
    polegar_x, polegar_y = pos_polegar
    pyautogui.moveTo(polegar_x, polegar_y)
    if abs(indicador_y - polegar_y) < 20:
        pyautogui.click()
        contador_clicks += 1  # Incrementa o contador de cliques
        print(f"Contador de Cliques: {contador_clicks}")  # Opcional: Imprime o contador no console
        pyautogui.sleep(1)
    elif abs(indicador_y - polegar_y) < 100:
        pyautogui.moveTo(indicador_x, indicador_y)

# Loop principal
while True:
    _, quadro = captura.read()
    altura_quadro, largura_quadro, _ = quadro.shape
    resultado, quadro = processar_quadro(quadro)
    maos = resultado.multi_hand_landmarks

    if maos:
        for mao in maos:
            posicoes = obter_posicoes_landmarks(mao, largura_quadro, altura_quadro)
            pos_indicador = posicoes[8]  # Posição do dedo indicador
            pos_polegar = posicoes[4]    # Posição do polegar

            # Desenhar círculos nos dedos indicador e polegar
            cv2.circle(img=quadro, center=pos_indicador, radius=10, color=(0, 255, 255), thickness=-1)
            cv2.circle(img=quadro, center=pos_polegar, radius=10, color=(0, 255, 255), thickness=-1)

            # Controlar o cursor e clicar
            controlar_cursor_e_clicar(pos_indicador, pos_polegar)

    # Opcional: Exibe o contador de cliques na janela do OpenCV
    cv2.putText(quadro, f"Cliques: {contador_clicks}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    quadro = desenhar_landmarks(quadro, maos)
    cv2.imshow('Mouse Virtual', quadro)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captura.release()
cv2.destroyAllWindows()