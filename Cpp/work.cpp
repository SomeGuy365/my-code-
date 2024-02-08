#include <iostream>

void boardprint(char board[3][3]) {
    std::cout << "   |     |  \n";
    std::cout << " " << board[0][0] << " |  " << board[0][1] << "  | " << board[0][2] << "  \n";
    std::cout << "___|_____|____\n";
    std::cout << "   |     |  \n";
    std::cout << " " << board[1][0] << " |  " << board[1][1] << "  | " << board[1][2] << "  \n";
    std::cout << "___|_____|____\n";
    std::cout << "   |     |  \n";
    std::cout << " " << board[2][0] << " |  " << board[2][1] << "  | " << board[2][2] << "  \n";
    std::cout << "   |     |  \n";
}

bool boardsolve(char board[3][3]) {
    for (int i;i<3;i++) {
        if (board[i][0]==board[i][1] && board[i][0]==board[i][2] || board[0][i]==board[1][i] && board[0][i]==board[2][i]) {//rows
            return true;
        }
    }
    if (board[0][0]==board[1][1] && board[1][1]==board[2][2] || board[0][2]==board[1][1] && board[1][1]==board[2][0]) {//columns
        return true;
    }
    if (board[0][0]==board[1][1] && board[1][1]==board[2][2] || board[0][2]==board[1][1] && board[1][1]==board[2][0]) {//diagnals
        return true;
    }
    return false;
}

int main() {
    bool win = false;
    int row = 0;
    int column = 0;
    char turn = 'X';
    char boards[3][3] = {
        {'1','2','3'},
        {'4','5','6'},
        {'7','8','9'}};
    
    while (win==false) {
        boardprint(boards);
        std::cout << "Its " << turn << "s turn" << std::endl;
        std::cout << "Enter a row:";
        std::cin >> row;
        std::cout << "Enter a column:";
        std::cin >> column;
        if (boards[row-1][column-1] !='X' && boards[row-1][column-1] !='O') {
            boards[row-1][column-1] = turn; 
        }
        else {
            std::cout << "Not cool,no turn for u" << std::endl;
        }
        win = boardsolve(boards);
        if (turn == 'X') {
            turn = 'O';
        }
        else {
            turn = 'X';
        }
        continue;
    }
    if (turn == 'X') {
        std::cout << "Player O Won!";
    }
    else {
        std::cout << "Player X Won!";
    }
    return 0;
}