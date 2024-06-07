import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def check_password_complexity(password):
    # Define the criteria for password complexity
    length_criteria = len(password) >= 8
    upper_case_criteria = bool(re.search(r'[A-Z]', password))
    lower_case_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Calculate score based on the criteria
    score = sum([length_criteria, upper_case_criteria, lower_case_criteria, digit_criteria, special_char_criteria])
    
    # Provide feedback based on the score
    feedback = ""
    if score == 5:
        feedback = "Strong password"
    elif score == 4:
        feedback = "Moderate password"
    elif score == 3:
        feedback = "Weak password"
    else:
        feedback = "Very weak password"
    
    # Detailed feedback
    if not length_criteria:
        feedback += "\n- Password should be at least 8 characters long."
    if not upper_case_criteria:
        feedback += "\n- Password should include at least one uppercase letter."
    if not lower_case_criteria:
        feedback += "\n- Password should include at least one lowercase letter."
    if not digit_criteria:
        feedback += "\n- Password should include at least one digit."
    if not special_char_criteria:
        feedback += "\n- Password should include at least one special character."
    
    return feedback

def on_check_password(event=None):
    password = entry.get()
    if password:
        result = check_password_complexity(password)
        messagebox.showinfo("Password Complexity", result)
    else:
        messagebox.showwarning("Input Error", "Please enter a password")

def toggle_password_visibility():
    if entry.cget('show') == '':
        entry.config(show='*')
        canvas.itemconfig(eye_open, state='hidden')
        canvas.itemconfig(eye_slash, state='normal')
    else:
        entry.config(show='')
        canvas.itemconfig(eye_open, state='normal')
        canvas.itemconfig(eye_slash, state='hidden')

def on_close():
    print("\nThank you for using SecurePassChecker. Have a great day!")
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("SecurePassChecker")

# Set window size and center it on the screen
root.geometry("400x250")
root.eval('tk::PlaceWindow . center')

# Use ttk for a modern look
style = ttk.Style()
style.configure("TLabel", font=("Arial", 14))
style.configure("TButton", font=("Arial", 14))

# Create a label
label = ttk.Label(root, text="Enter your password:")
label.pack(pady=10)

# Create an entry widget with an eye icon button
entry_frame = ttk.Frame(root)
entry_frame.pack(pady=10)

entry = ttk.Entry(entry_frame, show="*", font=("Arial", 14), width=28)
entry.pack(side=tk.LEFT, padx=5)
entry.bind('<Return>', on_check_password)  # Bind Enter key to check password

# Create a canvas for the eye icon
canvas = tk.Canvas(entry_frame, width=24, height=24, highlightthickness=0)
canvas.pack(side=tk.LEFT)

# Draw the eye icon
eye_open = canvas.create_oval(2, 10, 22, 14, outline="black", fill="")
canvas.create_oval(10, 8, 14, 16, outline="black", fill="black")
eye_slash = canvas.create_line(2, 2, 22, 22, fill="red", width=2)
canvas.itemconfig(eye_slash, state='hidden')

# Bind the canvas click event to toggle password visibility
canvas.bind("<Button-1>", lambda e: toggle_password_visibility())

# Create a button to check password complexity with rounded edges
style.configure("RoundedButton.TButton", font=("Arial", 14), relief="flat", padding=10)
style.map("RoundedButton.TButton",
          relief=[("active", "flat")],
          background=[("active", "#ececec")])

button = ttk.Button(root, text="Check Password", command=on_check_password, style="RoundedButton.TButton")
button.pack(pady=10)

# Handle the close event
root.protocol("WM_DELETE_WINDOW", on_close)

# Start the GUI event loop
try:
    root.mainloop()
except KeyboardInterrupt:
    on_close()
