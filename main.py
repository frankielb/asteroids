import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH,ASTEROID_KINDS,ASTEROID_MAX_RADIUS,ASTEROID_MIN_RADIUS,ASTEROID_SPAWN_RATE
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    pygame.init()
    print('Starting asteroids!')
    #print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for u in updatable:
            u.update(dt)
        
        for a in asteroids:
            if a.collision(player):
                print('Game over!')
                return
        screen.fill((0,0,0))
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == '__main__':
    main()