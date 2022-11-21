import turtle
from playsound import playsound
import time
from display import Display


class Sound:

    def __init__(self, music_note=None, display_class=None):
        if music_note is None:
            music_note = {}
        self.music_note = music_note    # {'name': ['a', 'b', 'c', 'r', 'e']}
        self.note_list = []
        self.screen = turtle.Screen()

        self.key = display_class.key

    def note_c(self):
        self.key.goto(-278, 123)
        self.key.showturtle()
        time.sleep(0.1)
        self.key.hideturtle()
        playsound("key_sounds/c-4.mp3", True)
        self.note_list.append("c")
        # self.key.hideturtle()

    def note_d(self):
        self.key.goto(-278 + (1*62), 123)
        self.key.showturtle()
        time.sleep(0.1)
        self.key.hideturtle()
        playsound("key_sounds/d-4.mp3", True)
        self.note_list.append("d")

    def note_e(self):
        self.key.goto(-130, 0)
        self.key.showturtle()
        time.sleep(0.05)
        self.key.hideturtle()
        playsound("key_sounds/e-4.mp3", True)
        self.note_list.append("e")

    def note_f(self):
        playsound("key_sounds/f-4.mp3", True)
        self.note_list.append("f")

    def note_g(self):
        playsound("key_sounds/g-4.mp3", True)
        self.note_list.append("g")

    def note_a(self):
        playsound("key_sounds/a-4.mp3", True)
        self.note_list.append("a")

    def note_b(self):
        playsound("key_sounds/b-4.mp3", True)
        self.note_list.append("b")

    def rest(self):
        time.sleep(0.4)
        self.note_list.append('')

    def play_notes(self, notes):
        note_l = notes
        # note_l = list(self.music_note.values())[0]
        for note in note_l:
            if note == 'c':
                playsound("key_sounds/c-4.mp3", True)
            if note == 'cc':
                playsound("key_sounds/c -4.mp3", True)
            if note == 'd':
                playsound("key_sounds/d-4.mp3", True)
            if note == 'dd':
                playsound("key_sounds/d -4.mp3", True)
            if note == 'e':
                playsound("key_sounds/e-4.mp3", True)
            if note == 'f':
                playsound("key_sounds/f-4.mp3", True)
            if note == 'ff':
                playsound("key_sounds/f -4.mp3", True)
            if note == 'g':
                playsound("key_sounds/g-4.mp3", True)
            if note == 'gg':
                playsound("key_sounds/g -4.mp3", True)
            if note == 'a':
                playsound("key_sounds/a-4.mp3", True)
            if note == 'aa':
                playsound("key_sounds/a -4.mp3", True)
            if note == 'b':
                playsound("key_sounds/b-4.mp3", True)
            if note == 'c5':
                playsound("key_sounds/c-5.mp3", True)
            if note == 'cc5':
                playsound("key_sounds/c -5.mp3", True)
            if note == 'd5':
                playsound("key_sounds/d-5.mp3", True)
            if note == 'dd5':
                playsound("key_sounds/d -5.mp3", True)
            if note == 'e5':
                playsound("key_sounds/e-5.mp3", True)

            if note == '':
                time.sleep(0.4)
        self.screen.exitonclick()

    def play_current_sound(self):
        self.screen.listen()
        # self.screen.onkey(self.note_)
        self.screen.onkey(self.note_c, 'a')
        self.screen.onkey(self.note_d, 's')
        self.screen.onkey(self.note_e, 'd')
        self.screen.onkey(self.note_f, 'f')
        self.screen.onkey(self.note_g, 'g')
        self.screen.onkey(self.note_a, 'h')
        self.screen.onkey(self.note_b, 'j')
        # self.screen.onkey(self.note_c5, 'k')
        # self.screen.onkey(self.note_b5, 'l')
        # self.screen.onkey(self.note_e5, ';')
        # self.screen.onkey(self.note_cc, 'w')
        # self.screen.onkey(self.note_bb, 'e')
        # self.screen.onkey(self.note_ff, 't')
        # self.screen.onkey(self.note_gg, 'y')
        # self.screen.onkey(self.note_aa, 'u')
        # self.screen.onkey(self.note_c5c, 'o')
        # self.screen.onkey(self.note_d5d, 'p')
        self.screen.onkey(self.rest, 'space')
        self.screen.exitonclick()


