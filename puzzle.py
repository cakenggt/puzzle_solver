import uuid;
import random;

class PuzzlePiece:
    left = None;
    right = None;
    up = None;
    down = None;

def generatePuzzle(size):
    formattedResult = []
    result = []
    for x in xrange(0, size):
        formattedResult.append([])
        for y in xrange(0, size):
            newPiece = PuzzlePiece();
            if x > 0:
                newPiece.left = formattedResult[x-1][y].right
            if y > 0:
                newPiece.up = formattedResult[x][y-1].down
            if x < size-1:
                newPiece.right = uuid.uuid4();
            if y < size-1:
                newPiece.down = uuid.uuid4();
            formattedResult[x].append(newPiece)
            result.append(newPiece)
    random.shuffle(result)
    return result
