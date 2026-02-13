import pygame  # Game library

# import
from button_01 import Button

# ----------------------------
# SETUP
# ----------------------------

pygame.init()  # Initialize all pygame modules

# SCREEN
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)  # Dinamic Window height
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create window

pygame.display.set_caption("Program Name")  # Window title

# FPS
clock = pygame.time.Clock()  # Controls FPS
FPS = 60

# FONTS
# Knewava
knewava_font = pygame.font.SysFont("Knewave", 40)
# Ravie
ravie_font = pygame.font.SysFont("Ravie", 40)
# Comic Sans MS
comic_sans_ms_font = pygame.font.SysFont("Comic Sans MS", 40)
# Courgette
forte_font = pygame.font.SysFont("Forte", 40)
# Epilog
epilog_font = pygame.font.SysFont("Epilog", 40)

# COLORS
BLUE_COLOR = (11, 43, 65)
GREEN_COLOR = (25, 60, 65)
RED_COLOR = (89, 28, 33)
YELLOW_COLOR = (242, 183, 5)

BG_COLOR = (50, 100, 150)

# VARIABLES

running = True  # Main loop control

click_counter = 0

# BUTTONS
start_button = Button(x=200,y=550,width=120,height=60,text="Click Me",font=knewava_font,button_color=RED_COLOR, hover_color=YELLOW_COLOR,click_color= GREEN_COLOR,text_color=(0,0,0))

# FUNCTIONS
def draw_text(text, font, text_color, x, y, centered_x=False):
    img = font.render(text, True, text_color)

    if centered_x:
        x = (screen.get_width() - img.get_width()) // 2

    screen.blit(img, (x, y))

# ----------------------------
# MAIN LOOP
# ----------------------------

while running:

    # ----------------------------
    # EVENTS
    # ----------------------------

    # EVENTS (keyboard, mouse, window)
    for event in pygame.event.get():

        # Close the window (X button)
        if event.type == pygame.QUIT:
            running = False

        # KEYDOWN happens ONCE when a key is pressed
        if event.type == pygame.KEYDOWN:

            # Press ESC to quit
            if event.key == pygame.K_ESCAPE:
                running = False

        # KEYUP happens ONCE when a key is released
        if event.type == pygame.KEYUP:
            pass  # Placeholder for future logic

    # ----------------------------
    # RENDERING
    # ----------------------------

    # Render everything
    screen.fill(BG_COLOR)  # Clear screen every frame

    # Other rendering
    if start_button.draw(screen=screen):
        click_counter += 1

    draw_text(f"You clicked START: {click_counter} times.", knewava_font, RED_COLOR, 50, 100, True)
    


    pygame.display.update()  # Show frame

    # FPS LIMIT
    clock.tick(FPS)

# ----------------------------
# CLEANUP
# ----------------------------

pygame.quit()  # Close pygame safely
quit()         # Exit program


