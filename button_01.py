import pygame  # Game library

# ----------------------------
# BUTTON CLASS
# ----------------------------

class Button:
    def __init__(self, x, y, width, height, text, font,
                 button_col, hover_color, click_color, text_color):
        """
        Button Constructor

        x, y           → Top-left position of button
        width, height  → Minimum size of button
        text           → Text displayed on button
        font           → Pygame font object
        button_col     → Default color
        hover_color    → Color when mouse is over button
        click_color    → Color while mouse button is pressed
        text_color     → Color of text
        """

        # Position
        self.x = x
        self.y = y

        # Minimum size (button can grow if text is larger)
        self.min_width = width
        self.min_height = height

        # Text settings
        self.text = text
        self.font = font

        # Colors
        self.button_col = button_col
        self.hover_col = hover_color
        self.click_col = click_color
        self.text_col = text_color

        # Internal state (tracks mouse press)
        self.clicked = False


    def draw(self, screen):
        """
        Draws the button and handles mouse interaction.

        Returns:
            True  → when button is clicked (on mouse release)
            False → otherwise
        """

        action = False

        # Get current mouse position
        pos = pygame.mouse.get_pos()

        # ----------------------------
        # TEXT RENDERING
        # ----------------------------

        # Render the text surface
        text_img = self.font.render(self.text, True, self.text_col)

        # Get text size
        text_w = text_img.get_width()
        text_h = text_img.get_height()

        # ----------------------------
        # AUTO-SIZE LOGIC
        # ----------------------------

        # Button grows if text is larger than minimum size
        width = max(self.min_width, text_w + 20)     # 20px horizontal padding
        height = max(self.min_height, text_h + 10)   # 10px vertical padding

        # Create button rectangle
        button_rect = pygame.Rect(self.x, self.y, width, height)

        # ----------------------------
        # MOUSE INTERACTION
        # ----------------------------

        # Check if mouse is over button
        if button_rect.collidepoint(pos):

            # If left mouse button is being held down
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(screen, self.click_col, button_rect)
                self.clicked = True

            # If mouse button was released
            else:
                if self.clicked:
                    action = True  # Register click action

                pygame.draw.rect(screen, self.hover_col, button_rect)
                self.clicked = False

        else:
            # Default button color when not hovered
            pygame.draw.rect(screen, self.button_col, button_rect)
            self.clicked = False

        # ----------------------------
        # BORDER / SHADING EFFECT
        # ----------------------------

        # Light top/left edges
        pygame.draw.line(screen, (255, 255, 255),
                         button_rect.topleft, button_rect.topright, 2)
        pygame.draw.line(screen, (255, 255, 255),
                         button_rect.topleft, button_rect.bottomleft, 2)

        # Dark bottom/right edges
        pygame.draw.line(screen, (0, 0, 0),
                         button_rect.bottomleft, button_rect.bottomright, 2)
        pygame.draw.line(screen, (0, 0, 0),
                         button_rect.topright, button_rect.bottomright, 2)

        # ----------------------------
        # CENTER TEXT INSIDE BUTTON
        # ----------------------------

        text_rect = text_img.get_rect(center=button_rect.center)
        screen.blit(text_img, text_rect)

        return action
