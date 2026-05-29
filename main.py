# Imports here
import tkinter as tk
from tkinter import ttk
import time 
from playsound3 import playsound


# Global Variables here


# GUI 
class PomodoroApp:   
    """
    __init__(root) - sets up the GUI window and initializes status variables
    validate_num()
    
    """
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
        self.work_session_active = False 
        
        self.root = root
        style = ttk.Style()
        style.configure("TButton", font=("Verdana", 12))
        
        # inital work and rest intervals
        self.init_work_val = tk.IntVar(root)
        self.init_work_val.set(25)
        self.init_rest_val = tk.IntVar(root)
        self.init_rest_val.set(5)  

        # App Icon
        icon = tk.PhotoImage(file=".venv\pom_icon.png")
        root.iconphoto(True, icon)

        # Main Layout Widgets
        menu_frame = ttk.Frame(root)
        main_frame = ttk.Frame(root)

        # Main 'place' layout
        menu_frame.place(x = 0, y = 0,relwidth= 0.3, relheight = 1)
        main_frame.place(relx = 0.3, y = 0, relwidth = 0.7, relheight = 1)
        
        # menu widgets
        work_title = ttk.Label(menu_frame, text="Work Interval: ", font=("Verdana", 12))
        rest_title = ttk.Label(menu_frame, text="Rest Interval: ", font=("Verdana", 12))
        # These spinboxes can only take in integer values
        self.work_interval = ttk.Spinbox(menu_frame, from_=1, to=999, font=("Verdana", 12),
                                         textvariable=self.init_work_val,
                                         state='readonly'
                                         )
        
        self.rest_interval = ttk.Spinbox(menu_frame, from_=1, to=999, font=("Verdana", 12),
                                         textvariable=self.init_rest_val,
                                         state= 'readonly')

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
        
        
    # Main logic? Timedate? Time? or TimeDelta?
    def start_timer(self):
        playsound("Sound_effects\\506054__mellau__button-click-1.wav", False)
        # time remaining = time_now + (work_interval OR rest_interval) depending
        # on which state we are in
        self.time_remaining = int(self.work_interval.get())
        # Hide the start button and show the pause button   
        self.start_button.grid_remove()
        self.pause_button.grid()
        
        print("The timer was started")
        pass

    def pause_timer(self):
        playsound("Sound_effects\\506054__mellau__button-click-1.wav", False)
        # hide the pause button and show the start button
        self.pause_button.grid_remove()
        self.start_button.grid()
        # add stuff here
        print("The timer was paused!")
        pass

    def reset_timer(self):
        playsound("Sound_effects\\506054__mellau__button-click-1.wav", False)
        # add stuff here
        print("The timer was reset!")
        pass

    def countdown(self):
        # This part is crucial
        print("Counting down...")
        pass


# Set up GUI
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