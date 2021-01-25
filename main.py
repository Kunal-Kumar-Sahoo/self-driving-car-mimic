import pygame # pip install pygame

pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track6.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))
car_x, car_y = 155, 300
focal_dist = 25
cam_x_offset, cam_y_offset = 0, 0
direction = 'up'
clock = pygame.time.Clock()
drive = True
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    clock.tick(60)
    cam_x, cam_y = car_x + cam_x_offset + 15, car_y + cam_y_offset + 15
    up_px = window.get_at((cam_x, cam_y - focal_dist))[0]
    right_px = window.get_at((cam_x + focal_dist, cam_y))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dist))[0]
    print(up_px, right_px, down_px)
    # change direction
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        car_x += 30
        cam_x_offset, cam_y_offset = 0, 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        car = pygame.transform.rotate(car, 90)
        car_y += 30
        cam_x_offset, cam_y_offset = 30, 0
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        car_x += 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90)
    # drive
    if direction == 'up' and up_px == 255:
        car_y -= 2
    elif direction == 'right' and right_px == 255:
        car_x += 2
    elif direction == 'down' and down_px == 255:
        car_y += 2
    window.blit(track, (0, 0))  # Block-Image-Transfer
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()
