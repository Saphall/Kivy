from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder

helper_string = '''
ScreenManager:
    HomePage:
    ScreenOne:

<HomePage>:
    name:'home'
    MDLabel:
        id: text_change
        text: 'Hello World'
        halign:'center'
        font_style: 'H6'
    MDRectangleFlatIconButton:
        icon:'android'
        text: 'Next Screen'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        on_release:
            root.manager.current='first_screen'
            root.manager.transition.direction='left'
    MDRoundFlatButton:
        text:'Theme Changer'
        pos_hint:{'center_x':0.5,'center_y':0.8}
        on_release:
            app.theme_changer()
    MDRoundFlatButton:
        text:'Property Changer'
        pos_hint:{'center_x':0.5,'center_y':0.7}
        on_release:
            app.property_changer()

<ScreenOne>:
    name: 'first_screen'
    MDLabel:
        text:'Second'
        halign:'center'
        font_style:'H6'
    MDRectangleFlatIconButton:
        icon:'home'
        text:'Homepage'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        on_release:
            root.manager.current='home'
            root.manager.transition.direction ='right'
'''

class HomePage(Screen):
    pass
class ScreenOne(Screen):
    pass

sm=ScreenManager()
sm.add_widget(HomePage(name='home'))
sm.add_widget(ScreenOne(name='first_screen'))

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.help_str = Builder.load_string(helper_string)
        screen.add_widget(self.help_str)
        return screen

    def theme_changer(self):
        if self.theme_cls.theme_style=='Light':
            self.theme_cls.theme_style='Dark'
        else:
            self.theme_cls.theme_style='Light'

    def property_changer(self):
        if self.help_str.get_screen('home').ids.text_change.text=='Hello World':
            self.help_str.get_screen('home').ids.text_change.text='Bye World'
        else:
            self.help_str.get_screen('home').ids.text_change.text='Hello World'


DemoApp().run()
