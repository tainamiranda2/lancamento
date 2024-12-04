import pygame
import math
import random


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lançamento Oblíquo - Basquete")

FPS = 60
clock = pygame.time.Clock()
gravity = 9.8

acertos = 0
erros = 0

font = pygame.font.Font(None, 36)

background = pygame.image.load("quadra.png")
basket = pygame.image.load("cesta.png")
ball = pygame.image.load("bola.png")

background = pygame.transform.scale(background, (WIDTH, HEIGHT))
basket = pygame.transform.scale(basket, (50, 100))
ball = pygame.transform.scale(ball, (30, 30))

def draw_hoop(hoop_x, hoop_y):
    screen.blit(basket, (hoop_x, hoop_y))

def draw_ball(x, y):
    screen.blit(ball, (int(x), int(y)))

def draw_score(acertos, erros):
    acertos_text = font.render(f"Acertos: {acertos}", True, (0, 0, 0))
    erros_text = font.render(f"Erros: {erros}", True, (0, 0, 0))
    screen.blit(acertos_text, (10, 10))
    screen.blit(erros_text, (10, 40))

def simulate_shot(v0, angle, x_start, y_start, hoop_x, hoop_y):
    t = 0
    x = x_start
    y = y_start
    trajectory_points = []  

    while y < HEIGHT - 10:
        t += 0.1
        x = x_start + v0 * math.cos(math.radians(angle)) * t
        y = y_start - (v0 * math.sin(math.radians(angle)) * t - 0.5 * gravity * t ** 2)
        
        trajectory_points.append((x, y))

        screen.blit(background, (0, 0))  
        draw_hoop(hoop_x, hoop_y)  

        for point in trajectory_points:
            pygame.draw.circle(screen, (0, 0, 0), (int(point[0]), int(point[1])), 2)

        draw_ball(x, y) 
        draw_score(acertos, erros)  
        pygame.display.flip()
        clock.tick(FPS)

        if hoop_x < x < hoop_x + 50 and hoop_y < y < hoop_y + 100:
            return True  

    return False  

def main():
    global acertos, erros
    running = True
    while running:

        screen.blit(background, (0, 0))

        hoop_x = WIDTH - 150  
        hoop_y = (HEIGHT - 100) // 2  
        draw_hoop(hoop_x, hoop_y)

        draw_score(acertos, erros)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if random.random() < 0.02: 
            v0 = random.uniform(30, 60)  
            angle = random.uniform(30, 60) 
            
            x_start = WIDTH // 2  
            y_start =  hoop_y 

            acertou = simulate_shot(v0, angle, x_start, y_start, hoop_x, hoop_y)
            if acertou:
                acertos += 1
                print("Cesta!")
            else:
                erros += 1
                print("Errou!")

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
