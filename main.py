from note import Note
from sound import Sound
from data import Data
from display import Display

from turtle import textinput

stage = Display()

menu = stage.menu()
music = Sound({}, stage)

record = ['record', 'r']
practice = ['practice', 'p']
play_music = ['play music', 'playmusic', 'pm', 'm']

while menu and isinstance(menu, str):

    while menu.lower() in record or menu.lower() in practice or menu.lower() in play_music:

        if menu.lower() in record:
            print(f"You choose to record the music. "
                  f"~Enjoy~\n{'-----'*12}")
            stage.rec_screen()
            name = stage.ask_name_r()

            if name:    # print music's name
                print(f"music's title {name}\n{'-----'*12}")
            else:
                print("Aren't you really going to record the music? :(")
                quit()

            while len(name) >= 15:
                print(f"Music's name must be less than 15 characters.\n{'-----'*12}")
                name = stage.ask_name_r()
            while not name:
                print(f"Your music must have a name.\nPlease try again\n{'-----'*12}")
                name = stage.ask_name_r()
            music.play_current_sound()

            m = Note(music.note_list)
            m_with_n = m.record(name)
            data = Data(m_with_n)
            data.write()

            print(f"Your music is wonderful. Thank you for using our piano."
                  f"\nYou can now listen to your recorded music."
                  f"\n{'-----'*12}")
            quit()

        elif menu.lower() in play_music:
            print(f"You choose to play the music. ~Enjoy~\n{'-----' * 12}")
            stage.show_music_list()
            music_name = stage.ask_name_pm()
            stage.pm_screen()

            music_to_play = Data.read()
            try:
                while music_name not in music_to_play:
                    print(f"Sorry, The music you want doesn't seem to be in the data."
                          f"\nPlease try again, Ensure the song you entered is correct."
                          f"\n{'-----'*12}")
                    music_name = stage.ask_name_again_pm()
            except TypeError:
                quit()
            else:
                while music_name not in music_to_play:
                    print(f"There is no list of songs you want to play in our system."
                          f"\nPlease try one more time."
                          f"\n\n{'-----'*12}")
                    music_name = stage.ask_name_again_pm()

            note = Note()
            note.play_music(music_name)

            print(f"The music is over, Hope you're happy :)"
                  f"\n{'-----'*12}")
            quit()

        elif menu.lower() in practice:
            print(f"You choose to practice.\n{'-----'*12}")

            # stage.init_screen()
            stage.prac_screen()
            music.play_current_sound()

            print('You practiced well.\nYou can record your own music if you want!')
            quit()

    else:
        print(f'You did not choose any menu or choose the invalid one.'
              f'\nPlease try again'
              f"\n{'-----'*12}")
        menu = textinput("Which menu would you like to do?",
                         "record / practice / play music")

print("Aren't you really going to use my piano? :(")
