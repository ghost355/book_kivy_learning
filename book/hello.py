from kivy.uix.button import Label
from kivy.app import App
import kivy
kivy.require('1.9.0')


class HelloApp(App):
    def build(self):

        return Label(text="Hello MAZAFAKA!!")


if __name__ == '__main__':
    HelloApp().run()
