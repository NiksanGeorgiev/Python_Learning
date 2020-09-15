import pygame
import math

#setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
windows = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman")

#button variables
RADIUS = 20
GAP = 15
letters = []
startX = round((WIDTH-(RADIUS*2+GAP)*13)/2)
startY = 400
A = 65
for i in range(26):
    x = startX + GAP * 2 + (RADIUS * 2 + GAP) * (i % 13)
    y = startY + ((i // 13)) * (GAP+RADIUS*2)
    letters.append([x, y, chr(A + i), True])

#load images
images = []
for i in range(7):
    image = pygame.image.load('D:\Programing\Python\Python_Learning\Hangman\PyGame Hangman\hangman' + str(i) + '.png')
    images.append(image)

#game variables
hangman_status = 0
word = "DEVELOPER"
guessed = []

#fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)

#setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    windows.fill(WHITE)

    #draw words
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word +="_ "
    

    #draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(windows, BLACK, (x,y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            windows.blit(text,(x - text.get_width()/2, y - text.get_height()/2))


    
    windows.blit(images[hangman_status], (150,100))
    pygame.display.update()

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x,y, ltr, visible = letter
                if visible:
                    distance = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if distance < RADIUS:
                        letter[3] = False     

    draw()

 

                 
            

pygame.quit()