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

const verAnticipada = (queenPosition, queen) => {
  const n = queenPosition.length;
  const res = [];
  for (let move = 0; move < n; move++) {
    if (isValid(queenPosition, move, queen)) {
      res.push(move);
    }
  }
  return res;
};

const findQueenSolution = (queen, pro, queenPosition, all) => {
  // console.log("Profundidad",pro,":",queenPosition);
  n = queenPosition.length;
  if (queen == n) {
    if (all) solutions.push(JSON.parse(JSON.stringify(queenPosition)));
    return;
  }
  let okValues = verAnticipada(queenPosition, queen);
  while (okValues.length > 0) {
    // generate a random number
    const random = Math.floor(Math.random() * okValues.length);
    const move = okValues[random];
    queenPosition[queen] = move;
    // Delete the element from the array
    // console.log(okValues);
    okValues.splice(random, 1);
    // console.log('fin',okValues);
    // break
    findQueenSolution(queen + 1, pro + 1, queenPosition, all);
    if (!all)
      if (!queenPosition.some((x) => x == -1)) {
        return;
      }
  }

  queenPosition[queen] = -1;
};

const nQuens = (n, all) => {
  let queenPosition = new Array(n);
  queenPosition.fill(-1);
  findQueenSolution(0, 0, queenPosition, all);
  console.log(queenPosition);
};

const solutions = [];
console.time("Una solucion tarda");
nQuens(100, false);
console.timeEnd("Una solucion tarda");
