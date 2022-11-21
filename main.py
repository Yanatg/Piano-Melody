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

if isinstance(menu, str):

    while menu.lower() in record or menu.lower() in practice or menu.lower() in play_music:

        if menu.lower() in record:
            print(f"You choose to record the music. ~Enjoy~\n{'-----'*12}")
            name = stage.ask_name_r()
            stage.exit_msg()
            music.play_current_sound()

            m = Note(music.note_list)
            m_with_n = m.record(name)

            # print(m_with_n)
            # print(music.note_list)
            data = Data(m_with_n)
            data.write()

            print("Your music is wonderful. Thank you for using our piano."
                  "\nYou can now listen to your recorded music.")
            break

        elif menu.lower() in play_music:
            print(f"You choose to play the music. ~Enjoy~\n{'-----' * 12}")
            stage.show_music_list()
            music_name = stage.ask_name_pm()
            stage.pm_screen()
            music_to_play = Data.read()
            # print(music_to_play)
            note = Note()
            note.play_music(music_name)

            print("The music is over, Hope you're happy :)")
            break

        elif menu.lower() in practice:
            print('You choose to practice.')

            # stage.init_screen()
            stage.prac_screen()
            music.play_current_sound()

            print('You practiced well.\nYou can record your own music if you want!')
            break

        else:
            print('You did not choose any menu or choose the invalid one. \nPlease try again')
            menu = textinput("Which menu would you like to do?",
                             "record / practice / play music")

else:
    print("Aren't you really going to use my piano? :(")
