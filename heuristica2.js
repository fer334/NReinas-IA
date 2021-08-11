const print_board = (board) => {
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board.length; j++) {
      // process.stdout.write(board[i][j] === "Q" ? "Q " : board[i][j]+" ");
      process.stdout.write(board[i][j] === "Q" ? "Q " : "# ");
    }
    process.stdout.write("\n");
  }
};

const cal_conflicts = (board) => {
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board.length; j++) {
      if (board[i][j] !== "Q") {
        board[i][j] = 0;
        board[i][j] += queensOnRow(board, i, j);
        board[i][j] += queensOnColumn(board, i, j);
        board[i][j] += queensOnDiagonal(board, i, j);
      }
    }
  }
  return board;
};

const queensOnRow = (board, row, col) => {
  queens = 0;
  for (let i = 0; i < board.length; i++) {
    if (board[row][i] === "Q" && i != col) {
      queens++;
    }
  }
  return queens;
};

const queensOnColumn = (board, row, col) => {
  queens = 0;
  for (let i = 0; i < board.length; i++) {
    if (board[i][col] === "Q" && i != row) {
      queens++;
    }
  }
  return queens;
};

const queensOnDiagonal = (board, row, col) => {
  let queens = 0;
  let i = 1;
  while (!(row + i >= board.length || col + i >= board.length)) {
    if (board[row + i][col + i] === "Q") {
      queens++;
    }
    i++;
  }

  i = 1;
  while (!(row - i < 0 || col - i < 0)) {
    if (board[row - i][col - i] === "Q") {
      queens++;
    }
    i++;
  }

  i = 1;
  while (!(row + i >= board.length || col - i < 0)) {
    if (board[row + i][col - i] === "Q") {
      queens++;
    }
    i++;
  }

  i = 1;
  while (!(row - i < 0 || col + i >= board.length)) {
    if (board[row - i][col + i] === "Q") {
      queens++;
    }
    i++;
  }

  return queens;
};

const isSolved = (board) => {
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board.length; j++) {
      if (board[i][j] === "Q") {
        const attackQueens =
          queensOnColumn(board, i, j) +
          queensOnRow(board, i, j) +
          queensOnDiagonal(board, i, j);
        // console.log(attackQueens)
        if (attackQueens != 0) return false;
      }
    }
  }
  return true;
};

const min_conflict = (board) => {
  let min = Infinity;
  let minPos = [];
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board.length; j++) {
      if (board[i][j] < min && board[i][j] != "Q") {
        min = board[i][j];
        minPos = [{ i: i, j: j }];
      } else if (board[i][j] == min) {
        minPos.push({ i: i, j: j });
      }
    }
  }
  return minPos[getRandomInt(0, minPos.length)];
};

const queenPosFromCol = (board, pos) => {
  const row = pos.i;
  const col = pos.j;
  for (let i = 0; i < board.length; i++) {
    if (board[i][col] === "Q") {
      return { i: i, j: col };
    }
  }
};

const moveQueen = (board, queenPos, minPos) => {
  board[queenPos.i][queenPos.j] = 0;
  board[minPos.i][minPos.j] = "Q";
};

const iterate = () => {
  cal_conflicts(board);
  const pos = min_conflict(board);
  const queenPos = queenPosFromCol(board, pos);
  console.log("#########Antes de mover ###########");
  print_board(board);
  moveQueen(board, queenPos, pos);
  console.log("######Despues de mover");
  print_board(board);
};

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

const generate_board = (N) => {
  let board = Array(N)
    .fill(null)
    .map(() => Array(N).fill(0));
  for (let i = 0; i < N; i++) {
    board[getRandomInt(0, board.length)][i] = "Q";
  }
  return board;
};

let board = [
  ["Q", 0, 0, 0],
  [0, 0, "Q", 0],
  [0, "Q", 0, 0],
  [0, 0, 0, "Q"],
];
// board = [
//     [0,       0,    "Q",    0],
//     ["Q",     0,      0,    0],
//     [0,       0,      0,    "Q"],
//     [0,     "Q",      0,    0]
// ]
// board = [
//   [0, 0, 0, 0],
//   // [0, 0, 0, 0],
//   ["Q", 0, 0, 0],
//   [0, "Q", 0, 0],
//   [0, 0, 0, 0],
//   [0, 0, 0, 0],
// ];

board = generate_board(80);
cal_conflicts(board);
print_board(board);

// iterate(board)
// iterate(board)
// iterate(board)
// iterate(board)

console.time("algo");
while (isSolved(board) === false) {
  iterate(board);
}
console.timeEnd("algo");
