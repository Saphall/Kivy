from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MainApp(App):
    def build(self):
        layout = GridLayout(cols=2,row_force_default=True,
        row_default_height=40,padding=20,spacing=10)
        self.weight  = TextInput(text='Enter your weight: ')
        self.height = TextInput(text="Enter your height: ")
        submit = Button(text='Submit',on_press=self.submit)
        layout.add_widget(self.weight)
        layout.add_widget(self.height)
        layout.add_widget(submit)
        return layout

    def submit(self,obj):
        print(f"your weight is:"+self.weight.text)
        print(f"your height is :"+self.height.text)

MainApp().run()
