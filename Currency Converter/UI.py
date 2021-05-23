import tkinter
from converter import converter
from tkinter import *
from tkinter import ttk
import re
from tkinter import messagebox

class ui(converter):
    def __init__(self) -> None:
        super().__init__()
        self.window=Tk()
        self.window.title('Currency Converter')
    def create_label(self):
        self.label_header=Label(self.window,text='Foreign Currenciy Exchange Rate Against BDT',font=("Arial", 25))
        self.label_header.grid(row=1,column=1,padx=50,pady=10,rowspan=1,columnspan=1)
        self.label_us=Label(self.window,text='US Dollar',font=("Arial", 15))
        self.label_us.grid(row=2,column=1,pady=10,padx=50,rowspan=1,columnspan=1)
        self.label_br=Label(self.window,text='British Pound',font=("Arial", 15))
        self.label_br.grid(row=4,column=1,pady=20,padx=50,rowspan=1,columnspan=1)
        self.label_eu=Label(self.window,text='EU Euro',font=("Arial", 15))
        self.label_eu.grid(row=6,column=1,pady=20,padx=50,rowspan=1,columnspan=1)
        self.label_x=Label(self.window,text='Convert From',font=("Arial", 15))
        self.label_x.grid(row=9,column=0,pady=25,padx=15)
        self.label_y=Label(self.window,text='Convert To',font=("Arial", 15))
        self.label_y.grid(row=9,column=2,padx=15,pady=20)
        self.amount=Label(self.window,text="Amount",font=("Arial", 15))
        self.amount.grid(row=10,column=0,columnspan=1)
        self.conv=Label(self.window,text='Converted Amount',font=("Arial", 15))
        self.conv.grid(row=11,column=2,columnspan=1)

        self.text_us=StringVar()
        self.tk_us=Label(self.window,textvariable=self.text_us,bg='green',font=("Arial", 15))
        self.tk_us.grid(row=3,column=1,pady=1,columnspan=1,rowspan=1)

        self.text_br=StringVar()
        self.tk_br=Label(self.window,textvariable=self.text_br,bg='green',font=("Arial", 15))
        self.tk_br.grid(row=5,column=1,pady=1,columnspan=1,rowspan=1)

        self.text_eu=StringVar()
        self.tk_eu=Label(self.window,textvariable=self.text_eu,bg='green',font=("Arial", 15))
        self.tk_eu.grid(row=7,column=1,pady=1,columnspan=1,rowspan=1)
    def callback(self,P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

    def convert_sec(self):
        self.text_from=StringVar(self.window)
        self.from_box=ttk.Combobox(self.window,values=self.keys,textvariable=self.text_from,width=25,height=8)
        self.from_box.grid(row=10,column=0,pady=20,padx=10)

        vcmd = (self.window.register(self.callback))

        self.num_from=DoubleVar(self.window)
        self.e_from=Entry(self.window,width=30,validatecommand=(vcmd,'%P'))
        self.e_from.grid(row=12,column=0,pady=20,padx=5)

        self.text_to=StringVar(self.window)
        self.to_box=ttk.Combobox(self.window,values=self.keys,textvariable=self.text_to,width=12,height=8)
        self.to_box.grid(row=10,column=2,pady=20,padx=5,columnspan=1)

        self.num_to=DoubleVar(self.window)
        self.e_to=Label(self.window,font=("Arial", 25),textvariable=self.num_to,bg='green')
        self.e_to.grid(row=12,column=2,pady=20,padx=10)
    def change(self):
        if self.text_from.get()!='' and self.text_to.get()!='':
            if self.e_from.get():
                self.temp_1=self.e_from.get()
                if re.search("[+-]?[0-9]+(\\.[0-9]+)?([Ee][+-]?[0-9]+)?",self.temp_1):
                    self.value=float(self.temp_1)
                    self.num_to.set(self.convert(self.text_from.get(),self.text_to.get(),self.value))
                else:
                    self.e_from.delete(0,END)
                    messagebox.showerror('Error','Input Must be Number')
            else:
                messagebox.showerror('Error',"Input is Empty")
        else:
            messagebox.showerror('Error','Both currency Type must be choosen')
            self.e_from.delete(0,END)
    def clear(self):
        self.e_from.delete(0,END)
        self.from_box.delete(0,END)
        self.to_box.delete(0,END)
        #self.e_to.delete(0,END)

        self.num_to.set(0.0)
        self.text_to.set('')
        self.text_from.set('')
        self.num_from.set(0.0)                

    def value_setter_label(self):
        self.text_us.set(str(self.convert('USD','BDT')))
        self.text_br.set(str(self.convert('GBP','BDT')))
        self.text_eu.set(str(self.convert('EUR','BDT')))

    def create_window(self):
        self.create_label()
        self.value_setter_label()
        self.convert_sec()

        self.b_act=Button(self.window,text='Convert',font=("Arial", 15),command=self.change)
        self.b_act.grid(row=13,column=1)
        self.b_clear=Button(self.window,text='Clear',font=('Arial',15),command=self.clear)
        self.b_clear.grid(row=13,column=2)
    
ob2=ui()
ob2.create_window()
ob2.window.mainloop()
        