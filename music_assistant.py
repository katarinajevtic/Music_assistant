import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sqlite3
import speech_recognition as sr
import config

# Connect to Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=config.SPOTIFY_CLIENT_ID,
                                                      client_secret=config.SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Initialize SQLite Database
conn = sqlite3.connect('user_preferences.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS preferences (id INTEGER PRIMARY KEY, mood TEXT)''')
conn.commit()


# Collect Song Data
def collect_song_data(mood):
    try:
        results = sp.search(q='mood:' + mood, type='track', limit=7)  # Limiting to 7 songs for better performance
        songs = []
        for track in results['tracks']['items']:
            song_name = track['name']
            artist = track['artists'][0]['name']
            image_url = track['album']['images'][0]['url'] if track['album']['images'] else None
            popularity = track['popularity']
            songs.append({'song_name': song_name, 'artist': artist, 'image_url': image_url, 'popularity': popularity})
        return songs
    except spotipy.SpotifyException as e:
        st.error("An error occurred while accessing the Spotify API. Please try again later.")
        st.error(f"Error message: {e}")
        return []


# User Interaction (Speech Recognition or CLI)
def get_user_mood():
    st.subheader("Choose how you'd like to input your mood:")
    input_method = st.radio("", ('Speech Recognition', 'Typing mood'))

    mood = None
    if input_method == 'Speech Recognition':
        st.info("Please speak your current mood:")
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
        try:
            mood = recognizer.recognize_google(audio)
            st.success(f"Recognized mood: {mood}")
        except sr.UnknownValueError:
            st.error("Sorry, I couldn't understand your mood.")
        except sr.RequestError:
            st.error("Sorry, there was an issue with the speech recognition service.")
    else:
        mood = st.text_input("Enter your current mood (e.g., happy, sad, energetic, etc.):")

    return mood


# Recommendation Engine
def recommend_music(mood, songs):
    recommended_songs = []
    if songs:
        # Sort songs based on popularity
        sorted_songs = sorted(songs, key=lambda x: x['popularity'], reverse=True)

        # Limit the number of recommended songs
        recommended_songs = sorted_songs[:7]  # Limiting to top 7 recommended songs
    else:
        st.error("No songs found matching your mood. Try a different mood!")
    return recommended_songs


# Main Function
def main():
    st.title("Smart Music Assistant")

    mood = get_user_mood()

    # Validate user input (mood)
    if mood and mood.strip():
        with conn:
            c.execute("INSERT INTO preferences (mood) VALUES (?)", (mood,))
        songs = collect_song_data(mood)
        recommended_songs = recommend_music(mood, songs)

        if recommended_songs:
            st.subheader("Recommended Songs:")
            for song in recommended_songs:
                song_name, artist, image_url = song['song_name'], song['artist'], song['image_url']
                st.write(f"**{song_name}** by {artist}")
                if image_url:
                    st.image(image_url, caption=song_name, width=200)
                else:
                    st.write("Image not available")
        else:
            st.error("No songs found matching your mood.")


if __name__ == "__main__":
    main()
