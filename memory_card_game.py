import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Card Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (255, 165, 0),  # Orange
    (128, 0, 128)   # Purple
]

# Game variables
card_width, card_height = 100, 100
margin = 20
rows, cols = 4, 4
cards = []
revealed = []
selected = []
matched = []
font = pygame.font.Font(None, 36)
score = 0

# Create cards
for color in COLORS * 2:  # Each color appears twice
    cards.append(color)
random.shuffle(cards)

# Initialize revealed and matched lists
revealed = [False] * len(cards)
matched = [False] * len(cards)

# Draw cards
for i in range(len(cards)):
    row = i // cols
    col = i % cols
    card_x = col * (card_width + margin) + margin
    card_y = row * (card_height + margin) + margin
    
    if revealed[i] or matched[i]:
        pygame.draw.rect(screen, cards[i], (card_x, card_y, card_width, card_height))
    else:
        pygame.draw.rect(screen, GRAY, (card_x, card_y, card_width, card_height))
    
    pygame.draw.rect(screen, BLACK, (card_x, card_y, card_width, card_height), 2)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(60)