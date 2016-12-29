grid = [
    list("EMANRUOYARHNC"),
    list("JKLPSTKPYCJLL"),
    list("QRZTMBXWUXZOW"),
    list("DZJTMYOURNAME"),
    list("YLMBRMZHDDQHM"),
    list("GJZMFUFKRZTJK"),
    list("XUJCVGHIVXHIH"),
    list("JDJBGCYKSIMGE"),
    list("AUAGIVMWCZIGN"),
    list("TFKISPHPZINXQ"),
    list("DYOURNAMELDZN"),
    ]

word = "YOURNAME"

row = len(grid)
col = len(grid[0])

x_dir = [-1, -1, -1, 0, 0, 1, 1, 1]
y_dir = [-1, 0, 1, -1, 1, -1, 0, 1]

def search(x, y):
    if grid[x][y] != word[0]:
        return False   

    for dir_in in range(8):
        new_x, new_y = x + x_dir[dir_in], y + y_dir[dir_in]

        for ch in word[1:]:
            if new_x >= row or new_x < 0 or new_y >= col or new_y < 0:
                break;

            if grid[new_x][new_y] != ch:
                break;

            new_x, new_y = new_x + x_dir[dir_in], new_y + y_dir[dir_in]


        if ch == word[-1]:
            return True

    return False


def search_word():
        for x in range(row):
            for y in range(col):
                if search(x,y):
                    print "Found at L{}R{}".format(x,y)

search_word()
