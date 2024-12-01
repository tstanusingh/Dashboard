import matplotlib.pyplot as plt
import pandas as pd

# Sample data preparation
df = pd.DataFrame({
    'media_engagements': [150, 200, 50, 300, 400],
    'media_views': [1000, 1500, 1200, 1800, 2200],
    'engagement_rate': [4.5, 5.2, 3.0, 6.0, 4.8],
    'tweet_hour': [18, 19, 20, 22, 21],  # in 24-hour format
    'tweet_date': [1, 5, 3, 7, 9],  # Odd-numbered dates
    'word_count': [60, 70, 80, 55, 65],
    'replies': [12, 15, 20, 10, 13]
})

# Filter by time (6 PM to 11 PM IST)
df = df[(df['tweet_hour'] >= 18) & (df['tweet_hour'] <= 23)]

# Filter by tweet date (odd number) and word count > 50
df = df[(df['tweet_date'] % 2 != 0) & (df['word_count'] > 50)]

# Highlight engagement rate > 5%
highlight = df[df['engagement_rate'] > 5]

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(df['media_engagements'], df['media_views'], c=df['engagement_rate'] > 5, cmap='viridis')
plt.title('Media Engagements vs. Media Views')
plt.xlabel('Media Engagements')
plt.ylabel('Media Views')
plt.show()

