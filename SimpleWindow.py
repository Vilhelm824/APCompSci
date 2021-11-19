#   A program creates a window on your screen using Tkinter.
import tkinter as tk


def test_my_button():
    global password
    frame_auth.tkraise()
    password = ent_password.get()
    lbl_show_pwd.config(text=password)


# main window
root = tk.Tk()
root.wm_geometry("250x150")
root.title("Authorization")
# create login frame
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky='news')
lbl_username = tk.Label(frame_login, text='Username:', font='Courier')
lbl_username.pack()
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)
lbl_password = tk.Label(frame_login, text='Password: ', font='Courier')
lbl_password.pack()
ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack(pady=5)
btn_login = tk.Button(frame_login, text='Login', command=test_my_button)
btn_login.pack()

# create authorization fram
frame_auth = tk.Frame(root)
frame_auth.grid()
frame_auth.grid(row=0, column=0, sticky='news')
lbl_show_pwd = tk.Label(frame_auth, font="Courier")
lbl_show_pwd.pack()

frame_login.tkraise()

root.mainloop()
