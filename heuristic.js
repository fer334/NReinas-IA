function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

const queensOnRow = (board, row, col) => {
  queens = 0;
  for (let i = 0; i < this.size; i++) {
    if (board[row][i] === "Q" && i != col) {
      queens++;
    }
  }
  return queens;
};

const queensOnColumn = (board, row, col) => {
  queens = 0;
  for (let i = 0; i < this.size; i++) {
    if (board[i][col] === "Q" && i != row) {
      queens++;
    }
  }
  return queens;
};

const queensOnDiagonal = (board, row, col) => {
  let queens = 0;
  let i = 1;
  while (!(row + i >= this.size || col + i >= this.size)) {
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
  while (!(row + i >= this.size || col - i < 0)) {
    if (board[row + i][col - i] === "Q") {
      queens++;
    }
    i++;
  }

  i = 1;
  while (!(row - i < 0 || col + i >= this.size)) {
    if (board[row - i][col + i] === "Q") {
      queens++;
    }
    i++;
  }
  return queens;
};

class NQueens {
  constructor(size) {
    this.size = size;
    this.board = this.generate_board();
    this.solutions = [];
  }

  generate_board = () => {
    let board = Array(this.size)
      .fill(null)
      .map(() => Array(this.size).fill(0));
    for (let i = 0; i < this.size; i++) {
      board[getRandomInt(0, this.size)][i] = "Q";
    }
    return board;
  };

  print_board = () => {
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        process.stdout.write(
          this.board[i][j] === "Q" ? "Q " : this.board[i][j] + " "
        );
        // process.stdout.write(this.board[i][j] === "Q" ? "Q " : "# ");
      }
      process.stdout.write("\n");
    }
  };

  cal_conflicts = () => {
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        if (this.board[i][j] !== "Q") {
          this.board[i][j] = 0;
          this.board[i][j] += queensOnRow(this.board, i, j);
          this.board[i][j] += queensOnColumn(this.board, i, j);
          this.board[i][j] += queensOnDiagonal(this.board, i, j);
        }
      }
    }
  };

  min_conflict = () => {
    let min = Infinity;
    let minPos = [];
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        if (this.board[i][j] < min && this.board[i][j] != "Q") {
          min = this.board[i][j];
          minPos = [{ i: i, j: j }];
        } else if (this.board[i][j] == min) {
          minPos.push({ i: i, j: j });
        }
      }
    }
    return minPos[getRandomInt(0, minPos.length)];
  };

  queenPosFromCol = (pos) => {
    const row = pos.i;
    const col = pos.j;
    for (let i = 0; i < this.size; i++) {
      if (this.board[i][col] === "Q") {
        return { i: i, j: col };
      }
    }
  };

  moveQueen = (from, to) => {
    this.board[from.i][from.j] = 0;
    this.board[to.i][to.j] = "Q";
  };

  isSolved = () => {
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        if (this.board[i][j] === "Q") {
          const attackQueens =
            queensOnColumn(this.board, i, j) +
            queensOnRow(this.board, i, j) +
            queensOnDiagonal(this.board, i, j);
          // console.log(attackQueens)
          if (attackQueens != 0) return false;
        }
      }
    }
    return true;
  };

  solve = () => {
    while (!this.isSolved()) {
      this.cal_conflicts();
      const pos = this.min_conflict();
      const queenPos = this.queenPosFromCol(pos);
      console.log("#########Antes de mover ###########");
      this.print_board();
      this.moveQueen(queenPos, pos);
      console.log("######Despues de mover");
      this.print_board();
    }
  };
}

nqueens = new NQueens(8);
nqueens.cal_conflicts();
nqueens.print_board();
nqueens.solve()
