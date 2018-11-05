# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 10:55:36 2017

@author: Sun Yongjiao
"""

from functools import partial as pto
from Tkinker import Tk,Button,X
from tkMessageBox import showinfo,showwarning,showerror

WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNS = {
        'do not enter' : CRIT,
        'railroad crossing':WARN,
        '55\nspeed limit ':REGU,
        'wrong way' :CRIT,
        'merging': WARN,
        'one way': REGU,}
critCB = lambda:showerror('Error','Error Button Pressed!')
warnCB = lambda:showwarning('Warning','Warning Button Pressed!')
infoCB = lambda:showinfo('Info' 'Info Button Pressed!')
top = Tk()
top.title('Road Signs')
Button (top,text = 'QUIT',command=top.quit,bg='red',fd='white').pack()
MyButton = pto(Button,top)
CritButton = pto(MyButton,command = critCB,bd='white',fg='red')
WarnButton = pto(MyButton,command = warnCB,bd='golaenrod1')
ReguButton = pto(MyButton,command = infoCB,bd='white')

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = '%sButton(text=%r%s).pack(fill=X,expand=True)' % (signType = title(),eachSign,'.upper()' if signType ==CRIT else '.title()')
    eval(cmd)
top.mainloop()