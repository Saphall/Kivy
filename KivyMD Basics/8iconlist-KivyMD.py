from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList,TwoLineListItem,ThreeLineListItem,ThreeLineAvatarListItem
from kivymd.uix.list import IconLeftWidget,ThreeLineIconListItem,ImageLeftWidget
from kivy.uix.scrollview import ScrollView

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)

        for i in range (20):
            icon = IconLeftWidget(icon = 'language-python')
            #image = ImageLeftWidget(source = 'image.png')
            items = ThreeLineIconListItem(text='Item'+str(i),   #If using custom-image(avatar), use ThreeLineAvatarListItem
                                    secondary_text='hello world',
                                    tertiary_text='third text')
            items.add_widget(icon)
            list_view.add_widget(items)


        screen.add_widget(scroll)
        return screen

DemoApp().run()
