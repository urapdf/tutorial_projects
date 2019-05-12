SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

BOARD_SIZE = 10

VERTICAL_SHIP = '|'  # Not using this. Using 1st letter of ship
HORIZONTAL_SHIP = '-'
EMPTY = '0'
MISS = '-'
HIT = 'X'
SUNK = '!'
x = ""
NONEMPTY = [ship[0][0] for ship in SHIP_INFO]
myboard = [EMPTY for c in range(BOARD_SIZE)]


class Board(object):
    """
    Control most aspect of game board (player and opponents grids)
    """

    def __init__(self, side_dim=10):
        self.side_dim = side_dim
        self.myheader = [chr(c) for c in range(ord('A'), ord('A') + self.side_dim)]
        self.grid = []
        self.grid_public = []
        self.ship_tracker = {ship[0][0]: [ship, []] for ship in SHIP_INFO}
        self.bomb_tracker = set()

        for r in range(self.side_dim):
            row = []
            for c in range(self.side_dim):
                row.append('0')

            self.grid.append(row)

        #self.grid_public = self.grid[:]

    def create_grid_public(self):
          for r in range(self.side_dim):
            row = []
            for c in range(self.side_dim):
                row.append('0')

            self.grid_public.append(row)


    def print_current_board(self, grid, grid_public=None, hitMiss=None):
        """
        Prints Opponent's board and player's own board

        :param grid_public: list of list of chars, shows what the opponent can see ( Hit, miss ,or ocean)
        :param grid: List of List of chars, shows owners ship placement
        :param hitMiss: string, "Hit" or "Miss" depending on strike results
        :return: hitMiss
        """

        if hitMiss:
            print("You {}".format(hitMiss))

        def format_grid(g):

            print("=================")
            print("   " + " ".join(self.myheader))
            for i, row in enumerate(g):
                if i < 9:
                    print(str(i + 1) + "  " + " ".join(row))
                else:
                    print(str(i + 1) + " " + " ".join(row))
        if grid_public != None:
            boards = [grid_public, grid]
        else:
            boards = [grid]
        for i, g in enumerate(boards):
            if i == 0 and len(boards)==2:
                print("\nOpponent's Board")
            else:
                print("\nYour Board")

            format_grid(g)


    def isWrongPlace(self, slice, NONEMPTY, boat, grid, start_x, end_x, start_y, end_y, step, oreo):

        # start_position[0] = columns, dba: x
        # start_position[1] = rows, dba: y

        while set(NONEMPTY).intersection(slice):

            # ui_position = input('Invalid cordinates(collision detected)! please place your {}:'.format(boat))
            ui_position = input('Invalid cordinates(collision detected)! please enter new cordinates: ')
            start_position = self.translate_ui_coor(ui_position)
            start_x = start_position[0]
            start_y = start_position[1]

            # oreo =  input('Is {} horizontal? (Y)/N:'.format(boat)).upper()
            if (start_x < (BOARD_SIZE / 2)) and oreo == 'Y':

                end_x, step = start_x + len(boat), 1
            elif (start_x >= (BOARD_SIZE / 2)) and oreo == 'Y':

                end_x, step = start_x - len(boat), -1
            elif (start_y < (BOARD_SIZE / 2)) and oreo == 'N':

                end_y, step = start_y + len(boat), 1
            elif (start_y >= (BOARD_SIZE / 2)) and oreo == 'N':

                end_y, step = start_y - len(boat), -1

            if oreo == 'Y':
                row = grid[start_y]
                slice = row[start_x:end_x:step]

            if oreo == 'N':
                column = [row[start_x] for row in grid]
                slice = column[start_y:end_y:step]

        return start_x, end_x, start_y, end_y, slice, step

    def placeship(self, ship_arrays):
        # place boat in grid
        # check collision
        # check quadrant
        # start_y, end_y ( Y picks the row: Vertical)
        # start _x, end_x( X picks the column: Horizontal)
        # Y = whole row at poistion (y)
        # X = whole column at position (x)

        for index in range(len(SHIP_INFO) - 1, -1, -1):

            if len(ship_arrays) > 0:
                boat = ship_arrays[index]
                ui_position = input('where do you want to place your {}:'.format(SHIP_INFO[index][0]))

                start_position = self.translate_ui_coor(ui_position.strip())

                if start_position is None:
                    start_position = self.is_on_grid(BOARD_SIZE)
                oreo = input('Is {} horizontal? (Y)/N:'.format(SHIP_INFO[index][0])).upper()
                if oreo != 'Y':
                    oreo = 'N'

                # start_position[0] = columns
                # start_position[1] = rows
                start_x = start_position[0]
                start_y = start_position[1]

                if (start_x < (BOARD_SIZE / 2)) and oreo == 'Y':
                    end_x, step = start_x + len(boat), 1
                    end_y = start_y
                    row = self.grid[start_y]
                    slice = row[start_x:end_x:step]

                    start_x, end_x, start_y, end_y, slice, step \
                        = self.isWrongPlace(slice, NONEMPTY, boat, self.grid, start_x, end_x, start_y, end_y, step,
                                            oreo)
                    row = self.grid[start_y]

                    row[start_x:end_x:step] = boat  # updates grid with boat
                    del ship_arrays[index]

                if (start_y < (BOARD_SIZE / 2)) and oreo == 'N':
                    end_y, step = start_y + len(boat), 1
                    end_x = start_x

                    column = [row[start_x] for row in self.grid]
                    slice = column[start_y:end_y:step]
                    start_x, end_x, start_y, end_y, slice, step \
                        = self.isWrongPlace(slice, NONEMPTY, boat, self.grid, start_x, end_x, start_y, end_y, step,
                                            oreo)

                    for row in self.grid[start_y:end_y:step]:
                        row[start_x] = boat[0]

                    del ship_arrays[index]

                if (start_x >= (BOARD_SIZE / 2)) and oreo == 'Y':
                    end_x, step = start_x - len(boat), -1
                    end_y = start_y
                    row = self.grid[start_y]
                    slice = row[start_x:end_x:step]
                    start_x, end_x, start_y, end_y, slice, step \
                        = self.isWrongPlace(slice, NONEMPTY, boat, self.grid, start_x, end_x, start_y, end_y, step,
                                            oreo)
                    row = self.grid[start_y]

                    row[start_x:end_x:step] = boat
                    del ship_arrays[index]

                if (start_y >= (BOARD_SIZE / 2)) and oreo == 'N':
                    end_y, step = start_y - len(boat), -1
                    end_x = start_x

                    column = [row[start_x] for row in self.grid]
                    slice = column[start_y:end_y:step]
                    start_x, end_x, start_y, end_y, slice, step \
                        = self.isWrongPlace(slice, NONEMPTY, boat, self.grid, start_x, end_x, start_y, end_y, step,
                                            oreo)

                    for row in self.grid[start_y:end_y:step]:
                        row[start_x] = boat[0]

                    del ship_arrays[index]

            print("\033c", end="")
            self.print_current_board(self.grid)


    def translate_ui_coor(self, user_info, BOARD_SIZE=BOARD_SIZE):
        """
        :param user_info:
        :param BOARD_SIZE:
        :return: user_tup: tuple, (Column as int,Row as int)
        """
        user_info = user_info.upper()
        header_set_side = [str(num) for num in range(1, BOARD_SIZE + 1)]
        header_set_top = [chr(64 + num).upper() for num in range(1, BOARD_SIZE + 1)]

        try:
            _c = ord(user_info[0].upper()) - ord('A')
        except:
            return None

        try:

            _r = int(user_info[1:])
        except:
            return None

        user_tup = (ord(user_info[0].upper()) - ord('A'), int(user_info[1:]) - 1)

        on_grid = 0 <= user_tup[0] <= BOARD_SIZE - 1 and 0 <= user_tup[1] <= BOARD_SIZE - 1


        if 0 <= user_tup[0] <= BOARD_SIZE - 1 and 0 <= user_tup[1] <= BOARD_SIZE - 1:
            return user_tup
        else:
            return None

    def is_on_grid(self, BOARD_SIZE):

        user_tup = None

        while user_tup == None:
            user_try = input('Invalid cordinates(outside of grid)! Please Try again')
            user_tup = self.translate_ui_coor(user_try, BOARD_SIZE)
            if user_tup != None:
                if 0 <= user_tup[0] <= BOARD_SIZE - 1 and 0 <= user_tup[1] <= BOARD_SIZE - 1:
                    return user_tup
                else:
                    user_tup = None

    def has_been_bombed_before(self, BOARD_SIZE):

        user_tup = None

        while user_tup == None:
            user_try = input('Invalid cordinates(You have bombed here before)! Please Try again')
            user_tup = self.translate_ui_coor(user_try, BOARD_SIZE)
            if user_tup==None:
                user_tup =self.is_on_grid(BOARD_SIZE)
            if user_tup != None:
                if user_tup not in self.bomb_tracker:
                    return user_tup
                else:
                    user_tup = None

    def place_strike(self, name):
        bomb_coor = self.translate_ui_coor(input('where do you want to bombard?'))
        if bomb_coor is None:
            bomb_coor = self.is_on_grid(BOARD_SIZE)

        if bomb_coor in self.bomb_tracker:
            bomb_coor = self.has_been_bombed_before(BOARD_SIZE)


        if bomb_coor:
            self.bomb_tracker.add(bomb_coor)
            strike_loc = self.grid[bomb_coor[1]][bomb_coor[0]]
            if strike_loc in self.ship_tracker:
                # add sl into the list
                self.ship_tracker[strike_loc][1].append(bomb_coor)
                self.grid_public[bomb_coor[1]][bomb_coor[0]] = HIT
                self.grid[bomb_coor[1]][bomb_coor[0]] = HIT
                hitMiss = "Hit"

                if len(self.ship_tracker[strike_loc][1]) == self.ship_tracker[strike_loc][0][1]:
                    for coor in self.ship_tracker[strike_loc][1]:
                        self.grid_public[coor[1]][coor[0]] = SUNK
                        self.grid[coor[1]][coor[0]] = SUNK
                    print("the {} is sunk".format(self.ship_tracker[strike_loc][0][0]))
                    del self.ship_tracker[strike_loc]

            else:
                self.grid_public[bomb_coor[1]][bomb_coor[0]] = MISS
                self.grid[bomb_coor[1]][bomb_coor[0]] = MISS
                hitMiss = "Missed"

        return hitMiss



    def clear_screen(self, cont=True):
        if cont:
            if input("Are you done with your turn"):
                print("\033c", end="")
        else:
            print("\033c", end="")


class Player(Board):
    def __init__(self, name, team_color, hit_points=17):
        # self.own_board = own_board
        # self.strike_board = strike_board
        self.name = name
        self.team_color = team_color
        self.hit_points = hit_points

    def send_strike(self, cord):
        pass

    def recieve_strike(self, cord):
        pass


class Ship():
    def __init__(self, SHIP_INFO):
        # self.ship_name = ship_name
        # self.ship_hp = ship_hp

        self.ship_arrays = [[ship[0][0] for n in range(ship[1])] for ship in SHIP_INFO]


class bcolors:
    """
    Holds color information for terminal printing

    Sample:
    print (bcolors.HEADER + "Warning: No active frommets remain. Continue?"
      + bcolors.ENDC)

    Got Code from http://stackoverflow.com/a/287944
    """
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.BLUE = ''
        self.GREEN = ''
        self.WARNING = ''
        self.RED = ''
        self.ENDC = ''
