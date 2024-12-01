import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Sample data preparation
df = pd.DataFrame({
    'replies': [50, 70, 60, 80, 65],
    'retweets': [20, 30, 40, 10, 15],
    'likes': [100, 150, 130, 120, 140],
    'media_engagements': [300, 400, 500, 200, 300],
    'media_views': [1200, 1600, 1800, 2200, 1400],
    'tweet_date': [1, 2, 5, 7, 9],
    'tweet_character_count': [18, 19, 15, 16, 17],
    'timestamp': ['2020-07-01 14:30', '2020-08-05 16:00', '2020-06-10 14:30', '2020-07-22 11:00', '2020-08-01 17:00']
})

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Filter by date range (June-August 2020)
df = df[(df['timestamp'].dt.month >= 6) & (df['timestamp'].dt.month <= 8)]

# Filter by time
df = df[(df['timestamp'].dt.hour >= 15) & (df['timestamp'].dt.hour <= 17)]

# Filter by odd tweet date and even media views
df = df[(df['tweet_date'] % 2 != 0) & (df['media_views'] % 2 == 0)]

# Filter by character count < 20
df = df[df['tweet_character_count'] < 20]

# Calculate median media engagements
median_engagements = df['media_engagements'].median()

# Filter tweets with media engagements > median
df = df[df['media_engagements'] > median_engagements]

# Plot
df[['replies', 'retweets', 'likes']].plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Replies, Retweets, and Likes for Tweets with Media Engagements > Median')
plt.xlabel('Tweet Index')
plt.ylabel('Count')
plt.show()
