from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == "pankajgajpalla@gmail.com" and password == "123":
        messagebox.showinfo("yayay!", "login succefule")
    else:
        messagebox.showerror("oops!", "login fail")
    

root = Tk()

root.title('Pankaj Gajpalla')
root.iconbitmap('enstagam.ico')


# root.minsize(300, 300)
# root.maxsize(400, 400)
root.geometry('400x500')

root.configure(background='#0096DC')

img = Image.open('logoa.png')
resized_img = img.resize((150,100))

img = ImageTk.PhotoImage(resized_img)

img_label = Label(root, image = img)
img_label.pack(pady= (10, 10))

text_label = Label(root, text ='Monkey D. Luffy', fg = 'white', bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana', 24))

email_label = Label(root, text = 'Enter Email', fg ='white', bg = '#0096DC')
email_label.pack(pady=(20, 5))
email_label.config(font=('verdana', 12))

email_input = Entry(root, width=50)
email_input.pack(ipady=6, pady=(1,15))

password_label = Label(root, text = 'Enter password', fg ='white', bg = '#0096DC')
password_label.pack(pady=(20, 5))
password_label.config(font=('verdana', 12))

password_input = Entry(root, width=50)
password_input.pack(ipady=6, pady=(1,15))

login_btn = Button(root, text='Login', fg='black', bg='white', width=20, height=2, command= handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('vardana', 10))


root.mainloop()
# so that we can see it continuesly the screen