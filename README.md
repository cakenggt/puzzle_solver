Puzzle Solver
=====
A collection of puzzle solving algorithms.

Puzzle
---
A double array of puzzle pieces where puzzle pieces which occupy adjacent indicies have matching uuid's on those sides.

Puzzle Piece
----
A puzzle piece with a definite orientation. Each face of the puzzle piece has a uuid which will match up with another piece's opposite side uuid. Edge pieces have no uuid for that side.

Solutions
---
Included are two solutions. One runs in quadratic time and one runs in linear time.

### Quadratic
For every puzzle piece, this solution searches the entire set of puzzle pieces for a piece with a matching opposite side hash.

### Linear
This solution makes an entry in a dict for every puzzle piece's side's uuid. Then, starting at the piece with no left or top uuid (the left, top corner piece) it retrieve's the piece registered with the opposite side and uuid needed to match the current piece.

How To Use
---
Run `python solutions.py` to get printed timeit data for 1 Run each solution with a 100x100 puzzle. You can specify the run number and the puzzle size by including them in the command line like so: `python solutions.py runs size`. For example:

`python solutions.py 1 100`
