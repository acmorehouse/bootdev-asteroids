from circleshape import CircleShape
from shot import Shot
import pygame
import constants

# from main import dt

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x_pos = x
        self.y_pos = y
        self.radius = radius
        self.rotation = 0
        self.shoot_cooldown = 0

        # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, delta_time):
        self.rotation += (constants.PLAYER_TURN_SPEED * delta_time)

    def move(self, delta_time):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * delta_time
        self.position += rotated_with_speed_vector
    
    def shoot(self):
        if self.shoot_cooldown > 0:
            pass
        else:
            self.shoot_cooldown = constants.PLAYER_SHOOT_COOLDOWN_SECONDS
            shooter = Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)
            unit_vector = pygame.Vector2(0, 1)
            rotated_vector = unit_vector.rotate(self.rotation)
            shooter.velocity = rotated_vector * constants.PLAYER_SHOOT_SPEED
    
    def update(self, dt):
        self.shoot_cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()