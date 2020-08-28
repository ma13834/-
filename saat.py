from tkinter import *

root = Tk()
root.title("mohammadali")
width = 500
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)



#=======================================METHODS===================================================

def countdown(count):
    lbl_text['text'] = count
    if count > 0:
        root.after(1000, countdown, count-1)
    elif(count == 0):
        global NewForm
        NewForm = Toplevel() 
        NewForm.title("mohammadali")
        width = 500
        height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        NewForm.geometry("%dx%d+%d+%d" % (width, height, x, y))
        NewForm.resizable(0, 0)
        lbl_blast = Label(NewForm, text="Blast Off!", font=('arial', 50))
        lbl_blast.pack(fill=BOTH, pady=100)
        btn_back = Button(NewForm, text="Reset", font=('arial', 16), command=BackBtn)
        btn_back.pack(side=TOP)
        

def StartCountdown():
    countdown(11)
    btn_toggle.config(state=DISABLED)


def BackBtn():
    NewForm.destroy()
    btn_toggle.config(state=NORMAL)
    lbl_text.config(text="10")
    
    


#=======================================FRAMES====================================================
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
TextField = Frame(root)
TextField.pack(side=TOP)
BtnGroup = Frame(root, width=500)
BtnGroup.pack(side=BOTTOM)

#=======================================LABEL WIDGETS=============================================
lbl_title = Label(Top, width=500, text="mohammadali timer", font=('times new roman', 16))
lbl_title.pack(fill=X)
lbl_text = Label(TextField, text="10", font=('arial', 120))
lbl_text.pack(fill=BOTH) 
 
#=======================================Button WIDGETS=============================================
btn_toggle = Button(BtnGroup, text="Start Countdown", command=StartCountdown)
btn_toggle.pack()

#=======================================INITIALIZATION=============================================
if __name__ == '__main__':
    root.mainloop()
