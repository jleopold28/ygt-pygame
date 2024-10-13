# import libraries
import pygame
import random
import time

# Import pygame.locals for access to key coordinates
# allows us to reference K_UP instead of pygame.K_UP
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# define constant variables for screen height and width
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Download link - https://kenney.nl/assets/space-shooter-redux
        # using convert_alpha since there already is a transparent background
        self.surf = pygame.image.load("img/playerShip2_green.png").convert_alpha()
        # rotate player model
        self.surf = pygame.transform.rotate(self.surf, 270)
        # scale down player
        self.surf = pygame.transform.scale(
            self.surf,
            (int(self.surf.get_size()[0])/1.5 , int(self.surf.get_size()[1]/1.5))
        )
        self.rect = self.surf.get_rect()
    
    def update(self, pressed_keys):
        # move_ip = move in place 
        # use self.rect.move_ip(X,Y) to change position
        if pressed_keys[K_UP]:
            # TODO:
            # Move the player up 8 pixels
            # play the move_up_sound
        if pressed_keys[K_DOWN]:
            # TODO:
            # Move the player down 8 pixels
            # play the move_down_sound
        if pressed_keys[K_LEFT]:
            # TODO:
            # Move the player left 8 pixels
        if pressed_keys[K_RIGHT]:
            # TODO:
            # Move the player right 8 pixels

        # keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Create an enemy class by extending pygame.sprite.Sprite
# The surface drawn on screen will be an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load("img/enemyRed5.png").convert_alpha()
        # rotate enemy sprite
        self.surf = pygame.transform.rotate(self.surf, 270)
        # scale down enemy
        self.surf = pygame.transform.scale(
            self.surf,
            (int(self.surf.get_size()[0])/3, int(self.surf.get_size()[1]/3))
        )
        # update rect to be a random location
        # center of the rectangle is off screen (b/w 20 and 100 pixels away from right edge)
        # somewhere between top and bottom edges (height)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        # speed is random number between 2 and 20
        self.speed = random.randint(2, 10)

    # move the sprite based on speed
    # remove the sprite if it passes left edge of screen
    def update(self):
        # TODO: 
        # move the enemy based on speed
        # enemies move from right to left
        # when the enemy is fully off screen, kill enemy

# Create a class for moving stars
class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # size is 1x1 pixels and color is white (255, 255, 255)
        self.surf = pygame.Surface((1, 1))
        self.surf.fill((255, 255, 255))

        # define rectangle with random starting position (off screen, same as enemies)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
    
    # Move the stars at a constant speed
    # Remove when it passes left edge of screen
    def update(self):
        # TODO: 
        # move the star at a constant speed
        # stars move from right to left
        # when the star is fully off screen, kill star
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


# setup for sounds
pygame.mixer.init()

# initialize pygame
pygame.init()

# Load and play background music
# Loop background music with loops=-1
# https://ccmixter.org/files/BOCrew/68144
pygame.mixer.music.load("sounds/music.mp3")
pygame.mixer.music.play(loops=-1)

# Load all sound effects files
# https://freesound.org/people/PearceL/sounds/361613/
move_up_sound = pygame.mixer.Sound("sounds/rising.wav")
# https://freesound.org/people/Mega-X-stream/sounds/546278/
move_down_sound = pygame.mixer.Sound("sounds/falling.wav")
# https://freesound.org/people/wubitog/sounds/200466/
collision_sound = pygame.mixer.Sound("sounds/collision.wav")
# https://freesound.org/people/jivatma07/sounds/173859/
game_over_sound = pygame.mixer.Sound("sounds/game_over.wav")

# Setup clock for framerate
# Our game loop is running as fast as possible
# all sprites are moving once per frame
clock = pygame.time.Clock()

# create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
# Need custom events to allow for enemies to get created at regular intervals (instead of all just at the start)
# At set intervals, we want to:
# 1. Create a new enemy
# 2. Add it to all_sprites and enemies

# all events are assigned an integer, using USEREVENT + 1 ensures we have an unique integer
# fires a new ADDENEMY event every 250 milliseconds (4 times per second)
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Create custom event for start
# fires the ADDSTAR event every 1000 milliseconds (1 second)
ADDSTAR = pygame.USEREVENT + 2
pygame.time.set_timer(ADDSTAR, 100)

# create player
player = Player()

# Create sprite groups
# - holds a group of sprite objects (enemies, etc.)
# - using sprite groups allow us to easily check for collision with Enemy and Player
# creating 3 sprite groups 
# 1. Hold every sprite in the Game
# 2. Hold ONLY enemies
# 3. Hold only star sprites

enemies = pygame.sprite.Group()
stars = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# create a game loop to
# 1. process user input (keys, mouse, etc.)
# 2. update the state of game objects
# 3. Update display and audio
# 4. Maintain the speed of the game

# Every cycle of the loop is a frame
# frames continue until the loop ends (quit game, win, lose, etc.)

# keep the loop running until exit
running = True

# Main loop
while running:
    # look at EVERY event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the esc key? if so, stop the loop
            if event.key == K_ESCAPE:
                running = False

        # Did the user click close window button? if so, stop the loop
        elif event.type == QUIT:
            running = False
        
        # did we get ADDENEMY event (set to trigger every 250ms)
        elif event.type == ADDENEMY:
            # Create the new enemy - add to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        
        # did we get an ADDSTAR event (set to trigger every 100ms)
        elif event.type == ADDSTAR:
            # create new star
            new_star = Star()
            stars.add(new_star)
            all_sprites.add(new_star)
    
    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()

    # update the player sprite based on user key presses
    player.update(pressed_keys)

    # update enemy position
    # update() calls update() function for all enemies in the group
    enemies.update()

    # update star position
    stars.update()
    
    # fill screen with black
    screen.fill((0, 0, 0))

    # draw all sprites (player and enemies)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    
    # Check if any enemies have collided with the player
    # check every object in the group and check if the rect intersects with the rect of the Sprite
    # if collision, return True
    if pygame.sprite.spritecollideany(player, enemies):
        # If collision, remove the player and stop loop
        player.kill()

        # stop any moving sounds and play collision sound
        move_up_sound.stop()
        move_down_sound.stop()
        collision_sound.play()

        # sleep for length of collision sound
        # without this our game quits without full sound playing
        time.sleep(collision_sound.get_length())

        game_over_sound.play()
        time.sleep(game_over_sound.get_length())

        # Stop the loop
        running = False

    # Update the display
    pygame.display.flip()

    # ensure program maintains a rate of 60 frames per second
    # argument passed is desired framerate
    clock.tick(60)

# Stop and quit the mixer to end all sounds
pygame.mixer.music.stop()
pygame.mixer.quit()
