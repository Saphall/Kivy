from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor=(0.6,0.6,1,1)

class MainApp(App):
    def build(self):
        label = Label ( text="hello this is first kivy app",
        font_size='30sp',
        bold=True,italic=False,color=(0,0,0,1))
        return label



MainApp().run()
