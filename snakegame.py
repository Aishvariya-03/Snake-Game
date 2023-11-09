import pygame
import random

pygame.init()

background_color = (0, 0, 0)  # Black
snake_color = (148, 0, 211)    # Violet
food_color = (255, 255, 0)    # Yellow
text_color = (255, 255, 255)  # White

width = 600
height = 500
snake_block = 20
snake_speed = 15

font = pygame.font.Font(None, 36)
score_font = pygame.font.Font(None, 28)

def display_message(text, y_offset=0):
    message = font.render(text, True, text_color)
    message_rect = message.get_rect(center=(width // 2, height // 2 + y_offset))
    screen.blit(message, message_rect)

def display_score(score):
    score_text = score_font.render(f"Score: {score}", True, text_color)
    screen.blit(score_text, (10, 10))

def game_loop():
    snake_x, snake_y = width // 2, height // 2
    snake_x_change, snake_y_change = 0, 0
    snake_length = 1
    snake_list = []

    food_x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
    food_y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_x_change == 0:
                    snake_x_change = -snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT and snake_x_change == 0:
                    snake_x_change = snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_UP and snake_y_change == 0:
                    snake_y_change = -snake_block
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN and snake_y_change == 0:
                    snake_y_change = snake_block
                    snake_x_change = 0

        if snake_x >= width or snake_x < 0 or snake_y >= height or snake_y < 0:
            game_over = True

        snake_x += snake_x_change
        snake_y += snake_y_change

        screen.fill(background_color)
        pygame.draw.rect(screen, food_color, [food_x, food_y, snake_block, snake_block])

        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        for segment in snake_list:
            pygame.draw.rect(screen, snake_color, [segment[0], segment[1], snake_block, snake_block])

        display_score(snake_length - 1)
        pygame.display.update()

        if abs(snake_x - food_x) < snake_block and abs(snake_y - food_y) < snake_block:

            food_x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
            food_y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
            snake_length += 1

        pygame.display.update()
        clock.tick(snake_speed)
        
    return game_over

if __name__ == "__main__":
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game by Aishu')
    
    clock = pygame.time.Clock()

    while True:
        game_over = game_loop()
        if game_over:
            screen.fill(background_color)
            display_message("You Lost! Press C to Play Again or Q to Quit", 50)
            pygame.display.update()
            
            wait = True
            while wait:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            quit()
                        if event.key == pygame.K_c:
                            wait = False