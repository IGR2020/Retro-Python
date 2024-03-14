from LibraryRunner import Runner, Library
from apps import Pong
from settings import *

run = True

runner = Runner(
    Library(
        [
            Pong()
        ]
    )
)


def display():
    window.fill((255, 255, 255))
    runner.display(window)
    pg.display.update()


if __name__ == "__main__":
    while run:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            runner.event_handling(event)
        runner.script()
        display()
    pg.quit()
    quit()
