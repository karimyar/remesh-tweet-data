import json 
import pandas as pd
from collections import Counter
import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

## open and load given json file ## 
f = open("data.json")
data = json.load(f)

## transform json object into easy-to-work with dataframes ## 
tweets = pd.DataFrame(data=data['tweets'], columns=['id', 'user', 'text', 'hashtags', 'retweet_id', 'likes'])
hashtags = pd.DataFrame(data=data['hashtags'], columns=['id','name'])
users = pd.DataFrame(data=data['users'], columns=['id','username'])

## append additional important data to dataframe ## 
tweets['text-length'] = tweets['text'].str.len()
tweets['num-tags'] = tweets['hashtags'].str.len()
tweets['num-likes'] = tweets['likes'].str.len()
tweets['num-tags_str'] = tweets['num-tags'].astype(str)
tweets['num-likes_str'] = tweets['num-likes'].astype(str)
tweets['text-length_str'] = tweets['text-length'].astype(str)

## get max data for range selectors ## 
max_likes = max(tweets['num-likes'])
max_text = max(tweets['text-length'])

## DASH - web-based interactive data visualizations ## 
app = dash.Dash(__name__)

app.layout = (
    html.Div([
        dcc.Graph(id="scatter-plot-tags"),
        html.P("Hashtags per tweet:"),
        dcc.RangeSlider(
            id='tag-slider',
            min=0, max=4, step=1,
            marks={0: '0', 1: '1', 2: '2', 3: '3', 4: '4'},
            value=[0, 4],
            updatemode = "drag"
        ),

    html.Div([
      dcc.Graph(id="scatter-plot-likes"),
        html.P("Likes per tweet:"),
        dcc.RangeSlider(
            id='like-slider',
            min=0, max=max_likes, step=10,
            marks={i: '{}'.format(i) for i in range(0,max_likes,20)},
            value=[0, max_likes],
            updatemode = "drag"
       )
])]))

@app.callback(
    Output("scatter-plot-tags", "figure"),
    [Input("tag-slider", "value")])

## plot that has the range slider for hashtags per tweet
def scatter_graph_tag(tag_slider_range): 
    low, high = tag_slider_range
    mask = (tweets['num-tags'] >= low) & (tweets['num-tags'] <= high)
    fig = px.scatter(tweets[mask], x="id", y="num-likes", color="text-length", hover_data=['num-tags'],
        labels={"id": "Tweets (based on id)", "num-likes": "Total # of likes (per tweet)", "num-tags": "Number of hashtags", "text-length": "Length of tweet (characters)"}, title="Likes per Tweet based on # of hashtags")
    return fig

@app.callback(
    Output("scatter-plot-likes", "figure"),
    [Input("like-slider", "value")])

## plot that has the range slider for likes per tweet
def scatter_graphs_like(like_slider_range): 
    low, high = like_slider_range
    mask = (tweets['num-likes'] >= low) & (tweets['num-likes'] <= high)
    fig2 = px.scatter(tweets[mask], x="id", y="text-length", color="num-tags_str", hover_data=['num-likes'],
        labels={"id": "Tweets (based on id)", "text-length": "Length of tweet (characters)", "num-tags_str": "Number of hashtags", "num-likes": "Number of likes"}, title="Length of tweet based on # of likes")
    return fig2

if __name__ == '__main__':
    app.run_server(debug=True)
