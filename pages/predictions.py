import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

from app import app

from joblib import load
pipeline = load('assets/pipeline_3.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions


            """
        ),
        dcc.Markdown('#### Constitutional Issue'), 
        dcc.Dropdown(
            id = 'area1', 
            options = [
                {'label': 'Due Process', 'value': '1'}, 
                {'label': 'Substantive Rights', 'value': '2'}, 
                {'label': 'Equality', 'value': '3'}, 
                {'label': 'Economic', 'value': '4'}, 
                {'label': 'Federalism', 'value': '5'},
                {'label': 'Separation of Powers', 'value': '6'}, 
            ], 
            value = '1', 
            className='mb-5'
        ), 
        dcc.Markdown('#### Lower Court Decision'), 
        dcc.Dropdown(
            id = 'lower_court', 
            options = [
                {'label': 'Constitutional', 'value': '0'}, 
                {'label': 'Unconstitional', 'value': '1'},  
            ], 
            value = '0', 
            className='mb-5'
        ),
        dcc.Markdown('#### Congress'), 
        dcc.Slider(
            id = 'congress',
            min=0,
            max=180,
            marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(0, 181, 20)},
            value=100,
            className='mb-5'
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Expected Decision', className='mb-5'), 
        html.Div(id='prediction-decision', className='lead')
    ]
)

layout = dbc.Row([column1, column2])

@app.callback(
    Output('prediction-decision', 'children'),
    [Input('area1', 'value'), Input('lower_court', 'value'), Input('congress', 'value')],
)
def predict(area1, lower_court, congress):
    df = pd.DataFrame(
        columns=['area1', 'lower_court', 'congress'], 
        data=[[area1, lower_court, congress]]
    )
    y_pred = pipeline.predict(df)[0]
    verdict = 'Constitutional' if y_pred == 0 else 'Unconstitional'
    return f'Supreme Court decision: {verdict}'