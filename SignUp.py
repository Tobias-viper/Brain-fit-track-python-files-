from kivy.uix.screenmanager import Screen 
from kivy.lang import Builder
Builder.load_file('SignUp.kv')
class Up(Screen):    
    def change(self):
        self.sm.current ='log'
        self.sm.remove_widget(self)
    def on_enter(self,*args):
        self.x =0 
    
    def register(self,email,password,confirm):
        from kivymd.toast import toast 
        if (password == confirm):
            if len(password) >=7:
                try:
                    self.start()
                    self.x +=1
                    from threading import Thread
                    ti=Thread(target=self.Register,args=(email,password))
                    ti.start()
                except Exception as e:
                    toast('You have no data connection.')
            else:
                toast('Password must have a minimum of 7 characters.')
        else:
            
            toast('Password and Confirm Password don\'t match.')
    def start(self):
        if not int(self.x):
            from kivy.uix.modalview import ModalView
            from kivy.factory import Factory 
            self.modal =ModalView(background_color=[0,0,0,0])
            if not len(self.modal.children):
                self.modal.add_widget(Factory.CustomSpinner())
            self.modal.open()
        else:
            self.modal.open()

    def Register(self,email,password):
        try:
            from kivymd.toast import toast
            import fire
            import time
            fire.auth.create_user_with_email_and_password(email,password)
            from contextlib import closing
            from datetime import date
            from socket import socket,AF_INET,SOCK_DGRAM
            import struct
            import time
            NTP_PACKET_FORMAT = "!12I"
            NTP_DELTA = 2208988800  # 1970-01-01 00:00:00
            NTP_QUERY = b'\x1b' + 47 * b'\0'
            def ntp_time(host="pool.ntp.org", port=123):
                with closing(socket( AF_INET, SOCK_DGRAM)) as s:
                    s.sendto(NTP_QUERY, (host, port))
                    msg, address = s.recvfrom(1024)
                    unpacked = struct.unpack(NTP_PACKET_FORMAT,msg[0:struct.calcsize(NTP_PACKET_FORMAT)])
                return unpacked[10] + float(unpacked[11]) / 2**32 - NTP_DELTA
            j=time.ctime(ntp_time())
            rep={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
            da=date(int(j[20:]),rep[j[4:7]],int(j[8:10])).isocalendar()
            fire.db.child(email[:email.index('@')]).child('_w_e_e_k').set({'save':[1]})
            fire.db.child(email[:email.index('@')]).child('_w_e_e_k').update({'iso':[da[0],da[1]]})

            time.sleep(6)
            self.modal.dismiss()
            self.change()
            toast('done')
        except Exception as e:
            import json
            print(e.args)
            if len(e.args)>1:
                err=json.loads(e.args[1])['error']['message']
                toast(str(err))
            else:
                toast('You have no data connection.')
            self.modal.dismiss()

            
            
        
        

                
