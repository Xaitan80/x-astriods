import pygame
from constants import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        rotation_delta = PLAYER_TURN_SPEED * dt
        self.rotation = self.rotation + rotation_delta

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_timer = self.shoot_timer - dt

        if keys[pygame.K_a]:

            self.rotate(-dt) #rotate left

        if keys[pygame.K_d]:

            self.rotate(dt) #rotate right
        
        if keys[pygame.K_w]:

            self.move(dt)

        if keys[pygame.K_s]:

            self.move(-dt)
        
        if  keys[pygame.K_SPACE]:
            #print("Spacebar pressed")

            self.shoot()
            # ?
    def shoot(self):
        if self.shoot_timer > 0:
            return
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = forward * PLAYER_SHOOT_SPEED
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = velocity
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN





