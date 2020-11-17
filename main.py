import pygame # other comments can be seen in notion or on github

pygame.init()
width, height = 800,  600
backgroundColor = 255,  0,  0 # tuple of 3 elements representing rgb numbers

screen = pygame.display.set_mode((width, height)) # screen is a display surface that uses the set_mode method

dvdLogo = pygame.image.load("dvd.png") 
dvdLogoRect = dvdLogo.get_rect() # create a rectangle from the surface/image created in line 9 

while True:
	screen.fill(backgroundColor) 
  screen.blit(dvdLogo, dvdLogoRect) # Map the imported image into the rectangle so it stays inside the rectangle
	pygame.display.flip() # refreshes screen with the changes made to the display