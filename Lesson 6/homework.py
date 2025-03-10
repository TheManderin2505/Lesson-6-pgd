import pygame
import time

pygame.init()

screen = pygame.display.set_mode((500,500))

bgimg = pygame.image.load("space1.jpg")
playerimg = pygame.image.load("ship.png")

playerx = 100
playery = 10

keys = [False,False,False,False]

while playery < 400:
    screen.fill((0,0,0))
    screen.blit(bgimg,(0,0))
    screen.blit(playerimg,(playerx,playery))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        
        if event.type == pygame.KEYDOWN: #pressed
            if event.key == pygame.K_UP:
                keys[0] = True
            
            if event.key == pygame.K_DOWN:
                keys[2] = True

            if event.key == pygame.K_RIGHT:
                keys[3] = True

            if event.key == pygame.K_LEFT:
                keys[1] = True

        if event.type == pygame.KEYUP: #key relessed
            if event.key == pygame.K_UP:
                keys[0] = False
            
            if event.key == pygame.K_DOWN:
                keys[2] = False

            if event.key == pygame.K_RIGHT:
                keys[3] = False

            if event.key == pygame.K_LEFT:
                keys[1] = False

    if keys[0]: #up
        if playery > 0:
            playery -= 7

    if keys[2]: #down
        if playery < 499:
            playery += 7

    if keys[1]: #left
        if playerx > 0:
            playerx -= 7

    if keys[3]: #right
        if playerx < 499:
            playerx += 7
    

    playery += 5
    time.sleep(0.05)

print("game over")