from tkinter import ttk
from tkinter.ttk import Style, Button, Label
from tkinter.colorchooser import *
from tkinter.scrolledtext import *
from tkinter.filedialog import *
from tkFontChooser import askfont
from tkinter import filedialog
import pymysql
import time
from tkinter import *
from tkinter import Tk
from tkinter import IntVar
import pickle
import pprint
from sys import platform
import os
import logging


try:
    from urllib.request import Request, urlopen  # Python 3
except:
    from urllib2 import Request, urlopen  # Python 2


import time

import smtplib
from threading import Thread

global cursor
global ip 

ip = "193.11.186.133"

def db():
    global cursor,connecttodb
    try:
       connecttodb = pymysql.connect(host=ip, port=3306, user='sneha', passwd='sneha', db='Paint')
    except pymysql.Error:
        log("Connection error")
    cursor = connecttodb.cursor()
        


def getcurrenttime():
    global localtime
    localtime = time.asctime( time.localtime(time.time()) )
    print ("Local current time :", localtime)
    return localtime



def page_for_admin():
        global root_admin
        root_admin = Tk()
        button1= Button(root_admin , text = "select session" , command = select_session)
        root_admin.mainloop()

def register_as_user():
        global type1
        type1=str("user")
        Signup()

def register_as_emplo():
        global type1
        type1=str("employee")
        Signup()

def create_widgets_foruser():
        global cursor,connecttodb
        # function that crates the widget
        # Left Frame (Tools):
        global roota,root_user
        root_user.destroy()
        roota=Tk()
        global radiobuttonValue , tools_Thickness , outline_color , filling_color , font_str , font_size , font_weight , font_sla , response , lock , stack , x0 , y0 , x1 ,y1 , id , move , action
        global previousX , previousY
        radiobuttonValue = IntVar()
        radiobuttonValue.set(2)
        tools_Thickness = 2
        rgb = "#%02x%02x%02x" % (255, 255, 255)
        left_rgb = "#%02x%02x%02x" % (155, 48, 255)  # (217, 156, 230)
        outline_color = 'black'
        filling_color = 'white'
        font_str = 'Times'
        font_size = 10
        font_weight = "normal"
        font_sla = "normal"
        response = None
        #lock = "FALSE"
        #pack()
        stack = []
        x0 = 0
        y0 = 0
        x1 = 0
        y1 = 0
        id = None
        move = False
        action = None
        
        
        db()
        cursor.execute("""update login1 SET loginstatus='TRUE' where username=%s """,[nam] )
        

        connecttodb.commit()
        
        connecttodb.close()
        
       
        
        url="http://"
        url=url+ip
        url=url+":5000/getlock?name="
        url = url+nam
        print(url)
        q = Request(url)
        a = urlopen(q).read()
        lock = a
        
        


        



        
        global sheet , msg



        
        leftFrame = Frame(roota, bg=left_rgb)
        leftFrame.pack(side=LEFT, fill=BOTH, expand=True)
        labelTools = Label(leftFrame, text="\nChose a drawing tool:", bg=left_rgb,
                                font=("Helvetica", 12), anchor=W). \
            grid(padx=3, pady=2, row=2, column=0, sticky=EW)
        Radiobutton(leftFrame, text="Pencil", variable=radiobuttonValue, value=1, anchor=W). \
            grid(padx=3, pady=2, row=4, column=0, sticky=EW)
        Radiobutton(leftFrame, text="Line", variable=radiobuttonValue, value=2, anchor=W). \
            grid(padx=3, pady=2, row=4, column=1, sticky=EW)
        Radiobutton(leftFrame, text="Poly-line", variable=radiobuttonValue, value=3, anchor=W). \
            grid(padx=3, pady=2, row=6, column=0, sticky=EW)
        Radiobutton(leftFrame, text="Arrow", variable=radiobuttonValue, value=6, anchor=W). \
            grid(padx=3, pady=2, row=6, column=1, sticky=EW)
        Radiobutton(leftFrame, text="Oval/Circle", variable=radiobuttonValue, value=4, anchor=W). \
            grid(padx=3, pady=2, row=8, column=0, sticky=EW)
        Radiobutton(leftFrame, text="Rectangle/Square", variable=radiobuttonValue, value=5, anchor=W). \
            grid(padx=3, pady=2, row=8, column=1, sticky=EW)
        Radiobutton(leftFrame, text="Text  ", variable=radiobuttonValue, value=7, anchor=W). \
            grid(padx=3, pady=2, row=10, column=0, sticky=NSEW)
        Button(leftFrame, text='Select font', command=select_font). \
            grid(padx=1, pady=2, row=10, column=1, sticky=EW)
        Radiobutton(leftFrame, text="Eraser", variable=radiobuttonValue, value=8, anchor=W). \
            grid(padx=3, pady=2, row=12, column=0, sticky=NSEW)
        Button(leftFrame, text="Clear paper", command=delte_All) \
            .grid(padx=1, pady=2, row=12, column=1, sticky=EW)
        labelThickness = Label(leftFrame, text="\nTools' thickness:", bg=left_rgb,
                                    font=("Helvetica", 12), anchor=W) \
            .grid(padx=3, pady=2, row=13, column=0, sticky=NSEW)
        global myScale
        myScale = Scale(leftFrame, from_=1, to=30, orient=HORIZONTAL, command=set_Thickness)
        myScale.grid(padx=3, pady=2, row=14, column=0, sticky=EW, columnspan=2)
        myScale.set(2)
        Label(leftFrame, text="\nChose color:", bg=left_rgb, font=("Helvetica", 12), anchor=W). \
            grid(padx=3, pady=2, row=15, column=0, sticky=EW)
        Button(leftFrame, text='Outline Color', command=get_outline_color). \
            grid(padx=3, pady=2, row=16, column=0, sticky=EW)
        Button(leftFrame, text='Filling Color', command=get_filling_color). \
            grid(padx=3, pady=2, row=16, column=1, sticky=EW)
        #Label(leftFrame, text="\nEdit options:", bg=left_rgb, font=("Helvetica", 12), anchor=W). \
            #grid(padx=3, pady=2, row=17, column=0, sticky=EW)
        Button(leftFrame, text="sign_out", command=sign_out_app). \
            grid(padx=3, pady=2, row=18, column=0, sticky=EW)
        
        # Message console:
        msg = ScrolledText(state="normal", width=108, height=15, bg='black', foreground='yellow', font=10)
        msg.pack(side=BOTTOM, fill=BOTH, expand=True)

        # Create the frames(Tabs)
        notebook = ttk.Notebook(roota)
        sheet1 = ttk.Frame(notebook)
        notebook.add(sheet1, text='Sheet 1')
        sheet2 = ttk.Frame(notebook)
        notebook.add(sheet2, text='Sheet 2')
        notebook.pack(side=TOP, fill=BOTH, expand=True)
        global myCanvas_2 , myCanvas_1 
        # Create widget 2:
        myCanvas_2 = Canvas(sheet2, width=800, height=500,
                                 relief=RAISED, borderwidth=5, bg='white')
        horizon_bar_2 = Scrollbar(sheet2, orient=HORIZONTAL)
        horizon_bar_2.pack(side=BOTTOM, fill=X)
        horizon_bar_2.config(command=myCanvas_2.xview)
        vertical_bar_2 = Scrollbar(sheet2, orient=VERTICAL)
        vertical_bar_2.pack(side=RIGHT, fill=Y)
        vertical_bar_2.config(command=myCanvas_2.yview)
        myCanvas_2.config(xscrollcommand=horizon_bar_2.set, yscrollcommand=vertical_bar_2.set)
        myCanvas_2.pack(side=RIGHT, expand=True, fill=BOTH)
        myCanvas_2.bind("<Button-3>", select_sheet_2)

        # Create widget 1:
        myCanvas_1 = Canvas(sheet1, width=800, height=500, relief=RAISED, borderwidth=5, bg='white')
        horizon_bar_1 = Scrollbar(sheet1, orient=HORIZONTAL)
        horizon_bar_1.pack(side=BOTTOM, fill=X)
        horizon_bar_1.config(command=myCanvas_1.xview)
        vertical_bar_1 = Scrollbar(sheet1, orient=VERTICAL)
        vertical_bar_1.pack(side=RIGHT, fill=Y)
        vertical_bar_1.config(command=myCanvas_1.yview)
        myCanvas_1.config(xscrollcommand=horizon_bar_1.set, yscrollcommand=vertical_bar_1.set)
        myCanvas_1.pack(side=RIGHT, expand=True, fill=BOTH)
        myCanvas_1.bind("<Button-3>", select_sheet_1, add="+")
        log("please choose your sheet by right-click")
        roota.mainloop()


        

