from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


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
    MDTextField:
        id:username_text
        hint_text:'Enter Username'
        color_mode: 'custom'
        line_color_normal:app.theme_cls.primary_color
        line_color_focus:0,0.5,0,1
        helper_text:'Required'
        helper_text_mode:'on_error'
        #mode:'rectangle'
        icon_right:'account'
        icon_right_color:0,0.5,0,0.9
        pos_hint:{'center_x':0.5,'center_y':0.7}
        required:True
        size_hint:(0.8,0.1)
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.5, 'center_y':0.6}
        on_release:app.username_checker()

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
        self.theme_cls.theme_style=='Light'
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

    def username_checker(self):
        username_check_false=True
        username_text_data = self.help_str.get_screen('first_screen').ids.username_text.text
        try:
            int(username_text_data)
        except:
            username_check_false= False

        if username_check_false or username_text_data.split()==[]:
            cancel_btn=MDFlatButton(text='Retry',on_release=self.close_dialog)
            self.username_dialog = MDDialog(title='Invalid Username',text='Please enter a valid username',
                                    size_hint=(0.8,0.2),
                                    buttons=[cancel_btn])
            self.username_dialog.open()

    def close_dialog(self,obj):
        self.username_dialog.dismiss()


DemoApp().run()
