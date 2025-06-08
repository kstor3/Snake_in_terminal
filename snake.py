import curses
import random

def main(stdscr):
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(1)
    win.timeout(100)

    snk_x = sw // 4
    snk_y = sh // 2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
    ]

    food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
    win.addch(food[0], food[1], curses.ACS_PI)

    key = curses.KEY_RIGHT

    while True:
        next_key = win.getch()
        key = key if next_key == -1 else next_key

        head = snake[0]
        if key == curses.KEY_DOWN:
            new_head = [head[0] + 1, head[1]]
        elif key == curses.KEY_UP:
            new_head = [head[0] - 1, head[1]]
        elif key == curses.KEY_LEFT:
            new_head = [head[0], head[1] - 1]
        elif key == curses.KEY_RIGHT:
            new_head = [head[0], head[1] + 1]
        else:
            continue

        snake.insert(0, new_head)

        if (new_head[0] in [0, sh] or
            new_head[1] in [0, sw] or
            new_head in snake[1:]):
            curses.endwin()
            print("Game Over")
            break

        if new_head == food:
            food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
            win.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')

        win.addch(new_head[0], new_head[1], '#')

curses.wrapper(main)
