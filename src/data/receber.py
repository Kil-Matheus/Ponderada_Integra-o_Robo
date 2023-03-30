# Classes: Coordenadas que vai receber os dados do formulário e vai inserir no banco de dados
class Coordenadas():
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z