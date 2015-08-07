from puzzle import puzzle
import timeit

def quadratic(arg, size):
    top_left = None
    for piece in arg:
        if piece.up == None and piece.left == None:
            top_left = piece
            break
    result = []
    for y in xrange(size):
        result.append([])
        for x in xrange(size):
            if y == 0:
                if x == 0:
                    result[y].append(top_left)
                    continue
                else:
                    focus = result[y][x-1].right
            else:
                if x == 0:
                    focus = result[y-1][x].down
                else:
                    focus = result[y][x-1].right
            for piece in arg:
                if x == 0:
                    if piece.up == focus:
                        result[y].append(piece)
                        break
                else:
                    if piece.left == focus:
                        result[y].append(piece)
                        break
    return result

def linear(arg, size):
    resultDict = {}
    result = []
    top_left = None
    for piece in arg:
        if piece.left is None and piece.up is None:
            top_left = piece
        if piece.up is not None:
            resultDict['u'+str(piece.up)] = piece
        if piece.down is not None:
            resultDict['d'+str(piece.down)] = piece
        if piece.left is not None:
            resultDict['l'+str(piece.left)] = piece
        if piece.right is not None:
            resultDict['r'+str(piece.right)] = piece
    for y in xrange(size):
        result.append([])
        for x in xrange(size):
            if y == 0:
                if x == 0:
                    result[y].append(top_left)
                    continue
                else:
                    focus = result[y][x-1].right
                    found = resultDict['l'+str(focus)]
                    result[y].append(found)
            else:
                focus = result[y-1][x].down
                result[y].append(resultDict['u'+str(focus)])
    return result

def check_puzzle(arg):
    for y in xrange(len(arg)):
        for x in xrange(len(arg)):
            piece = arg[y][x]
            if piece.left is not None:
                if piece.left is not arg[y][x-1].right:
                    return False
            if piece.right is not None:
                if piece.right is not arg[y][x+1].left:
                    return False
            if piece.up is not None:
                if piece.up is not arg[y-1][x].down:
                    return False
            if piece.down is not None:
                if piece.down is not arg[y+1][x].up:
                    return False
    return True

def test_quadratic():
    puzzle10 = puzzle.generatePuzzle(100)
    result = quadratic(puzzle10, 100)
    #print('quadratic function success: ' + str(check_puzzle(result)))

def test_linear():
    puzzle10 = puzzle.generatePuzzle(100)
    result = linear(puzzle10, 100)
    #print('linear function success: ' + str(check_puzzle(result)))

def main():
    tests = 1
    print('quadratic: ' + str(timeit.timeit('test_quadratic()', setup='from __main__ import test_quadratic', number=tests)))
    print('linear: ' + str(timeit.timeit('test_linear()', setup='from __main__ import test_linear', number=tests)))

if __name__ == "__main__":
    main()
