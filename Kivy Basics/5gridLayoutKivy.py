from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
Window.clearcolor=(0.2,0.2,0.2,1)

class MainApp(App):
    def build(self):
        layout=GridLayout(cols=2,row_force_default=True,
        row_default_height=40)
        b1 = Button(text='Hello1',size_hint=(None,None),width=100,height=40)
        b2 = Button(text='Hello1')
        b3 = Button(text='Hello1',size_hint=(None,None),width=100,height=40)
        b4 = Button(text='Hello1')
        layout.add_widget(b1)
        layout.add_widget(b2)
        layout.add_widget(b3)
        layout.add_widget(b4)
        return layout

MainApp().run()