def create_widgets():
        # function that crates the widget
        # Left Frame (Tools):
      
        global roota,root_employee
        global cursor,connecttodb
        
        root_employee.destroy()
        roota=Tk()
        global radiobuttonValue , tools_Thickness , outline_color , filling_color , font_str , font_size , font_weight , font_sla , response , lock , stack , x0 , y0 , x1 ,y1 , id , move , action
        global previousX , previousY
        radiobuttonValue = IntVar()
        radiobuttonValue.set(2)
        tools_Thickness = 2
        rgb = "#%02x%02x%02x" % (255, 255, 255)
        left_rgb = "#%02x%02x%02x" % (155, 48, 255)  # (217, 156, 230)
        outline_color = 'black'
        filling_color = 'white'
        font_str = 'Times'
        font_size = 10
        font_weight = "normal"
        font_sla = "normal"
        response = None
        lock = "FALSE"
        #pack()
        stack = []
        x0 = 0
        y0 = 0
        x1 = 0
        y1 = 0
        id = None
        move = False
        action = None

        db()
        cursor.execute("""update login1 SET loginstatus='TRUE' where username=%s""",[nam] )

        connecttodb.commit()
        
        connecttodb.close()
        
        
        
        global sheet , msg



        
        leftFrame = Frame(roota, bg=left_rgb)
        leftFrame.pack(side=LEFT, fill=BOTH, expand=True)
        labelTools = Label(leftFrame, text="\nChose a drawing tool:", bg=left_rgb,
                                font=("Helvetica", 12), anchor=W). \
            grid(padx=3, pady=2, row=2, column=0, sticky=EW)
        Radiobutton(leftFrame, text="Pencil", variable=radiobuttonValue, value=1, anchor=W). \
            grid(padx=3, pady=2, row=4, column=0, sticky=EW)
        Radiobutton(leftFrame, text="Line", variable=radiobuttonValue, value=2, anchor=W). \
            grid(padx=3, pady=2, row=4, column=1, sticky=EW)
        Radiobutton(leftFrame, text="Poly-line", variable=radiobuttonValue, value=3, anchor=W). \
            grid(padx=3, pady=2, row=6, column=0, sticky=EW)
        Radiobutton(leftFrame, text="Arrow", variable=radiobuttonValue, value=6, anchor=W). \
            grid(padx=3, pady=2, row=6, column=1, sticky=EW)
        Radiobutton(leftFrame, text="Oval/Circle", variable=radiobuttonValue, value=4, anchor=W). \
            grid(padx=3, pady=2, row=8, column=0, sticky=EW)
        Radiobutton(leftFrame, text="Rectangle/Square", variable=radiobuttonValue, value=5, anchor=W). \
            grid(padx=3, pady=2, row=8, column=1, sticky=EW)
        Radiobutton(leftFrame, text="Text  ", variable=radiobuttonValue, value=7, anchor=W). \
            grid(padx=3, pady=2, row=10, column=0, sticky=NSEW)
        Button(leftFrame, text='Select font', command=select_font). \
            grid(padx=1, pady=2, row=10, column=1, sticky=EW)
        Radiobutton(leftFrame, text="Eraser", variable=radiobuttonValue, value=8, anchor=W). \
            grid(padx=3, pady=2, row=12, column=0, sticky=NSEW)
        Button(leftFrame, text="Clear paper", command=delte_All) \
            .grid(padx=1, pady=2, row=12, column=1, sticky=EW)
        labelThickness = Label(leftFrame, text="\nTools' thickness:", bg=left_rgb,
                                    font=("Helvetica", 12), anchor=W) \
            .grid(padx=3, pady=2, row=13, column=0, sticky=NSEW)
        global myScale
        myScale = Scale(leftFrame, from_=1, to=30, orient=HORIZONTAL, command=set_Thickness)
        myScale.grid(padx=3, pady=2, row=14, column=0, sticky=EW, columnspan=2)
        myScale.set(2)
        Label(leftFrame, text="\nChose color:", bg=left_rgb, font=("Helvetica", 12), anchor=W). \
            grid(padx=3, pady=2, row=15, column=0, sticky=EW)
        Button(leftFrame, text='Outline Color', command=get_outline_color). \
            grid(padx=3, pady=2, row=16, column=0, sticky=EW)
        Button(leftFrame, text='Filling Color', command=get_filling_color). \
            grid(padx=3, pady=2, row=16, column=1, sticky=EW)
        Label(leftFrame, text="\nEdit options:", bg=left_rgb, font=("Helvetica", 12), anchor=W). \
            grid(padx=3, pady=2, row=17, column=0, sticky=EW)
        Button(leftFrame, text="Undo", command=undo). \
            grid(padx=3, pady=2, row=18, column=0, sticky=EW)
        Button(leftFrame, text="Reload", command=reload). \
            grid(padx=3, pady=2, row=18, column=1, sticky=EW)
        Button(leftFrame, text='Lock', command=locker). \
            grid(padx=3, pady=2, row=20, column=0, sticky=EW)
        Button(leftFrame, text='Unlock', command=unlock). \
            grid(padx=3, pady=2, row=20, column=1, sticky=EW)
        Button(leftFrame, text='Save as *.ps', command=save_project). \
            grid(padx=3, pady=2, row=22, column=0, sticky=EW)
        Button(leftFrame, text='Clear history', command=truncate_db). \
            grid(padx=3, pady=2, row=22, column=1, sticky=EW)

        Button(leftFrame, text='Change moderator', command=change_moderator). \
            grid(padx=3, pady=2, row=23, column=1, sticky=EW)
        Button(leftFrame, text="sign_out", command=sign_out_app). \
            grid(padx=3, pady=2, row=24, column=0, sticky=EW)
        

        


        # Message console:
        msg = ScrolledText(state="normal", width=108, height=15, bg='black', foreground='yellow', font=10)
        msg.pack(side=BOTTOM, fill=BOTH, expand=True)

        # Create the frames(Tabs)
        notebook = ttk.Notebook(roota)
        sheet1 = ttk.Frame(notebook)
        notebook.add(sheet1, text='Sheet 1')
        sheet2 = ttk.Frame(notebook)
        notebook.add(sheet2, text='Sheet 2')
        notebook.pack(side=TOP, fill=BOTH, expand=True)
        global myCanvas_2 , myCanvas_1 
        # Create widget 2:
        myCanvas_2 = Canvas(sheet2, width=800, height=500,
                                 relief=RAISED, borderwidth=5, bg='white')
        horizon_bar_2 = Scrollbar(sheet2, orient=HORIZONTAL)
        horizon_bar_2.pack(side=BOTTOM, fill=X)
        horizon_bar_2.config(command=myCanvas_2.xview)
        vertical_bar_2 = Scrollbar(sheet2, orient=VERTICAL)
        vertical_bar_2.pack(side=RIGHT, fill=Y)
        vertical_bar_2.config(command=myCanvas_2.yview)
        myCanvas_2.config(xscrollcommand=horizon_bar_2.set, yscrollcommand=vertical_bar_2.set)
        myCanvas_2.pack(side=RIGHT, expand=True, fill=BOTH)
        myCanvas_2.bind("<Button-3>", select_sheet_2)

        # Create widget 1:
        myCanvas_1 = Canvas(sheet1, width=800, height=500, relief=RAISED, borderwidth=5, bg='white')
        horizon_bar_1 = Scrollbar(sheet1, orient=HORIZONTAL)
        horizon_bar_1.pack(side=BOTTOM, fill=X)
        horizon_bar_1.config(command=myCanvas_1.xview)
        vertical_bar_1 = Scrollbar(sheet1, orient=VERTICAL)
        vertical_bar_1.pack(side=RIGHT, fill=Y)
        vertical_bar_1.config(command=myCanvas_1.yview)
        myCanvas_1.config(xscrollcommand=horizon_bar_1.set, yscrollcommand=vertical_bar_1.set)
        myCanvas_1.pack(side=RIGHT, expand=True, fill=BOTH)
        myCanvas_1.bind("<Button-3>", select_sheet_1, add="+")
        log("please choose your sheet by right-click")
        roota.mainloop()

