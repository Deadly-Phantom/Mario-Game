# Mario Game

A simple, fun platformer inspired by classic Mario gameplay, built with Python and Pygame. Run, jump, and dodge Goombas as you explore a side-scrolling world!

---

## Features

- **Fullscreen Gameplay:** Immersive experience with a scrolling camera that follows Mario.
- **Classic Controls:**  
  - Arrow keys to move left/right  
  - Up arrow to jump
- **Goomba Enemies:** Goombas move toward Mario and end the game on collision.
- **Game Over Screen:** Restart by clicking after losing.
- **Custom Graphics:** Mario, Goombas, and a background image for a nostalgic feel.
- **Simple Physics:** Gravity and jumping mechanics for platformer action.

---

## Getting Started

### Option 1: Download the PyInstaller Binary

- **Recommended for most users!**
- Download the binary for your platform from the [Releases](../../releases) page.
- Unzip the file and run the executable:
  - **macOS:** Double-click `Mario Game.app` or run from Terminal.
  - **Windows:** Double-click `Mario Game.exe`.
- No Python or Pygame installation required!

### Option 2: Run from Source

1. **Install Python 3**  
   Download from [python.org](https://www.python.org/downloads/).

2. **Install Pygame**  
   Open a terminal and run:
   ```
   pip install pygame
   ```

3. **Download the Source Code**  
   Clone this repository or download the ZIP.

4. **Add Assets**  
   Place `mario.png`, `goomba.png`, and `wallpaper.jpg` in the same directory as `mario.py`.

5. **Run the Game**  
   ```
   python mario.py
   ```

---

## Controls

- **Left/Right Arrow:** Move Mario  
- **Up Arrow:** Jump  
- **Escape:** Quit the game

---

## Objective

Avoid Goombas and survive as long as you can!

---

## Customization

- **Ground Level:**  
  If Mario or Goombas don't align with the ground, adjust the `GROUND_Y` constant in `mario.py`.
- **Jump Height & Gravity:**  
  Tweak `JUMP_STRENGTH` and `GRAVITY` in `mario.py` for your preferred feel.

---

## Known Issues

- Mario and Goombas may not align perfectly with the background ground—adjust `GROUND_Y` if needed.
- No sound effects or music (yet!).

---

## License

This project is for educational and personal use.  
All character and background images are for demonstration purposes only.

---

## Feedback

Please report bugs or suggestions via [Issues](../../issues) or Pull Requests.

---

**Enjoy the game!**
