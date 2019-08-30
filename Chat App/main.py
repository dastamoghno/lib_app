import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput



class ConnectPage(GridLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Defining the number of columns in the grid to be 2
        self.cols = 2
        
        # Adding IP data
        self.add_widget(Label(text="IP:"))
        self.ip = TextInput(multiline=False)
        self.add_widget(self.ip)
        
        # Adding port data
        self.add_widget(Label(text="Port:"))
        self.port = TextInput(multiline=False)
        self.add_widget(self.port)
        
        # Adding IP data
        self.add_widget(Label(text="Username:"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)


class MainApp(App):

    def build(self):
        return ConnectPage()
        
if __name__=="__main__":
    MainApp().run()
