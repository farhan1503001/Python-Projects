from backend import connect, delete, insert, search, view
from Mydatepick import Mydatepick
from calendar import Calendar, month
from datetime import datetime
from tkinter import *
from tkcalendar import *
#Intialize the window
from tkcalendar import *
from tkinter import *
from tkinter import messagebox
import time
#Functions
def clear():
    e_date.delete(0,END)
    e_earn.delete(0,END)
    e_ex.delete(0,END)
    e_study.delete(0,END)
    e_diet.delete(0,END)
    e_py.delete(0,END)
    earn_text=''
    ex_text=''
    study_text=''
    diet_text=''
    py_text=''



def get_selected_row(event):
    if len(lister.curselection())>0:
        global holder
        b_insert.config(state='disabled')
        #messagebox.showwarning('Warning','Inserting Disabled')
        print(lister.curselection())
        holder=lister.curselection()
        value=holder[0]
        select_row=lister.get(value)
        prev_sel=lister.curselection()
        clear()
        e_date.insert(END,select_row[1])
        e_earn.insert(END,select_row[2])
        e_ex.insert(END,select_row[3])
        e_study.insert(END,select_row[4])
        e_diet.insert(END,select_row[5])
        e_py.insert(END,select_row[6])
        print(select_row)
    else:
        b_insert.config(state='active')
        clear()
        messagebox.showinfo('Attention','Inserting Enabled')
def delete_command():
    for i in holder:
        value=lister.get(holder[i])
        delete(value[0])
def view_command():
    lister.delete(0,END)
    result=view()
    for row in result:
        lister.insert(END,row)
    clear()

def insert_command():
    if e_date.get()==0:
        date=e_date.get_date().strftime("%d-%m-%Y")
        earning=earn_text.get()
        exercise=ex_text.get()
        study=study_text.get()
        diet=diet_text.get()
        python=py_text.get()
        if date and earning and study and diet and python:
            insert(date,earning,exercise,study,diet,python)
            lister.delete(0,END)
            lister.insert(END,(date,earning,exercise,study,diet,python))
        else:
            messagebox.showerror("Error","All items is not filled")
    else:
        messagebox.showerror('Error','Fill the date')
    clear()  
def search_command():
    lister.delete(0,END)
    date=e_date.get_date().strftime("%d-%m-%Y")
    earning=earn_text.get()
    exercise=ex_text.get()
    study=study_text.get()
    diet=diet_text.get()
    python=py_text.get()
    result=search(date,earning,exercise,study,diet,python)
    for row in result:
        lister.insert(END,row)
    clear()

#Creating windows
window=Tk()
window.title('My Routine Wedget')
connect()
#Now initializing the label
l_date=Label(window,text='Date')
l_date.grid(row=0,column=0)
l_earn=Label(window,text='Earning')
l_earn.grid(row=0,column=2)
l_exercise=Label(window,text='Exercise')
l_exercise.grid(row=1,column=0)
l_study=Label(window,text='Study')
l_study.grid(row=1,column=2)
l_diet=Label(window,text='Diet')
l_diet.grid(row=2,column=0)
l_py=Label(window,text='python')
l_py.grid(row=2,column=2)

#Now creating data entry tables
date_text=StringVar()
e_date=Mydatepick(window,textvariable=date_text)
e_date.grid(row=0,column=1,rowspan=1,columnspan=1)

#Entry for earning
earn_text=StringVar()
e_earn=Entry(window,textvariable=earn_text)
e_earn.grid(row=0,column=3,pady=10,padx=10)
#Spinbox for excercise
ex_text=StringVar()
e_ex=Spinbox(window,values=['','No exercise','one hour','More than one hour '],textvariable=ex_text)
e_ex.grid(row=1,column=1,columnspan=1,padx=10,pady=10)
#Spinbox for study
items=list()
items.append('')
for i in range(25):
    items.append(i)
study_text=StringVar()
e_study=Spinbox(window,values=items,textvariable=study_text)
e_study.grid(row=1,column=3,columnspan=1,pady=10,padx=10)
#Spinbox for diet
diet_text=StringVar()
e_diet=Spinbox(window,values=['','Taken','Not Taken'],textvariable=diet_text)
e_diet.grid(row=2,column=1,columnspan=1,pady=10,padx=10)

#Spinbox for python
py_text=StringVar()
e_py=Spinbox(window,values=['','did python','Sorry,didnot'],textvariable=py_text)
e_py.grid(row=2,column=3,columnspan=1,pady=10,padx=10)
#Now creating list for holding values
lister=Listbox(window,height=15,width=35,selectmode=MULTIPLE)
lister.grid(row=3,column=0,rowspan=9,columnspan=3,pady=10,padx=2)
#Scrollbar
sc=Scrollbar(window)
sc.grid(row=3,column=2,rowspan=9,padx=10)
lister.bind('<<ListboxSelect>>',get_selected_row)
#lister.bind('<FocusOut>', lambda e: lister.selection_clear(0, END))

#Now creating Buttons
b_insert=Button(window,text='Insert',width=12,pady=10,command=insert_command)
b_insert.grid(row=3,column=3,pady=10)

b_search=Button(window,text='Search',width=12,pady=10,command=search_command)
b_search.grid(row=4,column=3)

b_view=Button(window,text='View all',width=12,pady=10,command=view_command)
b_view.grid(row=5,column=3,pady=10)

b_del=Button(window,text='Delete',width=12,pady=10,command=delete_command)
b_del.grid(row=6,column=3)

b_close=Button(window,text='Close',width=12,pady=10,command=window.destroy)
b_close.grid(row=7,column=3,pady=10)

window.mainloop()
'''
dateobj=datetime.now()
d=dateobj.strftime("%d-%m-%Y")
val=e_date.get_date().strftime("%d-%m-%Y")
if d==val:
    print('Yes')
else:
    print('No')


'''