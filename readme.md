# 🏋️‍♂️ Workout Logger 🏃‍♀️
📌 Description
Workout Logger is a Python-based desktop application built with Tkinter that helps users track their workouts 💪. It fetches exercise details like calories burned & duration using the Nutritionix API 🥗 and stores the data in Google Sheets via Sheetly 📊.

This tool is perfect for fitness enthusiasts who want a simple & automated way to log their exercises! ✅


## 🔄 Project Flow
### 1️⃣ User Input:

Enter an exercise (e.g., "ran 5 miles" or "30 minutes cycling") in the Tkinter app.

Click "Submit" to process the request.

### 2️⃣ Fetching Data (Nutritionix API) 🥗:

The app sends a request to Nutritionix, retrieving exercise name, duration, and calories burned 🔥.

### 3️⃣ Saving to Google Sheets (Sheetly API) 📊:

The data, along with date & time, is sent to Sheetly to log in a Google Sheet.

If successful, a confirmation pop-up appears ✅.

### 4️⃣ Error Handling ❌:

If the API request fails, an error message is displayed 🚨.

