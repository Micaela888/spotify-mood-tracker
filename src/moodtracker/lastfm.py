"""Funciones para pedirle datos a la API de Last.fm."""

import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://ws.audioscrobbler.com/2.0/"
API_KEY = os.getenv("LASTFM_API_KEY")
USER = os.getenv("LASTFM_USER")


def _request(method, **params):
    """Hace una petición a la API de Last.fm y devuelve la respuesta como diccionario."""
    params["method"] = method 
    params["api_key"] = API_KEY
    params["format"] = "json"

    response = requests.get(
        API_URL,
        params=params,
        headers={"User-Agent": "SpotifyMoodTracker/0.1"},
        timeout=10,
    )
    data = response.json()

    if "error" in data:
        raise RuntimeError(f"Error de Last.fm {data['error']}: {data['message']}")

    return data


def get_recent_tracks(user, limit=10):
    """Devuelve una lista con las últimas canciones escuchadas por el usuario."""
    data = _request("user.getrecenttracks", user=user, limit=limit)

    tracks = []
    for item in data["recenttracks"]["track"]:
        if "date" not in item:
            continue

        tracks.append({
            "artist": item["artist"]["#text"],
            "title": item["name"],
            "played_at": datetime.fromtimestamp(int(item["date"]["uts"])),
        })

    return tracks


if __name__ == "__main__":
    for track in get_recent_tracks(USER):
        print(f"{track['played_at']:%d/%m/%Y %H:%M}  {track['artist']} — {track['title']}")