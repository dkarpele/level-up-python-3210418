import time
from random import randint


def waiting_game():
    rand = randint(2, 4)
    input(f'Your target time is {rand} seconds\n'
          f'---Press Enter to Begin---\n')
    start = time.time()
    print(f'...Press Enter again after {rand} seconds...')
    input()
    finish = round(time.time() - start, 3)
    if finish == float(rand):
        suffix = 'right on target'
    elif finish > float(rand):
        suffix = f'{abs(rand - finish)} seconds too slow'
    else:
        suffix = f'{abs(rand - finish)} seconds too fast'

    print(f'''Elapsed time: {finish} seconds
({suffix})''')
# commands used in solution video for reference


if __name__ == '__main__':
    waiting_game()
