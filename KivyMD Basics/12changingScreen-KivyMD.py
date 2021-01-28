from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager

screen_helper='''
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<MenuScreen>:
    name:'menu'
    MDRectangleFlatButton:
        text:'Profile'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current ='profile'
    MDRectangleFlatButton:
        text:'Upload'
        pos_hint:{'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current ='profile'

<ProfileScreen>:
    name:'profile'
    MDLabel:
        text:'Saphall'
        halign:'center'
    MDRectangleFlatButton:
        text:'Back'
        pos_hint:{'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current ='menu'

<UploadScreen>:
    name:'upload'
    MDLabel:
        text:'Upload some file'
        halign:'center'
    MDRectangleFlatButton:
        text:'Upload'
        pos_hint:{'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current ='Back'

'''
class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class UploadScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(ProfileScreen(name='upload'))

class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

DemoApp().run()
