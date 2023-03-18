# Classes: Coordenadas que vai receber os dados do formulário e vai inserir no banco de dados
class Coordenadas():
    def __init__(self, id, x, y, z) -> None:
        self.id = id
        self.x = x
        self.y = y
        self.z = z