import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
orange= (255, 165, 0)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
violet = (238,130,238)
 
dis_width = 600
dis_height = 400

with open("highscore.txt","r") as f:
        highscore=f.read().split('""')[1]
        
current_score=0
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('A simple snake game')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15

 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
'''def highscore(Your_score):
    global highscore
    value = score_font.render("Your Score: " + str(Your_score) + "Highscore:" + str(highscore), True, red)
    dis.blit(value, [0, 0])'''



 
 
def Your_score(score):
    global highscore
    value = score_font.render("Your Score: " + str(score) + "Highscore:" + str(highscore), True, red)
    dis.blit(value, [0, 0]) 
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [int(x[0]), int(x[1]), int(snake_block), int(snake_block)])
 
 
def message(msg, color):
    msg = font_style.render(msg, True, color)
    #print([((dis_width) / 6, (dis_height) / 3)])
    dis.blit(msg, [100,100]) 

 
 
def gameLoop():
    global highscore
    global current_score
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(violet)
            message("You Lost! Press F-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            current_score=Length_of_snake 
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == event.key == pygame.K_f:
                        gameLoop()
 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(violet)
        pygame.draw.rect(dis, green, [int(foodx), int(foody), int(snake_block), int(snake_block)])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1) 
        current_score=Length_of_snake 
        

   
        
        pygame.display.update() 
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            if (current_score)>int(highscore):
                highscore=current_score
                with open('highscore.txt','w') as fle:
                    fle.write('""'+str(highscore)+'""')# read garni haina rw aab vayo  taahh b adiytsto vayo aaja game vitrai highscore baxa AHHHH
                
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
    
    
    
gameLoop()

