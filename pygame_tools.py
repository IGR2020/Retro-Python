import pygame
from os.path import join, isfile
from os import listdir

pygame.font.init()


def blit_text(
    win, text, pos=(0, 0), colour=(0, 0, 0), size=30, font="arialblack", blit=True
):
    font_style = pygame.font.SysFont(font, size)
    text_surface = font_style.render(text, False, colour)
    if blit:
        win.blit(text_surface, pos)
    return text_surface


class Button:
    def __init__(self, pos, text, scale=1, *args):
        self.x, self.y = pos
        self.width, self.height = text.get_width() * scale, text.get_height() * scale
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.transform.scale(text, (self.width, self.height))
        if len(args) == 1:
            self.info = args[0]
        elif len(args) > 1:
            self.info = args

    def clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True

    def display(self, win):
        win.blit(self.image, self.rect)


def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(dir1, dir2, width, height, direction=True):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()
        sprites = []

        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


def load_sprite_sheet(path, width, height, resize, direction=True):
    path = join("assets", path)

    sprite_sheet = pygame.image.load(path).convert_alpha()
    sprites = []
    resize_sprites = []

    for i in range(sprite_sheet.get_width() // width):
        surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        rect = pygame.Rect(i * width, 0, width, height)
        surface.blit(sprite_sheet, (0, 0), rect)
        sprites.append(pygame.transform.scale2x(surface))
        if direction:
            sprites.append(flip(pygame.transform.scale2x(surface)))

    for sprite in sprites:
        resize_sprites.append(pygame.transform.scale(sprite, resize))

    return resize_sprites


def load_assets(path, size : None | tuple[int, int] = None):
    files = {}
    for file in listdir(path):
        if size is None:
            files[file.replace(".png", "")] = pygame.image.load(join(path, file))
        else:
            files[file.replace(".png", "")] = pygame.transform.scale(pygame.image.load(join(path, file)), size)
    return files
