from kivy.app import App
from kivy.core.window import Window
Window.clearcolor=(1,1,1,1)
Window.size=(368,600)

from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical',spacing=100,padding=80)
        img = AsyncImage(source='https://maps.wbphed.gov.in/pwss_new/admin/images/login-img.jpg')
        btn = Button(text='Login',size_hint=(None,None),
        width=150,height=40,pos_hint={'center_x':0.5})
        layout.add_widget(img)
        layout.add_widget(btn)
        return layout

MainApp().run()
