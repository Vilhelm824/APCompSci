import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename


root = tk.Tk()
frame = tk.Frame(root)
frame.grid()
# adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=20, width=65)

# run process 
def do_command(command):
    global command_textbox, url_entry
    url_val = url_entry.get()
    if(len(url_val)==0):
        url_val = "127.0.0.1"
    command_textbox.delete(1.0, tk.END)
    
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()
    
    if(command == "ping"):
        p = subprocess.Popen([command, "-c", "5", url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2
    else:
        p = subprocess.Popen([command, url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)


# Save function.
def mSave():
    global command_textbox
    filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
    if filename is None:
        return
    file = open (filename, mode = 'w')
    text_to_save = command_textbox.get("1.0", tk.END)

    file.write(text_to_save)
    file.close()
  

# set up buttons
ping_btn = tk.Button(frame, text="Ping Server", activebackground="cyan", bg="blue", bd=5, width=8, font=("comic sans", 14), command=lambda:do_command("ping"))
tracert_btn = tk.Button(frame, text="Trace Ping", activebackground="cyan", bg="blue", bd=5, width=8, font=("comic sans", 14), command=lambda:do_command("traceroute"))
nslookup_btn = tk.Button(frame, text="DNS Lookup", activebackground="cyan", bg="blue", bd=5, width=8, font=("comic sans", 14), command=lambda:do_command("nslookup"))
save_btn = tk.Button(frame, text="Save Output", activebackground="cyan", bg="blue", bd=5, width=8, font=("comic sans", 14), command=mSave)

# creates the frame with label for the text box
# frame_URL = tk.Frame(root, pady=10, bg="black") # change frame color

# decorative label
url_label = tk.Label(frame, text="Enter a URL: ", compound="left", font=("comic sans", 14), bd=0, relief=tk.FLAT, cursor="heart", fg="cyan", bg="grey")
url_entry= tk.Entry(frame,  font=("comic sans", 14), width=22) # change font

# arrange everything
nslookup_btn.grid(column=0,row=0)
ping_btn.grid(column=1, row=0)
tracert_btn.grid(column=2, row=0)
save_btn.grid(column=3, row=0)
url_label.grid(column=0, row=1)
url_entry.grid(column=1, row=1, columnspan=2)
command_textbox.grid(column=0, row=2, columnspan=4)


root.mainloop()
