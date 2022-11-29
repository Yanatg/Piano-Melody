from data import Data
from sound import Sound
from display import Display

all_music = Data()


class Note:
    """ manage the music and notes """
    def __init__(self, note_list=None):
        self.note_l = note_list
        self.all_note = [all_music.d_note, all_music.music]

    def record(self, name):
        """ make the data to record the music """
        m_n = {name: self.note_l}
        return m_n

    def play_music(self, name):
        """ play music that the user picked """
        # for data in self.dict_note[0]:
        for music, notes in self.all_note[0].items():
            if music == name:
                current_m = {name: notes}
                music_ = Sound(current_m, Display())
                music_.play_notes(notes)
