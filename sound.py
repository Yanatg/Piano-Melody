import turtle
import time
from playsound import playsound


class Sound:
    """ sounds management """
    def __init__(self, music_note=None, display_class=None):
        self.music_note = music_note    # {'name': ['a', 'b', 'c', 'r', 'e']}
        self.note_list = []
        self.screen = turtle.Screen()

        self.__key = display_class.key
        self.__b_key = display_class.b_key

    def note_c(self):
        """ display the piano key and play the sound """
        self.__key.goto(-278, 123)
        self.__key.showturtle()
        playsound("key_sounds/c-4.mp3", True)
        self.__key.hideturtle()
        self.note_list.append("c")

    def note_d(self):
        """ display the piano key and play the sound """
        self.__key.goto(-278 + (1*62), 123)
        self.__key.showturtle()
        playsound("key_sounds/d-4.mp3", True)
        self.__key.hideturtle()
        self.note_list.append("d")

    def note_e(self):
        """ display the piano key and play the sound """
        self.__key.goto(-278 + (2 * 62), 123)
        self.__key.showturtle()
        playsound("key_sounds/e-4.mp3", True)
        self.__key.hideturtle()
        self.note_list.append("e")

    def note_f(self):
        """ display the piano key and play the sound """
        self.__key.goto(-278 + (3 * 62), 123)
        self.__key.showturtle()
        playsound("key_sounds/f-4.mp3", True)
        self.__key.hideturtle()
        self.note_list.append("f")

    def note_g(self):
        """ display the piano key and play the sound """
        self.__key.goto(-278 + (4 * 62), 123)
        self.__key.showturtle()
        playsound("key_sounds/g-4.mp3", True)
        self.__key.hideturtle()
        self.note_list.append("g")

    def note_a(self):
        """ display the piano key and play the sound """
        self.__key.goto(-278 + (5 * 62), 123)
        self.__key.showturtle()
        playsound("key_sounds/a-4.mp3", True)
        self.__key.hideturtle()
        self.note_list.append("a")

    def note_b(self):
        """ display the piano key and play the sound """
        self.__key.goto(-278 + (6 * 62), 123)
        self.__key.showturtle()
        playsound("key_sounds/b-4.mp3", True)
        self.__key.hideturtle()
        self.note_list.append("b")

    def note_c5(self):
        """ display the piano key and play the sound """
        self.__key.goto(-278 + (7 * 62), 123)
        self.__key.showturtle()
        playsound("key_sounds/c-5.mp3", True)
        self.__key.hideturtle()
        self.note_list.append('c5')

    def note_d5(self):
        """ display the piano key and play the sound """
        self.__key.goto(-278 + (8 * 62), 123)
        self.__key.showturtle()
        playsound("key_sounds/d-5.mp3", True)
        self.__key.hideturtle()
        self.note_list.append('d5')

    def note_e5(self):
        """ display the piano key and play the sound """
        self.__key.goto(-278 + (9 * 62), 123)
        self.__key.showturtle()
        playsound("key_sounds/e-5.mp3", True)
        self.__key.hideturtle()
        self.note_list.append('e5')

    def note_cc(self):
        """ display the piano key and play the sound """
        self.__b_key.goto(-248 + (0 * 62), 176)
        self.__b_key.showturtle()
        playsound("key_sounds/c -4.mp3", True)
        self.__b_key.hideturtle()
        self.note_list.append('cc')

    def note_dd(self):
        """ display the piano key and play the sound """
        self.__b_key.goto(-248 + (1 * 63), 176)
        self.__b_key.showturtle()
        playsound("key_sounds/d -4.mp3", True)
        self.__b_key.hideturtle()
        self.note_list.append('dd')

    def note_ff(self):
        """ display the piano key and play the sound """
        self.__b_key.goto(-248 + (3 * 62.1), 177.5)
        self.__b_key.showturtle()
        playsound("key_sounds/f -4.mp3", True)
        self.__b_key.hideturtle()
        self.note_list.append('ff')

    def note_gg(self):
        """ display the piano key and play the sound """
        self.__b_key.goto(-248 + (4 * 62.2), 177.5)
        self.__b_key.showturtle()
        playsound("key_sounds/g -4.mp3", True)
        self.__b_key.hideturtle()
        self.note_list.append('gg')

    def note_aa(self):
        """ display the piano key and play the sound """
        self.__b_key.goto(-248 + (5 * 62.3), 177.5)
        self.__b_key.showturtle()
        playsound("key_sounds/a -4.mp3", True)
        self.__b_key.hideturtle()
        self.note_list.append('aa')

    def note_cc5(self):
        """ display the piano key and play the sound """
        self.__b_key.goto(-248 + (7 * 61.9), 177.5)
        self.__b_key.showturtle()
        playsound("key_sounds/c -5.mp3", True)
        self.__b_key.hideturtle()
        self.note_list.append('cc5')

    def note_dd5(self):
        """ display the piano key and play the sound """
        self.__b_key.goto(-248 + (8 * 62.1), 177.5)
        self.__b_key.showturtle()
        playsound("key_sounds/d -5.mp3", True)
        self.__b_key.hideturtle()
        self.note_list.append('dd5')

    def rest(self):
        """ display the piano key and sleep the program """
        time.sleep(0.4)
        self.note_list.append('')

    def play_notes(self, notes):
        """ play all note in list """
        note_l = notes
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
        """ keyboard binding """
        self.screen.listen()
        self.screen.onkey(self.note_c, 'a')
        self.screen.onkey(self.note_d, 's')
        self.screen.onkey(self.note_e, 'd')
        self.screen.onkey(self.note_f, 'f')
        self.screen.onkey(self.note_g, 'g')
        self.screen.onkey(self.note_a, 'h')
        self.screen.onkey(self.note_b, 'j')
        self.screen.onkey(self.note_c5, 'k')
        self.screen.onkey(self.note_d5, 'l')
        self.screen.onkey(self.note_e5, ';')
        self.screen.onkey(self.note_cc, 'w')
        self.screen.onkey(self.note_dd, 'e')
        self.screen.onkey(self.note_ff, 't')
        self.screen.onkey(self.note_gg, 'y')
        self.screen.onkey(self.note_aa, 'u')
        self.screen.onkey(self.note_cc5, 'o')
        self.screen.onkey(self.note_dd5, 'p')
        self.screen.onkey(self.rest, 'space')
        self.screen.exitonclick()
