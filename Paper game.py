import pygame
import math


# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)


GRAVITY = .0005
VELOCITY = 5
FORCE_MULTIPLIER = 50

pygame.init()

# Set the width and height of the screen [width, height]
size = (333, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Paperball")
background_image = pygame.image.load("room.jpg").convert()

targetx = 140
targety = 100



change_pos = False


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.x = ""
        self.y = ""

        # Initialize some variables
        self.change = [0,0]
        self.gravity = [0,0]
        self.force = [0,0]
        self.distance = [10,20]
        self.collision1 = [0,0]


        self.bounce = False
        self.bounce_length = 0
        self.bounce_done = False

        self.image = pygame.image.load("paper20.png").convert()
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect(center=(168,600))
        print self.rect.x
        print self.rect.y

    def calculate_collision(self):
        # Calculate distance to 1st collision point
        self.distance[0] = FORCE_MULTIPLIER * self.force[0]
        self.distance[1] = FORCE_MULTIPLIER * self.force[1]

        # Calculate collision point
        self.collision1[0] = self.rect.x + self.distance[0]
        self.collision1[1] = self.rect.y - self.distance[1]



    def update(self):
        if change_pos == True:

            # Test if hit 1st collision point

            # print "collision1 x = ", self.collision1[0]
            # if self.rect.x >= self.collision1[0]:
            #     self.gravity[0] += GRAVITY*3

            #print "collision1 y = ", self.collision1[1]
            if self.rect.y <= self.collision1[1]:
                self.bounce = True

            # Bounce

            if self.bounce == True and self.bounce_done == False:
                self.rect.x += 10
                self.rect.y -= 10
                self.bounce_length += 1
                print "self.bounce_done = ", self.bounce_done
                if self.bounce_done >= 10:
                    self.bounce_done = True

            # Change position
            if self.bounce == False and self.bounce_done == False:
                self.rect.x += VELOCITY
                self.rect.y -= VELOCITY


    def target_collision(self):
        self.center = (self.rect[0] + 28, self.rect[1] + 24)

        if targetx <= (self.collision1[0] + 7) and (self.collision1[0] + 7) <= targetx + 50 and targety <= (self.collision1[1] + 4) and (self.collision1[1] + 4) <= targety + 50:
        elif targetx <= (self.collision1[0] + 52) and (self.collision1[0] + 52) <= targetx + 50 and targety <= (self.collision1[1] + 4) and (self.collision1[1] + 4) <= targety + 50:
        elif targetx <= (self.collision1[0] + 7) and (self.collision1[0] + 7) <= targetx + 50 and targety <= (self.collision1[1] + 48) and (self.collision1[1] + 48) <= targety + 50:
        elif targetx <= (self.collision1[0] + 52) and (self.collision1[0] + 52) <= targetx + 50 and targety <= (self.collision1[1] + 48) and (self.collision1[1] + 48) <= targety + 50:
            hit_target = True


paper_ball = Ball()
paper_ball.x = 139
paper_ball.y = 600
all_sprites = pygame.sprite.Group()
all_sprites.add(paper_ball)


# Loop until the user clicks the close button.
done = False


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:

    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and change_pos == False:
                paper_ball.force[0] += 1
                print "x = " + str(paper_ball.force[0])
            if event.key == pygame.K_LEFT and change_pos == False:
                paper_ball.force[0] -= 1
                print "x = " + str(paper_ball.force[0])
            if event.key == pygame.K_UP and change_pos == False:
                paper_ball.force[1] += 1
                print "y = " + str(paper_ball.force[1])
            if event.key == pygame.K_DOWN and change_pos == False:
                paper_ball.force[1] -= 1
                print "y = " + str(paper_ball.force[1])
            if event.key == pygame.K_SPACE:
                paper_ball.calculate_collision()
                change_pos = True


    # --- Game logic should go here


    # --- Drawing code should go here
    screen.blit(background_image, [0, 0])

    pygame.draw.rect(screen, BLACK, [targetx, targety, 50, 50])

    # Call the update() method for all blocks in the block_list
    all_sprites.update()



    # Update & display ball sprite
    all_sprites.draw(screen)

    paper_ball.target_collision()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
