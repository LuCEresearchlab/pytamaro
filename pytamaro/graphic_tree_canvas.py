from pytamaro.graphic import *
import sys


class Canvas:
    def __init__(self, width):
        self.line_width = width
        self.canvas = []

    def put_char(self, x, y, c):
        if x < self.line_width:
            pos = y * self.line_width + x
            l = len(self.canvas)
            if pos < l:
                self.canvas[pos] = c
            else:
                self.canvas[l:] = [' '] * (pos - l)
                self.canvas.append(c)

    def print_out(self):
        i = 0
        sp = 0
        for c in self.canvas:
            if c != ' ':
                sys.stdout.write(' ' * sp)
                sys.stdout.write(c)
                sp = 0
            else:
                sp += 1
            i = i + 1
            if i % self.line_width == 0:
                sys.stdout.write('\n')
                sp = 0
        if i % self.line_width != 0:
            sys.stdout.write('\n')


def print_binary_tree_r(t, x, y, canvas):
    max_y = y
    if isinstance(t, Primitive) or isinstance(t, Operation):
        x, max_y, lx, rx = print_binary_tree_r(t.left_node, x, y + 2, canvas)
        x = x + 1
        for i in range(rx, x):
            canvas.put_char(i, y + 1, '/')

    middle_l = x
    if isinstance(t, Graphic):
        for c in str(type(t).__name__):
            canvas.put_char(x, y, c)
            x = x + 1
    if isinstance(t, str):
        for c in t:
            canvas.put_char(x, y, c)
            x = x + 1
    middle_r = x

    if isinstance(t, Primitive) or isinstance(t, Operation):
        canvas.put_char(x, y + 1, '\\')
        x = x + 1
        x0, max_y2, lx, rx = print_binary_tree_r(t.right_node, x, y + 2, canvas)
        if max_y2 > max_y:
            max_y = max_y2
        for i in range(x, lx):
            canvas.put_char(i, y + 1, '\\')
        x = x0

    return x, max_y, middle_l, middle_r


def print_tree(t):
    print_tree_w(t, 30000)


def print_tree_w(t, width):
    canvas = Canvas(width)
    print_binary_tree_r(t, 0, 0, canvas)
    canvas.print_out()
