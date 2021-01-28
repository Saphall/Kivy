from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon


class DemoApp(MDApp):
    def build(self):
        Label= MDLabel(text='Hello world',halign='center',theme_text_color='Custom',
        text_color=(0,0,1,1),font_style='H6')
        Icon_Label= MDIcon(icon='language-python',halign='center')
        #return Label
        return Icon_Label



DemoApp().run()
