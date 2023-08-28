from enum import Enum

from temporizador import Temporizador


class Estado(Enum):
    Vermelho = 1
    Amarelo = 2
    Verde = 3


class SemafaroTemporizado:
    def __init__(self, estadoInicial: Estado = Estado.Vermelho):
        # 1: verde, 2: amarelo, 3: vermelho
        self.estadoAtual = estadoInicial
        self.timer = Temporizador()
        self.tempoTransicao = {Estado.Verde: 20, Estado.Amarelo: 5, Estado.Vermelho: 10}

    def getEstadoAtual(self) -> Estado:
        return self.estadoAtual

    def __str__(self):
        return f"""
        +-------+
        |  ({"x" if self.estadoAtual == Estado.Vermelho else " "})  |
        |  ({"x" if self.estadoAtual == Estado.Amarelo else " "})  |
        |  ({"x" if self.estadoAtual == Estado.Verde else " "})  |
        +-------+
        """

    def setup(self, tempoVermelho: int, tempoAmarelo: int, tempoVerde: int):
        """
        ----------
        Método que permite ajustar o tempo dos estados do semáfaro.
        Aceita um tempo em segundo entre 1 e 59
        ----------
        Args:
            tempoVermelho (int): tempo de segundos de permanência no vermelho
            tempoAmarelo (int): tempo de segundos de permanência no amarelo
            tempoVerde (int): tempo de segundos de permanência no verde
        """

        if tempoVermelho < 1 or tempoVermelho > 50:
            return
        elif tempoAmarelo < 1 or tempoAmarelo > 50:
            return
        elif tempoVerde < 1 or tempoVerde > 50:
            return

        self.tempoTransicao[Estado.Vermelho] = tempoVermelho
        self.tempoTransicao[Estado.Amarelo] = tempoAmarelo
        self.tempoTransicao[Estado.Verde] = tempoVerde
