from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.uix.list import MDList,OneLineListItem,TwoLineListItem,ThreeLineListItem

helper_string='''
ScreenManager:
    Home:

<Home>:
    name:'home'

    ScrollView:
        MDList:
            id:ls

'''
class Home(Screen):
    pass

sc = ScreenManager()
sc.add_widget(Home(name='home'))

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.help_str = Builder.load_string(helper_string)
        screen.add_widget(self.help_str)
        return screen

    def on_start(self):
        for i in range(20):
            self.help_str.get_screen(name='home').ids.ls.add_widget(
                OneLineListItem(text=f'Hello {i+1}'))
            self.help_str.get_screen(name='home').ids.ls.add_widget(
                TwoLineListItem(text='Hello',secondary_text=f'{i+1}'))
            self.help_str.get_screen(name='home').ids.ls.add_widget(
                ThreeLineListItem(text='HHH',secondary_text=f'{i}',
                tertiary_text=f'pro')
            )

DemoApp().run()
