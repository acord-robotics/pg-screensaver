import pygame as pg

pg.init()
width, height = 800,  600
backgroundColor = 255,  0,  0

screen = pg.display.set_mode((width, height))

while True:
	screen.fill(backgroundColor)
	pg.display.flip()