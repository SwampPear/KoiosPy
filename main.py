from email import message
import sys
import time
import os
from text import Text
from terminalutilities import *


class List:
    def __init__(self, prompt, answers):
        self.prompt = prompt
        self.answers = answers

    def draw(self):
        print(f'{self.prompt}')

        for answer in self.answers:
            print(answer)

q = List(
    prompt='What action will you like to perform?',
    answers=[
        'Get information',
        'Set information',
        'Overwrite file'
    ]
)

q.draw()

a = Text(text="fuck eggs", color='blue', formatting='blink')

time.sleep(1.0)
erase_last_n_rows(3)
#sys.stdout.flush()
print("asdf")
print("dfs")
print("fs")
print("asdfsda")

