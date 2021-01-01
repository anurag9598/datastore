from tkinter import *
import sqlite3 as sql

class DATA_STORE:
    def __init__(s):
        s.client=sql.connect('‪user.db')
        s.cu=s.client.cursor()
        s.Start()


    def Start(s):
        try:
            s.root.destroy()
        except:
            pass
        s.root = Tk()
        s.root.geometry('1200x600+0+0')#widthxheight+x+y
        s.root.config(bg='aqua')

        canvas = Canvas(s.root, width =800, height=900)      
        canvas.pack()      
        img = PhotoImage(file="F:\db.gif")      
        canvas.create_image(150,150,anchor=NW, image=img)
        T = Label(s.root,text='BROWSER',font=('Verdana',30,'bold'))
        b = Button(s.root,bg="grey",fg="aqua",relief='ridge',state="active",text='START..',font=('',15,'italic'),command=lambda:s.Browser())
        b.place(x=670,y=375)
        T.place(x=400,y=380)
        s.root.mainloop()

    def Browser(s):
        try:
            s.root.destroy()
        except:
            pass
        s.root = Tk()
        s.root.geometry('1200x600+0+0')#widthxheight+x+y
        s.root.config(bg='aqua')
        l = Label(s.root,bg='grey',font=('times',30,'bold'),text='Welcome to Sqlite3 browser')
        l.pack(side=TOP,fill=X)
        Open = Button(s.root,bg="grey",fg="aqua",relief='sunken',state="active",text='Open',font=('times',20,'italic'),command=lambda:s.func())                
        Open.place(x=160,y=60)
        fm.place(x=336,y=60)
        Create = Button(s.root,bg="grey",fg="aqua",relief='sunken',state="active",text='Create',font=('times',20,'italic'),command=lambda:s.cfunc())
        Create.place(x=550,y=60)
        Del = Button(s.root,bg="grey",fg="aqua",relief='sunken',state="active",text='Delete',font=('times',20,'italic'))
        Del.place(x=960,y=60)


        c=Canvas(s.root,bg='white',width=600,height=420)
        c.place(x=500,y=120)
        Exe = Button(s.root,bg="grey",fg="aqua",relief='raised',state="active",text='Execute',font=('times',15,'italic'))
        Exe.place(x=450,y=560)
        Search=Entry(s.root,font=('Georgia',15,'bold'))
        Search.place(x=550,y=560)
        Go = Button(s.root,bg="grey",fg="aqua",relief='raised',state="active",text='Go',font=('times',15,'italic'))
        Go.place(x=850,y=560)  
        Exit = Button(s.root,bg="grey",fg="aqua",relief='groove',state="active",text='Exit',font=('times',15,'italic'),command=lambda:s.root.destroy())
        Exit.place(x=980,y=560)
        s.root.mainloop()

    def func(s):#To show tables in database
         con = sql.connect('user.db')
         cursorObj = con.cursor()
         cursorObj.execute('SELECT name from sqlite_master where type= "table"')

         l=cursorObj.fetchall()
         for i in range(len(l)):
            Table=Button(s.root,bg='grey',fg="aqua",relief='raised',state="active",font=('times',20,'bold'))
            Table.config(text=str(*(l[:][i])))
            Table.place(x=10,y=i+200)
            Table.config(command=lambda:s.tfunc())
            
    def tfunc(s):#To show data of employees table 
            con = sql.connect('user.db')
            cursorObj = con.cursor()
            cursorObj.execute('SELECT * FROM employees')
            rows = cursorObj.fetchall()
            for row in rows:
                    Content=Label(s.root,bg='grey',font=('verdana',15,'bold'))
                    Content.config(text=row)
                    Content.place(x=550,y= 180+len(row))
                    
    def ttfunc(s):#for other tables ....
            con = sql.connect('user.db')
            cursorObj = con.cursor()
            cursorObj.execute('SELECT name from sqlite_master where type= "table"')
            l=cursorObj.fetchall()
            for i in l:
                cursorObj.execute('SELECT * FROM '+str(*i))
                rows = cursorObj.fetchall()
                for row in rows:
                    Content=Label(s.root,bg='grey',font=('verdana',15,'bold'))
                    Content.config(text=row)
                    Content.place(x=550,y= 300+len(row))
        
  
    def cfunc(s):#for creating new table
        con = sql.connect('user.db')
        cursorObj = con.cursor()
        B1 =Entry(s.root,bg='gray65',show ="",relief='raised',width='30')
        B1.place(x=500,y=400)
        v=B1.get()
        cursorObj.execute("CREATE TABLE"+str(v)+"(id integer PRIMARY KEY, name text, salary real, department text, position text, HireDate text)")
        con.commit()
        s.root.mainloop()
        
    def hello():
           tkMessageBox.showinfo("ENTER NAME OF TABLE:")

           
DATA_STORE()


     







