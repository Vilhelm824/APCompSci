import tkinter as tk
import tkinter.scrolledtext as tksc

 
def test_my_button():
    frame_auth.tkraise()
 
 
# main window
root = tk.Tk()
root.wm_geometry("250x150")
root.title("Authorization")

# Add this code before the code that creates your "Login" button
bt_image = tk.PhotoImage(file="button.gif")
bt_image = bt_image.subsample(10,10)

# create empty frame
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
btn_login = tk.Button(frame_login, text='Login', command=test_my_button, image=bt_image)
btn_login.pack()

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky='news')
 
frame_login.tkraise()
 
test_textbox = tksc.ScrolledText(frame_auth)
test_textbox.configure(height=10, width=50, bg='red', font='Courier')
root.mainloop()
