data =[
{"Tue":{'l': [3, 3, 3, 3], 's': [1, 1, 1, 1]},
"Mon":{'l': [3, 3, 3, 3], 's': [1, 1, 1, 1]},
"Wed":{'l': [3, 3, 3, 3], 's': [1, 1, 1, 1]},
"Thu":{'l': [3, 3, 3, 3], 's': [1, 1, 1, 1]},
"Fri":{'l': [3, 3, 3, 3], 's': [1, 1, 1, 1]},
"Sat":{'l': [3, 3, 3, 3], 's': [1, 1, 1, 1]},
"Sun":{'l': [3, 3, 3, 3], 's': [1, 1, 1, 1]}
}
]
f=[];a=[];r=[];d=[];l1=[];l2=[];l3=[];l4=[]
for i in data:
    for mm in i:
        kk=i[mm]
        for ll in kk:
            if ll =="s":
                f.append(kk['s'][0])
                a.append(kk['s'][1])
                r.append(kk['s'][2])
                d.append(kk['s'][3])
            else:
                l1.append(kk['l'][0])
                l2.append(kk['l'][1])
                l3.append(kk['l'][2])
                l4.append(kk['l'][3])

print(len(f))
'''from kivy.clock import mainthread
from kivy.uix.screenmanager import Screen 
from kivy.lang import Builder 
from kivymd.uix.menu import MDDropdownMenu
Builder.load_file('progress.kv')


class Prog(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.x =0#to avoid adding widgets to the today tab multiple time 
        self.y=0
        self.R=0
        self.kk=0
        self.A =0
        from kivymd.app import MDApp
        self.menu_tem=[{'text':f'Week {i}','viewclass':'OneLineListItem'
        ,'on_release':lambda x=f'Week {i}':self.cal(x)}
        for i in range(1,MDApp.get_running_app().week+1)]
        self.menu =MDDropdownMenu(items=self.menu_tem,width_mult=4)
        
    def back(self,button):
        self.menu.caller=button
        self.menu.open()
    def cal(self,x):
    
        from kivy.uix.modalview import ModalView
        self.load =ModalView(background_color=[0,0,0,0])
        from kivy.factory import Factory
        self.load.add_widget(Factory.Card())
        self.load.open()     
        from threading import Thread 
        th =Thread(target=self.add_graph,args=(x,),name='ca')
        th.start()
            
        
    def add_graph(self,x):
        from kivymd.app import MDApp
        today=MDApp.get_running_app().today
        user = MDApp.get_running_app().mail
        week=MDApp.get_running_app().week
        try:
            from fire import db 
            doc=db.child(user).child(x).get()
            data=doc.val()
            print(data)
            days =['Mon','Tue','Wed','Thu','Fri','Sat','Sun']  
            for k in days:
                if k not in data:
                    data[k]={'l':[0,0,0,0],'s':[0,0,0,0]}
            for i in data:
                if len(data[i]) !=2:
                  if 's' in data[i]:
                    data[i]['l']=[0,0,0,0]
                  else:
                    data[i]['s']=[0,0,0,0]#for days not recorded into the db 
            #------------------------------#spliting into flexible,regulated,deliberate,attentive ____level 1,level 2 level 3,level 4
            self.flex=[];self.reg=[];self.delk=[];self.att=[];self.l1=[];self.l2=[];self.l3=[];self.l4=[]
            #print(data)
            for i in range(7):
                k=data[days[i]];x=0
                for l in k:
                    if l=='s':
                        self.flex.append(k[l][0])
                        self.reg.append(k[l][1])
                        self.delk.append(k[l][2])
                        self.att.append(k[l][3])
                    else:
                        self.l1.append(k[l][0])
                        self.l2.append(k[l][1])
                        self.l3.append(k[l][2])
                        self.l4.append(k[l][3])
            
            from kivy.metrics import dp 
            from kivymd.utils import asynckivy
            async def add():
                for i in range(len(self.ids.Week.children)):
                    await asynckivy.sleep(2)
                    self.ids.Week.remove_widget(self.ids.Week.children[0])

                days =['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
                y=[self.flex,self.reg,self.delk,self.att,self.l1,self.l2,self.l3,self.l4]
                title=['Flexible','Regulate','Attentive','Deliberate','Level 1','Level 2','Level 3','Level 4']
                for i in range(8):
                    
                    await asynckivy.sleep(1)
                    from backend_kivyagg import FigureCanvasKivyAgg
                    import matplotlib.pyplot as plt
                    #plt.figure(i)
                    plt.plot(days,y[i])
                    plt.xlabel('Days of the week')
                    plt.ylabel('Point each day')
                    plt.title(title[i])
                    await asynckivy.sleep(1)
                    from kivy.uix.boxlayout import BoxLayout
                    Box=BoxLayout(size_hint_y=None,height=dp(400))
                    Box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
                    self.ids.Week.add_widget(Box)
                    plt.close()
                self.load.dismiss()
            
            asynckivy.start(add())
        except Exception as e:
            print(e.args)
            from kivymd.toast import toast 
            toast('Couldn\'t fetch data')
            self.load.dismiss()
    def One(self,*args):
        from kivy.metrics import dp
        from kivymd.utils import asynckivy
        from kivymd.app import MDApp
        today=MDApp.get_running_app().today
        user = MDApp.get_running_app().mail
        week=MDApp.get_running_app().week
        from fire import db
        self.call=False
        days =['Mon','Tue','Wed','Thu','Fri','Sat','Sun','s','l']
        
        try:
            scores_s = db.child(user).child(f'Week {week}').child(today).get().val()['s']
            async def add():
                if scores_s:
                    
                    scores_s.insert(0,-0)
                    
                    scores_s.append(-0)
                    
                    score = []
                    
                    y_lab=[]
                    for i in range(6):
                        
                        if (i==0) or (i==5):
                            
                            score.append(scores_s[i])
                            
                            y_lab.append('    ')
                        
                        else:
                            
                            x=scores_s[i]
                            
                            score.append(x)
                            
                            y_lab.append(f'{x}')
                    
                    print(True)
                    if  scores_s==[0,0,0,0,0,0]:
                        self.call=True
                    else:
                        helpful_bar = Bar(line_width=dp(2),bars_spacing=dp(55),min_bar_width=dp(40),bg_color=[.0196,.4,.0313725,1],pos_hint={'center_x':.5},x_labels=['  ',f'Flexible', f'Attentive', f'Deliberate', f'Regulated','   '],x_values=[0,10,20,30,40,0],
                        y_values=score,labels=True,size_hint_y=None,height=dp(300),y_labels=y_lab)
                        self.ids.today.add_widget(helpful_bar)
                        self._One()
                            
                    self.modal.dismiss()
            asynckivy.start(add())

        except Exception as e:
            self.modal.dismiss()
            from kivymd.toast import toast
            if not len(self.ids.today.children):
                toast('You have no data connection')

            if 'NoneType' in e.args[0][:] or e.args[0] in days:
                toast('You haven\'t filled Todays helpful skill')
            
    def _One(self,*args):
        from kivy.metrics import dp
        from kivymd.utils import asynckivy
        from kivymd.app import MDApp
        today=MDApp.get_running_app().today
        user = MDApp.get_running_app().mail
        week=MDApp.get_running_app().week
        from fire import db
        self.call=False
        days =['Mon','Tue','Wed','Thu','Fri','Sat','Sun','s','l']
        self.call_2=False
        print(1)
        try:
            scores_l = db.child(user).child(f'Week {week}').child(today).get().val()['l']
            async def ad_d():
                
                
                if scores_l:
                    #scores_l=scores_l[::-1]#remove this
                    scores_l.insert(0,-0)
                    scores_l.append(-0)
                    score = []
                    y_lab=[]
                    
                    for i in range(6):
                        
                        if (i==0) or (i==5):
                            
                            score.append(scores_l[i])
                            
                            y_lab.append('    ')
                        
                        else:
                            
                            x=scores_l[i]
                            
                            score.append(x)
                            
                            y_lab.append(f'{x}')
                    if  scores_l==[0,0,0,0,0,0]:
                        self.call_2=True
                    else:
                        Unhelful_bar = Bar(line_width=dp(4),bars_spacing=dp(20),min_bar_width=dp(40),size_hint_y=None,height=dp(300),x_values=[0,10,20,30,400,0],pos_hint={'center_x':.5},y_values=score
                    ,x_labels=['  ','Level 1','Level 2','Level 3','Level 4','  '],anim=True,y_labels=y_lab)
                        self.ids.today.add_widget(Unhelful_bar)
                            
                    self.modal.dismiss()
                            
                    
            asynckivy.start(ad_d())
                
        except Exception as e:
            self.modal.dismiss()
            from kivymd.toast import toast
            if not len(self.ids.today.children):
                toast('You have no data connection')
            if 'NoneType' in e.args[0][:]:
                toast('You haven\'t filled Todays unhelpful behaviour')
            
        
        
        if self.call:
            from kivymd.toast import toast
            import time 
            toast('No Chart to display for Helpful skill')
            time.sleep(2)
        
        if self.call_2:
            from kivymd.toast import toast
            import time 
            toast('No Chart to display for UnHelpful Behaviour')
            time.sleep(2)
        
    @mainthread
    def add_graph_3(self):
        from kivymd.app import MDApp
        today=MDApp.get_running_app().today
        user = MDApp.get_running_app().mail
        
        self.ids.R.clear_widgets()
        
        try:
            from fire import db
            from kivymd.app import MDApp
            #dat=db.collection('Up').get()
            num =MDApp.get_running_app().week
            f=[];a=[];r=[];d=[];l1=[];l2=[];l3=[];l4=[]
            days =['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
            from backend_kivyagg import FigureCanvasKivyAgg
            import matplotlib.pyplot as plt
            if num<4:
                data=[]
                for ni in range(1,num):
                    pi=db.child(user).child(f"Week {ni}").get()
                    data.append(pi.val())
                for ki in range(len(data)):
                    for k in days:
                        if k not in data[ki]:
                            data[ki][f'{k}']={'l':[0,0,0,0],'s':[0,0,0,0]}
                for i in range(len(data)):
                    for m in data[i]:
                        if len(data[i][m]) !=2:
                            if 's' in data[i]:
                                data[i][m]['l']=[0,0,0,0]
                            else:
                                data[i][m]['s']=[0,0,0,0]
                for i in data:
                    for m in i:
                        p=i[m]
                        if type(p)!=int:
                            for mi in p:
                                v=p[mi]
                                if mi=='s':
                                    f.append(v[0])
                                    r.append(v[1])
                                    d.append(v[2])
                                    a.append(v[3])
                                else:
                                    l1.append(v[0])
                                    l2.append(v[1])
                                    l3.append(v[2])
                                    l4.append(v[3])
                y_axis=[f,r,d,a,l1,l2,l3,l4]
                
                if num==1:
                    x=[f'Week {num}']
                elif num==2:
                    x=[f'Week {num-1}',f'Week {num}']
                else:
                    x=[f'Week {num-2}',f'Week {num-1}',f'Week {num}']
                from kivymd.utils import asynckivy
                async def add():
                    title=['Flexible','Regulate','Attentive','Deliberate','Level 1','Level 2','Level 3','Level 4']
                    for i in range(len(y_axis)):
                        if num==1:
                            y=[sum(y_axis[i])]
                        elif num==2:
                            y=[sum(y_axis[i][:7]),sum(y_axis[i][7:])]
                        else:
                            y=[sum(y_axis[i][:7]),sum(y_axis[i][7:14]),sum(y_axis[i][14:])]
                        #plt.figure(i)
                        plt.plot(x,y)
                        plt.xlabel('Weeks')
                        plt.ylabel('Point')
                        plt.title(title[i])
                        await asynckivy.sleep(2)
                        from kivy.metrics import dp 
                        from kivy.uix.boxlayout import BoxLayout
                        Box=BoxLayout(size_hint_y=None,height=dp(400))
                        Box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
                        self.ids.R.add_widget(Box)
                        plt.close()
                    self.modal.dismiss()
                asynckivy.start(add())
            
            else:
                data=[]
                for ni in range(num-3,num+1):
                    kip=db.child(user).child(f"Week {ni}").get()
                    data.append(kip.val())
                for ki in range(len(data)):
                    for k in days:
                        if k not in data[ki]:
                            data[ki][f'{k}']={'l':[0,0,0,0],'s':[0,0,0,0]}
                for i in range(len(data)):
                    for m in data[i]:
                        if len(data[i][m]) !=2:
                            if 's' in data[i]:
                                data[i][m]['l']=[0,0,0,0]
                            else:
                                data[i][m]['s']=[0,0,0,0]
        
                for i in data:
                    for m in i:
                        p=i[m]
                        if type(p)!=int:
                            for mi in p:
                                v=p[mi]
                                if mi=='s':
                                    f.append(v[0])
                                    r.append(v[1])
                                    d.append(v[2])
                                    a.append(v[3])
                                else:
                                    l1.append(v[0])
                                    l2.append(v[1])
                                    l3.append(v[2])
                                    l4.append(v[3])
                y_axis=[f,r,d,a,l1,l2,l3,l4]
                
                x=[f'Week {num-3}',f'Week {num-2}',f'Week {num-1}',f'Week {num}']
                from kivymd.utils import asynckivy
                async def add():
                    title=['Flexible','Regulate','Attentive','Deliberate','Level 1','Level 2','Level 3','Level 4']
                    for i in range(len(y_axis)):
                        y=[sum(y_axis[i][:7]),sum(y_axis[i][7:14]),sum(y_axis[i][14:21]),sum(y_axis[i][21:])]
                        #plt.figure(i)
                        plt.plot(x,y)
                        plt.xlabel('Weeks')
                        plt.ylabel('Point')
                        plt.title(title[i])
                        await asynckivy.sleep(3)
                        from kivy.metrics import dp 
                        from kivy.uix.boxlayout import BoxLayout
                        Box=BoxLayout(size_hint_y=None,height=dp(400))
                        Box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
                        self.ids.R.add_widget(Box)
                        plt.close()
                    self.modal.dismiss()
                asynckivy.start(add())
                
        except Exception as e:
            print(e.args)
            self.modal.dismiss()
            from kivymd.toast import toast
            toast('You have no data connection.')
    @mainthread
    def All(self):
        try:
            from kivymd.app import MDApp 
            W=MDApp.get_running_app().week
            today=MDApp.get_running_app().today
            user = MDApp.get_running_app().mail
            n=0
            self.ids.Al.clear_widgets()
            import time
            time.sleep(2)
            if W>39:
                n=MDApp.get_running_app().week
                W-=(W//39)*39
                if W==0:
                    W=39
            if W >= 8:
                from fire import db
                f=[];a=[];r=[];d=[];l1=[];l2=[];l3=[];l4=[]
                days =['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
                from backend_kivyagg import FigureCanvasKivyAgg
                import matplotlib.pyplot as plt
                data=[]
                from kivymd.utils import asynckivy
                if n:
                    for ni in range(n-W+1,n+1):
                        lip=db.child(user).child(f"Week {ni}").get()
                        data.append(lip.val())
                else:
                    for ni in range(1,W+1):
                        lip=db.child(user).child(f"Week {ni}").get()
                        data.append(lip.val())
            
                
                for ki in range(len(data)):
                    for k in days:
                        if k not in data[ki]:
                            data[ki][f'{k}']={'l':[0,0,0,0],'s':[0,0,0,0]}
                        
                for i in range(len(data)):
                    for m in data[i]:
                        if len(data[i][m]) !=2:
                            if 's' in data[i]:
                                data[i][m]['l']=[0,0,0,0]
                            else:
                                data[i][m]['s']=[0,0,0,0]
                for i in data:
                    for m in i:
                        p=i[m]
                        if type(p)!=int:
                            for mi in p:
                                v=p[mi]
                                if mi=='s':
                                    f.append(v[0])
                                    r.append(v[1])
                                    d.append(v[2])
                                    a.append(v[3])
                                else:
                                    l1.append(v[0])
                                    l2.append(v[1])
                                    l3.append(v[2])
                                    l4.append(v[3])
                y_axis=[f,r,d,a,l1,l2,l3,l4]
                title=['Flexible','Regulate','Attentive','Deliberate','Level 1','Level 2','Level 3','Level 4']
                from kivymd.utils import asynckivy
                async def ad():
                    fi=0
                    for k in y_axis:
                        x=0
                        save=int(len(k)//4)
                        rem=len(k)%4
                        f=-3;t=0
                        y=[]
                        label=[]
                        if rem ==0:
                            while x!=save:
                                y.append(sum(k[:28]))
                                del k[:28]
                                x+=7
                                f+=4;t+=4
                                label.append(f'week{f}-{t}')
                        else:
                            while x<=save:
                                if x!=save:
                                    l=k[:28]
                                    y.append(sum(k[:28]))
                                    m=len(l)
                                    del k[:28]
                                    x+=7
                                    if m==28:
                                        f+=4;t+=4
                                        label.append(f'week{f}-{t}')
                                    else:
                                        get=int(m/7)
                                        f+=4;t+=get
                                        if f==t:
                                            label.append(f'week{f}')
                                        else:
                                            label.append(f'week{f}-{t}')
                        x=[i for i in range(len(label))]
                        plt.plot(x,y)
                        plt.xticks(x,label,rotation=25)
                        plt.xlabel('Weeks')
                        plt.ylabel('Point')
                        plt.title(title[fi])
                        await asynckivy.sleep(2)
                        from kivy.metrics import dp 
                        from kivy.uix.boxlayout import BoxLayout
                        Box=BoxLayout(size_hint_y=None,height=dp(720))
                        Box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
                        self.ids.Al.add_widget(Box)
                        plt.close()
                        fi+=1
                    self.modal.dismiss()
                            
                    asynckivy.start(ad())           
                    
                
            else:
                import time 
                time.sleep(2)
                self.modal.dismiss()
        except Exception as e:
            print(e.args)
            self.modal.dismiss()
            from kivymd.toast import toast 
            toast('You have no data connection')

                
    def switch(self,*args):
        from kivy.uix.modalview import ModalView
        from kivy.factory import Factory 
        self.modal =ModalView(background_color=[0,0,0,0])
        self.modal.add_widget(Factory.Card())
        self.modal.open()
        from threading import Thread
        if args[3]=='Week':
            self.ids.tool.right_action_items =[['dots-vertical',lambda x:self.back(x)]]
            from kivymd.utils import asynckivy
            self.modal.dismiss()
        
        elif args[3]=='Today':
            self.ids.tool.right_action_items =[]
            from kivymd.utils import asynckivy
            async def a_dd():
                await asynckivy.sleep(2)
                t=Thread(target=self.One)
                t.start()
                t.join()
                #k=Thread(target=self._One)
                #k.start()
                #k.join()
            asynckivy.start(a_dd())
        elif args[3]=='4 weeks':
            from kivymd.utils import asynckivy
            self.ids.tool.right_action_items =[]
            async def add_():
                await asynckivy.sleep(2)
                t=Thread(target=self.add_graph_3)
                t.start()
                t.join()
            asynckivy.start(add_())
        else:
            from kivymd.utils import asynckivy
            self.ids.tool.right_action_items =[]
            async def _add():
                await asynckivy.sleep(2)
                t=Thread(target=self.All)
                t.start()
                t.join()
            asynckivy.start(_add())

    
from kivymd_extensions.akivymd.uix.charts import AKBarChart
class Bar(AKBarChart):
    pass 
from kivymd.uix.tab import MDTabsBase
from kivy.uix.boxlayout import BoxLayout
class Tab(BoxLayout,MDTabsBase):
    pass'''
