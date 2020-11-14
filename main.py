import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty


class TextWidget(Widget):
    text = StringProperty()

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ""

    def buttonClicked(self):
        self.text = self.ids["text_box"].text

class MyApp(App):

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.title = 'timer.py'
    
    def build(self):
        return TextWidget()

if __name__ == '__main__':
    MyApp().run()