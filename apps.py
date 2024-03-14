from settings import *


class Object(pg.Rect):
    def __init__(self, image: pg.Surface, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = image

    def display(self, win, xf=0, yf=0):
        win.blit(self.image, (self.x - xf, self.y - yf))


class BaseApp:

    def __init__(self, icon, pos=(0, 0)):
        self.icon = icon
        self.window = pg.Surface((window_width, window_height))
        self.pos = pos
        self.icon_rect = None

    def script(self, *args): ...

    def display(self, win):
        win.blit(self.window, self.pos)


class Ball(Object):
    def __init__(self, image, x, y, width, height):
        super().__init__(image, x, y, width, height)
        self.vel = (-2, -1)

    def script(self, rect1, rect2):
        if self.colliderect(rect1):
            self.vel = (2, self.vel[1])
        if self.colliderect(rect2):
            self.vel = (-2, self.vel[1])
        if self.y < 0:
            self.vel = (self.vel[0], 1)
        if self.bottom > window_height:
            self.vel = (self.vel[0], -1)
        self.topleft = (self.x + self.vel[0], self.y + self.vel[1])


class Pong(BaseApp):
    def __init__(self):
        super().__init__(app_icons["Pong"])
        assets = load_assets("assets/Pong")
        self.player1 = Object(assets["Bar"], 10, 0, 75, 150)
        self.player2 = Object(
            assets["Bar"], window_width - 85, window_height - 150, 75, 150
        )
        assets["Ball"] = pg.transform.scale(assets["Ball"], (64, 64))
        self.ball = Ball(assets["Ball"], window_width / 2, window_height / 2, 64, 64)

    def script(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.player1.y += 1
        if keys[pg.K_s]:
            self.player1.y -= 1
        if keys[pg.K_UP]:
            self.player2.y += 1
        if keys[pg.K_DOWN]:
            self.player2.y -= 1
        self.ball.script(self.player1, self.player2)

    def display(self, win):
        self.window.fill((10, 10, 10))
        self.player1.display(self.window)
        self.player2.display(self.window)
        self.ball.display(self.window)
        super().display(win)
