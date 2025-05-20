import pandas as pd
import matplotlib.pyplot as plt

'''
This script performs statistical analysis and visualization on height data 
for four sports teams: Men's Swimming, Women's Swimming, Men's Volleyball, 
and Women's Volleyball.

It loads data from CSV files, calculates the average height for each team, 
identifies the tallest and shortest athletes (accounting for ties), and 
generates a bar graph visualizing average height by group.

Outputs:
- Printed general statistics for each group
- Printed average heights for each team
- Printed lists of the five tallest and shortest athletes (including ties) per group
- Bar graph saved as 'average_height_by_team.png'
'''

#Loading each CSV from scraped data
men_swim = pd.read_csv("data/mens_swimming_diving.csv")
women_swim = pd.read_csv("data/womens_swimming_diving.csv")
men_volley = pd.read_csv("data/mens_volleyball.csv")
women_volley = pd.read_csv("data/womens_volleyball.csv")

#Labeling each dataset to identify the group when merging or plotting
men_swim['Group'] = "Men's Swimming"
women_swim['Group'] = "Women's Swimming"
men_volley['Group'] = "Men's Volleyball"
women_volley['Group'] = "Women's Volleyball"

#Mens Swimming and Diving general statistics
print(f'Mens Swimming and Diving: general statistics:')
print(men_swim.describe())

#Womens Swimming and Divng general statistics
print(f'Womens Swimming and Diving: general statistics:')
print(women_swim.describe())

#Mens Volleyball general statistics 
print(f'Mens Volleyball: general statistics:')
print(men_volley.describe())

#Womens Volleyball general statistics 
print(f'Womens Volleyball general statistics:')
print(women_volley.describe())

#Calculating average height for each group
men_swim_avg = men_swim['Height'].mean()
women_swim_avg = women_swim['Height'].mean()
men_volley_avg = men_volley['Height'].mean()
women_volley_avg = women_volley['Height'].mean()

#Printing the results in the terminal
print(f"The average height of the Men's Swimming & Diving team: {men_swim_avg:.2f} inches")
print(f"The average height of the Women's Swimming & Diving team: {women_swim_avg:.2f} inches")
print(f"The average height of the Men's Volleyball team: {men_volley_avg:.2f} inches")
print(f"The average height of the Women's Volleyball team: {women_volley_avg:.2f} inches")

#Creating a DataFrame for average heights by team
avg_data = {
    'Team': ["Men's Swimming", "Women's Swimming", "Men's Volleyball", "Women's Volleyball"],
    'Avg Height': [men_swim_avg, women_swim_avg, men_volley_avg, women_volley_avg]
}

avg_data_df = pd.DataFrame(avg_data)

#Plotting the bar graph
avg_data_df.plot.bar(x='Team', y='Avg Height', title='Average Heights Among Athletes', legend=False)
plt.ylabel('Height (inches)')
plt.xticks(rotation=45)
plt.tight_layout()

#Saving and showing the graph
plt.savefig('average_height_by_team.png')
plt.show()

#Mens swimming and diving team: five tallest heights
top_heights = men_swim['Height'].nlargest(5).unique()
fifth_height = top_heights[-1]
print(f'Five Tallest Mens Swimmers & Divers:')
print(men_swim[men_swim['Height'] >= fifth_height])

#Mens swimming and diving team: five shortest heights
bottom_heights = men_swim['Height'].nsmallest(5).unique()
fifth_shortest = bottom_heights[-1]
print(f'Five shortest Mens Swimmers & Divers:')
print(men_swim[men_swim['Height'] <= fifth_shortest])

#Womens swimming and diving team: five tallest heights
top_heights = women_swim['Height'].nlargest(5).unique()
fifth_height = top_heights[-1]
print(f'Five Tallest Womens Swimmers & Divers:')
print(women_swim[women_swim['Height'] >= fifth_height])

#Womens swimming and diving team: five shortest heights
bottom_heights = women_swim['Height'].nsmallest(5).unique()
fifth_shortest = bottom_heights[-1]
print(f'Five Shortest Womens Swimmers & Divers:')
print(women_swim[women_swim['Height'] <= fifth_shortest])

#Mens volleyball: five shortest height 
top_heights = men_volley['Height'].nlargest(5).unique()
fifth_height = top_heights[-1]
print(f'Five Tallest Mens Volleyball Players:')
print(men_volley[men_volley['Height'] >= fifth_height])

#Mens volleyball: five shortest height 
bottom_heights = men_volley['Height'].nsmallest(5).unique()
fifth_shortest = bottom_heights[-1]
print(f'Five Shortest Mens Volleyball Players:')
print(men_volley[men_volley['Height'] <= fifth_shortest])

#Womens volleyball: five tallest heights 
top_heights = women_volley['Height'].nlargest(5).unique()
fifth_height = top_heights[-1]
print(f'Five Tallest Womens Volleyball Players:')
print(women_volley[women_volley['Height'] >= fifth_height])

#Womens volleyball: five shortest heights
bottom_heights = women_volley['Height'].nsmallest(5).unique()
fifth_shortest = bottom_heights[-1]
print(f'Five Shortest Womens Volleyball Players:')
print(women_volley[women_volley['Height'] <= fifth_shortest])

