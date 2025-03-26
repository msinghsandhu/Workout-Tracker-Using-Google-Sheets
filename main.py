import tkinter as tk
from tkinter import messagebox
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

APP_ID = os.getenv("SECRET_APP_ID")
API_KEY = os.getenv("SECRET_API_KEY")
NUTRITIONIX_ENDPOINT = os.getenv("SECRET_NUTRITIONIX_ENDPOINT")
SHEET_ENDPOINT = os.getenv("SECRET_SHEET_ENDPOINT")

# Function to handle workout input and send data
def submit_exercise():
    exercise_input = exercise_entry.get()
    if not exercise_input:
        messagebox.showerror("Input Error", "Please enter an exercise.")
        return

    workout_parameters = {
        "query": exercise_input
    }

    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
    }

    try:
        response = requests.post(url=NUTRITIONIX_ENDPOINT, json=workout_parameters, headers=headers)
        result = response.json()

        if 'exercises' not in result:
            messagebox.showerror("API Error", "Exercise not found or an error occurred.")
            return

        Date = datetime.now().strftime('%d/%m/%Y')
        Time = datetime.now().strftime('%H:%M:%S')
        Excercise = result['exercises'][0]['name']
        Duration = result['exercises'][0]['duration_min']
        Calories = result['exercises'][0]['nf_calories']

        results_parameters = {
            'sheet1': {
                'date': Date,
                'time': Time,
                'exercise': Excercise.title(),
                'duration': Duration,
                'calories': Calories
            }
        }

        response = requests.post(SHEET_ENDPOINT, json=results_parameters)
        if response.status_code == 200:
            messagebox.showinfo("Success", f"Workout data recorded for {Excercise.title()}")
        else:
            messagebox.showerror("Error", "Failed to record data in sheet.")

    except Exception as e:
        messagebox.showerror("Request Error", str(e))

# Set up the main window
root = tk.Tk()
root.title("Workout Logger")
root.geometry("400x300")
root.config(bg="#f5f5f5")  # Light background color

# Styling
label_style = {'font': ('Arial', 12, 'bold'), 'bg': '#f5f5f5'}
button_style = {'bg': '#4CAF50', 'fg': 'white', 'font': ('Arial', 10, 'bold')}
entry_style = {'font': ('Arial', 12), 'width': 30}

# UI Elements
title_label = tk.Label(root, text="Log Your Exercise", **label_style)
title_label.pack(pady=20)

exercise_label = tk.Label(root, text="Enter Exercise:", **label_style)
exercise_label.pack()

exercise_entry = tk.Entry(root, **entry_style)
exercise_entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=submit_exercise, **button_style)
submit_button.pack(pady=20)

# Run the app
root.mainloop()
