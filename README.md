# 🎵 Smart Music Assistant with Sentiment Analysis 
A Python-based music assistant that tailors song recommendations based on your mood. This project leverages the Spotify API, sentiment analysis, and a simple yet interactive interface built with Streamlit. Users can input their mood either through speech recognition or by typing, and the app will recommend songs that match their mood, displaying song details along with album cover images.

## 🚀 Features

+ Mood-Based Song Recommendations: Tailored recommendations based on the user's mood.
+ Spotify Integration: Fetches song data and album covers using the Spotify API.
+ Interactive Interface: Built with Streamlit for a simple and user-friendly experience.
+ Speech Recognition: Users can input their mood through voice commands.
+ SQLite Database: Stores user mood preferences for future reference.

## 🛠️ Technologies Used

+ Python: Core language for the project.
+ Spotipy: A lightweight Python library for the Spotify Web API.
+ Streamlit: Used to create the interactive user interface.
+ SpeechRecognition: Allows the app to recognize spoken input.
+ SQLite: For storing user preferences.
  
## Prerequisites
Ensure you have the following installed:
+ Python 3.x
+ Spotipy (pip install spotipy)
+ SQLite (comes pre-installed with Python)

## 🔧 Setup Instructions
1. Clone the Repository:
   
```
git clone https://github.com/yourusername/smart-music-assistant.git
cd smart-music-assistant   
 ```
2. Install Dependencies:

```
pip install -r requirements.txt
```
3. Set Up Spotify API Credentials:

+ Create a Spotify Developer account [here.](https://developer.spotify.com)
+ Create an app to get your CLIENT_ID and CLIENT_SECRET.
+ Replace 'YOUR_CLIENT_ID' and 'YOUR_CLIENT_SECRET' in the code with your actual credentials.
4. Run the Script:

```
streamlit music_assistant.py
```

## 🎤 How It Works
1. Input Mood: Users can input their mood either through speech recognition or by typing it into the interface.
2. Fetch Songs: The app searches for songs on Spotify that match the mood.
3. Display Results: Recommended songs are displayed horizontally with their album cover images.
U4. ser Preferences: The user's mood is stored in an SQLite database for future reference.

![music_assistant](https://github.com/user-attachments/assets/253db7de-a2f6-4ad3-be48-8689d23334dc)

![music_assistant2](https://github.com/user-attachments/assets/75d63b4c-1012-42ed-861d-3ee5778f1fdf)




## 📝 License
This project is licensed under the MIT License. See the [LICENCE](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) file for more details.     
