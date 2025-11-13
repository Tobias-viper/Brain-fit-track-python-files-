from kivy.uix.screenmanager import Screen 
from kivy.lang import Builder 
Builder.load_file('Overall.kv')
from kivymd.uix.datatables import MDDataTable
from kivy.core.window import Window
from kivy.metrics import dp 
class Oval(Screen):
    def __init__(self,**kws):
        super().__init__(**kws)     
        self.Widget()

    
    def Widget(self):
        from kivymd.utils import asynckivy
        from kivymd.app import MDApp 
        self.today=MDApp.get_running_app().today
        self.mail = MDApp.get_running_app().mail
        self.week=MDApp.get_running_app().week
        from fire import db
        async def call():
            from kivymd.uix.label import MDLabel
            #from Home_page import scores_l,scores_s
            trans = {'5':'All the time','4':'Most of the time','3':'Some of the time','1':'Once or twice','0':'Not at all'}#to translate give correspoinding number in scores_l and _s option 

            try:
                scores_l=db.child(self.mail).child(f'Week {self.week}').child(self.today).get().val()['l']
                row_data_l=[('Level 1',trans[f'{scores_l[0]}'],f'{scores_l[0]}'),('Level 2',trans[f'{int(scores_l[1]/2)}'],f'{scores_l[1]}'),('Level 3',trans[f'{int(scores_l[2]/3)}'],f'{scores_l[2]}'),('Level 4',trans[f'{int(scores_l[3]/4)}'],f'{scores_l[3]}')]
            except Exception as e:
                print(e.args)
                row_data_l=[]
            try:
                scores_s=db.child(self.mail).child(f'Week {self.week}').child(self.today).get().val()['s']
                row_data_s=[('Flexible',trans[f'{scores_s[0]}'],f'{scores_s[0]}'),('Regulated',trans[f'{scores_s[1]}'],f'{scores_s[1]}'),('Deliberate',trans[f'{scores_s[2]}'],f'{scores_s[2]}'),('Attentive',trans[f'{scores_s[3]}'],f'{scores_s[3]}')]
            except Exception as e:
                print(e.args)
                row_data_s=[]
            
            
            lab_1=MDLabel(text='Scores For Today\'s Helpful Skills',halign='center',adaptive_height=True)
            
            helpful_table=MDDataTable(check=False,use_pagination=False,column_data=
                [('Skill',Window.width/13.5),('Option',Window.width/13.5),('Score',Window.width/30)],size_hint_y=None,height=dp(210),row_data=row_data_s)
            
            up =[lab_1,helpful_table]
            
            lab_2=MDLabel(text='Scores For Today\'s Unhelpful Behaviour',halign='center',adaptive_height=True)
            
            unhelpful_table=MDDataTable(check=False,use_pagination=False,column_data=
                [('Level',Window.width/13.5),('Option',Window.width/13.5),('Score',Window.width/30)],size_hint_y=None,height=dp(210),row_data=row_data_l)
            
            down =[lab_2,unhelpful_table]
            
            for i in range(2):
                await asynckivy.sleep(2)
                self.children[1].add_widget(up[i])
            for i in range(2):
                await asynckivy.sleep(2)
                self.children[0].add_widget(down[i])
            try:
                if scores_s:
                    self.children[1].add_widget(MDLabel(text=f'Total:{sum(scores_s)}',pos_hint={'x':.8}))
            except:
                pass
            try:
                if scores_l:
                    self.children[0].add_widget(MDLabel(text=f'Total:{sum(scores_l)}',pos_hint={'x':.8}))
            except:
                pass
        asynckivy.start(call())
                
        