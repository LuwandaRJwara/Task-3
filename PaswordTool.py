import tkinter as tk
from tkinter import messagebox
import re
import string

# Password strength checking functions (same as before)
def check_length(password):
    """Check if the password has a minimum length of 8 characters."""
    return len(password) >= 8

def check_uppercase(password):
    """Check if the password has at least one uppercase letter."""
    return bool(re.search(r'[A-Z]', password))

def check_lowercase(password):
    """Check if the password has at least one lowercase letter."""
    return bool(re.search(r'[a-z]', password))

def check_numbers(password):
    """Check if the password has at least one digit."""
    return bool(re.search(r'\d', password))

def check_special_characters(password):
    """Check if the password has at least one special character."""
    special_characters = string.punctuation
    return any(char in special_characters for char in password)

def check_common_passwords(password):
    """Check if the password is a common password."""
    common_passwords = [
        'password', '123456', '123456789', 'qwerty', 'abc123', 'password1', '12345'
    ]
    return password.lower() not in common_passwords

def check_repeated_characters(password):
    """Check if the password contains repeated characters or patterns."""
    return len(set(password)) > len(password) // 2  # Ensure enough variety

def password_strength(password):
    """Assess the strength of the password."""
    score = 0
    feedback = []

    if check_length(password):
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if check_uppercase(password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if check_lowercase(password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if check_numbers(password):
        score += 1
    else:
        feedback.append("Include at least one digit.")

    if check_special_characters(password):
        score += 1
    else:
        feedback.append("Include at least one special character (e.g., !@#$%^&*()).")

    if check_common_passwords(password):
        score += 1
    else:
        feedback.append("Your password is too common. Try something more unique.")

    if check_repeated_characters(password):
        score += 1
    else:
        feedback.append("Avoid repeated characters or patterns.")

    # Determine strength based on score
    if score == 6:
        return "Very Strong", feedback
    elif score == 5:
        return "Strong", feedback
    elif score == 4:
        return "Moderate", feedback
    elif score == 3:
        return "Weak", feedback
    else:
        return "Very Weak", feedback

# GUI for password strength checker
class PasswordStrengthCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")

        # Set the window size
        self.root.geometry("400x300")

        # Create widgets
        self.label = tk.Label(root, text="Enter your password:")
        self.label.pack(pady=10)

        self.password_entry = tk.Entry(root, width=30, show="*")
        self.password_entry.pack(pady=10)

        self.check_button = tk.Button(root, text="Check Strength", command=self.check_password_strength)
        self.check_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 10), justify=tk.LEFT)
        self.feedback_label.pack(pady=10)

    def check_password_strength(self):
        # Get password input
        password = self.password_entry.get()

        # Check password strength
        strength, feedback = password_strength(password)

        # Display strength
        self.result_label.config(text=f"Strength: {strength}")

        # Display feedback
        feedback_text = "\n".join(feedback) if feedback else "Your password is strong. Well done!"
        self.feedback_label.config(text=feedback_text)

        # Show a message box for very weak passwords
        if strength == "Very Weak":
            messagebox.showwarning("Weak Password", "Your password is too weak. Please improve it.")
            self.result_label.config(fg="red")

        # Show a message box for very strong passwords
        elif strength == "Very Strong":
            messagebox.showwarning("Strong Passwaord.")
            self.result_label.config(fg="green")

        
            

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthCheckerApp(root)
    root.mainloop()
