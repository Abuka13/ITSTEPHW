import json
f = "user_sttings.txt"
myfile = open(f,mode='w',encoding='Latin-1')
player1 = {
    'PlfyerName': 'Abuka',
    'Score': 13,
    'awards': None
}
player2 = {
    'PlayerName': 'Miras',
    'Score': 9,
    'awards': None
}
players = []
players.append(player1)
players.append(player2)
#TODO SAVE
json.dump(players, myfile)