def sign_out_app():
        
        global t3
            
            
        global cursor,connecttodb
        t3=Thread(target=t3start)
        t3.start()
        
        print("kk")
            

        
        roota.destroy()
        buttons_regis()


def t3start():
        global t3
        global cursor,connecttodb
        db()
        cursor.execute("""update login1 SET loginstatus='FALSE' where username=%s""",[nam] )
        
        connecttodb.commit()
        connecttodb.close()
            


def get_moderator():
        global moderator_name

        url="http://"
        url=url+ip
        url=url+":5000/getmoderator"
        

        q = Request(url)
        moderator_name = urlopen(q).read()

        
        

def change_moderator():
        global x,moderator_name,rootB,e1
        global cursor,connecttodb
        get_moderator()
        xooo=str(moderator_name)
        db()
        cursor.execute("""select username from login1""")
        
        users = cursor.fetchall()
        rootB = Tk()  
        connecttodb.commit()
        connecttodb.close()

        x=Text(rootB)
        x.insert(INSERT, " the present moderator is \n ")
        x.insert(INSERT, xooo)
        x.insert(INSERT,'\n')
        x.insert(INSERT,"select the moderator by entering it in the entry box below from the following list\n")
        for u in users:

            x.insert(INSERT,u)
            x.insert(INSERT,'\n')
        x.insert(END,"end")
        x.grid(row=0,column=1,rowspan=20)
        e1=Entry(rootB)
        e1.grid(row=20,column=1)
        Label(rootB,text="enter moderator name").grid(row=20)
        Button(rootB,text="select",command=change_mod_indatabase).grid(row=21,column=2)
        Button(rootB,text="quit",command=quit_root).grid(row=22,column=2)
        rootB.title('Change moderator')  
        
        rootB.mainloop()        
        
        


def quit_root():
        global rootB
        rootB.destroy()


def change_mod_indatabase():
        global rootB,mod,e1
        global cursor,connecttodb
        
        mod=e1.get()
        db()
        cursor.execute("""UPDATE login1 SET moderator='TRUE' WHERE username  = %s""",[mod])
        cursor.execute("""UPDATE login1 SET moderator='FALSE' WHERE username  != %s""",[mod])
        connecttodb.commit()
        connecttodb.close()  
    
        

def select_sheet_1( event):
        # select the sheet 1 by right click
        global sheet
        myCanvas_2.unbind("<B1-Motion>")
        myCanvas_2.unbind("<Button-1>")
        myCanvas_2.unbind("<ButtonRelease-1>")
        global myCanvas
        myCanvas = myCanvas_1
        myCanvas.bind("<B1-Motion>", draw)
        myCanvas.bind("<Button-1>", set_Previous_XY)
        myCanvas.bind("<ButtonRelease-1>", set_Current_XY, add="+")
        myCanvas.bind("<ButtonRelease-1>", stop_shape, add="+")
        sheet = str("sheet_1")
        log("Sheet 1 is selected")

def select_sheet_2( event):
        # select the sheet 2 by right click
        global sheet
        myCanvas_1.unbind("<B1-Motion>")
        myCanvas_1.unbind("<Button-1>")
        myCanvas_1.unbind("<ButtonRelease-1>")
        global myCanvas
        myCanvas = myCanvas_2
        myCanvas.bind("<B1-Motion>", draw)
        myCanvas.bind("<Button-1>", set_Previous_XY)
        myCanvas.bind("<ButtonRelease-1>", set_Current_XY, add="+")
        myCanvas.bind("<ButtonRelease-1>", stop_shape, add="+")
        sheet = str("sheet_2")
        log("Sheet 2 is selected")

def save_project():
        # save the widget to an image file (.ps format)
        output_file = filedialog.asksaveasfilename(filetypes=[('postscript', '*.ps')],
                                                   title='save project as postscript')
        try:
            with open(output_file, 'wb') as output:
                myCanvas.update()
                myCanvas.postscript(file=output_file, colormode='color')
                output.close()
        except FileNotFoundError:
            log("Cancelled save or error in filename")

def log( message):
        # log messages to the console to notify user
        msg.insert(END, message + "\n" + "\n")
        msg.see("end")

