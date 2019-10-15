from tkinter import *

import admin_b

def search_admin1_text():
    admin_b.search_admin1(trainnumber_text.get(), name_text.get())
    list1.delete(0, END)
    for rows_search in admin_b.search_admin1(trainnumber_text.get(),name_text.get()):
        list1.insert(END, rows_search)

def view_admin1_text():
    list1.delete(0, END)
    for rows_view in admin_b.view_admin1():
        list1.insert(END,rows_view)

def insert_admin1_text():
    admin_b.insert_admin1(trainnumber_text.get(),name_text.get(),age_text.get(),gender_text.get(),aadharnumber_text.get(),nationality_text.get(),source_text.get(),destination_text.get(),foodservice_text.get(),berthpreference_text.get(),coach_text.get(),departuretime_text.get(),arrivaltime_text.get())
    list1.delete(0, END)
    list1.insert(END,trainnumber_text.get(),name_text.get(),age_text.get(),gender_text.get(),aadharnumber_text.get(),nationality_text.get(),source_text.get(),destination_text.get(),foodservice_text.get(),berthpreference_text.get(),coach_text.get(),departuretime_text.get(),arrivaltime_text.get())



window=Tk()

window.configure(bg="light pink")

l0=Label(window,text="ONLINETRAINBOOKING",bg="white",fg="red",font="Times 18 ")
l0.grid(row=0,column=1)

l1=Label(window,text="name",bg="white",fg="purple",font=" Gabriola 16 ")
l1.grid(row=1,column=1)

l2=Label(window,text="age",bg="white",fg="purple",font=" Gabriola  16 ")
l2.grid(row=2,column=1)

l3=Label(window,text="gender",bg="white",fg="purple",font=" Gabriola  16 ")
l3.grid(row=3,column=1)

l4=Label(window,text="aadharnumber",bg="white",fg="purple",font="Gabriola  16 ")
l4.grid(row=4,column=1)

l5=Label(window,text="nationality",bg="white",fg="purple",font="Gabriola  16 ")
l5.grid(row=5,column=1)

l6=Label(window,text="source",bg="white",fg="purple",font=" Gabriola 16" )
l6.grid(row=6,column=1)

l7=Label(window,text="destination",bg="white",fg="purple",font=" Gabriola 16 ")
l7.grid(row=7,column=1)

l8=Label(window,text="foodservice",bg="white",fg="purple",font="Gabriola  16 ")
l8.grid(row=8,column=1)

l9=Label(window,text="berthpreference",bg="white",fg="purple",font="Gabriola 16")
l9.grid(row=9,column=1)

l10=Label(window,text="coach",bg="white",fg="purple",font="Gabriola 16")
l10.grid(row=10,column=1)

l11=Label(window,text="departuretime",bg="white",fg="purple",font="Gabriola 16" )
l11.grid(row=11,column=1)

l12=Label(window,text="arrivaltime",bg="white",fg="purple",font="Gabriola 16 ")
l12.grid(row=12,column=1)

l13 = Label(window, text="trainnumber", bg="white", fg="purple", font="Gabriola 16 ")
l13.grid(row=13, column=1)


name_text =StringVar()
e1=Entry(window,textvariable=name_text,bg="white",fg="green",font=" Gabriola 16")
e1.grid(row=1,column=2)

age_text =StringVar()
e2=Entry(window,textvariable=age_text,bg="white",fg="green",font=" Gabriola 16")
e2.grid(row=2,column=2)

gender_text =StringVar()
e3=Entry(window,textvariable=gender_text,bg="white",fg="green",font=" Gabriola 16")
e3.grid(row=3,column=2)

aadharnumber_text =IntVar()
e4=Entry(window,textvariable=aadharnumber_text,bg="white",fg="green",font=" Gabriola 16")
e4.grid(row=4,column=2)

nationality_text =StringVar()
e5=Entry(window,textvariable=nationality_text,bg="white",fg="green",font=" Gabriola 16")
e5.grid(row=5,column=2)

source_text= StringVar()
e6=Entry(window,textvariable=source_text,bg="white",fg="green",font=" Gabriola 16",)
e6.grid(row=6,column=2)

destination_text= StringVar()
e7=Entry(window,textvariable=destination_text,bg="white",fg="green",font=" Gabriola 16")
e7.grid(row=7,column=2)


foodservice_text =StringVar()
e8=Entry(window,textvariable=foodservice_text,bg="white",fg="green",font=" Gabriola 16")
e8.grid(row=8,column=2)

berthpreference_text= StringVar()
e9=Entry(window,textvariable=berthpreference_text,bg="white",fg="green",font=" Gabriola 16",)
e9.grid(row=9,column=2)

coach_text= StringVar()
e10=Entry(window,textvariable=coach_text,bg="white",fg="green",font=" Gabriola 16")
e10.grid(row=10,column=2)

departuretime_text= StringVar()
e11=Entry(window,textvariable=departuretime_text,bg="white",fg="green",font=" Gabriola 16")
e11.grid(row=11,column=2)

arrivaltime_text= StringVar()
e12=Entry(window,textvariable=arrivaltime_text,bg="white",fg="green",font=" Gabriola 16")
e12.grid(row=12,column=2)

trainnumber_text = StringVar()
e13 = Entry(window, textvariable=trainnumber_text, bg="white", fg="green", font=" Gabriola 16")
e13.grid(row=13, column=2)

list1=Listbox(window,height=16,width=80)
list1.grid(row=1,column=5,rowspan=6,columnspan=20)

#sb1=Scrollbar(window)
#sb1.grid(row=10,column=3,rowspan=6,columnspan=1)
#list1.configure(yscrollcommand=sb1.set)
#sb1.configure(command=list1.yview)

b1=Button(window,text="insert",command=insert_admin1_text,bg="white",fg="purple",font=" Gabriola 16 ")
b1.grid(row=9,column=3)

b2=Button(window,text="search",command=search_admin1_text,bg="white",fg="purple",font=" Gabriola 16 ")
b2.grid(row=10,column=3)

b3=Button(window,text="view",command=view_admin1_text,bg="white",fg="purple",font=" Gabriola 16" )
b3.grid(row=11,column=3)

window.mainloop()
