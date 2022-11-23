from data import Data
from sound import Sound
from display import Display


class Note:
    """ manage the music and notes """
    def __init__(self, note_list):
        self.note_l = note_list
        self.dict_note = Data.read()

    def record(self, name):
        """ make the data to record the music """
        m_n = {name: self.note_l}
        return m_n

    def play_music(self, name):
        """ play music that the user picked """
        for music, notes in self.dict_note.items():
            if music == name:
                current_m = {name: notes}
                music_ = Sound(current_m, Display())
                music_.play_notes(notes)
