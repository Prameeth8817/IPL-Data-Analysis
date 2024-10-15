# Importing Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/matches.csv")

# Display first few rows of the dataset
print(df.head())

# Drop columns that are not necessary
df.drop(columns=['umpire3', 'city'], inplace=True)

# Data Cleaning: Fill missing values in winner and player_of_match columns
df['winner'].fillna('No result', inplace=True)
df['player_of_match'].fillna('No award', inplace=True)

# Display the number of matches per season
matches_per_season = df['season'].value_counts()
print(matches_per_season)

# Visualize the number of matches per season
plt.figure(figsize=(10,6))
sns.countplot(data=df, x='season', palette='Set2')
plt.title('Number of Matches per Season')
plt.show()

# Top 10 players who won the most Player of the Match awards
top_players = df['player_of_match'].value_counts().head(10)
print(top_players)

# Visualize top players
plt.figure(figsize=(10,6))
sns.barplot(x=top_players.values, y=top_players.index, palette='magma')
plt.title('Top 10 Players with Most Player of the Match Awards')
plt.show()

# Display teams with the most wins
most_wins = df['winner'].value_counts()
print(most_wins)

# Visualize teams with most wins
plt.figure(figsize=(10,6))
sns.barplot(x=most_wins.values, y=most_wins.index, palette='coolwarm')
plt.title('Teams with Most Wins in IPL')
plt.show()

# Venue with the most matches
most_venues = df['venue'].value_counts().head(10)
print(most_venues)

# Visualize venues with the most matches
plt.figure(figsize=(10,6))
sns.barplot(x=most_venues.values, y=most_venues.index, palette='viridis')
plt.title('Top 10 Venues with Most Matches in IPL')
plt.show()

# Analyze toss decisions (bat or field)
toss_decisions = df['toss_decision'].value_counts()
print(toss_decisions)

# Visualize toss decisions
plt.figure(figsize=(6,6))
sns.pie(toss_decisions, labels=toss_decisions.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
plt.title('Toss Decisions in IPL')
plt.show()

# Probability of winning if a team wins the toss
toss_winner = df[df['toss_winner'] == df['winner']]
win_percentage = (len(toss_winner) / len(df)) * 100
print(f'Probability of winning if a team wins the toss: {win_percentage:.2f}%')
