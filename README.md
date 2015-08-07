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
