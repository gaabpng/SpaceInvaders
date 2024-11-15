from PPlay.window import Window
from PPlay.gameimage import GameImage
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse

janela = Window(800, 600)
janela.set_title("Space Invaders - Menu")
teclado = Keyboard()
mouse = Mouse()

background = GameImage("templates/background.png")
botao_jogar = GameImage("templates/botao_jogar.png")
botao_dificuldade = GameImage("templates/botao_dificuldade.png")
botao_ranking = GameImage("templates/botao_ranking.png")
botao_sair = GameImage("templates/botao_sair.png")

botao_largura = botao_jogar.width
botao_altura = botao_jogar.height
espacamento = 20

x_centro = (janela.width - botao_largura) / 2
y_inicial = (janela.height - (4 * botao_altura + 3 * espacamento)) / 2

botao_jogar.set_position(x_centro, y_inicial)
botao_dificuldade.set_position(x_centro, y_inicial + botao_altura + espacamento)
botao_ranking.set_position(x_centro, y_inicial + 2 * (botao_altura + espacamento))
botao_sair.set_position(x_centro, y_inicial + 3 * (botao_altura + espacamento))

estado = "MENU"
dificuldade = 3

while True:
    background.draw()

    if estado == "MENU":
        botao_jogar.draw()
        botao_dificuldade.draw()
        botao_ranking.draw()
        botao_sair.draw()

        if mouse.is_over_object(botao_jogar) and mouse.is_button_pressed(1):
            estado = "JOGAR"
        elif mouse.is_over_object(botao_dificuldade) and mouse.is_button_pressed(1):
            estado = "DIFICULDADE"
        elif mouse.is_over_object(botao_ranking) and mouse.is_button_pressed(1):
            estado = "RANKING"
        elif mouse.is_over_object(botao_sair) and mouse.is_button_pressed(1):
            break

    elif estado == "JOGAR":
        janela.draw_text("Game Loop - Pressione ESC para voltar", janela.width // 2 - 150, janela.height // 2,
                         size=24, color=(255, 255, 255))
        if teclado.key_pressed("ESC"):
            estado = "MENU"

    elif estado == "DIFICULDADE":
        janela.draw_text("Selecione a dificuldade:", janela.width // 2 - 100, 200, size=24, color=(255, 255, 255))
        janela.draw_text("[1] Fácil", janela.width // 2 - 50, 250, size=24, color=(0, 255, 0))
        janela.draw_text("[2] Normal", janela.width // 2 - 50, 300, size=24, color=(255, 255, 0))
        janela.draw_text("[3] Difícil", janela.width // 2 - 50, 350, size=24, color=(255, 0, 0))

        if teclado.key_pressed("1"):
            dificuldade = 2
        elif teclado.key_pressed("2"):
            dificuldade = 3
        elif teclado.key_pressed("3"):
            dificuldade = 4
        elif teclado.key_pressed("ESC"):
            estado = "MENU"

    elif estado == "RANKING":
        janela.draw_text("Ranking ainda não implementado.", janela.width // 2 - 150, janela.height // 2,
                         size=24, color=(255, 255, 255))
        if teclado.key_pressed("ESC"):
            estado = "MENU"

    janela.update()
