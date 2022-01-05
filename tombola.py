import time
import random
import re
import tkinter as tk
import os
root=tk.Tk()
root.title("tambola")
logo3= tk.PhotoImage(file="tambola.png")
root.configure(background="yellow")
scrollbar = tk.Scrollbar(root,
                         bg="black")
scrollbar.pack(side="right", fill="y")
SScrollbar = tk.Scrollbar(root)
SScrollbar.pack(side="bottom", fill="x")
frame=tk.Frame(root,
               background="navy",
               width=200)
frame.pack()
logo = tk.PhotoImage(file="label_with_image.png")
def o987():
    dict1={}
    q32=open("dict1.txt","r+")
    q33=list(q32)
    for i in range(0,len(q33),5):
        p4=re.sub("\n","",q33[i])
        p5=re.sub("\n","",q33[i+1])
        p6=re.sub("\n","",q33[i+2])
        p7=re.sub("\n","",q33[i+3])
        p8=re.sub("\n","",q33[i+4])
        dict1[p4]=[p5,p6,p7,p8]
    root2=tk.Tk()
    root2.configure(bg="sky blue")
    frame2=tk.Frame(root,bg="sky blue")
    frame2.pack()
    w167=tk.Label(root2,text="Welcome to sign up page\n\n",font=["times new roman",29,"bold"],fg="blue",bg="sky blue")
    w167.pack()
    w168=tk.Label(root2,text="Enter your first name",font=["times new roman",22,"bold"],fg="blue",bg="sky blue")
    w168.pack()
    e667=tk.Entry(root2,font=["times new roman",22,"bold"])
    e667.pack()
    w169=tk.Label(root2,text="Enter your last name",font=["times new roman",22,"bold"],fg="blue",bg="sky blue")
    w169.pack()
    e666=tk.Entry(root2,font=["times new roman",22,"bold"])
    e666.pack()
    w198=tk.Label(root2,text="Enter your email",font=["times new roman",22,"bold"],fg="blue",bg="sky blue")
    w198.pack()
    e616=tk.Entry(root2,font=["times new roman",22,"bold"])
    e616.pack()
    w170=tk.Label(root2,text="Enter your username",font=["times new roman",22,"bold"],fg="blue",bg="sky blue")
    w170.pack()
    e668=tk.Entry(root2,font=["times new roman",22,"bold"])
    e668.pack()
    w171=tk.Label(root2,text="enter your password",font=["times new roman",22,"bold"],fg="blue",bg="sky blue")
    w171.pack()
    e669=tk.Entry(root2,font=["times new roman",22,"bold"],show="*" )
    e669.pack()
    w172=tk.Label(root2,text="enter your mobile number",font=["times new roman",22,"bold"],fg="blue",bg="sky blue")
    w172.pack()
    e670=tk.Entry(root2,font=["times new roman",22,"bold"])
    e670.pack()
    def o173():
        q36=open("dict1.txt","a+")
        a=str(e668.get())
        b=str(e669.get())
        c=str(e667.get())+" "+str(e666.get())
        d=str(e616.get())
        e=str(e670.get())
        if a in dict1.keys():
            w175=tk.Label(root2,text="the username already exists",font=["times new roman",22,"bold"],fg="blue",bg="sky blue")
            w175.pack()
        else:
            q36.write("\n"+a)
            q36.write("\n"+b)
            q36.write("\n"+c)
            q36.write("\n"+d)
            q36.write("\n"+e)
            dict1[a]=[b,c,d,e]
            w580=tk.Label(root2,text="your account has been created")
            w580.pack()
            root2.destroy()
            
    w174=tk.Checkbutton(root2,text="I hereby declare that the above details are correct and verified",font=["times new roman",21,"bold"],fg="blue",bg="sky blue")
    w174.pack()
    w173=tk.Button(root2,text="submit",command=o173,fg="blue",bg="sky blue",font=["times new roman",19,"bold"])
    w173.pack()
    
    
