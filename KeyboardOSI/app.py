from operator import iconcat

import keyboard
from tkinter import *

#update labels
#wasd
def pressw(event=None):
    labelw.config(image=i_w_pressed)
def unpressw(event=None):
    labelw.config(image=i_w_unpressed)

def pressa(event=None):
    labela.config(image=i_a_pressed)
def unpressa(event=None):
    labela.config(image=i_a_unpressed)

def presss(event=None):
    labels.config(image=i_s_pressed)
def unpresss(event=None):
    labels.config(image=i_s_unpressed)

def pressd(event=None):
    labeld.config(image=i_d_pressed)
def unpressd(event=None):
    labeld.config(image=i_d_unpressed)

#qerf
def pressq(event=None):
    labelq.config(image=i_q_pressed)
def unpressq(event=None):
    labelq.config(image=i_q_unpressed)

def presse(event=None):
    labele.config(image=i_e_pressed)
def unpresse(event=None):
    labele.config(image=i_e_unpressed)

def pressr(event=None):
    labelr.config(image=i_r_pressed)
def unpressr(event=None):
    labelr.config(image=i_r_unpressed)

def pressf(event=None):
    labelf.config(image=i_f_pressed)
def unpressf(event=None):
    labelf.config(image=i_f_unpressed)

#zxc
def pressz(event=None):
    labelz.config(image=i_z_pressed)
def unpressz(event=None):
    labelz.config(image=i_z_unpressed)

def pressx(event=None):
    labelx.config(image=i_x_pressed)
def unpressx(event=None):
    labelx.config(image=i_x_unpressed)

def pressc(event=None):
    labelc.config(image=i_c_pressed)
def unpressc(event=None):
    labelc.config(image=i_c_unpressed)

#tab shift ctrl space
def presstab(event=None):
    labeltab.config(image=i_tab_pressed)
def unpresstab(event=None):
    labeltab.config(image=i_tab_unpressed)

def pressshift(event=None):
    labelshift.config(image=i_shift_pressed)
def unpressshift(event=None):
    labelshift.config(image=i_shift_unpressed)

def pressctrl(event=None):
    labelctrl.config(image=i_ctrl_pressed)
def unpressctrl(event=None):
    labelctrl.config(image=i_ctrl_unpressed)

def pressspace(event=None):
    labelspace.config(image=i_space_pressed)
def unpressspace(event=None):
    labelspace.config(image=i_space_unpressed)



# Create the main window
window = Tk()
window.title("Keypress Display")
window.geometry('505x305')
window.config(background='blackqwesadfsfrtrasfda  ')
#window.wm_attributes('-transparentcolor','black')

#set photos
#icon
icon = PhotoImage(file='caption.png')
window.iconphoto(True,icon)

#wasd
i_w_pressed = PhotoImage(file='key pngs/w_pressed.png')
i_w_unpressed = PhotoImage(file='key pngs/w_unpressed.png')

i_a_pressed = PhotoImage(file='key pngs/a_pressed.png')
i_a_unpressed = PhotoImage(file='key pngs/a_unpressed.png')

i_s_pressed = PhotoImage(file='key pngs/s_pressed.png')
i_s_unpressed = PhotoImage(file='key pngs/s_unpressed.png')

i_d_pressed = PhotoImage(file='key pngs/d_pressed.png')
i_d_unpressed = PhotoImage(file='key pngs/d_unpressed.png')

#qerf
i_q_pressed = PhotoImage(file='key pngs/q_pressed.png')
i_q_unpressed = PhotoImage(file='key pngs/q_unpressed.png')

i_e_pressed = PhotoImage(file='key pngs/e_pressed.png')
i_e_unpressed = PhotoImage(file='key pngs/e_unpressed.png')

i_r_pressed = PhotoImage(file='key pngs/r_pressed.png')
i_r_unpressed = PhotoImage(file='key pngs/r_unpressed.png')

i_f_pressed = PhotoImage(file='key pngs/f_pressed.png')
i_f_unpressed = PhotoImage(file='key pngs/f_unpressed.png')

#zxc
i_z_pressed = PhotoImage(file='key pngs/z_pressed.png')
i_z_unpressed = PhotoImage(file='key pngs/z_unpressed.png')

i_x_pressed = PhotoImage(file='key pngs/x_pressed.png')
i_x_unpressed = PhotoImage(file='key pngs/x_unpressed.png')

