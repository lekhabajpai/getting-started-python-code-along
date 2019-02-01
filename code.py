# --------------
import yaml

# Read the data of the format .yaml type
with open(path) as f:
    data = yaml.load(f)
f.close()
#print(data)
# Find data type of the file
type_of_data = type(data)
print("Type of Data= ", type_of_data)
# In which city, and at which venue the match was played and where was it played ?
city = data['info']['city']
print('City= ', city)
venue = data['info']['venue']
print('Venue= ', venue)
# Which are all the teams that played in the tournament ? How many teams participated in total?
team1 = data['info']['teams'][0]
team2 = data['info']['teams'][1]
print('Teams that played are',team1, 'and', team2)
# Which team won the toss and what was the decision of toss winner ?
decision = data['info']['toss']['decision']
toss_winner = data['info']['toss']['winner']
print('decision=',decision, 'toss won by =', toss_winner)
# Find the first bowler and first batsman who played the first ball of the first inning
first_bowler = data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']
first_batsman = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
print('First Bowler= ',first_bowler, 'First Batsman= ', first_batsman)
# How many deliveries were delivered in first inning ?
deliveries_1stinning = len(data['innings'][0]['1st innings']['deliveries'])
print('Deliveries in 1st Innings= ', deliveries_1stinning)
# How many deliveries were delivered in second inning ?
deliveries_2ndinning = len(data['innings'][1]['2nd innings']['deliveries'])
print('Deliceries in 2nd Innings= ', deliveries_2ndinning)
# Which team won and how ?
winner = data['info']['outcome']['winner']
how = data['info']['outcome']['by']['runs']
print('Winner=', winner, 'How= ', how)



