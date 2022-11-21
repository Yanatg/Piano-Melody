from data import Data
from sound import Sound
from display import Display


class Note:

    def __init__(self, note_list=[]):
        self.note_l = note_list
        self.dict_note = Data.read()

    def record(self, name):
        m_n = {name: self.note_l}
        return m_n

    def play_music(self, name):
        for music, notes in self.dict_note.items():
            if music == name:
                current_m = {name: notes}
                s = Sound(current_m, Display())
                s.play_notes(notes)


# m = Note([])
# print(m.dict_note)
#
# print(m.record('eee'))
