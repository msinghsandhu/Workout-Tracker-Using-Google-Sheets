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

## 🛠️ Setup Instructions
### 1️⃣ Get API Keys & Endpoints 🔑
Before running the project, create API credentials for Nutritionix & Sheetly:

Nutritionix API 🥗:

Sign up at Nutritionix Developer

Create an app & get APP_ID and API_KEY 🔑

Obtain the API endpoint for exercise data.

Sheetly API 📊:

Sign up at Sheetly and connect it to Google Sheets.

Create an endpoint that allows POST requests to store workout data.

### 2️⃣ Store API Credentials Securely 🔒
Create a .env file in your project directory & add your credentials:
SECRET_APP_ID=your_nutritionix_app_id
SECRET_API_KEY=your_nutritionix_api_key
SECRET_NUTRITIONIX_ENDPOINT=https://trackapi.nutritionix.com/v2/natural/exercise
SECRET_SHEET_ENDPOINT=your_sheetly_endpoint

### 3️⃣ Install Dependencies 📦
Ensure you have the required Python libraries installed:
pip install requests python-dotenv tk

### 4️⃣ Run the Application 🚀
Execute the script using:
python workout_logger.py

## 🚀 Future Improvements
🔹 Add data visualization 📈 (e.g., workout trends over time).
🔹 Implement user authentication 🔑 for personalized tracking.
🔹 Support multiple exercise inputs in a single request.