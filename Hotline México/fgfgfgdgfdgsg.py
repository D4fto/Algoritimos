import pygame
import math
from pygame.locals import *

# Set the colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

#intialize the pygamem constructor
pygame.init()

#Set dimensions of screen
w, h = 600, 440
screen = pygame.display.set_mode((w, h))

# Set the intial running, angle and scale values
running = True
angle = 0
scale = 1

# Set a sample image
img_logo = pygame.image.load('chaves-16.png')
img_logo.convert()

# Draw a rectangle around the image using get_rect()
rect_logo = img_logo.get_rect()
pygame.draw.rect(img_logo, RED, rect_logo, 1)

# Set the current center and mouse position
center = w//2, h//2
mouse = pygame.mouse.get_pos()
img = img_logo
rect = img.get_rect()
rect.center = center

# we need to set what happens when game is in running state
while running:
	for event in pygame.event.get():

		# Close if the user quits the game
		if event.type == QUIT:
			running = False

		# Dealing with the angle part
		if event.type == KEYDOWN:
			if event.key == K_ra:
				if event.mod & KMOD_SHIFT:
					angle -= 5
				else:
					angle += 5

			# Dealing with the scaling part
			elif event.key == K_sa:
				if event.mod & KMOD_SHIFT:
					scale /= 1.5
				else:
					scale *= 1.5
				
		# Move the image with the modified coordinates,
		# angle and scale		
		elif event.type == MOUSEMOTION:
			mouse = event.pos
			xi = mouse[0] - center[0]
			yi = mouse[1] - center[1]
			d = math.sqrt(xi ** 2 + yi ** 2)
			angle = math.degrees(-math.atan2(yi, xi))
			scale = abs(5 * d / w)
			img = pygame.transform.rotozoom(img_logo, angle, scale)
			rect = img.get_rect()
			rect.center = center
	
	# Set screen color and image on screen
	screen.fill(YELLOW)
	screen.blit(img, rect)

	# Draw the rectangle, line and circle through which image can be transformed
	pygame.draw.rect(screen, BLACK, rect, 3)
	pygame.draw.line(screen, RED, center, mouse, 2)
	pygame.draw.circle(screen, RED, center, 6, 1)
	pygame.draw.circle(screen, BLACK, mouse, 6, 2)
	
	# Updating the pygame application
	pygame.display.update()

# Quit the GUI game
pygame.quit()