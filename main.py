# Put any imports and global variable here
import tkinter as tk
from tkinter import ttk

# Window
root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry('600x600')
root.minsize(900,600)

# ttk style
style = ttk.Style()
style.configure("TButton", font=("Verdana", 12))

# App Icon
icon = tk.PhotoImage(file="pom_icon.png")
root.iconphoto(True, icon)

# Main Layout Widgets
menu_frame = ttk.Frame(root)
main_frame = ttk.Frame(root)

# Main 'place' layout
menu_frame.place(x = 0, y = 0,relwidth= 0.3, relheight = 1)
main_frame.place(relx = 0.3, y = 0, relwidth = 0.7, relheight = 1)
# ttk.Label(menu_frame, background='red').pack(expand=True, fill='both')
# ttk.Label(main_frame, background='yellow').pack(expand=True, fill='both')

# menu widgets
work_title = ttk.Label(menu_frame, text="Work Interval: ", font=("Verdana", 12))
rest_title = ttk.Label(menu_frame, text="Rest Interval: ", font=("Verdana", 12))
work_interval = ttk.Spinbox(menu_frame, from_=0, to=999, font=("Verdana", 12))
rest_interval = ttk.Spinbox(menu_frame, from_=0, to=999, font=("Verdana", 12))

start_button = ttk.Button(menu_frame, text = 'Start')
pause_button = ttk.Button(menu_frame, text = 'Pause')
reset_button = ttk.Button(menu_frame, text = 'Reset')

# Menu Layout
menu_frame.columnconfigure((0,1), weight = 1, uniform = 'a')
# menu_frame.rowconfigure((0,1,2,3), weight = 1, uniform = 'a')
menu_frame.rowconfigure((0,1), uniform = 'a')
menu_frame.rowconfigure((2,3,4), weight = 1, uniform = 'a')

work_title.grid(row = 0, column= 0, sticky='nwe', pady= 40)
work_interval.grid(row = 0, column = 1, sticky = 'nwe', pady = 40)

rest_title.grid(row = 1, column= 0, sticky='new', pady = 20)
rest_interval.grid(row = 1, column = 1, sticky = 'nwe', pady = 20)

start_button.grid(row = 3, column = 0, sticky = 'nswe', columnspan = 2)
reset_button.grid(row = 4, column = 0, sticky = 'nswe', columnspan = 2)


# Main Widgets (The timer countdown and what state the app is in)
state_label = ttk.Label(main_frame, text = '[Click "start"]/[Work]/[Rest]/[Paused]',
                        font = ("Verdana", 14) )
timer_label = ttk.Label(main_frame, text = '25:00', font = ('Verdana', 25))

# Main layout 
state_label.pack(side = 'top', expand = False, fill = 'none', pady= 40)
timer_label.pack(side = 'top', expand = True, fill = 'none')

root.mainloop();
# Main logic? Timedate? Time? or TimeDelta?

# If the file gets too long, maybe I'll turn the timer into its own class...

# Forgot to make a main function, so I'll make one
def main():
    root = tk.Tk()
    root.title("Pomodoro Timer")
    root.geometry('600x600')
    root.minsize(900,600)
    app = PomodoroApp(root) # Will be making gui into its own class later on...
    root.mainloop()
    
if __name__ == "__main__":
    main()