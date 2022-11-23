import json


class Data:

    def __init__(self, music: dict):
        self.music = music

    def write(self):
        """ store the music's name with notes to database """
        try:
            with open('database.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('database.json', 'w') as data_file:
                json.dump(self.music, data_file, indent=4)
        else:
            data.update(self.music)
            with open('database.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

    @staticmethod
    def read():
        """ return the data of music list """
        try:
            with open('database.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            pass
        else:
            return data


# m_n = Data({'test': ['cc', 'c', 'd', '', 'e']})
# m_n.write()
# print(Data.read())
