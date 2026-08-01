const rows = 6;
const cols = 7;
let currentPlayer = 1;
let playerOne = '';
let playerTwo = '';
const boardState = Array.from({ length: rows }, () => Array(cols).fill(0));

const boardEl = document.getElementById('board');
const messageEl = document.getElementById('message');

// Criar células
function createBoard() {
  boardEl.innerHTML = '';
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const cell = document.createElement('div');
      cell.classList.add('cell');
      cell.dataset.row = r;
      cell.dataset.col = c;
      cell.addEventListener('click', () => dropPiece(c));
      boardEl.appendChild(cell);
    }
  }
}

// Lógica de queda
function dropPiece(col) {
  for (let r = rows - 1; r >= 0; r--) {
    if (boardState[r][col] === 0) {
      boardState[r][col] = currentPlayer;
      const cell = document.querySelector(`.cell[data-row="${r}"][data-col="${col}"]`);
      cell.classList.add(currentPlayer === 1 ? 'blue' : 'red');
      if (checkWin(r, col)) {
        messageEl.textContent = currentPlayer === 1 ? `${playerOne} wins!` : `${playerTwo} wins!`;
        disableBoard();
      } else {
        currentPlayer = currentPlayer === 1 ? 2 : 1;
        messageEl.textContent = currentPlayer === 1
          ? `${playerOne}, it's your turn. Please pick a column to drop your blue chip.`
          : `${playerTwo}, it's your turn. Please pick a column to drop your red chip.`;
      }
      return;
    }
  }
  alert('Column is full!');
}

// Verificação simples de vitória (horizontal, vertical, diagonal)
function checkWin(row, col) {
  const directions = [
    [0, 1], [1, 0],   [1, 1], [1, -1]
  ];
  for (const [dr, dc] of directions) {
    let count = 1;
    count += countDirection(row, col, dr, dc);
    count += countDirection(row, col, -dr, -dc);
    if (count >= 4) return true;
  }
  return false;
}

function countDirection(r, c, dr, dc) {
  let count = 0;
  let player = boardState[r][c];
  let nr = r + dr;
  let nc = c + dc;
  while (nr >= 0 && nr < rows && nc >= 0 && nc < cols && boardState[nr][nc] === player) {
    count++;
    nr += dr;
    nc += dc;
  }
  return count;
}

function disableBoard() {
  document.querySelectorAll('.cell').forEach(cell => cell.style.pointerEvents = 'none');
}

// Iniciar jogo
document.getElementById('startBtn').addEventListener('click', () => {
  playerOne = document.getElementById('playerOneName').value || 'Player One';
  playerTwo = document.getElementById('playerTwoName').value || 'Player Two';
  currentPlayer = 1;
  boardState.forEach(row => row.fill(0));
  createBoard();
  messageEl.textContent = `${playerOne}, it's your turn. Please pick a column to drop your blue chip.`;
});
