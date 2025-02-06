import pygame

# This code to draw a line in Bresenham Algorithm is modified from https://blog.mbedded.ninja/programming/algorithms-and-data-structures/bresenhams-line-algorithm/ 
def draw_line(window, color, point1, point2):
    try:
        x1, y1 = round(point1[0]), round(point1[1])
        x2, y2 = round(point2[0]), round(point2[1])
    except OverflowError:   # Handle the case where x or y equals infinity
        return
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        window.set_at((x1, y1), color)
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 >= -dy:
            err -= dy
            x1 += sx
        if e2 <= dx:
            err += dx
            y1 += sy


if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((800, 600))
  
    pygame.display.set_caption('Bresenham Line Drawing')
    window.fill((255, 255, 255))
    
    # Example points for the line
    point1 = (100, 100)
    point2 = (700, 500)

    draw_line(window, (0, 0, 0), point1, point2)
    pygame.display.update()

    # Game loop to keep the window open
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
