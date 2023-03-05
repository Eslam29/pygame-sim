# Import and initialize pygame.
import pygame
import random
import math
import numpy as np 
pygame.font.init()
# -------------------------------------------------------------------------
def make_window(width: int, height: int, caption: str) -> pygame.Surface:
    """Create and return a pygame window."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen
textfont = pygame.font.SysFont("monospace",30)
#-------------------------------------------------------------------------
def main() -> None:
    """Move an image randomly on the screen."""
    # Annotate and initialize variables.
    SCREEN_SIZE: int = 480
    screen: pygame.Surface
    background: pygame.Surface
    image: pygame.surface
    radar:pygame.surface
    user_quit: bool = False
    e: pygame.event.Event
    counter: int = 0
    imagex: int = 0
    imagey: int = 0
    radarx1: int =400
    radary1: int =400
    """ dx: int = 10
    dy: int = 10 """
    # Set up assets.
    screen = make_window(SCREEN_SIZE, SCREEN_SIZE, "Basic Motion")
    background = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    background.fill((222, 237, 244))
    image = pygame.image.load("images.jpg")
    image = image.convert()
    radar = pygame.image.load("radar.gif")
    radar=radar.convert()
    imagey = random.randint(0,300)
    clock: pygame.time.Clock = pygame.time.Clock()
    Black=(0,0,0)
# -------------------------------------------------------------------------
    while not user_quit:                         # Loop 30 times per second
        clock.tick(30)
        background.fill((255,255,255))
        for e in pygame.event.get():             # Process a quit choice.
            if e.type == pygame.QUIT:
                user_quit = True
        # Change x and y.
        imagex += 5
        imagey += 0 
        startx=400; starty=400; endx=0; endy=400; width=2; 
        pygame.draw.line(background,(0,0,0),(startx,starty),(endx,endy),width)
        pygame.draw.line(background,(0,0,0),(imagex,imagey),(480,imagey),width=2)
        pygame.draw.line(background,(0,0,0),(radarx1,radary1),(imagex,imagey),width=2)   
        if imagex==480:
            break
        angle=0
        x1,y1=(radarx1,radary1)
        x2,y2=(imagex,imagey)
        x3,y3=(0,400)
        radian = np.arctan2(y2-y1,x2-x1)-np.arctan2(y3-y1,x3-x1)
        angle = np.abs(radian*180/np.pi)
        text = textfont.render(f"Angle : {int(abs(360)-(angle))}",1,(0,0,0))
        background.blit(text,(150,350)) 
        screen.blit(background, (0, 0))              # Draw to the screen and show.
        screen.blit(image, (imagex, imagey))         # Draw to the screen and show.
        screen.blit(radar,(radarx1,radary1))         # Draw to the screen and show.
        pygame.display.update()
    pygame.quit()
main()