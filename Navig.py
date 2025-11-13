from re import X
from kivy.uix.screenmanager import Screen 
from kivy.lang import Builder
from progress import Prog
Builder.load_file('Navig.kv')
from Home_page import Home

class vig(Screen):    
    from kivy.properties import ObjectProperty 
    sm= ObjectProperty()
    fi=ObjectProperty()

    def __init__(self,**kws):
        super().__init__(**kws)
        self.li=Prog()

    def open(self):
        from Overall import Oval
        self.ids.second.add_widget(Oval())
    
    def open_2(self):
        
        self.li=Prog()
        self.li.switch(1,2,3,'Today')
        self.ids.th.add_widget(self.li)
    
    def clear(self,*args):
        self.li.ids.today.clear_widgets()
        self.li.ids.Week.clear_widgets()
        self.li.ids.R.clear_widgets()
        self.li.ids.Al.clear_widgets()

        

    
    