def locker():
        # Use for locking the widget
        global lock
        lock = "TRUE"
        
        
        global cursor,connecttodb
        db()
        cursor.execute("""UPDATE login1 SET lok_flag='TRUE' WHERE moderator  = 'FALSE'""")
        cursor.execute("""UPDATE login1 SET lok_flag='FALSE' WHERE username  = 'TRUE'""")
        cursor = connecttodb.cursor()
        




        connecttodb.commit()
        connecttodb.close()
        

        log("now it is locked!")

def unlock():
        # Use for locking the widget
        global lock
        lock = "FALSE"

        global cursor,connecttodb
        db()
        cursor.execute("""UPDATE login1 SET lok_flag='FALSE' WHERE moderator  = 'FALSE'""")
        
        cursor = connecttodb.cursor()
        




        connecttodb.commit()
        connecttodb.close()


        
        log("now it is unlocked!")





def set_Thickness( event):
        # set the thickness of the tools
        global tools_Thickness
        tools_Thickness = myScale.get()

def select_font():
        global font , font_str , font_size , font_weight , font_sla 
        # select the type and size of the font by user choice
        font = askfont()
        font_str = "%(family)s" % font
        font_size = "%(size)i" % font
        font_weight = "%(weight)s" % font
        font_sla = "%(slant)s" % font
        log("font type is: " + str(font_str) +
                 "\nfont size is: " + str(font_size) +
                 "\nfont mode is: " + str(font_weight) + " , " + str(font_sla))

def get_outline_color():
        # select the outline color of tools by user choice
        global outline_color
        outline_color = askcolor()
        outline_color = outline_color[1]
        log("Outline color is:" + str(outline_color[1]))

def get_filling_color():
        # select the filling color of tools by user choice
        global filling_color
        filling_color = askcolor()
        filling_color = filling_color[1]
        log("Filling color is:" + str(filling_color[1]))

def poly_end( event):
        # add the last line of the  poly line tool
        if lock == "FALSE":
            global action
            newx = event.x
            newy = event.y
            myCanvas.create_line(previousX, previousY, newx,
                                      newy, width=tools_Thickness, fill=outline_color)
            action = str("Polyline")
            increment_db(event)
            myCanvas.bind("<Button-1>", set_Previous_XY)

def set_new_click( event):
        # add a line to the end of previous one for poly line tool
        if lock == "FALSE":
            global newx , newy , previousX , previousY , action
            newx = event.x
            newy = event.y
            history = myCanvas.create_line(previousX, previousY, newx, newy,
                                                     width=tools_Thickness, fill=outline_color)
            stack.append(history)
            action = str("Polyline")
            increment_db(event)
            previousX = newx
            previousY = newy
            myCanvas.bind("<Double-Button-1>", poly_end)
            log("You can end the poly-line by double click")

def process_callback( event):
        # Create text box and get the user entry
        global response , tx ,ty , font_str , font_size , font_weight , font_sla 
        response = entry.get()
        history = canvas_id = myCanvas.create_text(tx, ty,
                                                                  anchor="center", font=(
                font_str, font_size, font_weight, font_sla))
        stack.append(history)
        myCanvas.itemconfig(canvas_id, text=response)
        myCanvas.insert(canvas_id, 12, '\n')
        tx = previousX
        ty = previousY
        increment_db(event)
        entry.destroy()

def delte_All():
        # Clear all objects on the widget
        history = myCanvas.delete("all")
        stack.append(history)

def increment_db( event):
        # Add all details of an action to the database
        xxx=getcurrenttime()
        current_time=str(xxx)
        global typeofcustomer
        #typeo=str("employee")
        global cursor,connecttodb
        db()
        cursor.execute("""INSERT INTO history1(username,typeofuser,action,sheet,value,F_Collor,O_Collor,thikness,X0,Y0,X1,Y1,F_Type,F_Size,F_Weight,F_Mode,Text,Dateandtime)
         VALUES(%s ,%s ,%s , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s )""",
                            [nam,typeofcustomer,action, sheet, radiobuttonValue.get(), filling_color,
                             outline_color, tools_Thickness, previousX, previousY,
                             event.x, event.y, font_str, font_size, font_weight, font_sla,
                             response,current_time])
        connecttodb.commit()
        connecttodb.close()

def truncate_db():
        # Delete all the rows of table history in database
        user = str("user1")
        global cursor,connecttodb
        db()
        cursor.execute("""truncate table Paint.history1""")
        log("Data base is empty now!")
        connecttodb.commit()
        connecttodb.close()

def undo():
        # Delete the last object that created on the widget
        try:
            last_action = stack.pop()
            myCanvas.delete(last_action)
        except IndexError:
            log("There is no more action")


def reload():
        # restore all the created objects from database and re-create them
        global roota,nam
        global cursor,connecttodb
        db()
        total = cursor.execute("""Select count(*) from Paint.history1 where username = %s""",[nam])
        total = cursor.fetchone()[0]
        if total == 0:
            log("There is not any history!")
        else:
            for i in range(1, int(total) + 1):
                global sheet
                
                action = cursor.execute("""Select * from Paint.history1 where id= %s and sheet= %s """,[i, sheet])
                print(i,nam)
                
                    
                try:
                    row = cursor.fetchall()[0]
                    value = int(row[5])
                    filling_color = row[6]
                    outline_color = row[7]
                    tools_Thickness = row[8]
                    previousX = row[9]
                    previousY = row[10]
                    currentX = row[11]
                    currentY = row[12]
                    font_str = row[13]
                    font_size = row[14]
                    font_weight = row[15]
                    font_sla = row[16]
                    response = row[17]

                    if value == 1:
                        myCanvas.create_line(previousX, previousY, currentX, currentY,
                                                      width=tools_Thickness, fill=outline_color)
                        time.sleep(2)
                        roota.update()
                            
                    elif value == 2:
                        myCanvas.create_line(previousX, previousY, currentX, currentY,
                                                      width=tools_Thickness, fill=outline_color)
                        time.sleep(2)
                        roota.update()
                        
                            
                    elif value == 3:
                        myCanvas.create_line(previousX, previousY, currentX, currentY,
                                                      width=tools_Thickness, fill=outline_color)

                        time.sleep(2)
                        roota.update()
                        
                            
                    elif value == 4:
                        myCanvas.create_oval(previousX, previousY, currentX, currentY,
                                                      outline=outline_color, fill=filling_color,
                                                      width=tools_Thickness)
                        time.sleep(2)
                        roota.update()
                        
                            
                    elif value == 5:
                        myCanvas.create_rectangle(previousX, previousY, currentX, currentY,
                                                           outline=outline_color, fill=filling_color,
                                                           width=tools_Thickness)
                            
                        time.sleep(2)
                        roota.update()
                        
                            
                    elif value == 6:
                        myCanvas.create_line(previousX, previousY, currentX, currentY,
                                                      width=tools_Thickness, fill=outline_color, arrow="last")
                        time.sleep(2)
                        roota.update()
                        
                            
                    elif value == 7:
                        myCanvas.create_text(previousX, previousY,
                                                      anchor="center", font=(
                                    font_str, font_size, font_weight, font_sla), text=response)
                        time.sleep(2)
                        roota.update()
                        
                            
                    elif value == 8:
                        myCanvas.create_line(previousX, previousY, currentX, currentY,
                                                      width=tools_Thickness, fill='white')
                        time.sleep(2)
                        roota.update()
                        
                            
                        
                except IndexError:
                    continue
                except AttributeError:
                    log("Please choose a sheet first!")
                    break
            connecttodb.close()


