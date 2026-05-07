# Imports here
import tkinter as tk
from tkinter import ttk
import time 

# Global Variables here


# # Window
# root = tk.Tk()
# root.title("Pomodoro Timer")
# root.geometry('600x600')
# root.minsize(900,600)

# ttk style
# style = ttk.Style()
# style.configure("TButton", font=("Verdana", 12))

# # App Icon
# icon = tk.PhotoImage(file="pom_icon.png")
# root.iconphoto(True, icon)

# # Main Layout Widgets
# menu_frame = ttk.Frame(root)
# main_frame = ttk.Frame(root)

# # Main 'place' layout
# menu_frame.place(x = 0, y = 0,relwidth= 0.3, relheight = 1)
# main_frame.place(relx = 0.3, y = 0, relwidth = 0.7, relheight = 1)
# # ttk.Label(menu_frame, background='red').pack(expand=True, fill='both')
# # ttk.Label(main_frame, background='yellow').pack(expand=True, fill='both')

# # menu widgets
# work_title = ttk.Label(menu_frame, text="Work Interval: ", font=("Verdana", 12))
# rest_title = ttk.Label(menu_frame, text="Rest Interval: ", font=("Verdana", 12))
# work_interval = ttk.Spinbox(menu_frame, from_=0, to=999, font=("Verdana", 12))
# rest_interval = ttk.Spinbox(menu_frame, from_=0, to=999, font=("Verdana", 12))

# start_button = ttk.Button(menu_frame, text = 'Start')
# pause_button = ttk.Button(menu_frame, text = 'Pause')
# reset_button = ttk.Button(menu_frame, text = 'Reset')

# # Menu Layout
# menu_frame.columnconfigure((0,1), weight = 1, uniform = 'a')
# # menu_frame.rowconfigure((0,1,2,3), weight = 1, uniform = 'a')
# menu_frame.rowconfigure((0,1), uniform = 'a')
# menu_frame.rowconfigure((2,3,4), weight = 1, uniform = 'a')

# work_title.grid(row = 0, column= 0, sticky='nwe', pady= 40)
# work_interval.grid(row = 0, column = 1, sticky = 'nwe', pady = 40)

# rest_title.grid(row = 1, column= 0, sticky='new', pady = 20)
# rest_interval.grid(row = 1, column = 1, sticky = 'nwe', pady = 20)

# start_button.grid(row = 3, column = 0, sticky = 'nswe', columnspan = 2)
# reset_button.grid(row = 4, column = 0, sticky = 'nswe', columnspan = 2)


# # Main Widgets (The timer countdown and what state the app is in)
# state_label = ttk.Label(main_frame, text = '[Click "start"]/[Work]/[Rest]/[Paused]',
#                         font = ("Verdana", 14) )
# timer_label = ttk.Label(main_frame, text = '25:00', font = ('Verdana', 25))

# # Main layout 
# state_label.pack(side = 'top', expand = False, fill = 'none', pady= 40)
# timer_label.pack(side = 'top', expand = True, fill = 'none')

#root.mainloop();


# GUI 
class PomodoroApp:   
    def __init__(self, root):
        """
        Sets up the GUI window. It also initializes some of the status variables
        
        Args:
            self: A PomodoroApp object. Passed automatically
            root (Tkinter): A tkinter object
        """
        
        # status variables
        self.is_running = False
        self.is_paused = True # if it were false, it would conflict with is_running initially
        self.time_remaining = 0
        self.work_seesion_active = False 
        
        self.root = root
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

        vcmd= root.register(self.validate_num)
        
        # menu widgets
        work_title = ttk.Label(menu_frame, text="Work Interval: ", font=("Verdana", 12))
        rest_title = ttk.Label(menu_frame, text="Rest Interval: ", font=("Verdana", 12))
        # These spinboxes can only take in integer values
        self.work_interval = ttk.Spinbox(menu_frame, from_=0, to=999, font=("Verdana", 12),
                                         validate="key",
                                         validatecommand=(vcmd, '%P'))
        
        self.rest_interval = ttk.Spinbox(menu_frame, from_=0, to=999, font=("Verdana", 12),
                                         validate="key", 
                                         validatecommand=(vcmd, '%P'))

        self.start_button = ttk.Button(menu_frame, text = 'Start', command=self.start_timer)
        self.pause_button = ttk.Button(menu_frame, text = 'Pause', command=self.pause_timer)
        self.reset_button = ttk.Button(menu_frame, text = 'Reset', command=self.reset_timer)

        # Menu Layout
        menu_frame.columnconfigure((0,1), weight = 1, uniform = 'a')
        # menu_frame.rowconfigure((0,1,2,3), weight = 1, uniform = 'a')
        menu_frame.rowconfigure((0,1), uniform = 'a')
        menu_frame.rowconfigure((2,3,4), weight = 1, uniform = 'a')

        # place the spinbox titles for work and rest intervals spinboxes
        work_title.grid(row = 0, column= 0, sticky='nwe', pady= 40)
        self.work_interval.grid(row = 0, column = 1, sticky = 'nwe', pady = 40)
        
        rest_title.grid(row = 1, column= 0, sticky='new', pady = 20)
        self.rest_interval.grid(row = 1, column = 1, sticky = 'nwe', pady = 20)

        # Place the buttons
        self.start_button.grid(row = 3, column = 0, sticky = 'nswe', columnspan = 2)
        # The pause button is initially hidden
        self.pause_button.grid(row = 3, column = 0, sticky = 'nswe', columnspan = 2)
        self.pause_button.grid_remove()
        self.reset_button.grid(row = 4, column = 0, sticky = 'nswe', columnspan = 2)

        # Main Widgets (The timer countdown and what state the app is in)
        self.state_label = ttk.Label(main_frame, text = '[Click "start"]/[Work]/[Rest]/[Paused]',
                                font = ("Verdana", 14) )
        self.timer_label = ttk.Label(main_frame, text = '25:00', font = ('Verdana', 25))

        # Main layout 
        self.state_label.pack(side = 'top', expand = False, fill = 'none', pady= 40)
        self.timer_label.pack(side = 'top', expand = True, fill = 'none')
        
    def validate_num(self, char):
        """
        Determines if the value in a spinbox is a digit or not
        """
        return char.isdigit() or char == ""
        
    # Main logic? Timedate? Time? or TimeDelta?
    def start_timer(self):
        # time remaining = time_now + (work_interval OR rest_interval) depending
        # on which state we are in
        # try 
        self.time_remaining = int(self.work_interval.get())
        # except
            # set the time to 0
        
        print("work interval: " + str(self.time_remaining) + " minutes")
        
        print("the timer was started!")
        return -1

    def pause_timer(self):
        # add stuff here
        print("The timer was paused!")
        return -1

    def reset_timer(self):
        # add stuff here
        print("The timer was reset!")
        return -1

    def countdown(self):
        # add stuff here
        print("Counting down...")
        return -1


# Set up the GUI
def main():
    # set up the GUI
    root = tk.Tk()
    root.title("Pomodoro Timer")
    root.geometry('600x600')
    root.minsize(900,600)
    # create widgets for GUI
    app = PomodoroApp(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()