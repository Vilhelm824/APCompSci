import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()


def do_command(command):
    global command_textbox, url_entry
    url_val = url_entry.get()
    if(len(url_val)==0):
        url_val = "127.0.0.1"
    command_textbox.delete(1.0, tk.END)
    
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    p = subprocess.Popen([command, url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)


# set up button to run the do_command function
ping_btn = tk.Button(frame, text="Check to see if server is up & active", command=lambda:do_command("ping"))
ping_btn.pack()

tracert_btn = tk.Button(frame, text="Trace the servers a ping goes through", command=lambda:do_command("traceroute"))
tracert_btn.pack()

nslookup_btn = tk.Button(frame, text="lookup ip address of url", command=lambda:do_command("nslookup"))
nslookup_btn.pack()

# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", compound="center", font=("comic sans", 14), bd=0, relief=tk.FLAT, cursor="heart", fg="mediumpurple3", bg="black")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="black") # change frame color
frame.pack()

# adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()


root.mainloop()
