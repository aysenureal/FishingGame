import pygame, random

# Initialize Pygame	
pygame.init()

# Set up the display
width, height = 750, 750
window = pygame.display.set_mode((width, height))

# FPS and clock
FPS = 30
time = pygame.time.Clock()

# Classes
class Game():
    def __init__(self, fisher, fish_group):
        #Objects
        self.fisher = fisher
        self.fish_group = fish_group
        # Game variables
        self.time = 0
        self.fps_value = 0
        self.level_no = 0
        #Fishes
        fish1 = pygame.image.load("fish1.png")
        fish2 = pygame.image.load("fish2.png")
        fish3 = pygame.image.load("fish3.png")
        fish4 = pygame.image.load("fish4.png")
        self.fish_list = [fish1, fish2, fish3, fish4]
        self.fish_list_index_no = random.randint(0, len(self.fish_list) - 1)
        self.target_fish_image = self.fish_list[self.fish_list_index_no]
        self.target_fish_location = self.target_fish_image.get_rect()
        self.target_fish_location.top = 40
        self.target_fish_location.centerx = width // 2

    def update(self):
        self.fps_value +=1
        if self.fps_value == FPS:
            self.time += 1
            self.fps_value = 0
    def draw(self):
        window.blit(self.target_fish_image, self.target_fish_location)
    def contact(self):
        pass
    def game_over(self):
        pass
    def reset(self):
        pass
    def safe(self):
        pass
    def refresh_fish(self):
        pass
    def aim(self):
        pass


class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y, fish_img, tip):
        super().__init__()
        # Load the fish image and set its rect
        self.image = fish_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.tip = tip
        self.speed = random.randint(1, 5)
        self.direction_x = random.choice([-1, 1])
        self.direction_y = random.choice([-1, 1])

       
    def update(self):
        # Move the fish in a random direction
        self.rect.x += self.speed * self.direction_x
        self.rect.y += self.speed * self.direction_y
        
        # Bounce off the walls
        if self.rect.left < 0 or self.rect.right >= width:
            self.direction_x *= -1
        if self.rect.top < 0 or self.rect.bottom >= height:
            self.direction_y *= -1

class Fisher(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("fisher.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.lives = 3 # Number of lives
        self.speed = 10  # Speed of the fisher
    
    def update(self):
        self.moving()
    def moving(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_UP]:
            self.rect.y -= self.speed
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.speed

# Main character group operations
fisher_group = pygame.sprite.Group()
fisher = Fisher(width // 2, height // 2)
fisher_group.add(fisher)

#Fish test
fish1 = pygame.image.load("fish1.png")
fish_group = pygame.sprite.Group()
fish = Fish(random.randint(0, width - 32), random.randint(0, height - 32), fish1, 0)
fish_group.add(fish)

fish2 = pygame.image.load("fish2.png")
fish = Fish(random.randint(0, width - 32), random.randint(0, height - 32), fish2, 0)
fish_group.add(fish)

fish3 = pygame.image.load("fish3.png")
fish = Fish(random.randint(0, width - 32), random.randint(0, height - 32), fish3, 0)
fish_group.add(fish)

fish4 = pygame.image.load("fish4.png")
fish = Fish(random.randint(0, width - 32), random.randint(0, height - 32), fish4, 0)
fish_group.add(fish)


#Game Class
game = Game(fisher_group, fish_group)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((0, 0, 0))  # Clear the screen with black
    
    # Game Mechanic
    game.update()
    game.draw()
    # Fisher draw and update
    fisher_group.update()
    fisher_group.draw(window)
    # Fish test
    fish_group.update()
    fish_group.draw(window)
   
    # Update the display
    pygame.display.update()
    # Cap the frame rate
    time.tick(FPS)

# Quit Pygame
pygame.quit()