import turtle
from data import Data


class Display:

    def __init__(self):
        self.stage = turtle.Screen()
        self.painter = turtle.Turtle()
        self.painter.hideturtle()

        self.key = turtle.Turtle()
        self.key.hideturtle()
        self.key.penup()
        self.key.color('white')
        self.key.shape('square')
        self.key.shapesize(stretch_wid=10, stretch_len=3)

        self.b_key = turtle.Turtle()
        self.b_key.hideturtle()
        self.b_key.penup()
        self.b_key.color('black')
        self.b_key.shape('square')
        self.b_key.shapesize(stretch_wid=4.5, stretch_len=1.6)

        self.key.hideturtle()
        self.b_key.hideturtle()

    def init_screen(self):
        self.stage.setup(900, 600)
        self.stage.bgpic('pic/menu_bg.gif')
        self.stage.title('Piano Melody')

    def menu(self):
        self.init_screen()
        menu = self.stage.textinput('Which menu would you like to do?',
                                    'record / practice / play music"')
        return menu

    def exit_msg(self, color):
        self.painter.color(color)
        self.painter.penup()
        self.painter.goto(0, -260)
        self.painter.write('click to exit', align='center', font=("Arial", 12, "normal"))

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

    def ask_name_again_pm(self):
        name = self.stage.textinput("music's name",
                                    "May I ask you again for the music's name you want to listen?")
        return name

    def show_music_list(self):
        self.stage.clear()
        self.stage.bgcolor('pink')
        self.painter.penup()
        self.painter.goto(0, 200)
        self.painter.write('Music list', align='center', font=('Times New Roman', 20, 'bold'))

        all_music = Data({})
        # data = all_music.read()    # {'hbd': ['c', 'c', 'd', 'c', 'f', 'e']}

        data = all_music.read()
        # except TypeError:
        #     print("None of the musics have ever been recorded.")
        # else:
        try:
            for index, music in enumerate(data):
                pass
        except TypeError:
            print("None of the musics have ever been recorded.\nTry to record the music first.")
        else:
            for index, music in enumerate(data):
                if index <= 15:
                    self.painter.goto(-250, 150 - ((index + 1) * 25))
                    msg = f'{music}'
                    self.painter.penup()
                    self.painter.write(msg, align='center', font=('Times New Roman', 16, 'normal'))
                elif 15 < index <= 30:
                    self.painter.goto(0, 150 - ((index - 16 + 1) * 25))
                    msg = f'{music}'
                    self.painter.penup()
                    self.painter.write(msg, align='center', font=('Times New Roman', 16, 'normal'))
                else:
                    self.painter.goto(250, 150 - ((index - 31 + 1) * 25))
                    msg = f'{music}'
                    self.painter.penup()
                    self.painter.write(msg, align='center', font=('Times New Roman', 16, 'normal'))

        self.painter.hideturtle()

    def pm_screen(self):
        self.painter.clear()
        self.painter.hideturtle()
        self.stage.clear()
        self.stage.bgpic('pic/pm_bg.gif')
        self.exit_msg('black')

    def prac_screen(self):
        self.stage.bgpic('pic/key_bg.gif')
        self.stage.bgcolor('black')
        self.exit_msg('white')

    def rec_screen(self):
        self.stage.bgpic('pic/key_bg.gif')
        self.stage.bgcolor('black')
        self.exit_msg('white')

# d = Display()
# print(d.show_music_list())
