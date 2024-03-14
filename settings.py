import pygame as pg
from pygame_tools import load_assets

window_width, window_height = 1024, 512
window = pg.display.set_mode((window_width, window_height))
pg.display.set_caption("Retro Games")

clock = pg.time.Clock()
fps = 60

icon_size = 128
app_icons = load_assets("assets/icons", (icon_size, icon_size))
