import random
import tkinter as tk
from tkinter import messagebox

# Function to check the user's guess
def check_guess(event=None):
    try:
        guess = int(guess_entry.get())
        if guess == secret_number:
            messagebox.showinfo("Congratulations!", "You guessed the correct number!")
            reset_game()
        elif guess < secret_number:
            result_label.config(text="Too low! Try guessing higher.", fg="red")
        else:
            result_label.config(text="Too high! Try guessing lower.", fg="red")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

# Function to reset the game
def reset_game():
    global secret_number
    secret_number = random.randint(1, 100)
    result_label.config(text="", fg="black")
    guess_entry.delete(0, tk.END)

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Create main window
root = tk.Tk()
root.title("Number Guessing Game")

# Set window size and position
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Styling
root.configure(bg="#f0f0f0")
root.resizable(False, False)

# Guess Entry
guess_label = tk.Label(root, text="Enter your guess:", bg="#f0f0f0", fg="black", font=("Arial", 12))
guess_label.pack(pady=5)
guess_entry = tk.Entry(root, font=("Arial", 12))
guess_entry.pack(pady=5)

# Number Range Label
range_label = tk.Label(root, text="Guess a number between 1 and 100", bg="#f0f0f0", fg="black", font=("Arial", 12))
range_label.pack(pady=5)

# Guess Button
guess_button = tk.Button(root, text="Guess", command=check_guess, font=("Arial", 12))
guess_button.pack(pady=5)
guess_entry.bind("<Return>", check_guess)

# Result Label
result_label = tk.Label(root, text="", bg="#f0f0f0", fg="black", font=("Arial", 12))
result_label.pack(pady=5)

# Reset Button
reset_button = tk.Button(root, text="Reset", command=reset_game, font=("Arial", 12))
reset_button.pack(pady=5)

root.mainloop()
