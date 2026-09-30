# 📦 Release Notes — Py Tetris

## Version 1.0.0 (Initial Release)

We are excited to announce the initial release of **Py Tetris**, a modular, arcade-style classic Tetris clone built using **Python 3** and **Pygame**.

---

### ✨ Key Features

#### 🎮 Gameplay & Mechanics
- **Classic Tetris Mechanics**: Standard grid (10x20) block falling, movement, and collision detection.
- **7-Bag Random Generator**: Balanced piece spawning system adhering to modern Tetris standards.
- **Next Piece Preview**: Real-time side panel preview of the upcoming tetromino.
- **Ghost Piece**: Visual projection indicating exactly where the active piece will land.
- **Line Clearing & Scoring**: Real-time score calculation based on cleared lines with increasing difficulty.
- **Instant Hard Drop & Soft Drop**: Smooth keyboard controls for quick piece placement and rapid descent.

#### 🔊 Audio & Visuals
- **Background Music**: Looping 8-bit arcade soundtrack during gameplay.
- **Action Sound Effects**: Custom audio feedback for moving, rotating, soft dropping, hard dropping, line clears, and game over events.
- **Game Over Splash**: Graphical Game Over screen overlay with restart and exit options.
- **Clean UI**: Integrated side panel displaying current score, control guide, and next piece preview.

#### 🛠 Project Architecture & Tooling
- **Modular Codebase**: Clean separation of concerns with `game/core.py` and configuration variables in `game/utils/vars.py`.
- **One-Click Runner**: Automated shell script (`run.sh`) that manages Python virtual environment (`venv`) setup and dependency installation.
- **Asset Pipeline**: Organized directory layout for audio tracks, SFX, and graphical assets.

---

### 🎹 Controls Reference

| Key | Action |
| :--- | :--- |
| <kbd>←</kbd> / <kbd>→</kbd> | Move Piece Left / Right |
| <kbd>↓</kbd> | Soft Drop |
| <kbd>↑</kbd> | Rotate Piece |
| <kbd>Space</kbd> | Hard Drop (Instant Drop) |
| <kbd>ESC</kbd> | Quit Game |

---

### 🚀 Getting Started

Ensure you have Python 3 installed, then launch the game with:

```bash
./run.sh
```

Or manually:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
