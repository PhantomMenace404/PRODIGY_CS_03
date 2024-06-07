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
        toggle_button.config(text='Show Password')
    else:
        entry.config(show='')
        toggle_button.config(text='Hide Password')

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

# Create an entry widget
entry = ttk.Entry(root, show="*", font=("Arial", 14), width=30)
entry.pack(pady=10)
entry.bind('<Return>', on_check_password)  # Bind Enter key to check password

# Create a button to toggle password visibility
toggle_button = ttk.Button(root, text="Show Password", command=toggle_password_visibility)
toggle_button.pack(pady=5)

# Create a button to check password complexity
button = ttk.Button(root, text="Check Password", command=on_check_password)
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()