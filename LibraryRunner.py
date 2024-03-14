from settings import *


class Library:
    def __init__(self, apps):
        self.apps = apps
        i = 0
        for y in range(window_width // icon_size):
            for x in range(window_height // icon_size):
                if i == len(self):
                    return
                self[i].icon_rect = pg.Rect(x * (icon_size + 5), y * (icon_size + 5), icon_size, icon_size)
                i += 1

    def __getitem__(self, item):
        return self.apps[item]

    def __len__(self):
        return len(self.apps)

    def display(self, win):
        i = 0
        for y in range(window_width // icon_size):
            for x in range(window_height // icon_size):
                if i == len(self):
                    return
                win.blit(self[i].icon, (x * (icon_size + 5), y * (icon_size + 5)))
                i += 1


class Runner:
    def __init__(self, library: Library):
        self.library = library
        self.active_apps = []

    def event_handling(self, event):
        if event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            for i, app in enumerate(self.library.apps):
                if app.icon_rect.collidepoint(pos):
                    self.active_apps.append(i)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.active_apps.pop(-1)

    def script(self):
        for i in self.active_apps:
            self.library[i].script()

    def display(self, win):
        self.library.display(win)
        for i in self.active_apps:
            self.library[i].display(win)
