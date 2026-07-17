#imports
from tkinter import *
from tkinter import ttk

'''POPUPS'''
def helpPopup(master):
  """display a help popup"""
  t = Toplevel(master) # create new window
  
  #set min and max size
  t.minsize(300, 100)
  t.maxsize(300, 100)
  t.grid() # add grid manager
  
  #centre row and column 0
  t.grid_columnconfigure(0, weight=1)
  t.grid_rowconfigure(0, weight=1)
  
  #label
  ttk.Label(t, text="Read the documentation in doc.txt in the root folder").grid(column=0, row=0)

def aboutPopup(master):
  """display an about popup"""
  t = Toplevel(master) # create new window
  
  #set min and max size
  t.minsize(200, 100)
  t.maxsize(200, 100)
  t.grid() # add grid manager
  
  #centre row and column 0
  t.grid_columnconfigure(0, weight=1)
  t.grid_rowconfigure(0, weight=1)
  
  #labels
  ttk.Label(t, text="battlefield-aquaintance", anchor="center").grid(column=0, row=0)
  ttk.Label(t, text="A text editor", anchor="center").grid(column=0, row=1)
  ttk.Label(t, text="Made by CabrestopUK", anchor="center").grid(column=0, row=2)

class fileWindow():
  """Make a file window"""
  def __init__(self, master): # initialise window
    self.widgets(master) # initialise top bar widgets

  def widgets(self, master): #setup widgets
    """initialise menubar onto master"""
    # setup menubar on object
    menubar = Menu(master)
    master.config(menu=menubar) # make menu a bar
    
    '''MENUBAR BUTTONS'''
    m1 = Menu() #first cascading menu
    # add buttons to cascade NOTE use command=lambda: for func with arguments in buttons
    m1.add_command(label="About", command=lambda:aboutPopup(master)) # TODO add an about popup window
    m1.add_command(label="Help", command=lambda:helpPopup(master)) 
    
    menubar.add_cascade(label="battlefield-aquaintance", menu=m1) #add cascading menu to bar

class app():
  """App class"""
  root = Tk() # initialise tk

  def __init__(self):
    fileWindow(self.root) # create a file window
  
  def run(self):
    """Run the app"""
    self.root.mainloop() # run the program event loop

a = app()
a.run()