#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

# TOdo Prompt the players for their names. (done)
# TODO: "You sunk" message when ship is destroyed
# TODO: Clean up DOC STRING
# TODO: Clean up messages
# TODO: Welcome screen


from battleship_objects import *
import json


SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]


def main():
    """
    controls game setup and flow
    :return:
    """
    print("\033c", end="")

    loop_num = 1
    player1 = Player(*get_player_info("player #1"))
    # player1 = Player(name='Player 1', team_color='Blue')
    p1_boadr = Board()
    player2 = Player(*get_player_info("player #2"))
    # player2 = Player(name='Player 2', team_color='Red')
    p2_boadr = Board()



    looad = input("Do you want to load boards?")

    if looad == "y":
        # Load boards from json files and skip setup loop
        with open("player1_grid.json") as fh:
            p1_boadr.grid = json.load(fh)
        p1_boadr.create_grid_public()
        with open("player2_grid.json") as fh:
            p2_boadr.grid = json.load(fh)
        p2_boadr.create_grid_public()

    game_over = False

    while not game_over:

        if loop_num / 1 == 1 and looad != "y":

            print("placement for {}".format(player1.name))

            p1_boadr.print_current_board(p1_boadr.grid)
            ship_arrays = Ship(SHIP_INFO).ship_arrays
            p1_boadr.placeship(ship_arrays)
            input("\n {}, you have placed all of your ships!\n"
                  " Hit enter to continue\n".format(player1.name))
            # Ask Do you want to save the grids
            savve = input("Do you want to save board")
            if savve == "y":
                with open("player1_grid.json", "w") as outfile:
                    json.dump(p1_boadr.grid, outfile)
            p1_boadr.create_grid_public()
            p1_boadr.clear_screen()

        elif loop_num / 2 == 1 and looad != "y":

            print("placement for {}".format(player2.name))

            p2_boadr.print_current_board(p2_boadr.grid)
            ship_arrays = Ship(SHIP_INFO).ship_arrays
            p2_boadr.placeship(ship_arrays)
            input("\n {}, you have placed all of your ships!\n"
                  " Hit enter to continue\n".format(player2.name))
            # Ask Do you want to save the grids
            if savve == "y":
                with open("player2_grid.json", "w") as fh:
                    json.dump(p2_boadr.grid, fh)
            p2_boadr.create_grid_public()
            p2_boadr.clear_screen()

        # Player 2's turn
        elif loop_num % 2 == 0:
            print("{}, Now it is your turn!".format(player2.name))

            p2_boadr.print_current_board(p2_boadr.grid, p1_boadr.grid_public)

            # location to strike on player1's board
            hit_miss = p1_boadr.place_strike(player2.name)
            p1_boadr.clear_screen(cont=False)

            p2_boadr.print_current_board(p2_boadr.grid, p1_boadr.grid_public, hit_miss)
            if len(p1_boadr.ship_tracker) == 0:
                print( player2.name + " WON!")
                game_over = True
            p1_boadr.clear_screen()

        elif loop_num % 2 != 0:
            print("{}, Now it is your turn!".format(player1.name))

            p1_boadr.print_current_board(p1_boadr.grid, p2_boadr.grid_public)

            # location to strike on player2's board
            hit_miss = p2_boadr.place_strike(player1.name)
            p2_boadr.clear_screen(cont=False)
            p1_boadr.print_current_board(p1_boadr.grid, p2_boadr.grid_public, hit_miss)
            if len(p2_boadr.ship_tracker) == 0:
                print(player1.name + " WON!")
                game_over = True
            p2_boadr.clear_screen()

        loop_num += 1


def get_player_info(player_num):
    """
    Initilize player info
    :return: name, fleet color
    """

    name = input("What is your name {}? ".format(player_num))
    fleet_color = input("What is your fleet color? ")  # fleet_color not used yet
    # print(chr(27) + "[2J")
    print("\033c", end="")

    return name, fleet_color


if __name__ == "__main__":
    main()
