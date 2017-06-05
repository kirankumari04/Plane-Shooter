#Player name input
import pygame, Menus, GlobVar, sys
from pygame.locals import *


#Print the text prompt
def InputPrompt(pos):
    image=pygame.Surface([12,3])
    image.fill((255,255,255))
    rect=image.get_rect()
    rect.center=pos
    GlobVar.screen.blit(image,rect)

def InputName():
    Menus.SetMenuBackground()
    #global Name
    GlobVar.Name=''
    MAX=12
    font=pygame.font.Font(GlobVar.format_path("resources/fonts/game_font_7.ttf"), 30)
    text="please enter your name:"
    show=font.render(text,1,(150,100,0))
    rect=show.get_rect()
    rect.center=(500,250)
    GlobVar.screen.blit(show,rect)

    surface=pygame.Surface([300,50])
    pygame.display.flip()

    while 1:
        surface.fill((0,0,0))
        GlobVar.screen.blit(surface,(350,300))
        show=font.render(GlobVar.Name,1,(150,200,150))
        rect=show.get_rect()
        rect.left=380
        rect.bottom=340
        GlobVar.screen.blit(show, rect)
        InputPrompt((rect.right,rect.bottom))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==K_RETURN:
                    if len(GlobVar.Name)>0:
                        return
                elif event.key==K_BACKSPACE:
                    GlobVar.Name=GlobVar.Name[:-1]
                elif len(GlobVar.Name)<MAX:
                    GlobVar.Name=GlobVar.Name+event.unicode

        pygame.display.flip()
