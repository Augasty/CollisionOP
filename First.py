import pygame, sys
width,height = 800,800





first_rect = pygame.Rect(350,350,100,100)
x_first , y_first = 5,5

def wall_collision_for_first(rectangle,x,y):
    x_vel = x
    y_vel = y
    if rectangle.right >= width or rectangle.left <= 0:
        x_vel *= -1
    if rectangle.bottom >= height or rectangle.top <= 0:
        y_vel *= -1
    return [x_vel,y_vel]

# def collision_of_first_with_second()