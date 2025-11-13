import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
class Lay(FakeRectangularElevationBehavior,MDCard):
    pass

class Input(Lay):
    from kivy.properties import ObjectProperty
    obj = ObjectProperty('')

from kivy.uix.screenmanager import ScreenManager 
class login(ScreenManager):
    pass

from kivymd.app import MDApp
from kivy.properties import StringProperty,BooleanProperty,NumericProperty
from kivy.clock import mainthread
class ProjectApp(MDApp):
    mail =StringProperty('')
    week=NumericProperty(1)
    today=StringProperty('')
    date=StringProperty('')
    bool =BooleanProperty(False)
    bool_2=BooleanProperty(False)

    def build(self):
        
        from kivy.lang import Builder
        from kivy.clock import Clock
        from kivy.core.window import Window
        Builder.load_file('Login.kv')
        self.log = login()
        Clock.schedule_once(self.kill,1)
        self.theme_cls.primary_palette='Red'
        return self.log
    
    def change(self):
        from SignUp import Up
        Up.sm =self.log
        self.log.add_widget(Up(name='Up'))
        self.log.current = 'Up'
    
    def on_resume(self):
        from kivy.core.window import Window 
        print(2)
        Window.update_viewport()
    
    def call(self):
        
        from kivy.uix.modalview import ModalView
        from kivy.factory import Factory 
        self.modal =ModalView(background_color=[0,0,0,0])
        self.modal.add_widget(Factory.CustomSpinner())
        self.modal.open()
        from threading import Thread
        t =Thread(target=self.sleep)
        t.start()
    
    @mainthread    
    def sleep(self):
        pas=self.log.ids.password.ids.txt.text
        user=self.log.ids.Username.ids.txt.text
        try:
            from contextlib import closing
            from datetime import date
            from socket import socket,AF_INET,SOCK_DGRAM
            import struct
            NTP_PACKET_FORMAT = "!12I"
            NTP_DELTA = 2208988800  # 1970-01-01 00:00:00
            NTP_QUERY = b'\x1b' + 47 * b'\0'
            def ntp_time(host="pool.ntp.org", port=123):
                with closing(socket( AF_INET, SOCK_DGRAM)) as s:
                    s.sendto(NTP_QUERY, (host, port))
                    msg, address = s.recvfrom(1024)
                    unpacked = struct.unpack(NTP_PACKET_FORMAT,msg[0:struct.calcsize(NTP_PACKET_FORMAT)])
                
                return unpacked[10] + float(unpacked[11]) / 2**32 - NTP_DELTA
            import time
            
            j=time.ctime(ntp_time())
            self.today = j[:3]
            rep={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
            da=date(int(j[20:]),rep[j[4:7]],int(j[8:10])).isocalendar()
            
            
            try:
                from fire import auth
                auth.sign_in_with_email_and_password(user,pas)
                self.mail=user[:user.index('@')]
                from fire import db
                if [da[0],da[1]]!=db.child(self.mail).child('_w_e_e_k').get().val()['iso'][:2]:
                    r=db.child(self.mail).child('_w_e_e_k').child('save').get().val()[0]
                    db.child(self.mail).child('_w_e_e_k').update({'save':[r+1]})
                    db.child(self.mail).child('_w_e_e_k').update({'iso':[da[0],da[1]]})
                self.week =db.child(self.mail).child('_w_e_e_k').child('save').get().val()[0]
                
                try:
                    self.bool=False 
                    self.bool_2=False
                    valid=db.child(self.mail).child(f'Week {self.week}').child(self.today).get().val()
                    if valid:
                        try:
                            if valid['s']:
                                self.bool=True
                        except:
                            pass
                        try:
                            if valid['l']:
                                self.bool_2=True
                        except:
                            pass
                except:
                    pass
                self.modal.dismiss()
                self.log.current ='Home'
                self.modal.clear_widgets()
            except Exception as e:
                import json 
                if len(e.args)>1:
                    err=json.loads(e.args[1])['error']['message']
                    from kivymd.toast import toast
                    toast(str(err))
                else:
                    from kivymd.toast import toast
                    toast('You have no data connection.')
                self.modal.dismiss()
        except Exception as e:
            self.modal.dismiss()
            print(e.args,1)
            from kivymd.toast import toast
            toast('You have no data connection.')
        


    def kill(self,dt):
        from Navig import vig
        vig.sm = self.log 
        self.log.add_widget(vig(name='Home'))
        
if __name__ =='__main__':
    ProjectApp().run()

