class Button:
    def __init__(self, pos, text_input, font, base_color, hovering_color):
        # Una tupla que especifica la posición (x, y) del botón en la pantalla.
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        # font: La fuente utilizada para renderizar el texto.
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        # text_input: El texto que se muestra en el botón.
        self.text_input = text_input
        # renderiza el texto del botón utilizando la fuente y los colores base especificados.
        self.text = self.font.render(self.text_input, True, self.base_color)
        # obtiene un rectángulo que enmarca el texto renderizado, utiliza las cordenas (x, y)
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.text, self.text_rect)
        # actualizar y dibujar el botón en la pantalla

    def check_for_input(self, position):
        if position[0] in range(self.text_rect.left, self.text_rect.right) \
                and position[1] in range(self.text_rect.top, self.text_rect.bottom):
            return True
        return False
        # verifica si se ha hecho clic en el botón

    def change_color(self, position):
        if position[0] in range(self.text_rect.left, self.text_rect.right) \
                and position[1] in range(self.text_rect.top, self.text_rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
