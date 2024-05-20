import matplotlib.pyplot as plt

team1_score = [2,50,60,48,10,45,69,87]
team2_score = [56,32,98,74,12,65,5,56]

score_range = [5,10,15,20,25,30,35,40]

plt.scatter(team1_score,score_range,color = 'r')
plt.scatter(team2_score,score_range,color = 'b')

plt.show()