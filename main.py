# Put any imports and global variable here
import tkinter as tk
from tkinter import ttk

# Window
root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry('600x600')
root.minsize(600,600)

# App Icon
icon = tk.PhotoImage(file="pom_icon.png")
root.iconphoto(True, icon)

# Main Layout Widgets
menu_frame = ttk.Frame(root)
main_frame = ttk.Frame(root)

# Main place layout
menu_frame.place(x = 0, y = 0,relwidth= 0.3, relheight = 1)
main_frame.place(relx = 0.3, y = 0, relwidth = 0.7, relheight = 1)
ttk.Label(menu_frame, background='red').pack(expand=True, fill='both')
ttk.Label(main_frame, background='yellow').pack(expand=True, fill='both')

# menu widgets
start_button = ttk.Button(menu_frame, text = 'Start')
pause_button = ttk.Button(menu_frame, text = 'Pause')
reset_button = ttk.Button(menu_frame, text = 'Reset')

# Things...
welcome_msg = tk.Label(root, text="Welcome to my Pomodoro App!")
welcome_msg.pack()

# work_label = tk.Label(root, text="Work Interval: ")
# rest_title = tk.Label(root, text="Rest Interval: ")
# work_interval = tk.Spinbox(root, from_=0, to=999)
# rest_interval = tk.Spinbox(root, from_=0, to=999)

# work_label.grid(row=0, column=0)
# work_interval.grid(row=0,column=1)
# rest_title.grid(row=1, column=0)
# rest_interval.grid(row=1,column=1)

# #stop_btn = tk.Button(root, text="Stop")
# #stop_btn.pack()

root.mainloop();
# Main logic? Timedate? Time? or TimeDelta?

# If the file gets too long, maybe I'll turn the timer into its own class...