import sys
from colorama import Fore, Style

from note import Note
from sound import Sound
from data import Data
from display import Display

stage = Display()

menu = stage.menu()
music = Sound({}, stage)

record = ['record', 'r']
practice = ['practice', 'p']
play_music = ['play music', 'playmusic', 'pm', 'm']

while isinstance(menu, str):
    print()
    print(Fore.LIGHTYELLOW_EX + '         Welcome to Piano Melody!')
    print(Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX +
          ' _______________________________________\n'
          '|  | | | |  |  | | | | | |  |  | | | |  |\n'
          '|  | | | |  |  | | | | | |  |  | | | |  |\n'
          '|  | | | |  |  | | | | | |  |  | | | |  |\n'
          '|  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |\n'
          '|   |   |   |   |   |   |   |   |   |   |\n'
          '|   |   |   |   |   |   |   |   |   |   |\n'
          '|___|___|___|___|___|___|___|___|___|___|\n')
    print(Style.RESET_ALL)
    print('You have three menus to choose')
    print(Fore.LIGHTGREEN_EX +
          'record\n'
          'practice\n'
          'play music\n')
    print(Style.RESET_ALL)
    while menu.lower() in record or menu.lower() in practice or menu.lower() in play_music:

        if menu.lower() in record:
            print(f"You choose to record the music. "
                  f"~Enjoy~\n{'-----'*12}")
            stage.rec_screen()
            name = stage.ask_name_r()

            try:
                while len(name) >= 15 or not name:
                    if len(name) >= 15:
                        print(f"Music's name must be less than 15 characters.\n{'-----' * 12}")
                    if not name:
                        print(f"Your music must have a name.\nPlease try again\n{'-----' * 12}")
                    name = stage.ask_name_r()
            except TypeError:
                print(Fore.LIGHTMAGENTA_EX + "Aren't you really going to use my piano? :(")
                sys.exit()

            print(f"music's title {name}\n{'-----' * 12}")
            music.play_current_sound()

            m = Note(music.note_list)
            m_with_n = m.record(name)
            data = Data(m_with_n)
            data.write()

            print(f"Your music is wonderful. Thank you for using our piano."
                  f"\nYou can now listen to your recorded music."
                  f"\n{'-----'*12}")
            sys.exit()

        elif menu.lower() in play_music:
            print(f"You choose to play the music. ~Enjoy~\n{'-----' * 12}")
            stage.show_music_list()
            music_name = input("music's name\n"
                               "May I ask for the music's name you want to listen?\n"
                               "Enter here: ")
            stage.pm_screen()

            music_to_play = Data.read()
            try:
                while music_name not in music_to_play:
                    print(f"Sorry, The music you want doesn't seem to be in the data."
                          f"\nPlease try again, Ensure the song you entered is correct."
                          f"\n{'-----'*12}")
                    music_name = input("music's name\n"
                                       "May I ask you again for the music's name you want to listen?\n"
                                       "Enter here: ")
            except TypeError:
                sys.exit()
            else:
                while music_name not in music_to_play:
                    print(f"There is no list of songs you want to play in our system."
                          f"\nPlease try one more time."
                          f"\n\n{'-----'*12}")
                    music_name = input("music's name\n"
                                       "May I ask you again for the music's name you want to listen?\n"
                                       "Enter here: ")

            note = Note()
            note.play_music(music_name)

            print(f"The music is over, Hope you're happy :)"
                  f"\n{'-----'*12}")
            sys.exit()

        elif menu.lower() in practice:
            print(f"You choose to practice.\n{'-----'*12}")
            stage.prac_screen()
            music.play_current_sound()
            print('You practiced well.\nYou can record your own music if you want!')
            sys.exit()

    print(Fore.LIGHTRED_EX +
          f'You did not choose any menu or choose the invalid one.'
          f'\nPlease try again'
          f"\n{'-----'*12}")
    menu = stage.menu()

print(Fore.LIGHTMAGENTA_EX + "Aren't you really going to use my piano? :(")
