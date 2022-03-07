
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button


class gridviewdd(GridLayout):
    def __init__(self,**kwargs):
        super(gridviewdd, self).__init__()

        self.inside=GridLayout()
        self.inside.cols = 2
        self.inside.add_widget(Label(text="Name :"))
        self.s_name=TextInput(multiline=False)
        self.inside.add_widget(self.s_name)

        self.inside.add_widget(Label(text="Marks :"))
        self.s_marks = TextInput(multiline=False)
        self.inside.add_widget(self.s_marks)

        self.inside.add_widget(Label(text="gender :"))
        self.s_gen = TextInput(multiline=False)
        self.inside.add_widget(self.s_gen)

        self.add_widget(self.inside)
        self.cols=1

        self.press=Button(text="click me",font_size=40)
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)

    def click_me(self,instance):
        print("Enter {}".format(self.s_name.text))
        self.s_name.text=""

class first(App):
    def build(self):
        return gridviewdd()

if __name__=="__main__":
    first().run()
