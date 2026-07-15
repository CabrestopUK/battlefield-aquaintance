#imports
from tkinter import *
from tkinter import ttk

# file window object
class fileWindow():
  def __init__(self, obj): # initialise window
    self.widgets(obj) # initialise top bar widgets

  def widgets(self, obj): #setup widgets
    # setup menubar on object
    menubar = Menu(obj)
    obj.config(menu=menubar) # make menu a bar
    
    '''menubar buttons/functionality'''
    m1 = Menu() #first cascading menu
    m1.add_command(label="About") # TODO add an about popup window
    m1.add_command(label="Help") # TODO add a help popup window
    
    menubar.add_cascade(label="Text editor", menu=m1) #add cascading menu to bar

# init file window object
window = Tk()
app = fileWindow(window)

#runs the event loop
window.mainloop()