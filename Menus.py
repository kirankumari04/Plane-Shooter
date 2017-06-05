import pygame, sys
import Game, GlobVar


#Menu background
def SetMenuBackground():
    image=pygame.image.load(GlobVar.format_path("resources/images/menuback2.jpg")).convert()
    rect=image.get_rect()
    rect.center=(500,300)
    GlobVar.screen.blit(image,rect)
    pygame.display.flip()


#Main menu
def mainMenu():
    while 1:
        SetMenuBackground()
        list1=["Continue", "New Game", "Quit"]
        list2=["New Game", "Quit"]
        selected=0
        if GlobVar.over==True:
            selected=Menu_Screen(list2)
            if selected==0:
                new_game_menu()
            elif selected==1:
                pygame.quit()
                sys.exit()
            else:
                return
        else:
            selected=Menu_Screen(list1)
            if selected==0 or selected==-1:
                return
            if selected==1:
                new_game_menu()
            elif selected==2:
                pygame.quit()
                sys.exit()

                
"""
#Reset high score
def reset_score_menu():
    SetMenuBackground()
    menulist=["Mission", "Challenge", "Back"]
    selected=Menu_Screen(menulist)
    if selected==0:
        resetScore(1)
    elif selected==1:
        resetScore(2)
    else:
        return

#Method to reset highest scores to zero
def resetScore(_type):
    with open(GlobVar.format_path("resources/highscore"+str(_type)+".txt"), 'r+') as scorefile:
        scorefile.seek(0)
        scorefile.write("0\n")
        scorefile.truncate()

    resetAck()

#Reset acknowledgement menu
def resetAck():
    SetMenuBackground()
    font=pygame.font.Font(GlobVar.format_path("resources/fonts/game_font_7.ttf"), 30)
    color=(300,100,200,255)
    text="Score reset"
    show=font.render(text, 1, color, None)
    rect=show.get_rect()
    rect.center=(500,200)
    GlobVar.screen.blit(show,rect)
    menulist=["Back"]
    selected=Menu_Screen(menulist)
    return
"""
    
#New game menu
def new_game_menu():
    #pygame.mixer.music.fadeout(2000)
    SetMenuBackground()
    menulist=["Mission", "Challenge", "Back"]
    selected=Menu_Screen(menulist)
    if selected==0:
        Mission()
    elif selected==1:
        Challenge()
    else:
        return
            

#Game menu
def Menu_Screen(menulist):
    font=pygame.font.Font(GlobVar.format_path("resources/fonts/game_font_7.ttf"), 30)
    selected=0
    highlighted=(250,200,0)
    normal=(150,100,0)
    while 1:
        ypos=250
        for i in range(len(menulist)):
            text=menulist[i]
            if i==selected:
                color=highlighted
            else:
                color=normal
            show=font.render(text, 1, color)
            rect=show.get_rect()
            rect.center=(500,ypos)
            ypos+=50
            GlobVar.screen.blit(show,rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    return -1
                elif event.key==pygame.K_DOWN:
                    if selected<len(menulist)-1:
                        selected+=1
                elif event.key==pygame.K_UP:
                    if selected>0:
                        selected-=1
                elif event.key==pygame.K_RETURN:
                    return selected
                
                        
    
#First type game
def Mission():
    SetMenuBackground()
    font=pygame.font.Font(GlobVar.format_path("resources/fonts/blade.ttf"), 25)
    text="MISSION"
    show=font.render(text, 1, (250,180,0))
    rect=show.get_rect()
    rect.center=(500,200)
    GlobVar.screen.blit(show, rect)
    pygame.display.flip()
    menulist=["Start", "Back"]
    selected=Menu_Screen(menulist)
    if selected==0:
        Game.start_game(1)
    new_game_menu()



#Second type game
def Challenge():
    SetMenuBackground()
    font=pygame.font.Font(GlobVar.format_path("resources/fonts/blade.ttf"), 25)
    text="CHALLENGE"
    show=font.render(text, 1, (150,100,0))
    rect=show.get_rect()
    rect.center=(500,200)
    GlobVar.screen.blit(show, rect)
    pygame.display.flip()
    menulist=["Start", "Back"]
    selected=Menu_Screen(menulist)
    if selected==0:
        Game.start_game(2)
    new_game_menu()

