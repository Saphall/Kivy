from kivymd.app import MDApp
from  kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text='Hello World',
        pos_hint={'center_x':0.5,'center_y':0.5})
        icon_btn = MDFloatingActionButton(icon='language-python',
        pos_hint={'center_x':0.5,'center_y':0.5})
        screen.add_widget(btn_flat)  # add_widget(btn_flat) or add_widge(icon_btn)
        return screen

DemoApp().run()
