# Spotify Mood Tracker

A personal, non-commercial project that combines my daily music listening history with local weather data to explore how my mood changes over time — for example, whether rainy afternoons change what I listen to.

## How it works

1. Spotify scrobbles every track I play to my Last.fm profile.
2. This project reads my listening history through the **Last.fm API** (`user.getRecentTracks`).
3. *(Planned)* It matches each listening session with the weather at that time and place.
4. *(Planned)* It summarises the results as simple personal mood insights.

## Project status

Early development — built step by step as a learning project.

- [x] Environment and repository setup
- [x] Fetch and print recent tracks from the Last.fm API
- [ ] Store listening history locally
- [ ] Add weather data
- [ ] Mood insights

## Tech stack

- Python 3
- [`requests`](https://requests.readthedocs.io/) for HTTP calls
- [`python-dotenv`](https://pypi.org/project/python-dotenv/) for configuration
- [Last.fm API](https://www.last.fm/api)

## Setup

```bash
git clone git@github.com:Micaela888/spotify-mood-tracker.git
cd spotify-mood-tracker
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then fill in your own Last.fm API key and username
```

## Usage

```bash
python src/moodtracker/lastfm.py
```

Prints the last 10 tracks played by the configured Last.fm user.

## Data & privacy

- Only reads public listening data from the Last.fm account configured in `.env`.
- Read-only: it never writes to or modifies any Last.fm account.
- Requests are made at a low, personal-use rate.
- API keys are kept in a local `.env` file and are never committed.
- Use of the Last.fm API is subject to the [Last.fm API Terms of Service](https://www.last.fm/api/tos). Anyone running this project must use their own API key and comply with those terms.
- Not affiliated with or endorsed by Last.fm or Spotify. Music data provided by [Last.fm](https://www.last.fm).

## License

[MIT](LICENSE) © 2026 Micaela Sofia Agnolini
