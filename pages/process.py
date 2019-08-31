import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process

            There were 25 featues in the original data set, including two targets. One target was a simple constituional | unconstitional classifier, while the other broke the unconstitional class into partial ruling | complete ruling subclasses.

            A couple of features leaked data from the future. One was the number of justices who dissented from the majority opinion. The other was whether or not the decision reversed the lower court't ruling.

            This latter feature was used to engineer a useful feature that did not leak data. There was no indication of the lower court's ruling in the data set. That feature was created by comparing the Supreme Court's decision with the reversed feature and swaping the value of the decision of reversed was true. The information was captured in a 'lower court decision' column and the other two leaky features were discarded. This new feature does not leak data from the future if we consider a case as it is being presented to the Supreme Court but before a ruling is issued.


            """
        ),

    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src='assets/cases_per_issue.jpg', className='img-fluid'),
    ]
    
)

layout = dbc.Row([column1, column2])