if __name__ == '__main__':
    import csv

    def team_splitter(experienced_players, inexperienced_players):
        '''Takes a list of experienced players and a list of inexperienced
        players and divides them up in round-robin fashion and returns a
        list of players for each team.
        '''
        def split(players):
            while players:
                sharks.append(players.pop())
                dragons.append(players.pop())
                raptors.append(players.pop())

        sharks, dragons, raptors = [], [], []
        split(experienced_players)
        split(inexperienced_players)
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

    # Initializes the players variable, reads the csv file
    # and appends the list of players to the players variable.
    players = []
    with open('soccer_players.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for player in reader:
            players.append({'Name': player['Name'],
                            'Experienced': player['Soccer Experience'],
                            'Guardian Name(s)': player['Guardian Name(s)']
                            })

    # Initializes variables for experienced and inexperienced players then
    # iterates through the list of players and assigns the players accordingly.
    experienced_players = []
    inexperienced_players = []
    for player in players:
        if player['Experienced'] == 'YES':
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)

    sharks, dragons, raptors = team_splitter(experienced_players,
                                             inexperienced_players)
    team_writer('Sharks', sharks)
    team_writer('Dragons', dragons)
    team_writer('Raptors', raptors)
