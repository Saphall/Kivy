from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from helpers import username_helper

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette='Green'
        screen = Screen()

        button = MDRectangleFlatButton(text='Show',
        pos_hint={'center_x':0.5,'center_y':0.4},
        on_release=self.show_data)
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def show_data(self,obj):
        print(self.username.text)

DemoApp().run()
