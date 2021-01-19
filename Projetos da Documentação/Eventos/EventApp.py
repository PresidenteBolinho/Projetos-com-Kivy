from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

class RootWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(RootWidget,self).__init__(**kwargs)
        self.add_widget(Button(text = 'btn 1'))
        cb = CustomBtn()
        cb.bind(pressed = self.btn_pressed)
        self.add_widget(cb)
        self.add_widget(Button(text = 'btn 2'))

    def btn_pressed(self, instance, pos):
        print('pos: printed from root widget: {pos}'.format(pos=pos))

