import kivy
kivy.require('2.0.0')

from kivy.app import App


class MyApp(App):

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.title = 'timer.py'

if __name__ == '__main__':
    MyApp().run()