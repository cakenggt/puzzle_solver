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

def checkPuzzle(arg):
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

def main():
    puzzle10 = puzzle.generatePuzzle(10)
    result = quadratic(puzzle10, 10)
    print('quadratic function success: ' + str(checkPuzzle(result)))

if __name__ == "__main__":
    main()
