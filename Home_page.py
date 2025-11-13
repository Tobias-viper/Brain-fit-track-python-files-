from kivy.lang import Builder
Builder.load_file('Home_page.kv')
from kivy.uix.screenmanager import Screen

scores_l =[]
scores_s=[]

class Home(Screen):
    from kivy.properties import ObjectProperty
    sm= ObjectProperty()
    #eqivalent score for each ative checkbox
    #scores=[b t attentive,pb t deliberate,b tregula,b t flex]b=box t=ticked
    #b_val={not at all:4,one or twice :3,some:2,most:1,all:0} b_val=to read the meaning of the scores
    
    def level(self,x):
        
        from kivy.uix.modalview import ModalView
        from kivy.factory import Factory 
        self.modal =ModalView(background_color=[0,0,0,0])
        self.modal.add_widget(Factory.CustomSpinner())
        self.li_checkbox =[]#to save the each active checkbox 
        
        for i in range(4):
            if i == 0:
                check=x.children[i].children[2]
            else:
                check=x.children[i].children[1]
            #here is the cointainer,we need to interate it to get to each all checkbox
            for l in range(5):#this loop is for the 5 checkbox for a skill or level     
                checkbox=check.children[l].children[1].children[0].children[0]
                if checkbox.active:
                    self.li_checkbox.append(checkbox)
                    if l<=2:
                        scores_l.append(5-l)
                    else:
                        scores_l.append(4-l)
        if len(self.li_checkbox)!=4:
            from kivymd.toast import toast
            toast('Make sure you tick a box for each skill before submitting')
        else:
            self.modal.open()   
            from threading import Thread
            t =Thread(target=self.sleep,args=(2,))
            t.start()

    
    def sleep(self,number):
        try:
            from fire import db 
            import time
            from kivymd.app import MDApp
            today=MDApp.get_running_app().today
            user = MDApp.get_running_app().mail
            week=MDApp.get_running_app().week
            print(2)
            if number == 1:
                db.child(user).child(f'Week {week}').child(today).update({'s':scores_s[::-1]})
                for i in self.li_checkbo:
                    i.active =False
                self.ids.bttn_1.disabled = True
            else:
                lev = scores_l[::-1]
                new=[]
                for k in range(4):
                    new.append(lev[k]*(k+1))
                db.child(user).child(f'Week {week}').child(today).update({'l':new})
                self.ids.bttn_2.disabled = True
                for i in self.li_checkbox:
                    i.active =False
            time.sleep(3)
            self.modal.dismiss()
            self.modal.clear_widgets()
        except Exception as e:
            self.modal.dismiss()
            from kivymd.toast import toast
            toast('You have no data connection.')

    def skill(self,x):
    
        from kivy.uix.modalview import ModalView
        from kivy.factory import Factory 
        self.modal =ModalView(background_color=[0,0,0,0])
        self.modal.add_widget(Factory.CustomSpinner())
        self.li_checkbo =[]
        for i in range(4):
            if i == 0:
                check=x.children[i].children[2]
            else:
                check=x.children[i].children[1]
            #check here is the cointainer
            for l in range(5):    
                checkbox=check.children[l].children[1].children[0].children[0]
                if checkbox.active:
                    self.li_checkbo.append(checkbox)
                    if l<=2:
                        scores_s.append(5-l)
                    else:
                        scores_s.append(4-l)
        if len(self.li_checkbo)!=4:
            from kivymd.toast import toast
            toast('Make sure you tick a box for each skill before submitting')
        else:
            self.modal.open()
            from threading import Thread
            t =Thread(target=self.sleep,args=(1,))
            t.start()

from kivymd.uix.tab import MDTabsBase
from kivy.uix.boxlayout import BoxLayout
class Tab(BoxLayout,MDTabsBase):
    pass
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
class Card(MDCard,FakeRectangularElevationBehavior):
    pass
