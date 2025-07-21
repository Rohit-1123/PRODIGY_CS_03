import tkinter as tk
import re

def check_password_strength():
    password = password_entry.get()
    feedback = []
    
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    if length_error:
        feedback.append("• Minimum 8 characters required")
    if uppercase_error:
        feedback.append("• Add at least one uppercase letter")
    if lowercase_error:
        feedback.append("• Add at least one lowercase letter")
    if digit_error:
        feedback.append("• Add at least one number")
    if special_char_error:
        feedback.append("• Add at least one special character (!/@/#/$/*)")

    total_errors = sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])

    if total_errors == 0:
        strength_label.config(text="✅ Strong password", fg="green")
    elif total_errors <= 2:
        strength_label.config(text="🟡 Medium password", fg="orange")
    else:
        strength_label.config(text="🔴 Weak password", fg="red")

    feedback_text.delete("1.0", tk.END)
    if feedback:
        feedback_text.insert(tk.END, "Suggestions:\n" + "\n".join(feedback))
    else:
        feedback_text.insert(tk.END, "Your password meets all the criteria.")

def toggle_password():
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x330")
root.resizable(False, False)

tk.Label(root, text="Enter your password:", font=("Arial", 12)).pack(pady=10)

password_entry = tk.Entry(root, show='*', font=("Arial", 12), width=30)
password_entry.pack(pady=5)

# Show password checkbox
show_var = tk.BooleanVar()
tk.Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password).pack()

tk.Button(root, text="Check Strength", font=("Arial", 12), command=check_password_strength).pack(pady=10)

strength_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
strength_label.pack()

feedback_text = tk.Text(root, height=6, width=45, font=("Arial", 10))
feedback_text.pack(pady=5)

root.mainloop()
