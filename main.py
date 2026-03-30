# Put any imports and global variable here
import tkinter as tk

# 1. Set up a the basic parts for the Tkinter window?
root = tk.Tk()
root.title("Pomodoro Timer")

welcome_msg = tk.Label(root, text="Welcome to my Pomodoro App!")
welcome_msg.pack();

stop_btn = tk.Button(root, text="Stop")
stop_btn.pack()

work_interval = tk.Spinbox(root, from_=0, to=999)
rest_interval = tk.Spinbox(root, from_=0, to=999)
work_interval.pack()
rest_interval.pack()

root.mainloop();
# Main logic? Timedate? Time? or TimeDelta?

# If the file gets too long, maybe I'll turn the timer into its own class...