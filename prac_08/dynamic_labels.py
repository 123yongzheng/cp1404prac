from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class NamesApp(App):

    def build(self):
        names = ['Alice', 'Bob', 'Charlie', 'David', 'Emily']
        layout = BoxLayout(orientation='vertical')
        sub_layout = BoxLayout(orientation='horizontal')
        sub_layout.add_widget(Label(text='Name'))
        sub_layout.add_widget(Label(text='Length'))
        layout.add_widget(sub_layout)
        for name in names:
            sub_layout = BoxLayout(orientation='horizontal')
            sub_layout.add_widget(Label(text=name))
            sub_layout.add_widget(Label(text=str(len(name))))
            layout.add_widget(sub_layout)
        return layout

NamesApp().run()
