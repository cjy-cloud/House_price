import wx
import os
import base64
from pic_jpg import img as pic  
import requests
from lxml import etree
import re
import ip
import pandas as pd
import get_all_url
import webbrowser
import pymysql
from matplotlib import pyplot as plt
nowpath = os.getcwd()  # 获取当前本文件所在路径
tmp = open('pic.jpg', 'wb')  
tmp.write(base64.b64decode(pic))
tmp.close()
class MyFrame7(wx.Frame):
    '''用于显示功能的界面'''
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '功能', size=(800, 450),pos=(600,300))
        panel = wx.Panel(self)       
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)
        self.xinfang = wx.Button(panel, label='新房')
        font = wx.Font(20,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.xinfang.SetFont(font)
        self.xinfang.Bind(wx.EVT_BUTTON,self.Xinfang)        
        self.ershoufang = wx.Button(panel, label='二手房')
        font = wx.Font(20,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.ershoufang.SetFont(font)
        self.ershoufang.Bind(wx.EVT_BUTTON,self.Ershoufang)
        self.chuzufang = wx.Button(panel, label='出租房')
        font = wx.Font(20,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.chuzufang.SetFont(font)
        self.chuzufang.Bind(wx.EVT_BUTTON,self.Chuzufang)        
        self.bt_good = wx.Button(panel,label='宜居城市报告')
        font = wx.Font(20,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.bt_good.SetFont(font)
        self.bt_good.Bind(wx.EVT_BUTTON,self.Oncity)        
        self.bt_allTop10 = wx.Button(panel,label='中国十佳宜居城市')
        font = wx.Font(20,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.bt_allTop10.SetFont(font)
        self.bt_allTop10.Bind(wx.EVT_BUTTON,self.OnclickallTop10)
        self.bt_logout = wx.Button(panel,label='退出登录')
        font = wx.Font(20,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.bt_logout.SetFont(font)
        self.bt_logout.Bind(wx.EVT_BUTTON,self.Logout)
        hsizer_button2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button2.Add(self.bt_allTop10, proportion=0, flag=wx.ALL, border=15)
        hsizer_button2.Add(self.bt_good, proportion=0, flag=wx.ALL, border=15)        
        hsizer_button7 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button7.Add(self.xinfang, proportion=0, flag=wx.ALL, border=15)
        hsizer_button7.Add(self.ershoufang, proportion=0, flag=wx.ALIGN_CENTER, border=15)
        hsizer_button7.Add(self.chuzufang, proportion=0, flag=wx.ALL, border=15)
        hsizer_button19 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button19.Add(self.bt_logout, proportion=0, flag=wx.ALL, border=15)
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(hsizer_button7, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=30)
        vsizer_all.Add(hsizer_button2, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=30)
        vsizer_all.Add(hsizer_button19, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=30)
        panel.SetSizer(vsizer_all)
        menuBar = wx.MenuBar()  # 菜单栏
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW,"&使用说明")
        fileMenu.AppendSeparator()         
        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        fileMenu.AppendItem(qmi)
        menuBar.Append(fileMenu, '&帮助')
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU,self.Instructions)
        self.Bind(wx.EVT_MENU, self.Quit, qmi)    
    def Logout(self,event):
        '''退出登录'''
        frame = MyFrame5(parent=None,id=-1)
        frame.Show()   
        self.Destroy()
    def Xinfang(self,event):
        '''点击新房跳转至MyFrame8'''
        frame = MyFrame8(parent=None,id=-1)
        frame.Show()
    def Ershoufang(self,event):
        '''点击二手房跳转至MyFrame'''
        frame = MyFrame(parent=None,id=-1)
        frame.Show()        
    def Chuzufang(self,event):
        '''点击出租房跳转至MyFrame10'''
        frame = MyFrame10(parent=None,id=-1)
        frame.Show()
    def Oncity(self,event):
        '''显示宜居城市报告'''
        frame = MyFrame2(parent=None,id=-1)
        frame.Show()
    def OnclickallTop10(self,event):
        '''打开网页'''
        webbrowser.open('https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%8D%81%E4%BD%B3%E5%AE%9C%E5%B1%85%E5%9F%8E%E5%B8%82/6981907?fr=aladdin')
    def Instructions(self,event):
        '''使用说明'''
        N = event.GetId()
        message = ''
        if N ==wx.ID_NEW:
            message7= '''
            【本软件用于查询各地房价】
            请选择您所需的功能,点击确定按钮完成选择。
            感谢您对本产品的支持及使用！！！
            '''
        message8= '使用说明'
        wx.MessageBox(message7,message8)
    def Quit(self,event):
        '''退出此界面'''
        self.Close()    
    def OnEraseBack(self, event):
        '''加入图片背景'''
        try:
            dc = event.GetDC()
            if not dc:
                dc = wx.ClientDC(self)
                dc.SetClippingRect(self.GetUpdateRegion().GetBox())
            dc.Clear()
            dc.DrawBitmap(wx.Bitmap(nowpath + r'\pic.jpg'), 0, 0)
        except:
            pass
class MyFrame5(wx.Frame):
    '''用于用户登录的界面'''
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '用户登录', size=(600, 400),pos=(700,300))
        panel = wx.Panel(self)
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)
        self.bt_yes = wx.Button(panel, label='确定')
        font = wx.Font(10,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.bt_yes.SetFont(font)
        self.bt_yes.Bind(wx.EVT_BUTTON,self.Yes)        
        self.bt_register = wx.Button(panel, label='注册')
        font = wx.Font(10,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.bt_register.SetFont(font)
        self.bt_register.Bind(wx.EVT_BUTTON,self.Register)        
        self.title = TransparentStaticText(panel, label="请输入用户名和密码")
        font = wx.Font(20,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.title.SetFont(font)        
        self.label_user = TransparentStaticText(panel, label="用户名:")
        font = wx.Font(10,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.label_user.SetFont(font)        
        self.text_user = wx.TextCtrl(panel, style=wx.TE_LEFT)
        font = wx.Font(10,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.text_user.SetFont(font)       
        self.label_pwd = TransparentStaticText(panel, label="密  码:")
        font = wx.Font(10,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.label_pwd.SetFont(font)        
        self.text_password = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        font = wx.Font(10,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.text_password.SetFont(font)
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user, proportion=0, flag=wx.ALL, border=10)
        hsizer_user.Add(self.text_user, proportion=1, flag=wx.ALL, border=10)
        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.label_pwd, proportion=0, flag=wx.ALL, border=10)
        hsizer_pwd.Add(self.text_password, proportion=1, flag=wx.ALL, border=10)
        hsizer_button5 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button5.Add(self.bt_register, proportion=0, flag=wx.ALL, border=15)
        hsizer_button5.Add(self.bt_yes, proportion=0, flag=wx.ALIGN_CENTER, border=10)
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER,
                        border=30)
        vsizer_all.Add(hsizer_user, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_pwd, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_button5, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=15)
        panel.SetSizer(vsizer_all)
        menuBar = wx.MenuBar()  # 菜单栏    
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW,"&使用说明")
        fileMenu.AppendSeparator()        
        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        fileMenu.AppendItem(qmi)
        menuBar.Append(fileMenu, '&帮助')
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU,self.Instructions)
        self.Bind(wx.EVT_MENU, self.Quit, qmi)         
    def Yes(self,event):
        '''判断用户名和密码是否给予登录'''
        message = ''
        username = self.text_user.GetValue()
        password = self.text_password.GetValue()
        conn = pymysql.connect(host="localhost", user="root",password= "root", database='student',charset='utf8')
        cs = conn.cursor()
        sql = "SELECT 密码 FROM book WHERE 用户名 = '%s' AND 密码 = '%s'" % (username,password)
        cs.execute(sql)
        result = cs.fetchone()
        if result:
            if password == result[0]:
                frame = MyFrame7(parent=None,id=-1)
                frame.Show()
                self.Destroy()
        elif username == '' or password == '':
                message = '用户名或密码不能为空'
                wx.MessageBox(message)
        else:
            message = '用户名或密码输入错误'
            wx.MessageBox(message)            
    def Register(self,event):
        '''点击注册按钮跳转至MyFrame6'''
        frame = MyFrame6(parent=None,id=-1)
        frame.Show()        
    def Instructions(self,event):
        '''使用说明'''
        N = event.GetId()
        message = ''
        if N ==wx.ID_NEW:
            message3= '''
            【本软件用于查询各地房价】
            请输入用户名和密码,点击确定按钮完成登录。
            若是新用户,请先点击注册按钮进行注册！
            感谢您对本产品的支持及使用！！！
            '''
        message4= '使用说明'
        wx.MessageBox(message3,message4)
    def Quit(self,event):
        '''退出此界面'''
        self.Close()
    def OnEraseBack(self, event):
        '''加入图片背景'''
        try:
            dc = event.GetDC()
            if not dc:
                dc = wx.ClientDC(self)
                dc.SetClippingRect(self.GetUpdateRegion().GetBox())
            dc.Clear()
            dc.DrawBitmap(wx.Bitmap(nowpath + r'\pic.jpg'), 0, 0)
        except:
            pass
class MyFrame6(wx.Frame):
    '''用于用户注册的界面'''
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '注册', size=(600, 400),pos=(700,300))
        panel = wx.Panel(self)
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)
        self.bt_do = wx.Button(panel, label='注册')
        font = wx.Font(10,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.bt_do.SetFont(font)
        self.bt_do.Bind(wx.EVT_BUTTON,self.Do)       
        self.bt_return = wx.Button(panel, label='返回')
        font = wx.Font(10,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.bt_return.SetFont(font)
        self.bt_return.Bind(wx.EVT_BUTTON,self.Return)        
        self.title = TransparentStaticText(panel, label="注册")
        font = wx.Font(20,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.title.SetFont(font)        
        self.label_user = TransparentStaticText(panel, label="  用户名:")
        font = wx.Font(10,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.label_user.SetFont(font)        
        self.text_user = wx.TextCtrl(panel, style=wx.TE_LEFT)
        font = wx.Font(10,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.text_user.SetFont(font)        
        self.label_pwd = TransparentStaticText(panel, label="  密  码:")
        font = wx.Font(10,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.label_pwd.SetFont(font)        
        self.text_password = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        font = wx.Font(10,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.text_password.SetFont(font)        
        self.alabel_pwd = TransparentStaticText(panel, label="确认密码:")
        font = wx.Font(10,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.alabel_pwd.SetFont(font)        
        self.text_apassword = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        font = wx.Font(10,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.text_apassword.SetFont(font)        
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user, proportion=0, flag=wx.ALL, border=10)
        hsizer_user.Add(self.text_user, proportion=1, flag=wx.ALL, border=10)        
        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)        
        hsizer_pwd.Add(self.label_pwd, proportion=0, flag=wx.ALL, border=10)
        hsizer_pwd.Add(self.text_password, proportion=1, flag=wx.ALL, border=10)        
        hsizer_apwd = wx.BoxSizer(wx.HORIZONTAL)        
        hsizer_apwd.Add(self.alabel_pwd, proportion=0, flag=wx.ALL, border=10)
        hsizer_apwd.Add(self.text_apassword, proportion=1, flag=wx.ALL, border=10)
        hsizer_button6 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button6.Add(self.bt_return, proportion=0, flag=wx.ALIGN_CENTER, border=15)
        hsizer_button6.Add(self.bt_do, proportion=0, flag=wx.ALIGN_CENTER, border=15)      
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER,
                        border=15)
        vsizer_all.Add(hsizer_user, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_pwd, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_apwd, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_button6, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=15)
        panel.SetSizer(vsizer_all)
        menuBar = wx.MenuBar()  # 菜单栏
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW,"&使用说明")
        fileMenu.AppendSeparator()   
        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        fileMenu.AppendItem(qmi)
        menuBar.Append(fileMenu, '&帮助')
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU,self.Instructions)
        self.Bind(wx.EVT_MENU, self.Quit, qmi)      
    def Do(self,event):
        '''判断是否注册成功'''
        message=''
        username = self.text_user.GetValue()
        password = self.text_password.GetValue()      
        apassword = self.text_apassword.GetValue()
        if username == '':
            message = '用户名不能为空！'
            wx.MessageBox(message)
        elif password == '':
            message = '新密码不能为空！'
            wx.MessageBox(message)
        elif apassword == '':
            message = '新密码不能为空！'
            wx.MessageBox(message)
        elif password == apassword:
            db = pymysql.connect(host="localhost", user="root",password= "root", database='student',charset='utf8')
            cursor = db.cursor()
            name=[]
            word=[]
            name = [int(i) for i in username.split()]
            word = [int(i) for i in password.split()]
            sql='''select * from book where 用户名=%s '''
            if not cursor.execute(sql,name):
                array=list(zip(name,word))
                cursor.executemany("insert into book(用户名,密码) VALUES (%s,%s)",array)
                db.commit()
                db.close()
                message = '注册成功！'
                wx.MessageBox(message)
                self.Destroy()
            else:
                message = '用户名已存在！'
                wx.MessageBox(message)                
    def Return(self,event):
        '''返回上一界面'''
        frame = MyFrame5(parent=None,id=-1)
        frame.Show()
        self.Destroy()       
    def Instructions(self,event):
        '''使用说明'''
        N = event.GetId()
        message = ''
        if N ==wx.ID_NEW:
            message5= '''
            输入任意数字或文字作为用户名和密码，点击注册按钮完成注册。
            注：
            请选择较独特的文字或数字作为用户名，以防与其他人撞名导致注册不成功！
            感谢您对本产品的支持及使用！！！
            '''
        message6= '使用说明'
        wx.MessageBox(message5,message6) 
    def Quit(self,event):
        '''退出此界面'''
        self.Close()
    def OnEraseBack(self, event):
        '''加入图片背景'''
        try:
            dc = event.GetDC()
            if not dc:
                dc = wx.ClientDC(self)
                dc.SetClippingRect(self.GetUpdateRegion().GetBox())
            dc.Clear()
            dc.DrawBitmap(wx.Bitmap(nowpath + r'\pic.jpg'), 0, 0)
        except:
            pass
class MyFrame(wx.Frame):
    '''用于查询某城市二手房的界面'''
    def __init__(self,parent,id):       
        wx.Frame.__init__(self, parent,id, title="一种房价智能查询软件V1.0",pos=(200,80),size=(1500, 900))
        panel = wx.Panel(self)
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)
        self.title = TransparentStaticText(panel,label = '二手房信息查询系统')   
        font = wx.Font(50,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.title.SetFont(font)
        self.clabel_user = TransparentStaticText(panel,label = '城市')
        self.ctext_user = wx.TextCtrl(panel,-1,style=wx.TE_LEFT)
        font = wx.Font(30,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.clabel_user.SetFont(font)
        font = wx.Font(17,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.ctext_user.SetFont(font)
        self.bt_comfirm = wx.Button(panel,label='查询')
        font = wx.Font(30,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.bt_comfirm.SetFont(font)
        self.bt_comfirm.Bind(wx.EVT_BUTTON,self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel,label='清空')
        font = wx.Font(30,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.bt_cancel.SetFont(font)
        self.bt_cancel.Bind(wx.EVT_BUTTON,self.OnclickCancel)
        self.bt_return_1 = wx.Button(panel,label='   返回   ')
        font = wx.Font(30,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.bt_return_1.SetFont(font)
        self.bt_return_1.Bind(wx.EVT_BUTTON,self.Return)
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.clabel_user, proportion=0, flag=wx.ALL, border=25)
        hsizer_user.Add(self.ctext_user, proportion=1, flag=wx.ALL, border=28)        
        hsizer_button1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button1.Add(self.bt_comfirm, proportion=0, flag=wx.ALL, border=10)
        hsizer_button1.Add(self.bt_cancel, proportion=1, flag=wx.ALL, border=10)       
        hsizer_button8 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button8.Add(self.bt_return_1, proportion=1, flag=wx.ALL, border=10)
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER,
                        border=65)
        vsizer_all.Add(hsizer_user, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=350)     
        vsizer_all.Add(hsizer_button1, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=60)
        vsizer_all.Add(hsizer_button8, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=60)
        panel.SetSizer(vsizer_all)
        menuBar = wx.MenuBar()  # 菜单栏      
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW,"&使用说明")
        fileMenu.AppendSeparator()         
        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        fileMenu.AppendItem(qmi)
        menuBar.Append(fileMenu, '&帮助(H)')
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU,self.OnclickInstructions)
        self.Bind(wx.EVT_MENU, self.Quit, qmi)  
    def Quit(self,event):
        '''退出此界面'''
        self.Close() 
    def OnclickInstructions(self,event):  
        '''使用说明'''
        N = event.GetId()
        message = ''
        if N ==wx.ID_NEW:
            message1= '''
            【本软件用于查询各地房价】
            (1)正确输入城市,点击查询便可查询到所需要内容
            (2)正确输入城市点击查询便可查询到所需要内容,此法可更精确的定位到您所需的房源
            (3)若输入错误,可按清空键清空
            ！！！在运行时会出现弹窗窗口请留意弹窗信息。
            '''
        message2= '使用说明'
        wx.MessageBox(message1,message2)
    def Return(self,event): 
        '''返回上一界面'''
        self.Destroy()          
    def OnclickSubmit(self,event): 
        '''单击"查询"按钮，执行方法'''
        self.city_input=self.ctext_user.GetValue()
        message=''
        if self.city_input == '':
            message='请输入查询城市！'
            wx.MessageBox(message)
        else:
            db = pymysql.connect(host="localhost", user="root",password= "root", database='ershoufang',charset="utf8",autocommit=True)
            cursor = db.cursor()
            sql = "show tables;"
            cursor.execute(sql)
            tables = [cursor.fetchall()]
            table_list = re.findall('(\'.*?\')',str(tables))
            table_list = [re.sub("'",'',each) for each in table_list]
            if self.city_input not in table_list:
                message = '请输入正确城市名称！'
                wx.MessageBox(message)
            else:
                sql = "select * from %s " %self.city_input
                cursor.execute(sql)
                
                self.new_name=[]
                for name in cursor.fetchall():
                    name_1 = name[0]
                    self.new_name.append(name_1)
                db.close()
                
                if len(self.new_name) > 0:
                    frame = MyFrame3(parent=None,id=-1,chengshi=self.city_input)
                    frame.Show()
                else:
                    d='''
                        很抱歉给您带来的困扰,暂无此城市数据！！！
                        请查询其他城市！！！
                    '''
                    dial = wx.MessageDialog(None,d,'说明',wx.OK)
                    dial.ShowModal()
                return self.city_input
    def OnclickCancel(self,event):
        '''单击"清空"按钮，执行方法'''
        self.ctext_user.SetValue('')
    def OnEraseBack(self, event):
        '''加入图片背景'''
        try:
            dc = event.GetDC()
            if not dc:
                dc = wx.ClientDC(self)
                dc.SetClippingRect(self.GetUpdateRegion().GetBox())
            dc.Clear()
            dc.DrawBitmap(wx.Bitmap(nowpath + r'\pic.jpg'), 0, 0)
        except:
            pass
class MyFrame8(wx.Frame):
    '''用于查询某城市新房的界面'''
    def __init__(self,parent,id):        
        wx.Frame.__init__(self, parent,id, title="一种房价智能查询软件V1.0",pos=(200,80),size=(1500, 900))
        panel = wx.Panel(self)
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)        
        self.title = TransparentStaticText(panel,label = '新房信息查询系统')   
        font = wx.Font(50,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.title.SetFont(font)
        self.clabel_user = TransparentStaticText(panel,label = '城市')
        self.ctext_user = wx.TextCtrl(panel,-1,style=wx.TE_LEFT)
        font = wx.Font(30,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.clabel_user.SetFont(font)
        font = wx.Font(17,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.ctext_user.SetFont(font)       
        self.bt_comfirm = wx.Button(panel,label='查询')
        font = wx.Font(30,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.bt_comfirm.SetFont(font)
        self.bt_comfirm.Bind(wx.EVT_BUTTON,self.OnclickSubmit)        
        self.bt_cancel = wx.Button(panel,label='清空')
        font = wx.Font(30,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.bt_cancel.SetFont(font)
        self.bt_cancel.Bind(wx.EVT_BUTTON,self.OnclickCancel)        
        self.bt_return_1 = wx.Button(panel,label='   返回   ')
        font = wx.Font(30,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.bt_return_1.SetFont(font)
        self.bt_return_1.Bind(wx.EVT_BUTTON,self.Return)
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.clabel_user, proportion=0, flag=wx.ALL, border=25)
        hsizer_user.Add(self.ctext_user, proportion=1, flag=wx.ALL, border=28)        
        hsizer_button3 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button3.Add(self.bt_comfirm, proportion=0, flag=wx.ALL, border=10)
        hsizer_button3.Add(self.bt_cancel, proportion=1, flag=wx.ALL, border=10)        
        hsizer_button4 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button4.Add(self.bt_return_1, proportion=1, flag=wx.ALL, border=10)
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER,
                        border=65)
        vsizer_all.Add(hsizer_user, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=350)     
        vsizer_all.Add(hsizer_button3, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=60)
        vsizer_all.Add(hsizer_button4, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=60)
        panel.SetSizer(vsizer_all)
        menuBar = wx.MenuBar()  # 菜单栏
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW,"&使用说明")
        fileMenu.AppendSeparator()
        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        fileMenu.AppendItem(qmi)
        menuBar.Append(fileMenu, '&帮助(H)')
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU,self.OnclickInstructions)
        self.Bind(wx.EVT_MENU, self.Quit, qmi)  
    def Quit(self,event):
        '''退出此界面'''
        self.Close() 
    def OnclickInstructions(self,event):  
        '''使用说明'''
        N = event.GetId()
        message = ''
        if N ==wx.ID_NEW:
            message1= '''
            【本软件用于查询各地房价】
            (1)正确输入城市,点击查询便可查询到所需要内容
            (2)正确输入城市,点击查询便可查询到所需要内容,此法可更精确的定位到您所需的房源
            (3)若输入错误,可按清空键清空
            ！！！在运行时会出现弹窗窗口请留意弹窗信息。
            '''
        message2= '使用说明'
        wx.MessageBox(message1,message2)
    def Return(self,event): 
        '''返回上一界面'''
        self.Destroy()          
    def OnclickSubmit(self,event): 
        '''单击"查询"按钮，执行方法'''
        self.city_input=self.ctext_user.GetValue()
        message=''
        if self.city_input == '':
            message='请输入查询城市！'
            wx.MessageBox(message)
        else:
            db = pymysql.connect(host="localhost", user="root",password= "root", database='xinfang',charset="utf8",autocommit=True)
            cursor = db.cursor()
            sql = "show tables;"
            cursor.execute(sql)
            tables = [cursor.fetchall()]
            table_list = re.findall('(\'.*?\')',str(tables))
            table_list = [re.sub("'",'',each) for each in table_list]
            if self.city_input not in table_list:
                message = '请输入正确城市名称！'
                wx.MessageBox(message)
            else:
                sql = "select * from %s " %self.city_input
                cursor.execute(sql)
                
                self.new_name=[]
                for name in cursor.fetchall():
                    name_1 = name[0]
                    self.new_name.append(name_1)
                db.close()
                
                if len(self.new_name) > 0:
                    frame = MyFrame9(parent=None,id=-1,chengshi=self.city_input)
                    frame.Show()
                else:
                    d='''
                        很抱歉给您带来的困扰,暂无此城市数据！！！
                        请查询其他城市！！！
                    '''
                    dial = wx.MessageDialog(None,d,'说明',wx.OK)
                    dial.ShowModal()
                return self.city_input
    def OnclickCancel(self,event):
        '''单击"清空"按钮，执行方法'''
        self.ctext_user.SetValue('')
    def OnEraseBack(self, event):
        '''加入图片背景'''
        try:
            dc = event.GetDC()
            if not dc:
                dc = wx.ClientDC(self)
                dc.SetClippingRect(self.GetUpdateRegion().GetBox())
            dc.Clear()
            dc.DrawBitmap(wx.Bitmap(nowpath + r'\pic.jpg'), 0, 0)
        except:
            pass       
class MyFrame10(wx.Frame):
    '''用于查询某城市出租房的界面'''
    def __init__(self,parent,id):  
        wx.Frame.__init__(self, parent,id, title="一种房价智能查询软件V1.0",pos=(200,80),size=(1500, 900))
        panel = wx.Panel(self)
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)
        self.title = TransparentStaticText(panel,label = '出租房信息查询系统')   
        font = wx.Font(50,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.title.SetFont(font)
        self.clabel_user = TransparentStaticText(panel,label = '城市')
        self.ctext_user = wx.TextCtrl(panel,-1,style=wx.TE_LEFT)
        font = wx.Font(30,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.clabel_user.SetFont(font)
        font = wx.Font(17,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.ctext_user.SetFont(font)
        self.bt_comfirm = wx.Button(panel,label='查询')
        font = wx.Font(30,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.bt_comfirm.SetFont(font)
        self.bt_comfirm.Bind(wx.EVT_BUTTON,self.OnclickSubmit)        
        self.bt_cancel = wx.Button(panel,label='清空')
        font = wx.Font(30,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL) 
        self.bt_cancel.SetFont(font)
        self.bt_cancel.Bind(wx.EVT_BUTTON,self.OnclickCancel)        
        self.bt_return_1 = wx.Button(panel,label='   返回   ')
        font = wx.Font(30,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.bt_return_1.SetFont(font)
        self.bt_return_1.Bind(wx.EVT_BUTTON,self.Return)
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.clabel_user, proportion=0, flag=wx.ALL, border=25)
        hsizer_user.Add(self.ctext_user, proportion=1, flag=wx.ALL, border=28)      
        hsizer_button9 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button9.Add(self.bt_comfirm, proportion=0, flag=wx.ALL, border=10)
        hsizer_button9.Add(self.bt_cancel, proportion=1, flag=wx.ALL, border=10)
        hsizer_button10 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button10.Add(self.bt_return_1, proportion=1, flag=wx.ALL, border=10)
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER,
                        border=65)
        vsizer_all.Add(hsizer_user, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=350)     
        vsizer_all.Add(hsizer_button9, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=60)
        vsizer_all.Add(hsizer_button10, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=60)
        panel.SetSizer(vsizer_all)
        menuBar = wx.MenuBar()  # 菜单栏
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW,"&使用说明")
        fileMenu.AppendSeparator() 
        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        fileMenu.AppendItem(qmi)
        menuBar.Append(fileMenu, '&帮助(H)')
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU,self.OnclickInstructions)
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)  
    def OnQuit(self,event):
        '''退出此界面'''
        self.Close()
    def OnclickInstructions(self,event):
        '''使用说明'''
        N = event.GetId()
        message = ''
        if N ==wx.ID_NEW:
            message1= '''
            【本软件用于查询各地房价】
            (1)正确输入城市,点击查询便可查询到所需要内容
            (2)正确输入城市,点击查询便可查询到所需要内容,此法可更精确的定位到您所需的房源
            (3)若输入错误,可按清空键清空
            ！！！在运行时会出现弹窗窗口请留意弹窗信息。
            '''
        message2= '使用说明'
        wx.MessageBox(message1,message2)
    def Return(self,event): 
        '''返回上一界面'''
        self.Destroy() 
    def OnclickSubmit(self,event): 
        '''单击"查询"按钮，执行方法'''
        self.city_input=self.ctext_user.GetValue()
        message=''
        if self.city_input == '':
            message='请输入查询城市！'
            wx.MessageBox(message)
        else:
            db = pymysql.connect(host="localhost", user="root",password= "root", database='chuzu',charset="utf8",autocommit=True)
            cursor = db.cursor()
            sql = "show tables;"
            cursor.execute(sql)
            tables = [cursor.fetchall()]
            table_list = re.findall('(\'.*?\')',str(tables))
            table_list = [re.sub("'",'',each) for each in table_list]
            if self.city_input not in table_list:
                message = '请输入正确城市名称！'
                wx.MessageBox(message)
            else:
                sql = "select * from %s " %self.city_input
                cursor.execute(sql)                
                self.new_name=[]
                for name in cursor.fetchall():
                    name_1 = name[0]
                    self.new_name.append(name_1)
                db.close()               
                if len(self.new_name) > 0:
                    frame = MyFrame11(parent=None,id=-1,chengshi=self.city_input)
                    frame.Show()
                else:
                    d='''
                        很抱歉给您带来的困扰,暂无此城市数据！！！
                        请查询其他城市！！！
                    '''
                    dial = wx.MessageDialog(None,d,'说明',wx.OK)
                    dial.ShowModal()
                return self.city_input
    def OnclickCancel(self,event):
        '''单击"清空"按钮，执行方法'''
        self.ctext_user.SetValue('')
    def OnEraseBack(self, event):
        '''加入图片背景'''
        try:
            dc = event.GetDC()
            if not dc:
                dc = wx.ClientDC(self)
                dc.SetClippingRect(self.GetUpdateRegion().GetBox())
            dc.Clear()
            dc.DrawBitmap(wx.Bitmap(nowpath + r'\pic.jpg'), 0, 0)
        except:
            pass
class MyFrame2(wx.Frame):
    '''用于显示城市宜居报告内容的界面'''
    def __init__(self,parent,id):
        wx.Frame.__init__(self, parent,id, title="宜居城市报告",pos=(200,80),size=(1500, 900))
        panel = wx.Panel(self)        
        self.title = TransparentStaticText(panel,label = '宜居城市报告')   
        font = wx.Font(25,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.title.SetFont(font)       
        self.text = wx.TextCtrl(panel,style=wx.TE_MULTILINE,size=(1200,800)) 
        font = wx.Font(17,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.text.SetFont(font)       
        self.ninteen = wx.Button(panel,label='2019年')
        font = wx.Font(20,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.ninteen.SetFont(font)
        self.ninteen.Bind(wx.EVT_BUTTON,self.Ninteen)        
        self.twenty = wx.Button(panel,label='2020年')
        font = wx.Font(20,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.twenty.SetFont(font)
        self.twenty.Bind(wx.EVT_BUTTON,self.Twenty)     
        self.twentyone = wx.Button(panel,label='2021年')
        font = wx.Font(20,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.twentyone.SetFont(font)
        self.twentyone.Bind(wx.EVT_BUTTON,self.Twentyone)        
        hsizer_button11 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button11.Add(self.ninteen, proportion=0, flag=wx.ALL, border=5)
        hsizer_button11.Add(self.twenty, proportion=0, flag=wx.ALL, border=5)
        hsizer_button11.Add(self.twentyone, proportion=0, flag=wx.ALL, border=5)
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)
        vsizer_all = wx.BoxSizer(wx.VERTICAL)      
        vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER,
                        border=10)
        vsizer_all.Add(hsizer_button11, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=20)
        vsizer_all.Add(self.text, proportion = 0,flag=wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER, border=15)
        panel.SetSizer(vsizer_all)
    def Ninteen(self,event):
        '''显示2019年的宜居城市报告'''
        with open('comfortable city2019.txt','r+') as f:
            data = f.readlines()
            for line in data:
                self.text.AppendText(line)
            f.close()
    def Twenty(self,event):
        '''显示2020年的宜居城市报告'''
        with open('comfortable city2020.txt','r+') as f:
            data = f.readlines()
            for line in data:
                self.text.AppendText(line)
            f.close()
    def Twentyone(self,event):
        '''显示2021年的宜居城市报告'''
        with open('comfortable city2021.txt','r+') as f:
            data = f.readlines()
            for line in data:
                self.text.AppendText(line)
            f.close()
    def OnEraseBack(self, event):
        '''加入图片背景'''
        try:
            dc = event.GetDC()
            if not dc:
                dc = wx.ClientDC(self)
                dc.SetClippingRect(self.GetUpdateRegion().GetBox())
            dc.Clear()
            dc.DrawBitmap(wx.Bitmap(nowpath + r'\pic.jpg'), 0, 0)
        except:
            pass 
class MyFrame3(wx.Frame):
    '''用于显示某城市二手房信息的界面'''
    def __init__(self,parent,id,chengshi):
        self.chengshi =  chengshi       
        wx.Frame.__init__(self, parent,id, title="一种房价智能查询软件V1.0",pos=(200,80),size=(1500, 900))
        panel = wx.Panel(self) 
        self.text = wx.TextCtrl(panel,style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_CENTRE,size=(1400,800)) 
        font = wx.Font(13,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.text.SetFont(font)
        self.city_input1=self.chengshi      
        self.new_name=[]
        self.new_local=[]
        self.new_area=[]
        self.new_money=[]
        self.new_floor=[]
        self.new_year=[]        
        db = pymysql.connect(host="localhost", user="root",password= "root", database='ershoufang',charset="utf8",autocommit=True)
        cursor = db.cursor()
        sql = "select * from %s " %self.city_input1
        cursor.execute(sql)
        for name in cursor.fetchall():
            name_1 = name[1]
            self.new_name.append(name_1)
        db.close()
        db = pymysql.connect(host="localhost", user="root",password= "root", database='ershoufang',charset="utf8",autocommit=True)
        cursor = db.cursor()
        sql = "select * from %s " %self.city_input1
        cursor.execute(sql)
        for local in cursor.fetchall():
            local_1 = local[2]
            self.new_local.append(local_1)
        db.close()
        db = pymysql.connect(host="localhost", user="root",password= "root", database='ershoufang',charset="utf8",autocommit=True)
        cursor = db.cursor()
        sql = "select * from %s " %self.city_input1
        cursor.execute(sql)
        for area in cursor.fetchall():
            area_1 = area[3]
            self.new_area.append(area_1)
        db.close()
        db = pymysql.connect(host="localhost", user="root",password= "root", database='ershoufang',charset="utf8",autocommit=True)
        cursor = db.cursor()
        sql = "select * from %s " %self.city_input1
        cursor.execute(sql)
        for floor in cursor.fetchall():
            floor_1 = floor[4]
            self.new_floor.append(floor_1)
        db.close() 
        db = pymysql.connect(host="localhost", user="root",password= "root", database='ershoufang',charset="utf8",autocommit=True)
        cursor = db.cursor()
        sql = "select * from %s " %self.city_input1
        cursor.execute(sql)
        for year in cursor.fetchall():
            year_1 = year[5]
            self.new_year.append(year_1)
        db.close()
        db = pymysql.connect(host="localhost", user="root",password= "root", database='ershoufang',charset="utf8",autocommit=True)
        cursor = db.cursor()
        sql = "select * from %s " %self.city_input1
        cursor.execute(sql)
        for money in cursor.fetchall():
            money_1 = money[6]
            self.new_money.append(money_1)
        db.close()
        self.text.AppendText("小区         "+"      地址      "+"     面积    "+"   楼层  "+"    建造年代   "+"   价格      "+"\n")
        for i in range(len(self.new_name)):
            self.text.AppendText(self.new_name[i])
            self.text.AppendText('        '+ self.new_local[i])
            self.text.AppendText('        ' + self.new_area[i])
            self.text.AppendText('       ' + self.new_floor[i])
            self.text.AppendText('       ' + self.new_year[i])
            self.text.AppendText('      ' + self.new_money[i]+'\n')
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)
        self.bt_return = wx.Button(panel,label='返回')
        font = wx.Font(14,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.bt_return.SetFont(font)
        self.bt_return.Bind(wx.EVT_BUTTON,self.OnclickReturn)       
        self.bt_average = wx.Button(panel,label='平均房价')
        font = wx.Font(14,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.bt_average.SetFont(font)
        self.bt_average.Bind(wx.EVT_BUTTON,self.OnclickAverage)
        self.bt_photo = wx.Button(panel,label='房价排名前十')
        font = wx.Font(14,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.bt_photo.SetFont(font)
        self.bt_photo.Bind(wx.EVT_BUTTON,self.OnclickPhoto)
        hsizer_button12 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button12.Add(self.bt_return, proportion=0, flag=wx.ALL, border=1)
        hsizer_button13 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button13.Add(self.bt_average, proportion=0, flag=wx.ALL, border=1) 
        hsizer_button13.Add(self.bt_photo, proportion=0, flag=wx.ALL, border=1) 
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(hsizer_button13, proportion=0, flag= wx.LEFT|wx.BOTTOM , border=1)
        vsizer_all.Add(hsizer_button12, proportion=0, flag= wx.LEFT|wx.BOTTOM , border=1)
        vsizer_all.Add(self.text, proportion = 0,flag=wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER, border=15)
        panel.SetSizer(vsizer_all)
    def OnclickReturn(self,event):
        '''返回上级界面'''
        self.Destroy()
    def OnclickAverage(self,event):
        '''跳转至MyFrame4'''
        frame = MyFrame4(parent=None,id=-1,city_input=self.city_input1)
        frame.Show()
    def OnclickPhoto(self,event):   
        '''显示柱状图'''
        new_money=','.join(self.new_money)
        money=re.findall('\d+', new_money)
        o=[]
        for i in range(len(money)):
            mon=int(money[i])
            o.append(mon)
        m=dict(zip(self.new_name,o))
        m_dict=sorted(m.items(),key=lambda x:x[1],reverse=True)        
        no = []
        mo = []
        for i in m_dict:
            money1=i[1]
            mo.append(money1)
            name1=i[0]
            no.append(name1)
        m=[]
        n=[]
        for a in range(11):
            m.append(mo[a])
            n.append(no[a])
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        plt.figure(figsize=(15,8),dpi=80)
        plt.bar(range(len(n)),m,width=0.5)        
        plt.xticks(range(len(n)),n,rotation=35)        
        plt.xlabel("小区")
        plt.ylabel("单价（/万）")
        plt.title("二手房价前十名")
        plt.grid(alpha=0.3)
        plt.show()
    def OnEraseBack(self, event):
        '''加入图片背景'''
        try:
            dc = event.GetDC()
            if not dc:
                dc = wx.ClientDC(self)
                dc.SetClippingRect(self.GetUpdateRegion().GetBox())
            dc.Clear()
            dc.DrawBitmap(wx.Bitmap(nowpath + r'\pic.jpg'), 0, 0)
        except:
            pass
class MyFrame9(wx.Frame):
    '''用于显示某城市新房信息的界面'''
    def __init__(self,parent,id,chengshi):
        self.chengshi =  chengshi    
        wx.Frame.__init__(self, parent,id, title="一种房价智能查询软件V1.0",pos=(200,80),size=(1500, 900))
        panel = wx.Panel(self) 
        self.text = wx.TextCtrl(panel,style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_CENTRE,size=(1400,800)) 
        font = wx.Font(15,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.text.SetFont(font)
        self.city_input1=self.chengshi      
        self.new_name=[]
        self.new_area=[]
        self.new_money=[]
        self.new_layout=[]
        self.new_state=[]       
        db = pymysql.connect(host="localhost", user="root",password= "root", database='xinfang',charset="utf8",autocommit=True)
        cursor = db.cursor()
        sql = "select * from %s " %self.city_input1
        cursor.execute(sql)
        for name in cursor.fetchall():
            name_1 = name[1]
            self.new_name.append(name_1)
        db.close()
        db = pymysql.connect(host="localhost", user="root",password= "root", database='xinfang',charset="utf8",autocommit=True)
        cursor = db.cursor()
        sql = "select * from %s " %self.city_input1
        cursor.execute(sql)
        for area in cursor.fetchall():
            area_1 = area[2]
            self.new_area.append(area_1)
        db.close() 
        db = pymysql.connect(host="localhost", user="root",password= "root", database='xinfang',charset="utf8",autocommit=True)
        cursor = db.cursor()
        sql = "select * from %s " %self.city_input1
        cursor.execute(sql)
        for layout in cursor.fetchall():
            layout_1 = layout[3]
            self.new_layout.append(layout_1)
        db.close()
        db = pymysql.connect(host="localhost", user="root",password= "root", database='xinfang',charset="utf8",autocommit=True)
        cursor = db.cursor()
        sql = "select * from %s " %self.city_input1
        cursor.execute(sql)
        for state in cursor.fetchall():
            state_1 = state[5]
            self.new_state.append(state_1)
        db.close()       
        db = pymysql.connect(host="localhost", user="root",password= "root", database='xinfang',charset="utf8",autocommit=True)
        cursor = db.cursor()
        sql = "select * from %s " %self.city_input1
        cursor.execute(sql)
        for money in cursor.fetchall():
            money_1 = money[4]
            self.new_money.append(money_1)
        db.close()   
        self.text.AppendText("      小区         "+"         面积      "+"       布局    "+"      价格  "+"        状态  "+"\n")
        for i in range(len(self.new_name)):
            self.text.AppendText(self.new_name[i])
            self.text.AppendText('        ' + self.new_area[i])
            self.text.AppendText('       ' + self.new_layout[i])
            self.text.AppendText('       ' + self.new_money[i])
            self.text.AppendText('      ' + self.new_state[i]+'\n')
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)
        self.bt_return = wx.Button(panel,label='返回')
        font = wx.Font(14,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.bt_return.SetFont(font)
        self.bt_return.Bind(wx.EVT_BUTTON,self.OnclickReturn)
        self.bt_photo = wx.Button(panel,label='房价排名前十')
        font = wx.Font(14,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.bt_photo.SetFont(font)
        self.bt_photo.Bind(wx.EVT_BUTTON,self.OnclickPhoto)
        self.bt_photo1 = wx.Button(panel,label='户型比例')
        font = wx.Font(14,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.bt_photo1.SetFont(font)
        self.bt_photo1.Bind(wx.EVT_BUTTON,self.OnclickPhoto1)
        hsizer_button15 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button15.Add(self.bt_return, proportion=0, flag=wx.ALL, border=1)
        hsizer_button16 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button16.Add(self.bt_photo, proportion=0, flag=wx.ALL, border=1) 
        hsizer_button16.Add(self.bt_photo1, proportion=0, flag=wx.ALL, border=1) 
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(hsizer_button16, proportion=0, flag= wx.LEFT|wx.BOTTOM , border=1)
        vsizer_all.Add(hsizer_button15, proportion=0, flag= wx.LEFT|wx.BOTTOM , border=1)
        vsizer_all.Add(self.text, proportion = 0,flag=wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER, border=15)
        panel.SetSizer(vsizer_all)
    def OnclickReturn(self,event): 
        '''返回上级界面'''
        self.Destroy()    
    def OnclickPhoto(self,event):   
        '''显示柱状图'''
        new_money=','.join(self.new_money)
        money=re.findall('\d+', new_money)
        o=[]
        for i in range(len(money)):
            mon=int(money[i])
            o.append(mon)
        m=dict(zip(self.new_name,o))
        m_dict=sorted(m.items(),key=lambda x:x[1],reverse=True)        
        no = []
        mo = []
        for i in m_dict:
            money1=i[1]
            mo.append(money1)
            name1=i[0]
            no.append(name1)
        m=[]
        n=[]
        for a in range(11):
            m.append(mo[a])
            n.append(no[a])
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        plt.figure(figsize=(15,8),dpi=80)
        plt.bar(range(len(n)),m,width=0.5)        
        plt.xticks(range(len(n)),n,rotation=35)        
        plt.xlabel("小区")
        plt.ylabel("单价（/万）")
        plt.title("新房房价前十名")        
        plt.grid(alpha=0.3)
        plt.show()
    def OnclickPhoto1(self,event):
        '''显示圆饼图'''
        db = pymysql.connect(host="localhost", user="root",password= "root", database='xinfang',charset="utf8",autocommit=True)
        cursor = db.cursor()
        sql = "select * from %s " %self.city_input1
        new_layout = []
        cursor.execute(sql)
        for layout in cursor.fetchall():
            layout_1 = layout[3]
            new_layout.append(layout_1)
        db.close() 
        new_layout_1 = []
        for nl in new_layout:
            nl_1 = re.findall('\w室', str(nl))
            if nl_1 != []:
                new_layout_1 += nl_1
            nl_2 = re.findall('别墅',str(nl))
            if nl_2 != []:
                new_layout_1 += nl_2
            nl_3 = re.findall('商住',str(nl))
            if nl_3 != []:
                new_layout_1 += nl_3
        num_1 = 0
        num_2 = 0
        num_3 = 0
        num_4 = 0
        num_5 = 0
        for i in new_layout_1:
            if i == '1室':
                num_1 += 1
            elif i == '2室':
                num_2 += 1
            elif i == '别墅':
                num_3 += 1
            elif i == '商住':
                num_4 += 1
            else:
                num_5 += 1
        vals = [num_1, num_2, num_3,num_4,num_5]
        fig, ax = plt.subplots()
        labels = '1室', '2室', '别墅','商住','3室以上'
        colors = ['yellowgreen', 'gold', 'lightskyblue','lightcoral','cyan']
        explode = (0,0,0,0,0.1)
        ax.pie(vals, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90,radius=1.2)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        ax.set(aspect="equal", title='户型分布')
        plt.show()
    def OnEraseBack(self, event):
        '''加入图片背景'''
        try:
            dc = event.GetDC()
            if not dc:
                dc = wx.ClientDC(self)
                dc.SetClippingRect(self.GetUpdateRegion().GetBox())
            dc.Clear()
            dc.DrawBitmap(wx.Bitmap(nowpath + r'\pic.jpg'), 0, 0)
        except:
            pass
class MyFrame11(wx.Frame):
    '''用于显示某城市出租房信息的界面'''
    def __init__(self,parent,id,chengshi):
        self.chengshi =  chengshi       
        wx.Frame.__init__(self, parent,id, title="一种房价智能查询软件V1.0",pos=(200,80),size=(1500, 900))
        panel = wx.Panel(self) 
        self.text = wx.TextCtrl(panel,style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_CENTRE,size=(1400,800)) 
        font = wx.Font(15,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.text.SetFont(font)
        self.city_input1=self.chengshi      
        self.new_name=[]
        self.new_local=[]
        self.new_place=[]
        self.new_money=[]
        db = pymysql.connect(host="localhost", user="root",password= "root", database='chuzu',charset="utf8",autocommit=True)
        cursor = db.cursor()
        sql = "select * from %s " %self.city_input1
        cursor.execute(sql)
        for name in cursor.fetchall():
            name_1 = name[1]
            self.new_name.append(name_1)
        db.close()        
        db = pymysql.connect(host="localhost", user="root",password= "root", database='chuzu',charset="utf8",autocommit=True)
        cursor = db.cursor()
        sql = "select * from %s " %self.city_input1
        cursor.execute(sql)
        for local in cursor.fetchall():
            local_1 = local[2]
            self.new_local.append(local_1)
        db.close()       
        db = pymysql.connect(host="localhost", user="root",password= "root", database='chuzu',charset="utf8",autocommit=True)
        cursor = db.cursor()
        sql = "select * from %s " %self.city_input1
        cursor.execute(sql)
        for place in cursor.fetchall():
            place_1 = place[3]
            self.new_place.append(place_1)
        db.close()        
        db = pymysql.connect(host="localhost", user="root",password= "root", database='chuzu',charset="utf8",autocommit=True)
        cursor = db.cursor()
        sql = "select * from %s " %self.city_input1
        cursor.execute(sql)
        for money in cursor.fetchall():
            money_1 = money[4]
            self.new_money.append(money_1)
        db.close()          
        self.text.AppendText("   小区         "+"            位置         "+"          布局       "+"         价格     "+"\n")
        for i in range(len(self.new_name)):
            self.text.AppendText(self.new_name[i])
            self.text.AppendText('           ' + self.new_local[i])
            self.text.AppendText('               ' + self.new_place[i])
            self.text.AppendText('            ' + self.new_money[i]+'\n')
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)
        self.bt_return = wx.Button(panel,label='返回')
        font = wx.Font(14,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.bt_return.SetFont(font)
        self.bt_return.Bind(wx.EVT_BUTTON,self.OnclickReturn)
        self.bt_photo = wx.Button(panel,label='房价排名前十')
        font = wx.Font(14,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.bt_photo.SetFont(font)
        self.bt_photo.Bind(wx.EVT_BUTTON,self.OnclickPhoto)  
        self.bt_photo2 = wx.Button(panel,label='户型比例')
        font = wx.Font(14,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.bt_photo2.SetFont(font)
        self.bt_photo2.Bind(wx.EVT_BUTTON,self.OnclickPhoto2) 
        self.bt_average = wx.Button(panel,label='平均房价')
        font = wx.Font(14,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.bt_average.SetFont(font)
        self.bt_average.Bind(wx.EVT_BUTTON,self.OnclickAverage)
        hsizer_button17 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button17.Add(self.bt_photo, proportion=0, flag=wx.ALL, border=1) 
        hsizer_button17.Add(self.bt_photo2, proportion=0, flag=wx.ALL, border=1)
        hsizer_button17.Add(self.bt_average, proportion=0, flag=wx.ALL, border=1) 
        hsizer_button18 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button18.Add(self.bt_return, proportion=0, flag=wx.ALL, border=1)
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(hsizer_button17, proportion=0, flag= wx.LEFT|wx.BOTTOM , border=1)
        vsizer_all.Add(hsizer_button18, proportion=0, flag= wx.LEFT|wx.BOTTOM , border=1)
        vsizer_all.Add(self.text, proportion = 0,flag=wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER, border=15)
        panel.SetSizer(vsizer_all)
    def OnclickReturn(self,event):   
        '''返回上级界面'''
        self.Destroy()
    def OnclickAverage(self,event):
        '''跳转至MyFrame12'''
        frame = MyFrame12(parent=None,id=-1,city_input=self.city_input1)
        frame.Show()
    def OnclickPhoto(self,event):  
        '''显示柱状图'''
        new_money=','.join(self.new_money)
        money=re.findall('\d+', new_money)
        o=[]
        for i in range(len(money)):
            mon=int(money[i])
            o.append(mon)
        m=dict(zip(self.new_name,o))
        m_dict=sorted(m.items(),key=lambda x:x[1],reverse=True)         
        no = []
        mo = []
        for i in m_dict:
            money1=i[1]
            mo.append(money1)
            name1=i[0]
            no.append(name1)
        m=[]
        n=[]
        for a in range(11):
            m.append(mo[a])
            n.append(no[a])
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        plt.figure(figsize=(15,8),dpi=80)
        plt.bar(range(len(n)),m,width=0.5)        
        plt.xticks(range(len(n)),n,rotation=35)        
        plt.xlabel("小区")
        plt.ylabel("单价（/万）")
        plt.title("出租房房价前十名")      
        plt.grid(alpha=0.3)
        plt.show()
    def OnclickPhoto2(self,event):
        '''显示圆饼图'''
        db = pymysql.connect(host="localhost", user="root",password= "root", database='chuzu',charset="utf8",autocommit=True)
        cursor = db.cursor()
        sql = "select * from %s " %self.city_input1
        new_place = []
        cursor.execute(sql)
        for place in cursor.fetchall():
            place_1 = place[3]
            new_place.append(place_1)
        db.close() 
        new_place_1 = []
        for npl in new_place:
            npl_1 = re.findall('\w室',str(npl))  
            new_place_1 += npl_1        
        num_1=0
        num_2=0
        num_3=0
        for i in new_place_1:
            if i == '1室':
                num_1 += 1
            elif i == '2室':
                num_2 += 1
            else:
                num_3 += 1
        vals = [num_1, num_2, num_3]
        fig, ax = plt.subplots()
        labels = '一室', '两室', '三室及三室以上'
        colors = ['yellowgreen', 'gold', 'lightskyblue']
        explode = (0,0,0.1)
        ax.pie(vals, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90,radius=1.2)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        ax.set(aspect="equal", title='户型比例')
        plt.show()
    def OnEraseBack(self, event):
        '''加入图片背景'''
        try:
            dc = event.GetDC()
            if not dc:
                dc = wx.ClientDC(self)
                dc.SetClippingRect(self.GetUpdateRegion().GetBox())
            dc.Clear()
            dc.DrawBitmap(wx.Bitmap(nowpath + r'\pic.jpg'), 0, 0)
        except:
            pass
class MyFrame4(wx.Frame): 
    '''用于显示某城市二手房平均房价的界面'''
    def __init__(self,parent,id,city_input):
        self.city_input=city_input
        wx.Frame.__init__(self, parent,id, title="二手房平均房价",pos=(800,200),size=(600, 300),
                          style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        self.Center()
        panel = wx.Panel(self) 
        self.new_money=[]
        db = pymysql.connect(host="localhost", user="root",password= "root", database='ershoufang',charset="utf8",autocommit=True)
        cursor = db.cursor()
        sql = "select * from %s " %self.city_input
        cursor.execute(sql)
        for money in cursor.fetchall():
            money_1 = money[6]
            self.new_money.append(money_1)
        db.close()
        m=re.findall('\d+', str(self.new_money))
        number=[int(x) for x in m]
        sall=sum(number)
        answer=round(sall/len(m))
        self.title = TransparentStaticText(panel,label = self.city_input+'平均房价')
        font = wx.Font(30,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.title.SetFont(font)
        self.text = TransparentStaticText(panel,label = str(answer)+'元/㎡')
        font = wx.Font(40,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.text.SetFont(font)
        self.text.SetForegroundColour('red')
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER,
                        border=20)
        vsizer_all.Add(self.text, proportion=0, flag= wx.ALIGN_CENTER|wx.BOTTOM , border=30)
        panel.SetSizer(vsizer_all)        
class MyFrame12(wx.Frame): 
    '''用于显示某城市出租房平均房价的界面'''
    def __init__(self,parent,id,city_input):
        self.city_input=city_input
        wx.Frame.__init__(self, parent,id, title="出租房平均房价",pos=(800,200),size=(600, 300),
                          style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        self.Center()
        panel = wx.Panel(self) 
        self.new_money=[]      
        db = pymysql.connect(host="localhost", user="root",password= "root", database='chuzu',charset="utf8",autocommit=True)
        cursor = db.cursor()
        sql = "select * from %s " %self.city_input
        cursor.execute(sql)
        for money in cursor.fetchall():
            money_1 = money[4]
            self.new_money.append(money_1)
        db.close()
        m=re.findall('\d+', str(self.new_money))
        number=[int(x) for x in m]
        sall=sum(number)
        answer=round(sall/len(m))
        self.title = TransparentStaticText(panel,label = self.city_input+'平均房价')
        font = wx.Font(30,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.title.SetFont(font)
        self.text = TransparentStaticText(panel,label = str(answer)+'元/月')
        font = wx.Font(40,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        self.text.SetFont(font)
        self.text.SetForegroundColour('red')
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER,
                        border=20)
        vsizer_all.Add(self.text, proportion=0, flag= wx.ALIGN_CENTER|wx.BOTTOM , border=30)
        panel.SetSizer(vsizer_all)       
class TransparentStaticText(wx.StaticText):
    '''将静态文本框的背景色改为透明色'''
    def __init__(self, parent, id=wx.ID_ANY, label='', pos=wx.DefaultPosition, size=wx.DefaultSize,
                  style=wx.TRANSPARENT_WINDOW, name='TransparentStaticText'):
        wx.StaticText.__init__(self, parent, id, label, pos, size, style, name)
        self.Bind(wx.EVT_PAINT, self.On_Paint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, lambda event: None)
        self.Bind(wx.EVT_SIZE, self.On_Size)
    def On_Paint(self, event):
        bdc = wx.PaintDC(self)
        dc = wx.GCDC(bdc)
        font_face = self.GetFont()
        font_color = self.GetForegroundColour()
        dc.SetFont(font_face)
        dc.SetTextForeground(font_color)
        dc.DrawText(self.GetLabel(), 0, 0)
    def On_Size(self, event):
        self.Refresh()
        event.Skip()            
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame5(parent=None,id=-1)
    frame.Show()
    app.MainLoop()

