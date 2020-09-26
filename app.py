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


    # Paragraph
    html.Div(html.P([html.Br(),'Choose from the options below to predict your flight delay:',html.Br(),],
        style={
            'textAlign': 'left',
            'color': colors['paragraph']
        })),
# Dropdown boxes
# --------------

    html.Div(children='Choose Airline', style={
        'textAlign': 'left',
        'color': colors['text'],
        'width': '33%', 
        'display': 'inline-block'
    }),  
        html.Div(children='Choose Month', style={
        'textAlign': 'left',
        'color': colors['text'],
        'width': '33%', 
        'display': 'inline-block'
    }), 
        html.Div(children='Choose Departure Time', style={
        'textAlign': 'left',
        'color': colors['text'],
        'width': '33%', 
        'display': 'inline-block'
    }),   
    dcc.Dropdown(
        options=[
            {'label': u'United Air Lines Inc.', 'value': 'UA'},
            {'label': 'American Airlines Inc.', 'value': 'AA'},
            {'label': 'US Airways Inc.', 'value': 'US'},
            {'label': 'Frontier Airlines Inc.', 'value': 'F9'},
            {'label': 'JetBlue Airways', 'value': 'B6'},
            {'label': 'Skywest Airlines Inc.', 'value': 'OO'},
            {'label': 'Alaska Airlines Inc.', 'value': 'AS'},
            {'label': 'Spirit Air Lines', 'value': 'NK'},
            {'label': 'Southwest Airlines Co.', 'value': 'WN'},
            {'label': 'Delta Air Lines Inc.', 'value': 'DL'},
            {'label': 'Atlantic Southeast Airlines', 'value': 'EV'},
            {'label': 'Hawaiian Airlines Inc.', 'value': 'HA'},
            {'label': 'American Eagle Airlines Inc.', 'value': 'MQ'},
            {'label': 'Virgin America', 'value': 'VX'}	
        ],
        value='UA',
        style={'width': '33%', 'display': 'inline-block'}
    ),

    dcc.Dropdown(
        options=[
            {'label': u'January', 'value': '1'},
            {'label': 'February','value': '2'},
            {'label': 'March', 'value': '3'},
            {'label': 'April', 'value': '4'},
            {'label': 'May', 'value': '5'},
            {'label': 'June', 'value': '6'},
            {'label': 'July', 'value': '7'},
            {'label': 'August', 'value': '8'},
            {'label': 'September', 'value': '9'},
            {'label': 'October', 'value': '10'},
            {'label': 'November', 'value': '11'},
            {'label': 'December', 'value': '12'}
        ],
        value='1',
        style={'width': '33%', 'display': 'inline-block'}
    ),

    dcc.Dropdown(
        options=[
            {'label': 'Skywest Airlines Inc.', 'value': 'OO'},
            {'label': 'Alaska Airlines Inc.', 'value': 'AS'},
            {'label': 'Spirit Air Lines', 'value': 'NK'},
            {'label': 'Southwest Airlines Co.', 'value': 'WN'},
            {'label': 'Delta Air Lines Inc.', 'value': 'DL'},
            {'label': 'Atlantic Southeast Airlines', 'value': 'EV'},
            {'label': 'Hawaiian Airlines Inc.', 'value': 'HA'},
            {'label': 'American Eagle Airlines Inc.', 'value': 'MQ'},
            {'label': 'Virgin America', 'value': 'VX'}	
        ],
        style={'width': '33%', 'display': 'inline-block'}
    ),

    html.Div(children='Choose departure airport', style={
        'textAlign': 'left',
        'color': colors['text'],
        'width': '33%', 
        'display': 'inline-block'
    }),    

    html.Div(children='Day of the Week', style={
        'textAlign': 'left',
        'color': colors['text'],
        'width': '33%', 
        'display': 'inline-block'
    }),  
    # blank space for formatting
    html.Div(children='', style={
        'textAlign': 'left',
        'color': colors['text'],
        'width': '33%', 
        'display': 'inline-block'
    }),  

    
    dcc.Dropdown(
        options=[
            {'label': 'Skywest Airlines Inc.', 'value': 'OO'},
            {'label': 'Alaska Airlines Inc.', 'value': 'AS'},
            {'label': 'Spirit Air Lines', 'value': 'NK'},
            {'label': 'Southwest Airlines Co.', 'value': 'WN'},
            {'label': 'Delta Air Lines Inc.', 'value': 'DL'},
            {'label': 'Atlantic Southeast Airlines', 'value': 'EV'},
            {'label': 'Hawaiian Airlines Inc.', 'value': 'HA'},
            {'label': 'American Eagle Airlines Inc.', 'value': 'MQ'},
            {'label': 'Virgin America', 'value': 'VX'}	
        ],
        style={'width': '33%', 'display': 'inline-block'}
    ),    
    # Departure date
    dcc.Dropdown(
        options=[
            {'label': u'Monday', 'value': '1'},
            {'label': 'Tuesday', 'value': '2'},
            {'label': 'Wednesday', 'value': '3'},
            {'label': 'Thursday', 'value': '4'},
            {'label': 'Friday', 'value': '5'},
            {'label': 'Saturday', 'value': '6'},
            {'label': 'Sunday', 'value': '7'}
        ],
        value='1',
        style={'width': '33%', 'display': 'inline-block'}
    ),   
    
        # blank space for formatting
        html.Div(children='', style={
        'textAlign': 'left',
        'color': colors['text'],
        'width': '33%', 
        'display': 'inline-block'
    }), 

# Images

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


])

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
