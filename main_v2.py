import pygame, sys
import First
import Second
pygame.init()



clock = pygame.time.Clock()
width,height = 800,800

screen = pygame.display.set_mode((width,height))



# function to track and update movement and display accordingly
def movement():
    global x_first,y_first, x_second, y_second

# keypressing and movement of the second block
    pressed = pygame.key.get_pressed()
    if (pressed[pygame.K_d]):
        x_second = 4
    if (pressed[pygame.K_a]):
        x_second = -4
    if (pressed[pygame.K_w]):
        y_second = -4
    if (pressed[pygame.K_s]):
        y_second = 4
    

    # if the input will cause it to collide with the wall, nullify that input
    x_second,y_second = Second.wall_collision_for_second(second_rect,x_second,y_second)
        
    # to update movement
    first_rect.x += x_first
    first_rect.y += y_first
    second_rect.x += x_second
    second_rect.y += y_second


    x_second,y_second = 0,0
    # collision with screen border
    x_first,y_first = First.wall_collision_for_first(first_rect,x_first,y_first)


    # collision with second rectangle:
    collision_tolerance = 10
    if first_rect.colliderect(second_rect):
        if abs(second_rect.top - first_rect.bottom) < collision_tolerance and y_first > 0:
            y_first *= -1 
        if abs(second_rect.bottom - first_rect.top) < collision_tolerance and y_first < 0:
            y_first *= -1 
        if abs(second_rect.right - first_rect.left) < collision_tolerance and x_first < 0:
            x_first *= -1 
        if abs(second_rect.left - first_rect.right) < collision_tolerance and x_first > 0:
            x_first *= -1 



    # to draw something in the screen use the draw. function. here it takes 3 argument, 
    # in which screen to draw, color, object
    pygame.draw.rect(screen, (255,255,255),first_rect)
    pygame.draw.rect(screen, (255,0,0),second_rect)






# box

first_rect = First.first_rect
x_first,y_first = First.x_first,First.y_first

second_rect = Second.second_rect
x_second,y_second = Second.x_second,Second.y_second




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    


# creating the screen
    screen.fill((35,35,35))
    movement()
   
    pygame.display.flip()
    clock.tick(60)

