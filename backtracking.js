const subs = (row, col, row2, col2) => {
  return Math.abs(row - row2) === Math.abs(col - col2);
};

const isValid = (queenPosition, row, col) => {
  if (queenPosition.some((x) => x == row)) return false;

  for (let col2 = 0; col2 < queenPosition.length; col2++) {
    const row2 = queenPosition[col2];
    if (queenPosition[col2] != -1) {
      if (subs(row, col, row2, col2)) return false;
    } else return true;
  }
};
const findQueenSolution = (queen, n, queenPosition, all) => {
  if (queen == n) {
    if (all) solutions.push(JSON.parse(JSON.stringify(queenPosition)));

    return;
  }
  for (let move = 0; move < n; move++) {
    // console.log(move,queen,queenPosition,isValid(queenPosition,move,queen));
    if (isValid(queenPosition, move, queen)) {
      queenPosition[queen] = move;
      findQueenSolution(queen + 1, n, queenPosition, all);
      if (!all)
        if (!queenPosition.some((x) => x == -1)) {
          return;
        }
    }
  }

  queenPosition[queen] = -1;
};

const nQuens = (n, all) => {
  let queenPosition = new Array(n);
  queenPosition.fill(-1);
  findQueenSolution(0, n, queenPosition, all);
  console.log(queenPosition);
};

const solutions = [];
console.time("Una solucion de 20 tarda");
nQuens(20, false);
console.log(solutions.length);
console.timeEnd("Una solucion de 20 tarda");

// queenPosition=[2,2,3,-1]
// # Q # #  # # # #  # Q # #
// # # # Q  # # # #  # # # Q
// Q # # #  Q Q # #  Q # Q #
// # # Q #  # # Q #  # # # #
