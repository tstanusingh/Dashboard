import plotly.graph_objects as go

# Example data
labels = ['URL Clicks', 'Profile Clicks', 'Hashtag Clicks']
values = [40, 35, 25]  # Sample percentages for each click type

fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3)])

fig.update_layout(title='Proportion of Click Types for Tweets with >500 Impressions')
fig.show()
