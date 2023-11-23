import pygame

def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = top_left).center)
    win.blit(rotated_image, new_rect.topleft)

def blit_text_center(WIN, font, text):
    render = font.render(text, 1, (200, 200, 200))
    WIN.blit(render, (WIN.get_width()/2 - render.get_width()/2, WIN.get_height()/2 - render.get_height()/2))
