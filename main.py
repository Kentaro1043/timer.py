import time

import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.clock import Clock

hour = 0
minute = 0
second = 0

class TextWidget(Widget):
    text = StringProperty()

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ""

    def intervalCountdown(self,dt):
        self.text = str(int(self.text) - 1)
        if int(self.text) == -1:
            self.text = "finished"
            self.ids["stopButton"].disabled = True
            self.ids["pauseButton"].disabled = True
            self.ids["restartButton"].disabled = True
            self.ids["startButton"].disabled = False
            return False

    def startButton(self):
        try:
            hour = int(self.ids["hour_box"].text)
            minute = int(self.ids["minute_box"].text)
            second = int(self.ids["second_box"].text)
        except ValueError:
            self.text = "illegal value!"
            return 0
        allTime = hour * 3600 + minute * 60 + second
        if allTime < 0:
            self.text = "illegal value!"
            return 0
        self.text = str(allTime)
        self.ids["stopButton"].disabled = False
        self.ids["pauseButton"].disabled = False
        self.ids["restartButton"].disabled = True
        self.ids["startButton"].disabled = True
        Clock.schedule_interval(self.intervalCountdown,1)

    def stopButton(self):
        Clock.unschedule(self.intervalCountdown)
        self.text = ""
        self.ids["stopButton"].disabled = True
        self.ids["pauseButton"].disabled = True
        self.ids["restartButton"].disabled = True
        self.ids["startButton"].disabled = False

    def pauseButton(self):
        Clock.unschedule(self.intervalCountdown)
        self.ids["pauseButton"].disabled = True
        self.ids["restartButton"].disabled = False
    
    def restartButton(self):
        Clock.schedule_interval(self.intervalCountdown,1)
        self.ids["pauseButton"].disabled = False
        self.ids["restartButton"].disabled = True

class MyApp(App):

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.title = 'timer.py'
    
    def build(self):
        self.icon = 'icon.ico'
        return TextWidget()

if __name__ == '__main__':
    MyApp().run()