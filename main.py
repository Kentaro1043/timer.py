import time
import math

import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

hour = 0
minute = 0
second = 0

class TextWidget(Widget):
    text = StringProperty()

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ""

    def intervalCountdown(self,dt):
        self.allTime = self.allTime - 1
        self.hourText = "00" + str(math.floor(int(self.allTime) / 3600))
        self.minuteText = "00" + str(math.floor(int(self.allTime) % 3600 / 60))
        self.secondText = "00" + str(math.floor(int(self.allTime) %3600 % 60))
        self.text = self.hourText[-2:] + ":" + self.minuteText[-2:] + ":" + self.secondText[-2:]
        if self.allTime == -1:
            self.text = "finished"
            self.ids["okButton"].disabled = False
            self.ids["stopButton"].disabled = True
            self.ids["pauseButton"].disabled = True
            return False

    def startButton(self):
        try:
            if self.ids["hour_box"].text == "":
                hour = 0
            else:
                hour = int(self.ids["hour_box"].text)
            if self.ids["minute_box"].text == "":
                minute = 0
            else:
                minute = int(self.ids["minute_box"].text)
            if self.ids["second_box"].text == "":
                second = 0
            else:
                second = int(self.ids["second_box"].text)
        except ValueError:
            self.text = "illegal value!"
            return 0
        self.allTime = hour * 3600 + minute * 60 + second
        if self.allTime < 0:
            self.text = "illegal value!"
            return 0
        self.hourText = "00" + str(math.floor(int(self.allTime) / 3600))
        self.minuteText = "00" + str(math.floor(int(self.allTime) % 3600 / 60))
        self.secondText = "00" + str(math.floor(int(self.allTime) %3600 % 60))
        self.text = self.hourText[-2:] + ":" + self.minuteText[-2:] + ":" + self.secondText[-2:]
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

    def okButton(self):
        self.text = ""
        self.ids["okButton"].disabled = True
        self.ids["stopButton"].disabled = True
        self.ids["pauseButton"].disabled = True
        self.ids["restartButton"].disabled = True
        self.ids["startButton"].disabled = False

    
class MyApp(App):

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.title = 'timer.py'
    
    def build(self):
        self.icon = 'icon.ico'
        return TextWidget()

if __name__ == '__main__':
    MyApp().run()