import pygame  # Game library

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

# COLORS
BG_COLOR = (50,100,150)

# VARIABLES

running = True  # Main loop control

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

    # ----------------------------
    # RENDERING
    # ----------------------------

    # Render everything
    screen.fill(BG_COLOR)  # Clear screen every frame

    pygame.display.update()  # Show frame

    # FPS LIMIT
    clock.tick(FPS)
