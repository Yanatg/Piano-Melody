import json


class Data:
    """ read/write data """
    def __init__(self, music=None):
        self.music = music
        self.d_note = self.read()

    def write(self):
        """ store the music's name with notes to database """
        try:
            with open('database.json', 'r', encoding='utf-8') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('database.json', 'w', encoding='utf-8') as data_file:
                json.dump(self.music, data_file, indent=4)
        else:
            data.update(self.music)
            with open('database.json', 'w', encoding='utf-8') as data_file:
                json.dump(data, data_file, indent=4)

    @staticmethod
    def read():
        """ return the data of music list """
        try:
            with open('database.json', 'r', encoding='utf-8') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            pass
        else:
            return data
        return None
