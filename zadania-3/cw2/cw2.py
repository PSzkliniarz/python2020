import pygame, sys
pygame.init()

def main():
    clock = pygame.time.Clock()

    pygame.display.set_caption('Icy tower ball')
    icon = pygame.image.load('ball.gif')
    pygame.display.set_icon(icon)

    # pygame.mixer.music.load(r'D:\.studia\.5_Semestr\python\python-zadania\python2020\zadania-3\cw1\icy_tower.mp3')
    # pygame.mixer.music.play(-1)

    size = width, height = 1000, 700
    screen = pygame.display.set_mode(size)

    speed = [0, 0]
    accel = [1,  9.81]

    image = pygame.image.load(r'skatepark.jpg')
    image = pygame.transform.scale(image, size)

    surf_center = (
        (width - image.get_width()) / 2,
        (height - image.get_height()) / 2
    )
    screen.blit(image, surf_center)

    ball = pygame.image.load('ball.gif')
    ball = pygame.transform.scale(ball, (ball.get_width()//2, ball.get_height()//2))


    screen.blit(ball, (width/2, height/2))

    ballrect = ball.get_rect(center = (width/2,height/2))


    pygame.display.flip()

    while True:

        clock.tick(60)
        #print(clock.get_fps())
        pygame.time.delay(50)

        speed[1] = speed[1] + accel[1] * 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            sys.exit()

        # if keys[pygame.K_DOWN]:
        #     speed[1] = speed[1] + accel[1] * 1

        if keys[pygame.K_UP]:
            speed[1] -= accel[1] * 2

        if keys[pygame.K_LEFT]:
            speed[0] -= accel[0] * 1

        if keys[pygame.K_RIGHT]:
            speed[0] += accel[0] * 1

        if keys[pygame.K_SPACE]:
            speed[1] = 0

        ballrect = ballrect.move(speed)

        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]

        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]



        screen.blit(image,surf_center)
        screen.blit(ball,ballrect)
        pygame.display.flip()

        # print(event)

if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()