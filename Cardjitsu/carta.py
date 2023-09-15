class Carta:
    """
    Clase que representa una carta en el juego.

    Attributos:
        elemento (str): El elemento de la carta (p. ej., "Fuego", "Agua", "Nieve").
        nivel_de_poder (int): El nivel de poder de la carta.
        posx (int): La coordenada x de la posición de la carta (por defecto 0).
        posy (int): La coordenada y de la posición de la carta (por defecto 0).
    """

    def __init__(self, elemento, nivel_de_poder):
        """
        Inicializa una nueva instancia de la clase Carta.

        Args:
            elemento (str): El elemento de la carta (p. ej., "Fuego", "Agua", "Nieve").
            nivel_de_poder (int): El nivel de poder de la carta.
        """
        self.elemento = elemento
        self.nivel_de_poder = nivel_de_poder
        self.posx = 0
        self.posy = 0

    def mostrar_carta(self):
        """
        Devuelve una cadena que representa la carta y sus atributos.

        Returns:
            str: Una cadena que muestra el elemento y nivel de poder de la carta.
        """
        return f"Elemento: {self.elemento}, Nivel de Poder: {self.nivel_de_poder}"

if __name__ == "__main__":
    pass
