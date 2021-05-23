from tkcalendar import *
from tkinter import *

class Mydatepick(DateEntry):
    def __init__(self, master, **kw):
        DateEntry.__init__(self,master=master, **kw)
        self._top_cal.configure(bg='black', bd=1)
        self.delete(0,'end')