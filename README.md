# 🧱 Py Tetris — Python + Pygame

A classic Tetris-style game developed using **Python 3.12** and **Pygame**.
This project was created as a study and experimentation project focused on:

- Game loop architecture
- Collision systems
- Grid-based movement
- Piece rotation logic
- Score handling
- Real-time rendering with Pygame

---

🎮 Features

- Classic falling block gameplay
- Piece rotation system
- Line clearing mechanics
- Score tracking
- Increasing difficulty over time
- Keyboard controls
- Game Over detection
- Smooth rendering using Pygame

🛠 Technologies Used

- Python 3.12
- Pygame

---

## 📦 Installation

1. Clone the repository
git clone https://github.com/m4rkos/py-tetris.git
cd tetris-game
2. Create a virtual environment (optional but recommended)
Windows
python -m venv venv
venv\Scripts\activate
Linux / macOS
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install pygame

Or using requirements:

``pip install -r requirements.txt``

### ▶️ Running the Game

``python app.py``

---

## 🎹 Controls

**Key Action**:

``` text
⬅  Left Arrow      Move piece left
➡  Right Arrow     Move piece right
⬇   Down Arrow      Soft drop
⬆   Up Arrow        Rotate piece
Space               Hard drop
ESC                 Exit game
```

## 🧠 Project Structure

``` text
py-tetris/
│
├── app.py
├── game/
│   ├── board.py
│   ├── pieces.py
│   ├── collision.py
│   ├── score.py
│   └── settings.py
│
├── assets/
│   ├── sounds/
│   └── images/
│
├── requirements.txt
└── README.md
```

## 🚀 Future Improvements

Piece hold system
Next piece preview
Sound effects and music
Combo system
Level progression
Save high scores
Multiplayer mode
Mobile version with Kivy or Godot Engine

📚 Learning Goals

This project was developed to practice:

Object-oriented programming
Game development fundamentals
Real-time input handling
State management
Rendering optimization
Event-driven systems

### 📸 Preview

``` text
██████████████████
█                █
█      ██        █
█     ████       █
█      ██        █
█   ████████     █
█                █
██████████████████
```

### 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the project and open a pull request.

---

### 📄 License

This project is licensed under the MIT License.

---

### 👨‍💻 Author

Developed by **Marcos Eduardo** using Python and Pygame.