def set_Current_XY( event):
        global currentX , currentY
        # store current cursor position
        currentX = event.x
        currentY = event.y

def set_Previous_XY( event):
        global previousX , previousY , history , action
        # keep track of cursor position for creating shapes
        if (lock == "FALSE"):
            previousX = event.x
            previousY = event.y
        if radiobuttonValue.get() == 3:  # Poly_line
            previousX = event.x
            previousY = event.y
            myCanvas.bind("<Button-1>", set_new_click)
        elif radiobuttonValue.get() == 4:  # Circle
            global x0 , y0 , id
            move = True
            x0 = myCanvas.canvasx(event.x)
            y0 = myCanvas.canvasy(event.y)
           
            history = myCanvas.create_oval(x0, y0, x0, y0, outline=outline_color,
                                                     fill=filling_color, width=tools_Thickness)
            id = myCanvas.find_closest(x0, y0, halo=2)
        elif radiobuttonValue.get() == 5:  # Rectangular
            move = True
            x0 = myCanvas.canvasx(event.x)
            y0 = myCanvas.canvasy(event.y)
           
            history = myCanvas.create_rectangle(x0, y0, x0, y0,
                                                          outline=outline_color, fill=filling_color,
                                                         width=tools_Thickness)
            id = myCanvas.find_closest(x0, y0, halo=2)
        elif radiobuttonValue.get() == 7:  # Text
            global entry , tx ,ty , action
            tx = event.x
            ty = event.y
            entry = Entry(roota, bd=0, font=(font_str, font_size, font_weight, font_sla))
            entry.place(x=event.x, y=event.y)
            entry.focus_force()
            entry.bind('<Return>', process_callback)
            action = str("Text")
            # increment_db(event)
            print(entry)

def draw( event):
        # handle drawing tools - binded to the motion
        global previousX , previousY ,id , x0 , y0, x1 ,y1 , action , t1
        if (lock == "FALSE"):
            # Pencil
            if radiobuttonValue.get() == 1:
                history = myCanvas.create_line(previousX, previousY, event.x, event.y,
                                                         width=tools_Thickness, fill=outline_color)
                action = str("pencil")
                increment_db(event)
                previousX = event.x
                previousY = event.y
                stack.append(history)
            # oval/circle
            elif radiobuttonValue.get() == 4:
                if move:
                    x1 = myCanvas.canvasx(event.x)
                    y1 = myCanvas.canvasy(event.y)
                    myCanvas.coords(id, x0, y0, x1, y1)
            # Rectangle
            elif radiobuttonValue.get() == 5:
                if move:
                    x1 = myCanvas.canvasx(event.x)
                    y1 = myCanvas.canvasy(event.y)
                    myCanvas.coords(id, x0, y0, x1, y1)
                    
            # Eraser
            elif radiobuttonValue.get() == 8:
                
                history = myCanvas.create_line(previousX, previousY, event.x, event.y,
                                                         width=tools_Thickness, fill='white')
                action = str("Eraser")
                increment_db(event)
                previousX = event.x
                previousY = event.y
                stack.append(history)

                        
            

def stop_shape( event):
        # create shapes base on end point (mouse released)
        global previousX , previousY ,id , x0 , y0, x1 ,y1 , history,action
        
        if (lock == "FALSE"):
            if radiobuttonValue.get() == 2:  # Line
                
                history = myCanvas.create_line(previousX, previousY, currentX, currentY,
                                                         width=tools_Thickness, fill=outline_color)
                x0 = myCanvas.canvasx(currentX)
                y0 = myCanvas.canvasy(currentY)
                id = myCanvas.find_closest(x0, y0, halo=2)
                history = myCanvas.create_line(previousX, previousY, currentX, currentY,
                                                         width=tools_Thickness, fill=outline_color)
                stack.append(history)
                action = str("Line")
                increment_db(event)
            elif radiobuttonValue.get() == 4:  # Circle
                move = False
                
                x1 = myCanvas.canvasx(event.x)
                y1 = myCanvas.canvasy(event.y)
                myCanvas.coords(id, x0, y0, x1, y1)
                stack.append(history)
                action = str("Oval / Circle")
                increment_db(event)
            elif radiobuttonValue.get() == 5:  # Rectangular
                move = False
                
                x1 = myCanvas.canvasx(event.x)
                y1 = myCanvas.canvasy(event.y)
                myCanvas.coords(id, x0, y0, x1, y1)
                stack.append(history)
                action = str("Rectangle")
                increment_db(event)
                
            elif radiobuttonValue.get() == 6:  # Arrow
                x1 = myCanvas.canvasx(event.x)
                y1 = myCanvas.canvasy(event.y)
                
                history = myCanvas.create_line(previousX, previousY, x1, y1,
                                                         width=tools_Thickness, fill=outline_color,
                                                         arrow="last")

                x0 = myCanvas.canvasx(x1)
                y0 = myCanvas.canvasy(y1)
                id = myCanvas.find_closest(x0, y0, halo=2)
                action = str("Arrow")
                stack.append(history)
                increment_db(event)


def reload_rect():

#  select @last_id := MAX(id) From history1 where username = "user1";

# SELECT * FROM history1 WHERE id = @last_id;

