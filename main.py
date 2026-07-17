#imports
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo
import random

def readFile(file):
  """read from file"""
  if file != None:
    with file as f:
      read_data = f.read()
    return read_data

def writeFile(file, content):
  """write to file"""
  if file != None:
    with file as f:
      f.write(content)

def eightBall():
  """a magic 8-ball (returns a string)"""
  responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", 
               "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
               "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"] # list of responses
  return random.choice(responses) # pick random response

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
  ttk.Label(t, text="good luck :)").grid(column=0, row=0)

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
  e = None
  def __init__(self, master): # initialise window
    master.geometry('600x400+50+50')
    self.widgets(master) # initialise top bar widgets
    self.entry(master) #initialise entry text box

  def widgets(self, master): #setup widgets
    """initialise menubar onto master"""
    # setup menubar on object
    menubar = Menu(master)
    master.config(menu=menubar) # make menu a bar
    
    '''MENUBAR BUTTONS'''
    m1 = Menu() #first cascading menu
    # add buttons to cascade NOTE use command=lambda: for func with arguments in buttons
    m1.add_command(label="About", command=lambda:aboutPopup(master))
    m1.add_command(label="Help", command=lambda:helpPopup(master)) 

    m2 = Menu() #second cascading menu
    #add buttons to cascade
    m2.add_command(label="Open", command=self.openFile)
    m2.add_command(label="Save", command=self.saveFile)

    m3 = Menu() #third cascading menu
    #add buttons to cascade
    m3.add_command(label="Magic-8 ball", command=lambda:showinfo(title="Magic-8 ball", message=eightBall()))

    menubar.add_cascade(label="battlefield-aquaintance", menu=m1) #add cascading menu to bar
    menubar.add_cascade(label="File", menu=m2)
    menubar.add_cascade(label="Extras", menu=m3)

  def entry(self, master):
    """initialise text entry onto master"""
    master.grid()# add grid to master

    #fill screen with column and row 0
    master.grid_columnconfigure(0, weight=1)
    master.grid_rowconfigure(0, weight=1)

    self.e = Text(master) #set up text field
    self.e.grid(column=0, row=0) # make it fit the window (for now TODO fix resizing the window)
  
  def getEntry(self): 
    """get the content of the text entry"""
    return self.e.get(index1="1.0", index2="end") # return content from "1.0" to end NOTE this is really irritating why is there no start bruh
  
  def writeEntry(self, string):
    """write into the text entry"""
    self.e.delete(index1="1.0", index2="end") # delete all content in the text entry first
    self.e.insert("1.0", string) # insert into the text entry
  
  def openFile(self):
    """open from and read from a file"""
    o = filedialog.askopenfile() # win open file menu
    if o != None: # askopenfile() WILL return None if cancel is pressed so to avoid exceptions only run if not None
      f = readFile(o) #read the file
      self.writeEntry(f) #write to the text entry

  def saveFile(self):
    """save to a file"""
    o = filedialog.asksaveasfile() # win save file menu
    if o != None: # asksaveasfile() WILL return None if cancel is pressed so to avoid exceptions only run if not None
      writeFile(o, self.getEntry()) #write to the file

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