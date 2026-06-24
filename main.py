# Imports here
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time 
from playsound3 import playsound

# default values for timer
work_default_val = 25
rest_default_val = 5

# GUI 
class PomodoroApp:   
    """
    __init__(root) - sets up the GUI window and initializes status variables
    start_timer()   - Starts or resumes the timer
    pause_timer()   - pauses the timer
    reset_timer()   - resets the timer to original state
    countdown()     - counts down the timer to 00:00 
    end_timer()     - handles the end of the timer
    popupMsg()     - handles popups
    get_display_time - returns time as MM:SS
    """
    def __init__(self, root):
        """
        Sets up the GUI window. It also initializes some of the status variables
        
        Args:
            self: A PomodoroApp object. Passed automatically
            root (Tkinter): A tkinter object
        """
        
        # status variables
        self.time_remaining = 0
        self.work_session_active = True
        self.session_state = "idle" # can be "idle," "running," or "paused"
        
        self.root = root
        style = ttk.Style()
        style.configure("TButton", font=("Verdana", 12))
        
        # inital work and rest intervals
        self.init_work_val = tk.IntVar(root)
        self.init_work_val.set(work_default_val)
        self.init_rest_val = tk.IntVar(root)
        self.init_rest_val.set(rest_default_val)  

        # App Icon
        icon = tk.PhotoImage(file=".venv\\pom_icon.png")
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
        self.state_label = ttk.Label(main_frame, text = 'Click "Start" to begin.',
                                font = ("Verdana", 14) )
        self.timer_label = ttk.Label(main_frame, text = '25:00', font = ('Verdana', 25))

        # Main layout 
        self.state_label.pack(side = 'top', expand = False, fill = 'none', pady= 40)
        self.timer_label.pack(side = 'top', expand = True, fill = 'none')
        
        
    # Main logic? Timedate? Time? or TimeDelta?
    def start_timer(self):
        playsound("Sound_effects\\506054__mellau__button-click-1.wav", False)

        # Hide the start button and show the pause button   
        self.start_button.grid_remove()
        self.pause_button.grid()
      
        if self.session_state == "idle":
            if self.work_session_active == True:
                self.time_remaining = int(self.work_interval.get())*60
                self.state_label.config(text="Work")
                print("we are in a WORK session.")
            else:
                self.time_remaining = int(self.rest_interval.get())*60
                self.state_label.config(text="Rest")
                print("we are in a REST session.")
        
        self.end_time = time.time() + self.time_remaining
        
        self.session_state = "running"
        
        print("The timer was started")
        self.countdown()
        return 


    def pause_timer(self):
        playsound("Sound_effects\\506054__mellau__button-click-1.wav", False)
        # hide the pause button and show the start button
        self.pause_button.grid_remove()
        self.start_button.grid()
        
        # Update status variables
        self.session_state = "paused"
        # save the time remaining ensure the timer doesn't jump when unpausing
        self.time_remaining = self.end_time - time.time()
        self.state_label.config(text="Paused")
        print("The timer was paused!")
        return

    def reset_timer(self):
        playsound("Sound_effects\\506054__mellau__button-click-1.wav", False)
        # change timer state
        self.session_state = "idle"
        self.time_remaining = 0 

        # Hide the pause timer and show the start timer
        self.pause_button.grid_remove()
        self.start_button.grid()
        
        # Probably shouldn't hardcode, but whatever
        # Format label as "mm:00"
        mm_txt = self.work_interval.get()
        ss_txt = str(int(self.time_remaining % 60)).zfill(2)
        mm_ss_txt = f"{mm_txt}:{ss_txt}"
        self.timer_label.config(text=mm_ss_txt)
        self.state_label.config(text="Timer reset")
        print("The timer was reset!")
        return


    def countdown(self):
        # if the timer isn't running, then it shouldn't countdown 
        if self.session_state != "running":
            return 
        
        self.time_remaining = self.end_time - time.time()
        
        # Check if the time is up
        if self.time_remaining <= 0:
            # Handle end:
            self.end_timer()
            return

        mm_ss_txt = self.get_display_time(self.time_remaining)
        print(mm_ss_txt)
        self.timer_label.config(text=str(mm_ss_txt))
        # Schedule next tick?        
        self.root.after(1000, self.countdown)
    
    def end_timer(self):
        # The timer should now be idle 
        self.session_state = "idle"
        
        # Cycle to either "rest" or "work"
        self.work_session_active = not self.work_session_active
        
        # Hide the "pause" button and display the "start" button
        self.pause_button.grid_remove()
        self.start_button.grid()
        
        # Let the user know if it's time to work or rest by creating a pop up window
        cycle_msg = ""
        if self.work_session_active == True:
            cycle_msg = "working"
        else:
            cycle_msg = "resting"
            
        # make pop up window
        self.popupMsg('Timer Finished!', 'The timer has finished!'
                      f' Please Click the "start" button and begin {cycle_msg}.')
        
        self.state_label.config('Please click "Start"')
        return
    
    def popupMsg(self, title, msg):
        popup = messagebox.showinfo(title=title, message=msg)
        return
    
    def get_display_time(self, min):
        # Update display with time
        minutes_txt = str(int(min / 60))
        # Pad minutes with leading zeros 
        seconds_txt = str(int(min % 60)).zfill(2)
        return f"{minutes_txt}:{seconds_txt}"
    


# Set up GUI
def main():
    # set up the GUI
    root = tk.Tk()
    root.title("Pomodoro Timer")
    root.geometry('600x600')
    root.minsize(900,600)
    # create widgets for GUI
    app = PomodoroApp(root)
    # run the app!
    root.mainloop()
    
if __name__ == "__main__":
    main()