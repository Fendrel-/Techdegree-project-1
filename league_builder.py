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
    appends them to teams.txt.
    '''
    with open('teams.txt', 'w') as file:
        file.write('{}\n'.format(team))
        for player in players:
            file.write('{}, {}, {}\n'.format(player['Name'],
                                             player['Experienced'],
                                             player['Guardian Name(s)']))
        file.write('\n')


def welcome_letter(team, players, first_practice):
    '''Takes a list of players and their corresponding team name and creates
    a welcome letter to the parents as a .txt file for each player.
    '''
    for player in players:
        name = player['Name'].lower().split()
        name = '_'.join(name)
        with open('{}.txt'.format(name), 'w') as file:
            file.write('Dear {},\n\n\n'.format(player['Guardian Name(s)']))
            file.write('We are excited to announce the teams for this year\'s ')
            file.write('soccer league!\n\nCongratulations! {} has been chosen'.format(player['Name']))
            file.write(' to be part of\nTeam {} this year!\n\n'.format(team))
            file.write('The team\'s first practice will be held on {}.\n'.format(first_practice))
            file.write('We look forward to seeing you there! Here\'s to a safe and fun season!\n\n\n')
            file.write('Sincerely,\n\n')
            file.write('Dan\n')
            file.write('League Coordinator')


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


if __name__ == '__main__':
    players = csv_reader()
    experienced_players, inexperienced_players = player_splitter(players)
    sharks, dragons, raptors = team_splitter(experienced_players,
                                             inexperienced_players)
    team_writer('Sharks', sharks)
    team_writer('Dragons', dragons)
    team_writer('Raptors', raptors)
    welcome_letter('Sharks', sharks, 'October 25th at 4:00 PM')
    welcome_letter('Dragons', dragons, 'October 24th at 4:00 PM')
    welcome_letter('Raptors', raptors, 'October 25th at 6:00 PM')
