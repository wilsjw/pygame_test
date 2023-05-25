import pygame


class Player(pygame.Rect):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.health = 100.0
        self.speed = 3.0
        self.velocity = pygame.Vector2(0, 0)

        self.jumpHeight = 10.0
        self.MAX_JUMPS = 3
        self.jumps = 0
        self.jumpCooldown = 0

    def Move(self):
        self.x += self.velocity.x
        self.y += self.velocity.y

    def Jump(self):
        self.velocity.y = -self.jumpHeight
        self.jumps += 1

    def TakeDamage(self, damage):
        if self.health > 0:
            self.health -= damage

        if self.health <= 0:
            self.health = 0


def Update():
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    clock = pygame.time.Clock()
    running = True

    player = Player(screen.get_width() / 2.0, screen.get_height() / 2.0, 50.0, 50.0, (255, 0, 0))

    count = 0
    GRAVITY = 0.5
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        # Game loop starts here
        pygame.draw.rect(screen, player.color, player)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        if player.health > 0:
            count += 1
            if count >= 60:
                player.TakeDamage(10.0)
                count = 0

            player.velocity.y += GRAVITY
            if player.y + player.height >= screen.get_height():
                player.y = screen.get_height() - player.height
                player.velocity.y = 0
                player.jumps = 0

            if player.jumpCooldown > 0:
                player.jumpCooldown -= 1
            if keys[pygame.K_SPACE] and player.jumps < player.MAX_JUMPS:
                if player.jumpCooldown <= 0:
                    player.Jump()
                    player.jumpCooldown = 15

            if keys[pygame.K_a]:
                player.velocity.x = -1 * player.speed
            if keys[pygame.K_d]:
                player.velocity.x = 1 * player.speed
            if not keys[pygame.K_a] and not keys[pygame.K_d]:
                player.velocity.x = 0

            if player.x < 0:
                player.x = 0
            if player.x + player.width > screen.get_width():
                player.x = screen.get_width() - player.width

            player.Move()
        else:
            player.color = (30, 30, 30)

        # Game loop ends here

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    Update()
