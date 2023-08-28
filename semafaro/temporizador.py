import time


class Temporizador:
    def __init__(self):
        self.duracao = 0

    def setDuracao(self, novoTempo):
        self.duracao = novoTempo

    def iniciarContagem(self):
        for t in range(self.duracao, 0, -1):
            print(f"{t} seg")
            time.sleep(1)


tempo = Temporizador()
tempo.setDuracao(10)
tempo.iniciarContagem()
