import time

import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty

hour = 0
minute = 0
second = 0

class TextWidget(Widget):
    text = StringProperty()

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ""

    def buttonClicked(self):
        hour = int(self.ids["hour_box"].text)
        minute = int(self.ids["minute_box"].text)
        second = int(self.ids["second_box"].text)
        allTime = hour * 3600 + minute * 60 + second
        for i in range(allTime,-1,-1):
            self.text = str(i)
            time.sleep(1)
        self.text = "finished"

class MyApp(App):

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.title = 'timer.py'
    
    def build(self):
        return TextWidget()

if __name__ == '__main__':
    MyApp().run()