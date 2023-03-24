# this is redundant code
# just kept it because the glitch in it is very intersting


import pygame, sys

pygame.init()

clock = pygame.time.Clock()
width,height = 800,800

screen = pygame.display.set_mode((width,height))

def wall_collision(rectangle,x,y):
    x_vel = x
    y_vel = y
    if rectangle.right >= width or rectangle.left <= 0:
        x_vel *= -1
    if rectangle.bottom >= height or rectangle.top <= 0:
        y_vel *= -1
    return [x_vel,y_vel]


# function to track and update movement and display accordingly
def movement():
    global x_first,y_first, x_second, y_second

    # to update movement
    first_rect.x += x_first
    first_rect.y += y_first
    second_rect.x += x_second
    second_rect.y += y_second


    # collision with screen border
    x_first,y_first = wall_collision(first_rect,x_first,y_first)
    x_second,y_second = wall_collision(second_rect,x_second,y_second)


    # collision with second rectangle:
    collision_tolerance = 10
    if first_rect.colliderect(second_rect):
        if abs(second_rect.top - first_rect.bottom) < collision_tolerance:
            y_first *= -1 
        if abs(second_rect.bottom - first_rect.top) < collision_tolerance:
            y_first *= -1 
        if abs(second_rect.right - first_rect.left) < collision_tolerance:
            x_first *= -1 
        if abs(second_rect.left - first_rect.right) < collision_tolerance:
            x_first *= -1 

    # to draw something in the screen use the draw. function. here it takes 3 argument, 
    # in which screen to draw, color, object
    pygame.draw.rect(screen, (255,255,255),first_rect)
    pygame.draw.rect(screen, (255,0,0),second_rect)






# box
                        
first_rect = pygame.Rect(350,350,100,100)
x_first , y_first = 5,4

# location of this rect
# 300 pixels from the left, 600 pixels from the top
# it is 200 pixels wide and 100 pixels high
second_rect = pygame.Rect(300,600,200,100)
x_second , y_second = 0,2




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    


# creating the screen
    screen.fill((30,30,30))
    movement()
   
    pygame.display.flip()
    clock.tick(60)

