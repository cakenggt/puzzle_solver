import uuid
import random
import pickle

class PuzzlePiece:
    left = None;
    right = None;
    up = None;
    down = None;

    def __str__(self):
        return 'l:'+str(self.left)+' r:'+str(self.right)+' u:'+str(self.up)+' d:'+str(self.down)

def generatePuzzle(size):
    formattedResult = []
    result = []
    for x in xrange(size):
        formattedResult.append([])
        for y in xrange(size):
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
    output = open(str(size)+'x'+str(size)+'.pk', 'wb')
    pickle.dump(result, output)
    return result
