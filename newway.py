import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size=(500,700)



class MyGrid(Widget):
    def pressed(self,a):
        prior=self.ids.calc_input.text
        if 'error' in prior:
            self.ids.calc_input.text=f'{a}'
        elif prior=="0":
            self.ids.calc_input.text=f'{a}'
        else:
            self.ids.calc_input.text=f'{prior}{a}'
    def math_sign(self,sign):
        self.ids.calc_input.text=f'{self.ids.calc_input.text}{sign}'
    def on(self):
        prior=self.ids.calc_input.text
        if self.ids.calc_input.text[0]=='-':
            self.ids.calc_input.text = self.ids.calc_input.text[1:]
        else:
            self.ids.calc_input.text =f'-{prior}'


    def dot(self):
        prior=self.ids.calc_input.text
        list1=prior.split("+")

        if "+" in prior and '.' not in list1[-1]:
            self.ids.calc_input.text = f'{self.ids.calc_input.text}.'

        elif "." in prior:
            pass
        else:
            self.ids.calc_input.text=f'{self.ids.calc_input.text}.'
    def back(self):
        self.ids.calc_input.text=self.ids.calc_input.text[:-1]
    def equals(self):
        '''li=self.ids.calc_input.text.split("+")
        sum1=0
        for i in li:
            sum1=sum1+float(i)
        self.ids.calc_input.text=str(sum1)'''
        try:
            answer=eval(self.ids.calc_input.text)
            self.ids.calc_input.text=str(answer)
        except:
            self.ids.calc_input.text='error'


    def press(self):

        self.ids.calc_input.text='0'



class myapp(App):
    def build(self):
        return MyGrid()

if __name__=="__main__":
    myapp().run()