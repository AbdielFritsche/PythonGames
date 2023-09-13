class Carta:
    def __init__(self, elemento, nivel_de_poder):
        self.elemento = elemento
        self.nivel_de_poder = nivel_de_poder
        self.posx = 0
        self.posy = 0
        
    def mostrar_carta(self):
        return f"Elemento: {self.elemento}, Nivel de Poder: {self.nivel_de_poder}"
    
if __name__ == "__main__":
    pass