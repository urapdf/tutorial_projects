import sys

"""

You have volunteered to be the Coordinator for your town’s youth soccer league. As part of your job you need to divide the 18 children who have signed up for the league into three even teams - Dragons, Sharks and Raptors. In years past, the teams have been unevenly matched, so this year you are doing your best to fix that. For each child, you will have the following information: Name, height (in inches), whether or not they have played soccer before, and their guardians’ names.

The project has three major parts. For each part choose from the tools we have covered in the courses so far. Please don’t employ more advanced tools we haven’t covered yet, even if they are right for the job. However, if you identify a place where a more advanced tool is appropriate, please mention that in a code comment as you and your mentor may want to discuss it later.

Part 1: We have provided information for the 18 players in the attached spreadsheet. Please choose an appropriate data type to store the information for each player. Once you have decided on what tools to use, convert the player data so it can be used in Part 2.

    What I need to do for part 1 (readroster function)
        a) open and read provided spreadsheet
        b) for each file line, add to player dictionary ( Key = player name : value = list of player attributes)


Part 2: Create logic that can iterate through all 18 players and assign them to teams such that the number of experienced players on each team are the same. Store each team’s players in its own new collection variable for use in Part 3. (Please note: your logic should work correctly regardless of the initial ordering of the players. Also, if you would like to attain an “exceeds expectations” rating for this project, add logic to ensure that each teams’ average height is within 1 inch of the others.)

    What I need to do for part 2 (createteam function)
        a) Divide the player list into 2 lists ( experience players and non experience players)
        b) pop player from each list, add both to the next team



Part 3: Create logic that iterates through all three teams of players and generates a personalized letter to the guardians, letting them know which team the child has been placed on and when they should attend their first team team practice. As long as you provide the necessary information (player name, guardians’ names, practice date/time), feel free to have fun with the content of the letter. The team practice dates/times are as follows:

Dragons - March 17, 1pm, Sharks - March 17, 3pm, Raptors - March 18, 1pm

When your complete code is run, it should output individual letters to file. There should be a total of 18 letters, one for each player.

    What I need to do for part 3 (letters function)
        a) Create message template
        b) for each player on each team, print formated message

As always, meaningful and concise code comments are expected. Your code should be written and refined in workspaces or on your local machine, but be sure to upload it to GitHub, as per the instructions in this tutorial.

Good luck!


    Additional things I could add and work on ( error handling):
        a) What happens if file and/or line is not parsed and/or read correctly
        b) What happens if experienced and inexperienced players can't be distributed evenly?

"""



def readroster(filename):
    playerdict = {}
    with open(filename,"r") as fh:


        for i, line in enumerate(fh):
            if i == 0:
                myheader = line.strip().split(",")
            else:
                playerrecord = line.strip().split(",")
                playerdict[playerrecord[0]] = playerrecord[1:]

    return playerdict


def createteam(playerdict,team_list):

    newlist = [team_name for team_name in team_list]
    teams = {team:[] for team in team_list}


    exp_players =[ exp_player for exp_player in playerdict if playerdict[exp_player][1] == 'YES']

    inexp_players =[new_player for new_player in playerdict if new_player not in exp_players]


    if len(exp_players) % len(teams) == 0 and len(playerdict) % len(teams) ==0:

        for player in range(len(playerdict)//len(teams)):
            if exp_players:
                for team in teams:
                    next_player = exp_players.pop()
                    innext_player = inexp_players.pop()
                    teams[team].extend([next_player,innext_player])

    else:
        print('no even split of the players...get rid of the extras')

    return teams


def create_letters(playerdict, team_dict,team_date):
    """
    necessary information (player name, guardians’ names, practice date/time),
    feel free to have fun with the content of the letter. The team practice dates/times are as follows:
    Dragons - March 17, 1pm, Sharks - March 17, 3pm, Raptors - March 18, 1pm
    :param playerdict:
    :param team_dict:
    :return:

    """
    message_template = "Dear {parent},\n Congradulations! your child, {brat}, is on team:{team_name}.\n The 1st practice is {team_date} "

    print(playerdict)

    for team in team_dict:
        #print(team)
        date = team_date[team]
        #print(team,date)

        for player in team_dict[team]:
            parents = playerdict[player][-1]
            print(message_template.format(parent = parents,brat =player,team_name = team,team_date = date ))








def main():
    TEAM_LIST = ['Dragons','Sharks','Raptors']
    TEAM_PRACTICE_DATE ={'Dragons':'March 17, 1pm','Sharks':'March 17, 3pm','Raptors':'March 18, 1pm' }


    playerdict = readroster("roster")
    team_dict = createteam(playerdict, TEAM_LIST)
    create_letters(playerdict, team_dict, TEAM_PRACTICE_DATE)



if __name__ == "__main__":
    sys.exit(main())
