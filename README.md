# Witch Flight — 30-Second Haunted-House Challenge 🎃

A Halloween arcade game powered by Python/Streamlit and an HTML5 Canvas.

## Features
- 30-second rounds; hitting a tree ends the round instantly
- Candy +10, magic pumpkin +25
- Live score and screenshot-ready final score
- Spooky witch, responsive mouse controls, keyboard (up/down or W/S), touch drag
- Anna Hoang logo in top-right corner
- **Original procedural haunted-house music** plus candy, pumpkin, crash and victory sounds
- Sound ON/OFF toggle; sound starts only after the player clicks Start
- No external audio files, accounts or leaderboard

## Run locally

Open PowerShell in this folder:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Deploy

1. Create a public GitHub repository.
2. Upload `app.py`, `game.html`, `requirements.txt`, `.gitignore` and this README to the repository root.
3. Open https://share.streamlit.io/ and create an app from your GitHub repository.
4. Set the main file path to `app.py` and deploy.
5. Test the game, including audio, in a desktop and mobile browser before posting the link.

## Notes

The music and sound effects are synthesized using the browser Web Audio API (not an external music recording). Some browsers require an interaction to enable sound; press Start Game. The Sound ON/OFF control works during gameplay.