i_c_pressed = PhotoImage(file='key pngs/c_pressed.png')
i_c_unpressed = PhotoImage(file='key pngs/c_unpressed.png')

#tab shift ctrl space
i_tab_pressed = PhotoImage(file='key pngs/tab_pressed.png')
i_tab_unpressed = PhotoImage(file='key pngs/tab_unpressed.png')

i_shift_pressed = PhotoImage(file='key pngs/shift_pressed.png')
i_shift_unpressed = PhotoImage(file='key pngs/shift_unpressed.png')

i_ctrl_pressed = PhotoImage(file='key pngs/ctrl_pressed.png')
i_ctrl_unpressed = PhotoImage(file='key pngs/ctrl_unpressed.png')

i_space_pressed = PhotoImage(file='key pngs/space_pressed.png')
i_space_unpressed = PhotoImage(file='key pngs/space_unpressed.png')

# Create a label
#wasd
labelw = Label(window,
              image=i_w_unpressed,
               bg='black')
labels = Label(window,
                image=i_s_unpressed,
               bg='black')
labela = Label(window,
                image=i_a_unpressed,
               bg='black')
labeld = Label(window,
                image=i_d_unpressed,
               bg='black')

#qerf
labelq = Label(window,
               image = i_q_unpressed,
               bg='black')
labele = Label(window,
               image = i_e_unpressed,
               bg='black')
labelr = Label(window,
               image = i_r_unpressed,
               bg='black')
labelf = Label(window,
               image = i_f_unpressed,
               bg='black')

#zxc
labelz = Label(window,
               image = i_z_unpressed,
               bg='black')
labelx = Label(window,
               image = i_x_unpressed,
               bg='black')
labelc = Label(window,
               image = i_c_unpressed,
               bg='black')

#tab shift ctrl space
labeltab = Label(window,
                 image = i_tab_unpressed,
               bg='black')
labelshift = Label(window,
                   image = i_shift_unpressed,
               bg='black')
labelctrl = Label(window,
                  image = i_ctrl_unpressed,
               bg='black')
labelspace = Label(window,
                   image = i_space_unpressed,
               bg='black')


#actually draw the labels
#wasd
labelw.place(x=200,y=0)
labels.place(x=200,y=100)
labela.place(x=100,y=100)
labeld.place(x=300,y=100)

#qerf
labelq.place(x=100,y=0)
labele.place(x=300,y=0)
labelr.place(x=400,y=0)
labelf.place(x=400,y=100)

#zxc
labelz.place(x=100,y=200)
labelx.place(x=200,y=200)
labelc.place(x=300,y=200)


#tab shift ctrl space
labeltab.place(x=0,y=0)
labelshift.place(x=0,y=100)
labelctrl.place(x=0,y=200)
labelspace.place(x=400,y=200)

# Bind the keyboard events
#wasd
keyboard.on_press_key('w', pressw)
keyboard.on_release_key('w', unpressw)

keyboard.on_press_key('a',pressa)
keyboard.on_release_key('a',unpressa)

keyboard.on_press_key('s',presss)
keyboard.on_release_key('s',unpresss)

keyboard.on_press_key('d',pressd)
keyboard.on_release_key('d',unpressd)

#qerf
keyboard.on_press_key('q', pressq)
keyboard.on_release_key('q', unpressq)

keyboard.on_press_key('e', presse)
keyboard.on_release_key('e', unpresse)

keyboard.on_press_key('r', pressr)
keyboard.on_release_key('r',unpressr)

keyboard.on_press_key('f', pressf)
keyboard.on_release_key('f', unpressf)

#zxc
keyboard.on_press_key('z', pressz)
keyboard.on_release_key('z', unpressz)

keyboard.on_press_key('x', pressx)
keyboard.on_release_key('x', unpressx)

keyboard.on_press_key('c', pressc)
keyboard.on_release_key('c', unpressc)

#tab shift ctrl space
keyboard.on_press_key('tab', presstab)
keyboard.on_release_key('tab', unpresstab)

keyboard.on_press_key('shift', pressshift)
keyboard.on_release_key('shift', unpressshift)

keyboard.on_press_key('ctrl', pressctrl)
keyboard.on_release_key('ctrl', unpressctrl)

keyboard.on_press_key('space', pressspace)
keyboard.on_release_key('space', unpressspace)

# Run the Tkinter event loop
window.mainloop()