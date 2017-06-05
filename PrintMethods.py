"""
Functions to print game information on the gameplay screen
Function to print gameover information
"""
import pygame, sys, InputBox, GlobVar, random


#Method to show the remaining lives
def printLife(num):
    s = pygame.Surface((num*20,20))
    s.set_alpha(128)             
    s.fill((255,255,255))
    GlobVar.screen.blit(s, (10,10))
    
    
#Method to print the score
def printScore(num):
    font=pygame.font.Font(GlobVar.format_path("resources/fonts/namco__.ttf"), 20)
    text="score: %d" % (num)
    scoreboard=font.render(text, 1, (150, 200, 200))
    rect=scoreboard.get_rect()
    rect.right=GlobVar.width
    rect.y=10
    GlobVar.screen.blit(scoreboard, rect)


#Method to print the game level reached
def printLevel(num):
    font=pygame.font.Font(GlobVar.format_path("resources/fonts/namco__.ttf"), 20)
    text="level: %d" % (num)
    scoreboard=font.render(text, 1, (150, 200, 200))
    rect=scoreboard.get_rect()
    rect.center=(500,20)
    GlobVar.screen.blit(scoreboard, rect)      
        

#Method to print Game over
def printGameover(score, _type):
    font=pygame.font.Font(GlobVar.format_path("resources/fonts/blade.ttf"), 80)
    text="Game  Over"
    gameover=font.render(text, 1, (200, 200, 200))
    rect=gameover.get_rect()
    rect.center=(500,300)
    GlobVar.screen.blit(gameover, rect)
    holder=''
    with open(GlobVar.format_path("resources/highscore"+str(_type)+".txt"), 'r+') as scorefile:
        highest=int(scorefile.readline())
        holder=str(scorefile.readline())
        if highest<score:
            InputBox.InputName()
            scorefile.seek(0)
            scorefile.write("%d\n" % score)
            scorefile.write(GlobVar.Name)
            scorefile.truncate()
            highest=score
            holder=GlobVar.Name
    font=pygame.font.Font(GlobVar.format_path("resources/fonts/namco__.ttf"), 20)
    text="highest score"
    highscore=font.render(text, 1, (200, 200, 200))
    rect=highscore.get_rect()
    rect.center=(500,500)
    GlobVar.screen.blit(highscore, rect)

    text="%s  %d" % (str.lower(str(holder)), highest)
    highscore=font.render(text, 1, (200, 200, 200))
    rect=highscore.get_rect()
    rect.center=(500,550)
    GlobVar.screen.blit(highscore, rect)

#creating the stars
def initializeStars():
    global stars
    stars = []
    for i in range(300):
        star = [random.randrange(0, GlobVar.width - 1), random.randrange(0, GlobVar.height - 1)]
        stars.append(star)


#moving the stars around
def printStars():
    global stars
    for star in stars:
        star[1]+= 2
        if star[1] >= GlobVar.height:
            star[1] = 0
            star[0] = random.randrange(0, 1000)

        GlobVar.screen.set_at(star, (255, 255, 255))
#Settings menu
def Settings():
    pygame.mixer.music.fadeout(1000)
