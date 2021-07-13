#importing all the modules
import os
import tkinter
import subprocess

#making a window
window = tkinter.Tk()
window.title('pip not upgraded')
window.configure(bg='black')
window.geometry('700x300')

#defining all the variables
upgradepipcmd = 'pip install --upgrade pip'
pipversioncmd = 'pip --version'
output = subprocess.check_output(pipversioncmd, shell=True)
formatted_output = output[0:8]

#making a label
label = tkinter.Label(window,text = 'Upgrade Pip Gui',fg="white",bg="black").pack()

#upgrade pip function
def upgradepip():
    os.system('pip install --upgrade pip')
    window.title("pip is upgraded")

#making a button and a label
B = tkinter.Button(window, text = 'Upgrade Pip', command=upgradepip, highlightbackground='black',  foreground= "white",  font="Helvetica 16 bold").pack()
L = tkinter.Label(window, text='pip version: {0}'.format(formatted_output), bg="black", fg="white").pack()
#window main loop
window.mainloop()