# select @last_id := MAX(id) From history1 where username = "employee1";
    
    global myCanvas
    global cursor,connecttodb
    db()
    cursor.execute("""select username from login1 where loginstatus = 'TRUE' """)
    ee=cursor.fetchone()
    print(ee)
    action = cursor.execute("""select @last_id := MAX(id) From history1 where username = %s """,[ee])   
    action = cursor.execute("""Select * from Paint.history1 where id= @last_id""")
            
    row = cursor.fetchall()[0]
    name = row[1]
    sheetname=row[3]
    print(name) 
    print(sheetname)
    value = int(row[5])
    filling_color = row[6]
    outline_color = row[7]
    tools_Thickness = row[8]
    previousX = row[9]
    previousY = row[10]
    currentX = row[11]
    currentY = row[12]
    font_str = row[13]
    font_size = row[14]
    font_weight = row[15]
    font_sla = row[16]
    response = row[17]
    

    if value == 1:
        myCanvas.create_line(previousX, previousY, currentX, currentY,
                                                      width=tools_Thickness, fill=outline_color)
        log("drawn by ")
        log(name)
    
                            
    elif value == 2:
        myCanvas.create_line(previousX, previousY, currentX, currentY,
                                                      width=tools_Thickness, fill=outline_color)
        log("drawn by ")
        log(name)
    
                        
                            
    elif value == 3:
        myCanvas.create_line(previousX, previousY, currentX, currentY,
                                                      width=tools_Thickness, fill=outline_color)
        log("drawn by ")
        log(name)
    

                        
                            
    elif value == 4:
        myCanvas.create_oval(previousX, previousY, currentX, currentY,
                                                      outline=outline_color, fill=filling_color,
                                                      width=tools_Thickness)
        log("drawn by ")
        log(name)
    
                        
                            
    elif value == 5:
        myCanvas.create_rectangle(previousX, previousY, currentX, currentY,
                                                           outline=outline_color, fill=filling_color,
                                                           width=tools_Thickness)
        log("drawn by ")
        log(name)
    
                            
                        
                            
    elif value == 6:
        myCanvas.create_line(previousX, previousY, currentX, currentY,
                                                      width=tools_Thickness, fill=outline_color, arrow="last")
        log("drawn by ")
        log(name)
    
                        
                            
    elif value == 7:
        myCanvas.create_text(previousX, previousY,
                                                      anchor="center", font=(
                                    font_str, font_size, font_weight, font_sla), text=response)
        log("drawn by ")
        log(name)
    
                        
                            
    elif value == 8:
        myCanvas.create_line(previousX, previousY, currentX, currentY,
                                                      width=tools_Thickness, fill='white')
        log("drawn by ")
        log(name)
    
        
                        
                            
                        
    connecttodb.close()





def create_widgets_foradmin():
        global variable,t1,k
        variable=1
        # function that crates the widget
        # Left Frame (Tools):
        global roota,rootP
        global sheet , msg , myCanvas , stat

        rootP.destroy()
        roota=Tk()
        global radiobuttonValue , tools_Thickness , outline_color , filling_color , font_str , font_size , font_weight , font_sla , response , lock , stack , x0 , y0 , x1 ,y1 , id , move , action
        global previousX , previousY
        radiobuttonValue = IntVar()
        radiobuttonValue.set(2)
        tools_Thickness = 2
        rgb = "#%02x%02x%02x" % (255, 255, 255)
        left_rgb = "#%02x%02x%02x" % (155, 48, 255)  # (217, 156, 230)
        outline_color = 'black'
        filling_color = 'white'
        font_str = 'Times'
        font_size = 10
        font_weight = "normal"
        font_sla = "normal"
        response = None
        lock = "FALSE"
        #pack()
        stack = []
        x0 = 0
        y0 = 0
        x1 = 0
        y1 = 0
        id = None
        move = False
        action = None


        global cursor,connecttodb
        db()
        cursor.execute("""UPDATE admin1 SET status='TRUE' WHERE id = '2'""")
        
        
        global sheet , msg



        
        leftFrame = Frame(roota, bg=left_rgb)
        leftFrame.pack(side=LEFT, fill=BOTH, expand=True)
        Button(leftFrame, text="sign_out", command=sign_out_app). \
            grid(padx=3, pady=2, row=24, column=0, sticky=EW)
        

        


        # Message console:
        msg = ScrolledText(state="normal", width=108, height=15, bg='black', foreground='yellow', font=10)
        msg.pack(side=BOTTOM, fill=BOTH, expand=True)

        # Create the frames(Tabs)
        notebook = ttk.Notebook(roota)
        sheet1 = ttk.Frame(notebook)
        notebook.add(sheet1, text='Sheet 1')
        sheet2 = ttk.Frame(notebook)
        notebook.add(sheet2, text='Sheet 2')
        notebook.pack(side=TOP, fill=BOTH, expand=True)
        global myCanvas_2 , myCanvas_1 
        # Create widget 2:
        myCanvas_2 = Canvas(sheet2, width=800, height=500,
                                 relief=RAISED, borderwidth=5, bg='white')
        horizon_bar_2 = Scrollbar(sheet2, orient=HORIZONTAL)
        horizon_bar_2.pack(side=BOTTOM, fill=X)
        horizon_bar_2.config(command=myCanvas_2.xview)
        vertical_bar_2 = Scrollbar(sheet2, orient=VERTICAL)
        vertical_bar_2.pack(side=RIGHT, fill=Y)
        vertical_bar_2.config(command=myCanvas_2.yview)
        myCanvas_2.config(xscrollcommand=horizon_bar_2.set, yscrollcommand=vertical_bar_2.set)
        myCanvas_2.pack(side=RIGHT, expand=True, fill=BOTH)
        myCanvas_2.bind("<Button-3>", select_sheet_2)

        # Create widget 1:
        myCanvas_1 = Canvas(sheet1, width=800, height=500, relief=RAISED, borderwidth=5, bg='white')
        horizon_bar_1 = Scrollbar(sheet1, orient=HORIZONTAL)
        horizon_bar_1.pack(side=BOTTOM, fill=X)
        horizon_bar_1.config(command=myCanvas_1.xview)
        vertical_bar_1 = Scrollbar(sheet1, orient=VERTICAL)
        vertical_bar_1.pack(side=RIGHT, fill=Y)
        vertical_bar_1.config(command=myCanvas_1.yview)
        myCanvas_1.config(xscrollcommand=horizon_bar_1.set, yscrollcommand=vertical_bar_1.set)
        myCanvas_1.pack(side=RIGHT, expand=True, fill=BOTH)
        myCanvas_1.bind("<Button-3>", select_sheet_1, add="+")
        log("please choose your sheet by right-click")
        
        
            
        t1=Thread(target=p)
        t1.start()
        myCanvas=myCanvas_1
        
        roota.mainloop()

def p():
    i=1
    
    
    while i==1:
            
            checkforstatus()
            global stat
            if stat == "TRUE":
                reload_rect()
                time.sleep(3)
            elif stat==None:
                print("nakjbsnm")
                break

                

def checkforstatus():
    global stat
    global cursor,connecttodb
    db()
        
    cursor.execute("""select username from login1 where loginstatus = 'TRUE' """)
    bb=cursor.fetchone()
    
    cursor.execute("""select loginstatus from login1 where username = %s  """,[bb])
        
    xx=cursor.fetchone()
    print xx
    if xx==('FALSE',):
        stat="FALSE"
    elif xx==('TRUE',):
        stat = "TRUE"
    else:
        stat=None
    
    print(stat)
    return stat
    connecttodb.close()
        
        
                 
            




def Login():
    global nameEL
    global pwordEL 
    global rootA,roots
    rootw.destroy()
    rootA = Tk() 
    rootA.geometry('800x500')
    rootA.title('Login') 
    rootA.configure(background="orange")
    intruction = Label(rootA, text='Please Login\n') 
    intruction.grid(sticky=E) 
 
    nameL = Label(rootA, text='Username: ') 
    pwordL = Label(rootA, text='Password: ') 
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) 
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='Login', command=CheckLogin) 
    loginB.grid(columnspan=2, sticky=W)
    rootA.mainloop()





