from tkinter import *
from random import randint

main = Tk()

canvas = Canvas(main, width = 720, height = 720)



level_1_board = [[0, 0, 0, 2, 0, 2, 0, 2, 2, 0],
                [0, 2, 2, 2, 0, 2, 0, 2, 2, 0],
                [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
                [2, 2, 2, 2, 0, 2, 2, 2, 2, 0],
                [0, 2, 0, 2, 0, 0, 0, 0, 2, 0],
                [0, 2, 0, 2, 0, 2, 2, 0, 2, 0],
                [0, 0, 0, 0, 0, 2, 2, 0, 2, 0],
                [0, 2, 2, 2, 0, 0, 0, 0, 2, 0],
                [0, 0, 0, 2, 0, 2, 2, 0, 2, 0],
                [0, 2, 0, 2, 0, 2, 0, 0, 0, 0]]

level_1_spawn_locations = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 3, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 3, 1, 1, 1, 1, 3, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 3]]


class Validator(object):

    def __init__(self, vertical, horizontal):
        self.horizontal = horizontal
        self.vertical = vertical

    def validate_hero_left(self):
        if hero.horizontal > 0:
            hero.horizontal -= 1
            hero.hero_move_left()

    def validate_hero_right(self):
        if hero.horizontal < 9:
            hero.horizontal += 1
            hero.hero_move_right()

    def validate_hero_up(self):
        if hero.vertical > 0:
            hero.vertical -= 1
            hero.hero_move_up()


    def validate_hero_down(self):
        if hero.vertical < 10:
            hero.vertical += 1
            hero.hero_move_down()

class PlayField(object):

    def __init__(self, level_layout):
        self.level_layout = level_layout

    def set_playfield(self):
        self.tile_objects = []
        for y_coord in range(len(self.level_layout)):
            for x_coord in range(len(self.level_layout[y_coord])):
                self.get_tile_type(y_coord, x_coord)

    def get_tile_type(self, y_coord, x_coord):
        if self.level_layout[y_coord][x_coord] == 0:
            self.tile_objects.append(Floor(y_coord, x_coord))
        else:
            self.tile_objects.append(Wall(y_coord, x_coord))

    def print_playfield(self):
        for tile in self.tile_objects:
            tile.draw()


class Tile(object):

    def __init__(self, horizontal, vertical):
        self.size = 72
        self.horizontal = horizontal
        self.vertical = vertical

    def draw(self, pic):
        canvas.create_image(self.vertical * self.size, self.horizontal * self.size, image = pic, anchor = NW)

class Floor(Tile):

    def __init__(self, horizontal, vertical):
        super().__init__(horizontal, vertical)
        self.floor = PhotoImage(file = 'assets/floor.png')

    def draw(self):
        super().draw(self.floor)

class Wall(Tile):

    def __init__(self, horizontal, vertical):
        super().__init__(horizontal, vertical)
        self.wall = PhotoImage(file = 'assets/wall.png')

    def draw(self):
        super().draw(self.wall)


class Character(object):

    def __init__(self, vertical, horizontal, playfield):
        self.size = 72
        self.horizontal = horizontal
        self.vertical = vertical
        self.playfield = level_1_board

    def draw(self, pic):
        canvas.create_image(self.vertical * self.size, self.horizontal * self.size, image = pic, anchor = NW)

class Hero(Character):

    def __init__(self, horizontal, vertical, playfield):
        # self.health = 0
        # self.strike = 0
        # self.defense = 0
        # self.playfield = level_1_board
        self.hero_spawn = PhotoImage(file = 'assets/hero-down.png')
        self.hero_image = PhotoImage(file = 'assets/hero-down.png')
        super().__init__(horizontal, vertical, canvas)

    def spawn(self):
        super().draw(self.hero_spawn)

    def draw(self):
        self.hero_image = PhotoImage(file = 'assets/hero-down.png')

    def hero_move_left(self, event):
        if level_1_board[self.horizontal][self.vertical - 1] != 2 and self.vertical > 0:
            self.hero_image = PhotoImage(file = 'assets/hero-left.png')
            self.vertical -= 1
            super().draw(self.hero_image)
        else:
            self.hero_nomove()

    def hero_move_right(self, event):
        if level_1_board[self.horizontal][self.vertical + 1] != 2 and self.vertical < 9:
            self.hero_image = PhotoImage(file = 'assets/hero-right.png')
            self.vertical += 1
            super().draw(self.hero_image)
        else:
            self.hero_nomove()

    def hero_move_up(self, event):
        if level_1_board[self.horizontal - 1][self.vertical] != 2 and self.horizontal > 0:
            self.hero_image = PhotoImage(file = 'assets/hero-up.png')
            self.horizontal -= 1
            super().draw(self.hero_image)
        else:
            self.hero_nomove()

    def hero_move_down(self, event):
        if level_1_board[self.horizontal + 1][self.vertical] != 2 and self.horizontal < 9:
            self.hero_image = PhotoImage(file = 'assets/hero-down.png')
            self.horizontal += 1
            super().draw(self.hero_image)
        else:
            self.hero_nomove()

    def hero_nomove(self):
        self.horizontal += 0
        self.vertical += 0

# class TrashMob(Character):
#
#     def __init__():
#         self.health =
#         self.strike =
#         self.defense =
#
#     def draw(self):
#
# class Boss(Character):
#
#     def __init__():
#         self.health =
#         self.strike =
#         self.defense =
#
#     def draw(self):


wanderer = PlayField(level_1_board)
wanderer.set_playfield()
wanderer.print_playfield()
majom = Hero(0, 0, main)
majom.spawn()

main.bind('<Down>', majom.hero_move_down)
main.bind('<Up>', majom.hero_move_up)
main.bind('<Left>', majom.hero_move_left)
main.bind('<Right>', majom.hero_move_right)



canvas.pack()
main.mainloop()
