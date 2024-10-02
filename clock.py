import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Function to update the time on the label
def time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, time)

# Configure the label to display the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

# Call the time function to initiate the clock
time()

# Start the main event loop
root.mainloop()
