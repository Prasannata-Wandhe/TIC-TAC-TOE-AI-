from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def display_board(board):
    print("\nCurrent Board:")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print()
        symbol = "_" if board[i] == 0 else ("X" if board[i] == -1 else "O")
        print(symbol, end=" ")
    print("\n")

def user_move(board):
    try:
        pos = int(input("Enter X's position (1-9): "))
        if pos < 1 or pos > 9 or board[pos - 1] != 0:
            print("Invalid move! Try again.")
            user_move(board)
        else:
            board[pos - 1] = -1
    except ValueError:
        print("Please enter a valid number.")
        user_move(board)

def evaluate(board):
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for line in win_states:
        a, b, c = line
        if board[a] == board[b] == board[c] and board[a] != 0:
            return board[a]
    return 0

def minimax(board, player):
    winner = evaluate(board)
    if winner != 0:
        return winner * player

    best_value = -2
    for i in range(9):
        if board[i] == 0:
            board[i] = player
            score = -minimax(board, -player)
            board[i] = 0
            if score > best_value:
                best_value = score
    return best_value if best_value != -2 else 0

def computer_move(board):
    best_score = -2
    best_move = -1
    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            score = -minimax(board, -1)
            board[i] = 0
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 1

def main():
    board = [0] * 9
    print("Tic Tac Toe: You (X) vs Computer (O)")
    player_order = int(input("Do you want to play first or second? (1/2): "))

    for turn in range(9):
        if evaluate(board) != 0:
            break
        if (turn + player_order) % 2 == 0:
            computer_move(board)
        else:
            display_board(board)
            user_move(board)

    display_board(board)
    result = evaluate(board)
    if result == -1:
        print("You Win! 🎉")
    elif result == 1:
        print("Computer Wins! 💻")
    else:
        print("It's a Draw!")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    board = data['board']
    move = data['move']

    if board[move] != 0:
        return jsonify({'error': 'Invalid move'}), 400

    board[move] = -1  # Player move (X)

    if evaluate(board) == -1:
        return jsonify({'board': board, 'winner': 'player'})

    if 0 not in board:
        return jsonify({'board': board, 'winner': 'draw'})

    computer_move(board)

    result = evaluate(board)
    if result == 1:
        return jsonify({'board': board, 'winner': 'computer'})
    elif 0 not in board:
        return jsonify({'board': board, 'winner': 'draw'})
    else:
        return jsonify({'board': board, 'winner': None})

if __name__ == '__main__':
    app.run(debug=True)
