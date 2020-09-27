# Import dependencies
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Build app
# ---------------
app = dash.Dash()

# Data source
df = pd.read_csv('../resources/flights_sample.csv')

# Dict of colours
colors = {
    'background': '#1B6F93',
    'text': '#7FDBFF',
    'header': '#FFFFFF',
    'paragraph': '#9BECFA',
    'plot': '#9BECFA',
    'plot2': '#B0B0B0'
}

# Header
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.Img(id= 'panda', src='https://image.shutterstock.com/image-vector/little-panda-super-hero-flies-260nw-650591155.jpg', style={'height':'10%', 'width':'10%', 'display':'inline-block'}),
    html.H1(
        children='Flying Pandas',
        style={
            'textAlign': 'center',
            'color': colors['header'],
            'display':'inline-block'
        }
    ),
    html.H2(
        children='How late will your flight be?',
        style={
            'textAlign': 'left',
            'color': colors['text']
        }
    ),
# Background and Images
# --------------

# Intro
    html.Div(html.P(['Late flights are a pain, ruining schedules and delaying plans. Use our app to help regain control over your time by planning for your flight delays before they happen.', html.Br(), html.Br()],
        style={
            'textAlign': 'left',
            'color': colors['paragraph']
        })),
    
    # Delays by Airline Graph
    dcc.Graph(
        id='delays',
        figure={
            'data': [
                {'x':df['AIRLINE'], 'y': df['DEPARTURE_DELAY'], 'type':'box', 'name': 'Departure',
                'marker' : { "color" : colors['plot']}},
                {'x':df['AIRLINE'], 'y': df['ARRIVAL_DELAY'], 'type':'box', 'name': 'Arrival',
                'marker' : { "color" : colors['plot2']}}
            ],
            'layout' : {
                'title': 'Delays by Airline',
                'xaxis': {
                    'title':'Airline'
                },
                'yaxis':{
                    'title':'Delay in Minutes'
                },
                'plot_bgcolor':colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    ),


    # # Paragraph
    # html.Div(html.P([html.Br(),'Choose from the options below to predict your flight delay:',html.Br(),],
    #     style={
    #         'textAlign': 'left',
    #         'color': colors['paragraph']
    #     })),

# Initial Analysis Images

    html.Div(html.P([html.Br(), 'Our analyses have also shown the following patterns:'],
        style={
            'textAlign': 'left',
            'color': colors['paragraph']
        })),
    

    html.Img(id= 'dept_delay_by_month', 
            src='https://github.com/Pandas-UFT/Pandas/blob/master/figures/month_departure_delay.png?raw=true',
           style={'width': '45%', 
                'display': 'inline-block'
                } 
            ),

    html.Img(id= 'arr_delay_by_time', 
            src='https://github.com/Pandas-UFT/Pandas/blob/master/figures/time_arrival_delay.png?raw=true',
           style={'width': '45%', 
                'display': 'inline-block'
                }
            ), 

# Machine Learning Images

    html.Div(html.P([html.Br(), 'Our machine learning is still under development but has shown the following so far.'],
        style={
            'textAlign': 'left',
            'color': colors['paragraph']
        })),
    

    html.Img(id= 'ml_arrival', 
            src='https://github.com/Pandas-UFT/Pandas/blob/master/figures/month_departure_delay.png?raw=true',
           style={'Align': 'center',
                'width': '45%', 
                'display': 'inline'
                } 
            ),
    html.Img(id= 'ml_arrival_graph', 
            src='https://github.com/Pandas-UFT/Pandas/blob/master/figures/month_departure_delay.png?raw=true',
           style={'Align': 'center',
                'width': '45%', 
                'display': 'inline'
                } 
            )


])

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
