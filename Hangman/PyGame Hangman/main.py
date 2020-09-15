import pygame

#setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
windows = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman")

#load images
images = []
for i in range(7):
    image = pygame.image.load('D:\Programing\Python\Python_Learning\Hangman\PyGame Hangman\hangman' + str(i) + '.png')
    images.append(image)

#game variables
hangman_status = 0

#colors
WHITE = (255,255,255)

#setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)

    windows.fill(WHITE)
    windows.blit(images[hangman_status], (150,100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()