def Signup():  
    global pwordE 
    global nameE,root_user, root_employee
    global roots,email1
    
    roots = Tk() 
    roots.geometry('800x500')
    roots.title('Signup') 
    intruction = Label(roots, text='Please Enter new Credidentials\n') 
    intruction.grid(row=0, column=0, sticky=E) 
 
    nameL = Label(roots, text='New Username: ') 
    pwordL = Label(roots, text='New Password: ') 
    nameL.grid(row=1, column=0, sticky=W) 
    pwordL.grid(row=2, column=0, sticky=W) 
    email = Label(roots, text='email id: ') 
    email.grid(row=3 , column=0 , sticky=E)
    
 
    nameE = Entry(roots) 
    pwordE = Entry(roots, show='*') 
    email1=Entry(roots)
    email1.grid(row=3, column=1)
    nameE.grid(row=1, column=1) 
    pwordE.grid(row=2, column=1) 
 
    signupButton = Button(roots, text='Signup', command=FSSignup) 
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop() 








def FSSignup():
        global cursor,connecttodb
        
        name=nameE.get()
        pw=pwordE.get()
        email=email1.get()
        ema=str(email)
        print(ema)
        from datetime import datetime, timedelta

        date = datetime.now()


        valid_date = date + timedelta(days=3)


        date1=str(date)
        date2=str(valid_date)
        
        string="Login details  " + " \n username: " + name +"\n  password: " + pw + "\n validatidy period is from :" + date1 + "\n to: " + date2
        sender = 'technocratssdg4@gmail.com'
        receivers = [ema]

        message = """From: INTERNET WHITEBOARD<technocratsg4@gmail.com>
                    To: To Person <technocratesg4@gmail.com>
                        Subject: Welcome to INTERNET WHITEBOARD

                           Thankyou for signing up in internet white-board\n

                    """+ string
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()

        server.login('technocratssdg4@gmail.com','123456789techno')
        server.sendmail(sender, receivers, message)

        print ("Thanks for signing up, Check your mail for details")

       
        
        if type1=="employee":
             db()
             cursor.execute("""INSERT INTO login1(type,username,password,moderator,lok_flag)
                              VALUES(%s ,%s , %s, %s , %s )""",
                                               [type1,name,pw, "TRUE" , "FALSE"])
             connecttodb.commit()
             connecttodb.close()
             roots.destroy()
             
        if type1=="user":
             db()
             cursor.execute("""INSERT INTO login1(type,username,password,moderator,lok_flag)
                              VALUES(%s ,%s , %s, %s , %s )""",
                                               [type1,name,pw, "FALSE" , "FALSE"])
             connecttodb.commit()
             connecttodb.close()
             roots.destroy()
             



def buttons_regis():
        global rootw 
        rootw=Tk()
        rootw.title('INTERNET WHITEBOARD login')
        rootw.geometry('800x500')
        log = Button(rootw, text='login', command=Login) 
        log.grid(columnspan=2, sticky=W)
        rootw.configure(background='orange')
        



        rootw.mainloop()

def Login_admin():
    global A_name, A_pw , A_pw1 , A_name1
    rootw.destroy()
    root_admin=Tk()
    intruction = Label(root_admin, text='Please Login\n') 
    intruction.grid(sticky=E) 
 
    A_name = Label(root_admin, text='Username: ') 
    A_pw = Label(root_admin, text='Password: ') 
    A_name.grid(row=1, sticky=W)
    A_pw.grid(row=2, sticky=W)
 
    A_name1 = Entry(root_admin) 
    A_pw1 = Entry(root_admin, show='*')
    A_name1.grid(row=1, column=1)
    A_pw1.grid(row=2, column=1)
 
    loginB = Button(root_admin, text='Login', command=Login) 
    loginB.grid(columnspan=2, sticky=W)
    root_admin.mainloop()

def CheckLoginofadmin():
    global A_name1 , A_pw 
    name= A_name1.get()
    pw=A_pw1.get()
    if name=="admin" and pw=="admin":
        admin_page()
    


def doNothing():
    print("Adil")

def select_user_playback():
        global rootP,e2
        global cursor,connecttodb
        db()
        cursor.execute("""select username from login1""")
        users = cursor.fetchall()
        connecttodb.commit()
        connecttodb.close()

        rootP = Tk()  
        x=Text(rootP)
        x.insert(INSERT,"select the user to playback its modifications by entering it in the entry box below from the following list\n")
        for u in users:

            x.insert(INSERT,u)
            x.insert(INSERT,'\n')
        x.insert(END,"end")
        x.grid(row=0,column=1,rowspan=20)
        e2=Entry(rootP)
        e2.grid(row=20,column=1)
        Label(rootP,text="enter user name").grid(row=20)
        Button(rootP,text="select",command=user_playback).grid(row=21,column=2)
        Button(rootP,text="quit",command=quit_rootP).grid(row=22,column=2)
        rootP.title('select user')  
        
        rootP.mainloop()   
        
        
def quit_rootP():
        global rootP
        rootP.destroy()

def user_playback():
        global e2,play,root_admin,rootP
        root_admin.destroy()
        #rootP.destroy()
        print(e2.get())
        play=e2.get()
        print(play)
        create_widgets_foradmin()
        


def admin_page():
    global root_admin
    root_admin = Tk()
    root_admin.title('INTERNET WHITEBOARD ADMIN')
    root_admin.geometry('800x500')

    menu = Menu(root_admin)
    root_admin.configure(background='orange')
    root_admin.config(menu=menu)

    subMenu = Menu(menu)
    menu.add_cascade(label="Internet WhiteBoard", menu=subMenu)
    subMenu.add_command(label="Signout", command=signout_admin)
    subMenu.add_separator()
    
    clickMenu = Menu(menu)
    menu.add_cascade(label="Help", menu=clickMenu)
    clickMenu.add_command(label="About Us", command=info)
    frame = Frame(root_admin)
    frame.pack()
    printButton = Button(frame, text="select user to watch their playback", command=select_user_playback)
    printButton.pack(side=LEFT)


    printButton = Button(frame, text="Create Employee", command=register_as_emplo)
    printButton.pack(side=LEFT)

    printButton = Button(frame, text="Create User", command=register_as_user)
    printButton.pack(side=LEFT)


    root_admin.mainloop()





def Employee_page1():
    global root_employee
    #root_employee=root
    root_employee = Tk()
    root_employee.title('INTERNET WHITEBOARD EMPLOYEE')
    root_employee.geometry('800x500')

    menu = Menu(root_employee)
    root_employee.configure(background='orange')
    root_employee.config(menu=menu)

    subMenu = Menu(menu)
    menu.add_cascade(label="Internet WhiteBoard", menu=subMenu)
    #subMenu.add_command(label="Profile", command=doNothing)
    subMenu.add_command(label="Signout", command=signout_empl)
    subMenu.add_separator()
    
    clickMenu = Menu(menu)
    menu.add_cascade(label="Help", menu=clickMenu)
    clickMenu.add_command(label="About Us", command=info)
    frame = Frame(root_employee)
    frame.pack()

    printButton = Button(frame, text="Create User", command=register_as_user)
    printButton.pack(side=LEFT)

    printButton = Button(frame, text="START WHITEBOARD SESSION", command=create_widgets)
    printButton.pack(side=LEFT)


    root_employee.mainloop()


