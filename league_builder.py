import csv


def team_splitter(experienced_players, inexperienced_players):
    '''Takes a list of experienced players and a list of inexperienced
    players and divides them up in round-robin fashion and returns a
    list of players for each team.
    '''
    def assign_team(players):
            try:
                global last_added
                if last_added == raptors:
                    sharks.append(players.pop())
                    last_added = sharks
                elif last_added == sharks:
                    dragons.append(players.pop())
                    last_added = dragons
                elif last_added == dragons:
                    raptors.append(players.pop())
                    last_added = raptors
            except IndexError as error:
                pass


    sharks, dragons, raptors = [], [], []
    global last_added
    last_added = raptors
    while experienced_players:
        assign_team(experienced_players)
    while inexperienced_players:
        assign_team(inexperienced_players)
    return sharks, dragons, raptors


def team_writer(team, players):
    '''Takes a list of players and their corresponding team name and
    appends them to teams.txt
    '''
    with open('teams.txt', 'a') as file:
        file.write('{}\n'.format(team))
        for player in players:
            file.write('{}, {}, {}\n'.format(player['Name'],
                                             player['Experienced'],
                                             player['Guardian Name(s)']))
        file.write('\n')
        

def welcome_letter(team, players):
    '''Takes a list of players and their corresponding team name and creates
    a welcome letter to the parents in the form of a .txt file for each player
    '''
    for player in players:
        print(player['Name'])

def csv_reader():
    '''Initializes the players variable, reads the csv file
    and appends the list of players to the players variable.
    '''
    players = []
    with open('soccer_players.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for player in reader:
            players.append({'Name': player['Name'],
                            'Experienced': player['Soccer Experience'],
                            'Guardian Name(s)': player['Guardian Name(s)']
                            })
    return players


def player_splitter(players):
    '''Initializes variables for experienced and inexperienced players then
    iterates through the list of players and assigns the players accordingly.
    '''
    experienced_players = []
    inexperienced_players = []
    for player in players:
        if player['Experienced'] == 'YES':
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)
    return experienced_players, inexperienced_players


def main():
    players = csv_reader()
    experienced_players, inexperienced_players = player_splitter(players)
    sharks, dragons, raptors = team_splitter(experienced_players,
                                             inexperienced_players)
    team_writer('Sharks', sharks)
    team_writer('Dragons', dragons)
    team_writer('Raptors', raptors)
    welcome_letter('Sharks', sharks)
    welcome_letter('Dragons', dragons)
    welcome_letter('Raptors', raptors)


if __name__ == '__main__':
    main()
