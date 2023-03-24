import pygame, sys
width,height = 800,800



# location of this rect
# 300 pixels from the left, 600 pixels from the top
# it is 200 pixels wide and 100 pixels high
second_rect = pygame.Rect(300,600,200,100)
x_second , y_second = 0,0



def wall_collision_for_second(rectangle,x,y):
    x_vel = x
    y_vel = y
    if (rectangle.right >= width and x_vel > 0) or (rectangle.left <= 0 and x_vel < 0):
        x_vel = 0
    if (rectangle.bottom >= height and y_vel > 0) or (rectangle.top <= 0 and y_vel < 0):
        y_vel = 0
    return [x_vel,y_vel]


