from pyautogui import (
    moveTo as move,
    mouseDown as press,
    mouseUp as release,
    size as screen,
    position,
)
from time import sleep
from math import sin, cos, pi


def center_mouse(screen_size):
    """
    :params: screen_size:  (width, height) tuple of the screen size, in pixels.
    """
    go_to = (
        screen_size[0] // 2,
        (screen_size[1] // 2) - 19.1,
    )  # adjust here to center it perfectly
    move(go_to)


def create_circle(num_points: int, radius: int, center_x: int, center_y: int):
    sleep(3)
    for i in range(num_points + 1):
        press()
        angle = (i / num_points) * 2 * pi
        x = center_x + int(radius * cos(angle))
        y = center_y + int(radius * sin(angle))
        move(x, y, duration=0.01)
    release()


def main():
    screen_dims = screen()
    center_mouse(screen_size=screen_dims)
    get_mouse = position()
    create_circle(28, 500, get_mouse[0], get_mouse[1])


if __name__ == "__main__":
    main()
