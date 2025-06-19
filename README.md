# TIC-TAC-TOE-AI-
Implement an AI agent that plays the classic game of Tic-Tac-Toe  against a human player. You can use algorithms like Minimax with  or without Alpha-Beta Pruning to make the AI player unbeatable.  This project will help you understand game theory and basic search  algorithms
Tic Tac Toe AI (Single Player Game)
This is a Tic Tac Toe game where the player competes against a computer powered by the Minimax algorithm (without alpha-beta pruning). The game features a Flask backend and a responsive frontend rendered using HTML, CSS, and JavaScript.

🧩 Features
🎮 Single-player mode: Human vs Computer

🧠 AI logic using Minimax algorithm (perfect play)

🔄 Real-time interaction with Flask API

📱 Responsive frontend layout using HTML/CSS

❌ X (player) and ⭕ O (computer)

📂 Project Structure
bash
Copy code
.
├── app.py                  # Flask backend with AI logic
├── templates/
│   └── index.html          # Frontend UI
├── static/
│   ├── style.css           # CSS styling (if used)
│   └── script.js           # Game logic and API interaction
├── README.md               # Project documentation


🚀 How to Run the Project
  Clone the repository

bash
Copy code
git clone https://github.com/your-username/tic-tac-toe-ai.git
cd tic-tac-toe-ai
(Optional) Create a virtual environment

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy code
pip install flask flask_cors
Run the app

bash
Copy code
python app.py
Open your browser

cpp
Copy code
http://127.0.0.1:5000
🤖 AI Logic: Minimax Algorithm
The computer uses the Minimax algorithm to calculate the optimal move at every step.

It assumes the opponent plays optimally and chooses the move that minimizes the possible loss.

This makes the AI unbeatable unless you play perfectly.


💡 Future Improvements
Add difficulty levels (easy, medium, hard)

Add multiplayer mode

Add animations and sound effects

Deploy to platforms like Heroku or Render









