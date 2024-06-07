import re

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

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to check its complexity: ")
    result = check_password_complexity(password)
    print(result)
