if __name__ == "__main__":
    import csv

    def team_splitter(players, sharks, dragons, raptors):
        while players:
            sharks.append(players.pop())
            dragons.append(players.pop())
            raptors.append(players.pop())
        return sharks, dragons, raptors

    players = []
    with open('soccer_players.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for player in reader:
            players.append({"Name": player['Name'],
                            "Experienced": player['Soccer Experience'],
                            "Guardian Name(s)": player['Guardian Name(s)']
                            })

    experienced_players = []
    inexperienced_players = []
    for player in players:
        if player['Experienced'] == "YES":
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)

    sharks = []
    dragons = []
    raptors = []
    sharks, dragons, raptors = team_splitter(experienced_players,
                                             sharks,
                                             dragons,
                                             raptors)
    sharks, dragons, raptors = team_splitter(inexperienced_players,
                                             sharks,
                                             dragons,
                                             raptors)

    print("Sharks: {}".format(sharks), end="\n\n")
    print("Dragons: {}".format(dragons), end="\n\n")
    print("Raptors: {}".format(raptors), end="\n\n")
