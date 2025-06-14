
def get_song_for_mood(mood: str) -> str:
    playlist = {
        "gl\u00fccklich": "Happy Song - Artist",
        "traurig": "Sad Song - Artist",
        "w\u00fctend": "Angry Song - Artist",
        "ruhig": "Calm Song - Artist",
        "neutral": "Neutral Song - Artist",
    }
    song = playlist.get(mood, "Neutral Song - Artist")
    print(f"[Spotify] Spiele {song}")
    return song