def o99():
    gt6=str(e126.get())
    gt7=e129.get()
    dict2={}
    q34=open("dict1.txt","r")
    q35=list(q34)
    for i in range(0,len(q35),5):
        p1=re.sub("\n","",q35[i])
        p2=re.sub("\n","",q35[i+1])
        p3=re.sub("\n","",q35[i+2])
        p9=re.sub("\n","",q35[i+3])
        p10=re.sub("\n","",q35[i+4])
        dict2[p1]=[p2,p3,p9,p10]
    if gt6 in dict2.keys():
        if gt7==(dict2.get(gt6))[0]:
            q3="welcome "+str((dict2.get(gt6))[1])
            w98.destroy()
            w99.destroy()
            w123.destroy()
            w124.destroy()
            e126.destroy()
            e129.destroy()
            w45.destroy()
            butt=tk.Label(frame,
                           text="WELCOME TO FUNBOLA",
                           image=logo3,
                           compound="left",
                           fg="yellow",justify="center",
                           bg="teal",
                           bd=0,
                           font=["Times New Roman",40,"bold","italic","underline"])
            butt.pack(side="top")
            def o56():
                root3=tk.Tk()
                root3.configure(bg="black")
                a=random.randrange(1,10)
                e=random.randrange(10,100)
                f=random.randrange(10,100)
                c=random.randrange(65,91)
                d=random.randrange(97,123)
                h6=str(a)+str(chr(c))+str(e)+str(chr(d))
                h7="enter the capta code "+h6
                w158=tk.Label(root3,text=h7,font=["times new roman",27,"bold"],bg="black",fg="white")
                w158.pack()
                w136=tk.Entry(root3,font=["times new roman",24,"bold"],bg="black",fg="white")
                w136.pack()
                def o113():
                    if w136.get()==h6:
                        w768=tk.Label(root3,text="verified successfully",font=["times new roman",24,"bold"],bg="black",fg="white")
                        w768.pack()
                        def o333():
                            w158.destroy()
                            w136.destroy()
                            w768.destroy()
                            w113.destroy()
                            w333.destroy()
                            w890=tk.Label(root3,text="your profile info \n\n",font=["times new roman",30,"bold"],bg="black",fg="white")
                            w890.pack()
                            dict3={}
                            q36=open("dict1.txt","r")
                            q37=list(q36)
                            for i in range(0,len(q37),5):
                                p1=re.sub("\n","",q37[i])
                                p2=re.sub("\n","",q37[i+1])
                                p3=re.sub("\n","",q37[i+2])
                                p9=re.sub("\n","",q37[i+3])
                                p10=re.sub("\n","",q37[i+4])
                                dict3[p1]=[p2,p3,p9,p10]
                                g6="your name: "+str((dict2.get(gt6))[1])
                                g7="your email: "+str((dict2.get(gt6))[2])
                                g8="your phone number: "+str((dict2.get(gt6))[3])   
                            w456=tk.Label(root3,text=g6,font=["times new roman",30,"bold"],bg="black",fg="white")
                            w456.pack()
                            w457=tk.Label(root3,text=g7,font=["times new roman",30,"bold"],bg="black",fg="white")
                            w457.pack()
                            w458=tk.Label(root3,text=g8,font=["times new roman",30,"bold"],bg="black",fg="white")
                            w458.pack()
                        w333=tk.Button(root3,text="proceed",command=o333,font=["chiller",20,"bold"],bg="black",fg="white")
                        w333.pack()
                        
                    else:
                        w768=tk.Label(root3,text="invalid capta",font=["chiller",24,"bold"],bg="black",fg="white")
                        w768.pack()
                w113=tk.Button(root3,text="submit",command=o113,font=["chiller",20,"bold"],bg="black",fg="white")
                w113.pack()
            vty=tk.Button(frame,text=q3,font=["mangal",10,"bold"],bg="navy",relief="sunken",bd=0,fg="white",command=o56)
            vty.pack()
            w134=tk.Label(root,text="enter the question file",justify="center",font=["chiller",30,"bold"],bg="light blue")
            w134.pack()
            e10=tk.Entry(root,justify="center",font=["mangal",15,"bold"],bg="cyan",width=22)
            e10.pack()
            w135=tk.Label(root,text="enter the answer file",justify="center",font=["chiller",30,"bold"],bg="light blue")
            w135.pack()
            e11=tk.Entry(root,justify="center",font=["mangal",15,"bold"],bg="cyan",width=22)
            e11.pack()

            w1051 = tk.Label(root,
                          image=logo,
                            text="python",
                           compound="top")
            w1051.pack(side="right")
            w1052 = tk.Label(root,
                          image=logo,
                           text="python",
                           compound="top")
            w1052.pack(side="left")
            z=[]
            x=[]
            n=[]
            m=["breakfast","lunch","dinner","first row","second row","bottom row","corners"]
            k=0
                
            def o12(self):
                fn=e10.get()
                file=fn+".txt"
                f=open(file,"r")
                lines=list(f)
                e10.destroy()
                fn1=e11.get()
                file1=fn1+".txt"
                v=open(file1,"r")
                lines1=list(v)
                e11.destroy()
                w134.destroy()
                w135.destroy()
                but.destroy()
                l=list(range(0,len(lines)+1))
                print(len(l))
                listbox=tk.Listbox(root,
                                   width=90,
                                   height=50,
                                   bg="navy",
                                   font=["Times New Roman",20,"italic"],
                                   fg="orange")
                listbox.pack()
                listbox.config(yscrollcommand=scrollbar.set)
                scrollbar.config(command=listbox.yview)
                listbox.config(xscrollcommand=SScrollbar.set)
                SScrollbar.config(command=listbox.xview)
                def o3(self):
                    m.remove("breakfast")
                    root1=tk.Tk()
                    frame1=tk.Frame(root1)
                    frame1.pack()
                    w37=tk.Label(root1,text="enter the no.s seperated with space",font=["times new roman",18,"bold","italic"])
                    w37.pack()
                    e=tk.Entry(root1,font=["times new roman",18,"bold","italic"])
                    e.pack()
                    e.focus_set()
                    def quite():
                        root1.destroy()
                    e1=e.get().split()
                    vte=tk.Button(frame1,text="quit",
                                  command=quite,font=["times new roman",18,"bold","italic"])
                    vte.pack(side="right")
                    def value():
                        d=0
                        for i in range(0,len(e1)):
                            q=(e1[i])
                            x.append(q)
                            if q in z:
                                d+=1
                        if d == len(x):
                            w85=tk.Label(root1,text="okay",font=["times new roman",18,"bold","italic"])
                            w85.pack()
                            listbox.insert("end","breakfast is done")

                        else:
                            w86=tk.Label(root1,text="value is missing \n Check from these",font=["times new roman",18,"bold","italic"])
                            w86.pack()
                            w87=tk.Label(root1,text=z,justify="top")
                            w87.pack()
                    vt=tk.Button(frame1,text="check",font=["times new roman",18,"bold","italic"],
                                     command=value)
                    vt.pack(side="right")
                    
                def o4(self):
                    m.remove("lunch")
                    root1=tk.Tk()
                    frame1=tk.Frame(root1)
                    frame1.pack()
                    w37=tk.Label(root1,text="enter the no.s seperated with space",font=["times new roman",18,"bold","italic"])
                    w37.pack(side="top")
                    e=tk.Entry(root1,font=["times new roman",18,"bold","italic"])
                    e.pack()
                    e.focus_set()
                    def quite():
                        root1.destroy()
                    e1=e.get().split()
                    vte=tk.Button(frame1,text="quit",font=["times new roman",18,"bold","italic"],
                                  command=quite)
                    vte.pack(side="right")
                    def value():
                        e1=e.get().split()
                        print(e1)
                        print(z)
                        c=0
                        for i in range(0,len(e1)):
                            q=(e1[i])
                            x.append(q)
                            if q in z:
                                c+=1
                        if c == len(x):
                            w85=tk.Label(root1,text="okay",font=["times new roman",18,"bold","italic"])
                            w85.pack()
                            listbox.insert("end","lunch is done")
                        else:
                            w86=tk.Label(root1,text="value is missing \n Check from these",font=["times new roman",18,"bold","italic"])
                            w86.pack()
                            w87=tk.Label(root1,text=z)
                            w87.pack()
                    vt=tk.Button(frame1,text="check",font=["times new roman",18,"bold","italic"],
                                     command=value)
                    vt.pack(side="left")

                def o5(self):
                    m.remove("dinner")
                    root1=tk.Tk()
                    frame1=tk.Frame(root1)
                    frame1.pack()
                    w37=tk.Label(root1,text="enter the no.s seperated with space",font=["times new roman",18,"bold","italic"])
                    w37.pack(side="top")
                    e=tk.Entry(root1)
                    e.pack()
                    e.focus_set()
                    def quite():
                        root1.destroy()
                    e1=e.get().split()
                    vte=tk.Button(frame1,text="quit",font=["times new roman",18,"bold","italic"],
                                  command=quite)
                    vte.pack(side="right")
                    def value():
                        e1=e.get().split()
                        print(e1)
                        print(z)
                        t=0
                        for i in range(0,len(e1)):
                            q=(e1[i])
                            x.append(q)
                            if q in z:
                                t+=1
                        if t == len(x):
                            w85=tk.Label(root1,text="okay",font=["times new roman",18,"bold","italic"])
                            w85.pack()
                            listbox.insert("end","dinner is done")
                        else:
                            w86=tk.Label(root1,text="value is missing \n Check from these",font=["times new roman",18,"bold","italic"])
                            w86.pack()
                            w87=tk.Label(root1,text=z)
                            w87.pack()
                    vt=tk.Button(frame1,text="check",font=["times new roman",18,"bold","italic"],
                                     command=value)
                    vt.pack(side="left")
                def o6(self):
                    m.remove("first row")
                    root1=tk.Tk()
                    frame1=tk.Frame(root1)
                    frame1.pack()
                    w37=tk.Label(root1,text="enter the no.s seperated with space",font=["times new roman",18,"bold","italic"])
                    w37.pack(side="top")
                    e=tk.Entry(root1)
                    e.pack()
                    e.focus_set()
                    def quite():
                        root1.destroy()
                    e1=e.get().split()
                    vte=tk.Button(frame1,text="quit",font=["times new roman",18,"bold","italic"],
                                  command=quite)
                    vte.pack(side="right")
                    def value():
                        e1=e.get().split()
                        print(e1)
                        print(z)
                        y=0
                        for i in range(0,len(e1)):
                            q=(e1[i])
                            x.append(q)
                            if q in z:
                                y+=1
                        if y == len(x):
                            w85=tk.Label(root1,text="okay",font=["times new roman",18,"bold","italic"])
                            w85.pack()
                            listbox.insert("end","first row")
                        else:
                            w86=tk.Label(root1,text="value is missing \n Check from these",font=["times new roman",18,"bold","italic"])
                            w86.pack()
                            w87=tk.Label(root1,text=z)
                            w87.pack()
                    vt=tk.Button(frame1,text="check",font=["times new roman",18,"bold","italic"],
                                     command=value)
                    vt.pack(side="left")
                def o7(self):
                    m.remove("second row")
                    root1=tk.Tk()
                    frame1=tk.Frame(root1)
                    frame1.pack()
                    w37=tk.Label(root1,text="enter the no.s seperated with space",font=["times new roman",18,"bold","italic"])
                    w37.pack(side="top")
                    e=tk.Entry(root1)
                    e.pack()
                    e.focus_set()
                    def quite():
                        root1.destroy()
                    e1=e.get().split()
                    vte=tk.Button(frame1,text="quit",font=["times new roman",18,"bold","italic"],
                                  command=quite)
                    vte.pack(side="right")
                    def value():
                        e1=e.get().split()
                        print(e1)
                        print(z)
                        u=0
                        for i in range(0,len(e1)):
                            q=(e1[i])
                            x.append(q)
                            if q in z:
                                u+=1
                        if u == len(x):
                            w85=tk.Label(root1,text="okay",font=["times new roman",18,"bold","italic"])
                            w85.pack()
                            listbox.insert("end","second row")
                        else:
                            w86=tk.Label(root1,text="value is missing \n Check from these",font=["times new roman",18,"bold","italic"])
                            w86.pack()
                            w87=tk.Label(root1,text=z)
                            w87.pack()
                    vt=tk.Button(frame1,text="check",font=["times new roman",18,"bold","italic"],
                                     command=value)
                    vt.pack(side="left")
                def o8(self):
                    m.remove("bottom row")
                    root1=tk.Tk()
                    frame1=tk.Frame(root1)
                    frame1.pack()
                    w37=tk.Label(root1,text="enter the no.s seperated with space",font=["times new roman",18,"bold","italic"])
                    w37.pack(side="top")
                    e=tk.Entry(root1)
                    e.pack()
                    e.focus_set()
                    def quite():
                        root1.destroy()
                    e1=e.get().split()
                    vte=tk.Button(frame1,text="quit",font=["times new roman",18,"bold","italic"],
                                  command=quite)
                    vte.pack(side="right")
                    def value():
                        e1=e.get().split()
                        print(e1)
                        print(z)
                        o=0
                        for i in range(0,len(e1)):
                            q=(e1[i])
                            x.append(q)
                            if q in z:
                                o+=1
                        if o == len(x):
                            w85=tk.Label(root1,text="okay",font=["times new roman",18,"bold","italic"])
                            w85.pack()
                            listbox.insert("end","botom row")
                        else:
                            w86=tk.Label(root1,text="value is missing \n Check from these",font=["times new roman",18,"bold","italic"])
                            w86.pack()
                            w87=tk.Label(root1,text=z)
                            w87.pack()
                    vt=tk.Button(frame1,text="check",font=["times new roman",18,"bold","italic"],
                                     command=value)
                    vt.pack(side="left")
                def o9(self):
                    m.remove("corners")
                    root1=tk.Tk()
                    frame1=tk.Frame(root1)
                    frame1.pack()
                    w37=tk.Label(root1,text="enter the no.s seperated with space",font=["times new roman",18,"bold","italic"])
                    w37.pack(side="top")
                    e=tk.Entry(root1)
                    e.pack()
                    e.focus_set()
                    def quite():
                        root1.destroy()
                    e1=e.get().split()
                    vte=tk.Button(frame1,text="quit",font=["times new roman",18,"bold","italic"],
                                  command=quite)
                    vte.pack(side="right")
                    def value():
                        e1=e.get().split()
                        print(e1)
                        print(z)
                        g=0
                        for i in range(0,len(e1)):
                            q=(e1[i])
                            x.append(q)
                            if q in z:
                                g+=1
                        if g == len(x):
                            w85=tk.Label(root1,text="okay",font=["times new roman",18,"bold","italic"])
                            w85.pack()
                            listbox.insert("end","corners")
                        else:
                            w86=tk.Label(root1,text="value is missing \n Check from these",font=["times new roman",18,"bold","italic"])
                            w86.pack()
                            w87=tk.Label(root1,text=z)
                            w87.pack()
                    vt=tk.Button(frame1,text="check",font=["times new roman",18,"bold","italic"],
                                     command=value)
                    vt.pack(side="left")
                def o2(self):
                    
                    a=random.choice(l)
                    l.remove(a)
                    n.append(a)
                    listbox.insert("end",lines[a])
                    c=n[-1]
                    p=re.sub("\n","",lines1[c])
                    z.append(p)
                    os.system("rules.txt")
                def o45(self):
                    
                    a=random.choice(l)
                    l.remove(a)
                    n.append(a)
                    listbox.insert("end",lines[a])
                    c=n[-1]
                    p=re.sub("\n","",lines1[c])
                    z.append(p)
                
                def o11(self):
                    b=n[-1]
                    listbox.insert("end","answer is ",lines1[b])
                def o10():
                    k=var.get()
                    if k==1:
                        listbox.insert("end",m)
                    else:
                        pass
                def o100(self):
                    listbox.insert("end",z)
                    print(len(z))
                def o1000(self):
                    root.destroy()
                button=tk.Button(frame,
                                  text="Click to start-press k",
                                  fg="red",width=17,
                                 bg="cyan",underline=4,
                                 bd=0,
                                 font=["times new roman",17,"bold"],
                                  command=o2)
                button.pack()
                root.bind('k',o2)
                root.bind('<Button-1>',o2)

                button1=tk.Button(frame,
                                  text="Next-press n",width=17,
                                  fg="magenta",
                                  bg="cyan",bd=0,underline=0,
                                  font=["times new roman",17,"bold"],
                                  command=o45)
                button1.pack(side="top")
                root.bind('n',o45)
                root.bind('<Button-1>',o45)
                button10=tk.Button(frame,
                                   text="Answer-press a",
                                   fg="red",underline=0,
                                   bg="cyan",bd=0,width=17,
                                   font=["times new roman",17,"bold"],
                                   command=o11)
                button10.pack(side="top")
                root.bind('a',o11)
                root.bind('<Button-1>',o11)
                button100=tk.Button(frame,
                                   text="View No.s-press v",
                                   fg="red",underline=0,
                                   bg="cyan",bd=0,width=17,
                                   font=["times new roman",17,"bold"],
                                   command=o100)
                button100.pack(side="top")
                root.bind('v',o100)
                root.bind('<Button-1>',o100)
                button1000=tk.Button(frame,
                                   text="Exit-press Esc",
                                   fg="red",
                                   bg="cyan",bd=0,width=17,
                                   font=["times new roman",17,"bold"],
                                   command=o1000)
                button1000.pack(side="top")
                root.bind("<Escape>",o1000)
                root.bind('<Button-1>',o1000)
                button2=tk.Button(frame,
                                  text="Breakfast \n press b",
                                  fg="green",underline=0,
                                  bg="black",bd=0,width=9,
                                  activebackground="orange",
                                  activeforeground="black",
                                  font=["times new roman",17,"bold"],
                                  command=o3)
                button2.pack(side="right")
                root.bind('b',o3)
                root.bind('<Button-1>',o3)
                button3=tk.Button(frame,
                                  text="Lunch \n press l",
                                  fg="green",underline=0,
                                  bg="black",bd=0,width=9,
                                  activebackground="orange",
                                  activeforeground="black",
                                  font=["times new roman",17,"bold"],
                                  command=o4)
                button3.pack(side="right")
                root.bind('l',o4)
                root.bind('<Button-1>',o4)
                button4=tk.Button(frame,
                                  text="Dinner \n press d",
                                  fg="green",underline=0,
                                  bg="black",bd=0,
                                  activebackground="orange",width=8,
                                  activeforeground="black",
                                  font=["times new roman",17,"bold"],
                                  command=o5)
                button4.pack(side="right")
                root.bind('d',o5)
                root.bind('<Button-1>',o5)
                button5=tk.Button(frame,
                                  text="First row \n press f",
                                  fg="green",underline=0,
                                  bg="black",bd=0,width=9,
                                  activebackground="orange",
                                  activeforeground="black",
                                  font=["times new roman",17,"bold"],
                                  command=o6)
                button5.pack(side="left")
                root.bind('f',o6)
                root.bind('<Button-1>',o6)
                button6=tk.Button(frame,
                                  text="Second row \n press s",
                                  fg="green",bd=0,underline=0,
                                  bg="black",width=11,
                                  activebackground="orange",
                                  activeforeground="black",
                                  font=["times new roman",17,"bold"],
                                  command=o7)
                button6.pack(side="left")
                root.bind('s',o7)
                root.bind('<Button-1>',o7)
                button7=tk.Button(frame,
                                  text="Bottom row \n press o",
                                  fg="green",bd=0,underline=1,
                                  bg="black",width=11,
                                  activebackground="orange",
                                  activeforeground="black",
                                  font=["times new roman",17,"bold"],
                                  command=o8)
                button7.pack(side="left")
                root.bind('o',o8)
                root.bind('<Button-1>',o8)
                button8=tk.Button(frame,
                                  text="Corners \n press c",
                                  fg="green",width=8,
                                  bg="black",bd=0,underline=0,
                                  activebackground="orange",
                                  activeforeground="black",
                                  font=["times new roman",17,"bold"],
                                  command=o9)
                button8.pack(side="left")
                root.bind('c',o9)
                root.bind('<Button-1>',o9)
                var=tk.IntVar()
                button9=tk.Checkbutton(frame,
                                  text="remaining positions",
                                  fg="green",
                                  bg="black",
                                       bd=0,
                                    activebackground="orange",
                                  activeforeground="black",height=2,
                                  font=["times new roman",17,"bold"],
                                    command=o10,
                                    onvalue=1,
                                    offvalue=0,
                                    variable=var)
                button9.pack(side="left")
            
            but=tk.Button(root,text="submit",command=o12,justify="center",font=["chiller",20,"bold"],activebackground="red",width=10,bg="light blue")
            but.pack()
            root.bind('<Return>',o12)
        elif gt7!=(dict2.get(gt6))[0]:
            w245=tk.Label(root,text="password is wrong",justify="center")
            w245.pack()
            def o1000():
                w245.destroy()
            root.after(3000,o1000)
    elif gt6 not in dict2.keys():
        w255=tk.Label(root,text="account does not exist",justify="center")
        w255.pack()
        def o1001():
                w255.destroy()
        root.after(3000,o1001)
        
w98=tk.Label(root,text="Welcome to Fungames\n\n\n",image=logo3,compound="right",font=["times new roman",29,"bold"],bg="yellow",fg="red")
w98.pack(side="top")
w123=tk.Label(root,justify="center",text="enter the username",font=["times new roman",22,"bold"],bg="yellow")
w123.pack()
e126=tk.Entry(root,justif="center",font=["times new roman",19,"bold"])
e126.pack()
w124=tk.Label(root,text="enter the password",justify="center",font=["times new roman",22,"bold"],bg="yellow")
w124.pack()
e129=tk.Entry(root,justify="center",font=["times new roman",19,"bold"],show="*")
e129.pack()
w99=tk.Button(root,text="enter",command=o99,font=["times new roman",17,"bold"],bg="yellow")
w99.pack()
w45=tk.Button(root,text="sign up for free",command=o987,justify="center",font=["times new roman",17,"bold"],bg="yellow")
w45.pack()
tk.mainloop()
