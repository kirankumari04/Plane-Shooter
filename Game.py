import sys, pygame, random, time
from pygame.locals import *
import Objects, PrintMethods, Menus, GlobVar


#Start of a new game
def start_game(_type):
    pygame.mixer.music.fadeout(2000)
    GlobVar.reset()
    #global level
    GlobVar.level=1
    last=time.time()
    #global over
    GlobVar.over=False
    enemyLatency=50
    counter=0
    interval=0
    boonLatency=1000.0
    if _type==2:
        boonLatency=500.0
    timeforboon=random.randrange(100,int(boonLatency))


    player=Objects.Player()

    playerSprite = pygame.sprite.RenderPlain((player))

    enemyExplode=pygame.mixer.Sound(GlobVar.format_path("resources/audio/elaser.ogg"))
    playerExplode=pygame.mixer.Sound(GlobVar.format_path("resources/audio/grib.wav"))
    boon=pygame.mixer.Sound(GlobVar.format_path("resources/audio/boon.wav"))
    volume=boon.get_volume()
    global shoot
    shoot=pygame.mixer.Sound(GlobVar.format_path("resources/audio/laser.wav"))
    
        
    done=False

    clock=pygame.time.Clock()

    score=0
    no_of_life=5.0

    PrintMethods.initializeStars()
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    Menus.mainMenu()
                elif event.key==pygame.K_LEFT:
                    player.dx=-10
                elif event.key==pygame.K_RIGHT:
                    player.dx=10
                elif event.key==pygame.K_m:
                    if boon.get_volume()>0:
                        enemyExplode.set_volume(0)
                        playerExplode.set_volume(0)
                        boon.set_volume(0)
                    else:
                        enemyExplode.set_volume(volume)
                        playerExplode.set_volume(volume)
                        boon.set_volume(volume)
            elif event.type==KEYUP:
                if event.key==K_LEFT:
                    player.dx=0
                elif event.key==K_RIGHT:
                    player.dx=0


        """
        updating the positions of
        the sprites on the screen
        """
        GlobVar.screen.fill((0,0,0))
        PrintMethods.printStars()
        playerSprite.update()
        GlobVar.enemyList.update()
        GlobVar.playerBulletList.update()
        GlobVar.enemyBulletList.update()
        GlobVar.explosionList.update()
        GlobVar.lifeReceipt.update()
        GlobVar.lifeList.update()

        #draw
        playerSprite.draw(GlobVar.screen)
        GlobVar.enemyList.draw(GlobVar.screen)
        GlobVar.playerBulletList.draw(GlobVar.screen)
        GlobVar.enemyBulletList.draw(GlobVar.screen)
        GlobVar.explosionList.draw(GlobVar.screen)
        GlobVar.lifeReceipt.draw(GlobVar.screen)
        GlobVar.lifeList.draw(GlobVar.screen)

        if no_of_life>0:
            PrintMethods.printLife(no_of_life)
        PrintMethods.printScore(score)
        PrintMethods.printLevel(GlobVar.level)

        if GlobVar.over==True:
            PrintMethods.printGameover(score, _type)
        else:
            #Spawning new enemies
            now=time.time()
            elapsed=now-last
            if elapsed>60:
                enemyLatency-=15
                last=now
                GlobVar.level+=1
                GlobVar.screen.fill((0,0,0))
                pygame.display.update()
            counter+=1
            if counter>enemyLatency:
                GlobVar.enemyList.add(Objects.Enemy(_type))
                counter=0

            #Sending new lives
            interval+=GlobVar.level
            if interval>timeforboon:
                GlobVar.lifeList.add(Objects.Life())
                timeforboon=random.randrange(100,int(boonLatency))
                interval=0


            #collision between player's bullets and enemies
            for bullet in GlobVar.playerBulletList:
                planeCollisions=pygame.sprite.spritecollide(bullet,GlobVar.enemyList,True)
                for plane in planeCollisions:
                    GlobVar.explosionList.add(Objects.Explosion(plane.rect.center,"enemy"))
                    GlobVar.playerBulletList.remove(bullet)
                    GlobVar.enemyList.remove(plane)
                    score+=10
                    enemyExplode.play()


            #collision between player and enemies' bullets
            playerCollisions=pygame.sprite.spritecollide(player,GlobVar.enemyBulletList,True)
            for bullet in playerCollisions:
                GlobVar.explosionList.add(Objects.Explosion(player.rect.center,"player"))
                no_of_life-=boonLatency/1000.0
                playerExplode.play()
                if no_of_life==0:
                    playerSprite.remove(player)
                    GlobVar.over=True
                    break

            #collision between player and enemies
            playerCollisions=pygame.sprite.spritecollide(player,GlobVar.enemyList,False)
            for plane in playerCollisions:
                GlobVar.explosionList.add(Objects.Explosion(player.rect.center,"player"))
                playerExplode.play()
                GlobVar.enemyList.remove(plane)
                score+=10
                no_of_life-=boonLatency/1000.0
                if no_of_life==0:
                    playerSprite.remove(player)
                    GlobVar.over=True
                    break

            #collision between player and life
            lifeCollisions=pygame.sprite.spritecollide(player,GlobVar.lifeList,False)
            for life in lifeCollisions:
                GlobVar.lifeReceipt.add(Objects.AttainLife((player.rect.centerx, player.rect.top)))
                GlobVar.lifeList.remove(life)
                no_of_life+=1
                boon.play()

        pygame.display.flip()    
        clock.tick(60)
        
