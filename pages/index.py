import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Will It Stand?

            United States Supreme Court decisions are difficult to predict, often confounding even close watchers of the court.

            Nina, our computer model, will make these predicitions for us, using the limited information we provide it from previous decisions.

            We will limit the cases under consideration to those in which the Supreme Court ruled on the constitutionality of federal law. The data is from Keith E. Whittington, The Judicial Review of Congress Database (May 2019) (available at [https://scholar.princeton.edu/kewhitt/judicial-review-congress-database](https://scholar.princeton.edu/kewhitt/judicial-review-congress-database)) 

            """
        ),
        dcc.Link(dbc.Button('Predict a Case', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])