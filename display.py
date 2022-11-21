import turtle
from data import Data


class Display:

    def __init__(self):
        self.stage = turtle.Screen()
        self.painter = turtle.Turtle()
        self.painter.hideturtle()

        self.key = turtle.Turtle()
        # self.key_d = turtle.Turtle()
        # self.key_e = turtle.Turtle()
        # self.key_f = turtle.Turtle()
        # self.key_g = turtle.Turtle()
        # self.key_a = turtle.Turtle()
        # self.key_b = turtle.Turtle()
        # self.key_list = [self.key_c, self.key_d, self.key_e, self.key_f,
        #                  self.key_g, self.key_a, self.key_b]
        # self.color = ['purple', 'blue', 'green', 'yellow', 'orange', 'red', 'white']
        # for index, key in enumerate(self.key_list):
        #     key.hideturtle()
        #     key.penup()
        #     key.color('white')
        #     key.shape('square')
        #     key.goto(-192 + (index*62), 0)
        #     key.shapesize(stretch_wid=10, stretch_len=3)
        self.key.hideturtle()
        self.key.penup()
        self.key.color('white')
        self.key.shape('square')
        # self.key.goto(-192, 0)
        self.key.shapesize(stretch_wid=10, stretch_len=3)

        self.key.hideturtle()

    def init_screen(self):
        self.stage.setup(900, 600)
        self.stage.bgcolor('pink')
        self.stage.title('Piano Melody')

    def menu(self):
        self.init_screen()
        menu = self.stage.textinput('Which menu would you like to do?',
                                    'record / practice / play music"')
        return menu

    def exit_msg(self):
        self.painter.color('white')
        self.painter.penup()
        self.painter.goto(0, -260)
        self.painter.write('click to exit', align='left', font=("Arial", 12, "normal"))

    def ask_name_r(self):
        # self.init_screen()
        name = self.stage.textinput("music's name",
                                    "What would you like your music to be called?")
        return name

    def ask_name_pm(self):
        # self.init_screen()
        name = self.stage.textinput("music's name",
                                    "May I ask for the music's name you want to listen?")
        return name

    def show_music_list(self):
        self.painter.penup()
        self.painter.goto(0, 200)
        self.painter.write('~Music list~', align='center', font=('Leelawadee', 20, 'bold'))

        all_music = Data({})
        data = all_music.read()
        # {'hbd': ['c', 'c', 'd', 'c', 'f', 'e']}
        for index, music in enumerate(data):
            self.painter.goto(0, 150 - ((index + 1) * 20))
            msg = f'{music}'
            self.painter.penup()
            self.painter.write(msg, align='center', font=('Leelawadee', 16, 'bold'))
        self.painter.hideturtle()

    def pm_screen(self):
        self.painter.clear()
        self.painter.hideturtle()
        self.painter.write('playing...', align='center', font=('Leelawadee', 16, 'bold'))
        self.exit_msg()

    def prac_screen(self):
        self.stage.bgpic('pic/key_bg.gif')
        self.stage.bgcolor('black')
        self.exit_msg()

# d = Display()
# print(d.show_music_list())