def info():
    
    rootB = Tk()  
    y=Text(rootB)
    y.insert(INSERT, "This is an internet whiteboard application.Upon start, the application will connect to a predefined admin server.                                                                            The IP address of the admin server is configurable, so users can change it at any time. There are three types of user accounts: a predefined admin account, employee account and customer accounts. The admin account can create the other type of accounts as well as modify critical aspects of the system.Employees can create customer accounts, configure and start whiteboard sessions. Customers can join existing sessions. When an account is created an e-mail is sent to the owner of the account with login details and validity period for the account. The user account is maintained in a SQL DB.A whiteboard session consists of a set of potentially unlimited number of users (participants) and a set of whiteboard sheets.Each user is running the application on their own device. A sheet is a display window whose contents are replicated on all devices in real-time. The participants can simultaneously draw and type text on the sheets. A set of standard shape drawing tools are  provided: line, arrow, circle, oval, square, rectangle, poly-line, text, eraser and free-drawing tool. For each tool, the user is able to select thickness, the drawing color and the filling color (just like in other drawing applications). For text, there is no thickness or filling color. Instead, the user selects the font, size and optionally a modifier such as italics and/or bold. The users can't undo changes or move shapes, but they can erase.One of the participants is designated as moderator. By default, this is the creator of the session. However, the creator can assign the moderator role to any participant. The moderator can lock access to a sheet (to prevent editing wars), sequentially undo modifications and change to a different sheet.Each modification is saved in a list stored on the admin server (preferably in a DB). The modification data consists of a index, a timestamp, the name of user that produced the modification, and the type of modification and on what sheet occurred. After a moderator has locked the whiteboard, it can undo modifications. The undo operation retrieves the last change from the list. It then redraws the same shape, but all in white so that is indistinguishable from the background. The next undo operations picks the next modification from the back of the list. The undo modification are also saved to the modification list (so that participants can see that theirwork has been undone). However, the undo modifications have a special status in the list. They cannot be modified by later undo operations.An undo operation always select the latest regular (not undo) operation.It is possible to save and reload the list of changes. When the list of changes is reloaded the whiteboard is cleared (all sheets). Then, a user is able to move sequentially through the modifications by clicking the mouse. For each click, the next modification from the list is added to the whiteboard and the modification timestamp and name of user responsible for it are shown. It is  also able to playback all modifications automatically by providing a delay between each modification shown.Certificates areused for each user as well as for the central server hosting the database. Certificates can be self-signed in the releaseto the customer. Encryption features provided by well-known libraries such as OpenSSL/LibreSSL, libcurl or standard Java/Pythonlibraries (for example, HttpsURLConnection, httplib.py, ssl.py)  are used. It is possible to restart the system with encryption disabled for debugging purposes.All interaction user-to-user and user-to-server are based on a RESTful API with JSON data encoding. Such an API is  easily testable by using HTTP(S)and the command-line utility curl, from the package libcurl.")
    y.insert(END,"end")
    y.pack()
    rootB.mainloop()
   
    



def signout_empl():

    global root_employee
    root_employee.destroy()
    buttons_regis()



def signout_user():

    global root_user
    root_user.destroy()
    buttons_regis()

def signout_admin():

    global root_admin
    root_admin.destroy()
    buttons_regis()



def user_page():
    global root_user
    #root_user=root


    root_user = Tk()

    root_user.title('INTERNET WHITEBOARD USER')
    root_user.geometry('800x500')
    root_user.configure(background='orange')


    menu = Menu(root_user)
    root_user.config(menu=menu)

    subMenu = Menu(menu)
    menu.add_cascade(label="Internet WhiteBoard", menu=subMenu)
    subMenu.add_command(label="Signout", command=signout_user)
    subMenu.add_separator()
    
    clickMenu = Menu(menu)
    menu.add_cascade(label="Help", menu=clickMenu)
    clickMenu.add_command(label="About Us", command=info)
    frame = Frame(root_user)
    frame.pack()

    printButton = Button(frame, text="JOIN SESSION", command=create_widgets_foruser)
    printButton.pack(side=LEFT)
    root_user.mainloop()    











def CheckLogin():
    global nam , typeofcustomer,root_employee
    nam=nameEL.get()
    pws=pwordEL.get()
    types= str("user")
    typese=str("employee")
    


    global cursor,connecttodb
    db()
    cursor.execute("""select username , password from login1 where type = %s and username = %s and password = %s""",[types,nam,pws])
    row1 = cursor.fetchone()
    connecttodb.commit()
    connecttodb.close()
    
    if row1 is not None:
    
        print("user")
        typeofcustomer="user"
        db()
        cursor.execute("""select username , password from login1 where username = %s and password = %s """,[nam,pws])
        row = cursor.fetchone()
        connecttodb.commit()
        connecttodb.close()
    

        if row is not None:
            print("login success")
            print(row)
            print(nam)
            
            db()
            cursor.execute("""select moderator from login1 where username=%s""",[nam]
                                               )
            mode=cursor.fetchone()
            print(mode)
            connecttodb.commit()
        
            connecttodb.close()
            if mode==('FALSE',):
                mod="FALSE"
                print("login success")
                print(row)
                print(nam)
                rootA.destroy()
                user_page()
            else:
                mod= "TRUE"
                print("login success")
                print(row)
                print(nam)
                rootA.destroy()
                Employee_page1()
            
        
        
        else:
            r = Tk()
            r.title('D:')
            r.geometry('150x50')
            rlbl = Label(r, text='\n[!] Invalid Login')
            rlbl.pack()
            r.mainloop()

    if row1 == None:
    
        print("not user")
        typeofcustomer="employee"
        db()
        cursor.execute("""select username , password from login1 where username = %s and password = %s """,[nam,pws])
        row = cursor.fetchone()
        connecttodb.commit()
        connecttodb.close()
    

        if row is not None:
            print("login success")
            print(row)
            print(nam)
            db()
            cursor.execute("""select moderator from login1 where username=%s""",[nam]
                                               )
            mode=cursor.fetchone()
            print(mode)
            connecttodb.commit()
        
            connecttodb.close()
            if mode==('FALSE',):
                mod="FALSE"
                print("login success")
                print(row)
                print(nam)
                rootA.destroy()
                user_page()
            else:
                mod= "TRUE"
                print("login success")
                print(row)
                print(nam)
                rootA.destroy()
                Employee_page1()
        
        
        else:
            if nam=="admin" and pws== "admin":
                rootA.destroy()
                admin_page()
            else:
                r = Tk()
                r.title('D:')
                r.geometry('150x50')
                rlbl = Label(r, text='\n[!] Invalid Login')
                rlbl.pack()
                r.mainloop()







buttons_regis()

