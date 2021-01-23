import pygame
import random
import os

pygame.mixer.init()
pygame.mixer.music.load('C:/Users/user/Downloads/starting.mp3.mp3')
pygame.mixer.music.play()

pygame.init()

#backgound image
bgimg = pygame.image.load('C:/Users/user/Downloads/snake.jpg')
bgimg = pygame.transform.scale(bgimg,(800,500))
bgimg1 = pygame.image.load('C:/Users/user/Downloads/nagin.jpg')
bgimg1 = pygame.transform.scale(bgimg1,(800,500))
bgimg2 = pygame.image.load('C:/Users/user/Downloads/gameover.jpg')
bgimg2 = pygame.transform.scale(bgimg2,(800,500))

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,255,0)

#creating window
window_game = pygame.display.set_mode((800  ,500))
#Game Title
pygame.display.set_caption('SNAKE & FOOD')
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,35)


#creating function for print score on the screen
def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    window_game.blit(screen_text,[x,y])

def plot_snake(window_game,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(window_game,color,[x,y,snake_size,snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        window_game.fill((225,100,0))
        window_game.blit(bgimg,(0,0))
        text_screen('WELCOME TO SNAKE & FOOD',white,800/4,500/3)
        text_screen('PRESS ENTER TO PLAY A GAME',white,800/4,500/2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load('C:/Users/user/Downloads/back.mp3')
                    pygame.mixer.music.play()

                    game_loop()
        pygame.display.update()
        clock.tick(60)

#creating a game loop to handle the window
def game_loop():

    #creating game variables
    exit_game = False
    game_over = False
    velocity_x = 0
    velocity_y = 0
    snake_x = 65
    snake_y = 75
    food_x = random.randint(20,800/2)
    food_y = random.randint(20,500/2)
    snake_size = 10
    score = 0
    fps = 30
    snake_list = []
    snake_length = 1
    # check if hiscore does not exist
    if(not os.path.exists('hiscore.py')):
        with open('hiscore.py','w') as f:
            f.write('0')
    with open('hiscore.py','r') as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            with open('hiscore.py','w') as f:
                f.write(str(hiscore))
            window_game.fill(black)
            window_game.blit(bgimg2,(0,0))
            text_screen('Press Enter To Continue',red,800/3,500/3)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('C:/Users/user/Downloads/starting.mp3.mp3')
                        pygame.mixer.music.play()
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 4
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -4
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -4
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = 4
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            
            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score = score+10
                food_x = random.randint(20,800/2)
                food_y = random.randint(20,500/2)
                snake_length = snake_length+3
                if score>int(hiscore):
                    hiscore = score
                
                
            

            window_game.fill(white)
            window_game.blit(bgimg1,(0,0))
            text_screen('score::'+ str(score)+'  Hiscore::'+str(hiscore),black,5,5)
            pygame.draw.rect(window_game,black,[food_x,food_y,snake_size,snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                   del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('C:/Users/user/Downloads/ending.mp3.mp3')
                pygame.mixer.music.play()
            if snake_x<0 or snake_x>800 or snake_y<0 or snake_y>500:
                game_over = True
                pygame.mixer.music.load('C:/Users/user/Downloads/ending.mp3.mp3')
                pygame.mixer.music.play()
            
            
            #pygame.draw.rect(window_game,red,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(window_game,red,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
            

    #closing the window
    pygame.quit()
    quit()
welcome()
