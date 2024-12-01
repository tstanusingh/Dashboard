1. Pie Chart for Click Proportions (Tweets with >500 Impressions)
Requirements:
Represent the proportion of clicks: URL clicks, user profile clicks, and hashtag clicks.
Only for tweets with more than 500 impressions.
Provide a drill-down to view specific types of clicks for each tweet.
Approach:
Data Preprocessing:

Filter tweets with impressions greater than 500.
Extract and aggregate the total clicks for URL, user profile, and hashtags.
Calculate the percentage share for each type of click.
Visualization:

Use a Pie Chart to represent the proportion of each click type.
Implement a drill-down functionality where you can click on a segment to view detailed breakdowns for individual tweets.
Implementation Example (using Plotly):

python
Copy code
import plotly.graph_objects as go


labels = ['URL Clicks', 'Profile Clicks', 'Hashtag Clicks']
values = [40, 35, 25]  # Sample percentages for each click type

fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3)])

fig.update_layout(title='Proportion of Click Types for Tweets with >500 Impressions')
fig.show()
Drill-down functionality could be implemented via interactive dashboard tools, e.g., Tableau, Power BI, or using Plotly Dash for custom web apps.

2. Scatter Plot: Media Engagements vs. Media Views (Tweets with >10 Replies)
Requirements:
Scatter Plot showing the relationship between media engagements and media views.
Highlight tweets with an engagement rate above 5%.
Work only between 6 PM IST to 11 PM IST and only for tweets where:
Tweet date is an odd number.
Tweet word count is above 50.
Tweets must have received more than 10 replies.
Approach:
Data Preprocessing:

Filter tweets based on the timestamp (6 PM to 11 PM IST).
Check if the tweet date is an odd number and word count > 50.
Calculate engagement rate as:
Engagement Rate
=
Total Engagements (replies + likes + retweets)
Impressions
×
100
Engagement Rate= 
Impressions
Total Engagements (replies + likes + retweets)
​
 ×100
Identify tweets with engagement rate > 5% and color them differently in the scatter plot.
Time Filtering:

Filter data for the required hours (6 PM - 11 PM IST).
Convert timestamps to IST (considering time zone offsets if needed).
Visualization:

Use scatter plot with media engagements on the x-axis and media views on the y-axis.
Highlight points where the engagement rate is above 5%.