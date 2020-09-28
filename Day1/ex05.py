class Camera:
    def __init__(self): print('Camera.__init__() executed')
    def take_photo(self): print('Taking picture, smile please...')


class MusicPlayer:
    def __init__(self): print('MusicPlayer.__init__() executed')
    def play_song(self): print('Playing nice music...')


class Phone:
    def __init__(self): print('Phone.__init__() executed')
    def make_call(self): print('Making a call...')
    def take_photo(self): print('Taking picture using builtin phone camera')


class SmartPhone(Phone, Camera, MusicPlayer):

    def __init__(self):
        # super().__init__()
        Phone.__init__(self)
        Camera.__init__(self)
        MusicPlayer.__init__(self)
        print('SmartPhone.__init__() executed')

    def take_photo(self):
        # super().take_photo() # --> Phone.take_photo(self)
        Phone.take_photo(self)
        Camera.take_photo(self)


def hello(name):
    pass


def main():

    sp = SmartPhone()
    print(f'attributes in sp are {dir(sp)}')
    sp.make_call()
    sp.take_photo()
    sp.play_song()

    hello('vinod')
    hello(100)
    hello(False)

if __name__ == '__main__':
    main()
