from kivy.app import App
from kivy.core.window import Window
from kivy.uix.image import Image,AsyncImage

Window.clearcolor=(0,0,0,1)

class MainApp(App):
    def build(self):
        #img = Image(source='')
        img = AsyncImage(source='https://slackwarecafe.files.wordpress.com/2019/03/kivy-logo-250x250.jpg')

        return img

MainApp().run()
