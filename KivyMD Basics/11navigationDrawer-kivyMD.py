from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (360, 600)

navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Navigation Drawer"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

                    Widget:

                    MDBottomAppBar:
                        MDToolbar:
                            mode:'end'
                            type:'bottom'
                            icon:'camera'
                            on_action_button: app.open_camera()

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                spacing:'8dp'
                padding:'11dp'
                orientation:'vertical'
                Image:
                    source: 'mine.jpg'
                MDLabel:
                    text:'Saphall'
                    font_style:'Subtitle1'
                    size_hint_y:None
                    height: self.texture_size[1]
                MDLabel:
                    text:'safalsakha@gmail.com'
                    font_style:'Caption'
                    size_hint_y:None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Profile'
                            IconLeftWidget:
                                icon:'face'
                        OneLineIconListItem:
                            text:'About'
                            IconLeftWidget:
                                icon:'information'
                        OneLineIconListItem:
                            text:'Logout'
                            IconLeftWidget:
                                icon:'logout'

"""

class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette='Purple'
        screen = Builder.load_string(navigation_helper)
        return screen

    def open_camera(self):
        print('Camera will open')

DemoApp().run()
