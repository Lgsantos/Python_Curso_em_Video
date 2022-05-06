# import pygame
#
# pygame.init()
# pygame.mixer_music.load("Mon.ogg")
# pygame.mixer_music.play()
# pygame.event.wait()

from pygame import mixer
mixer.init()
mixer.music.load("Mon.mp3")
mixer.music.play()
import time
time.sleep(10) #toca apenas 10 segundos da música
mixer.quit()
