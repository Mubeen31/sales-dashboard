from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app
import pandas as pd

layout = html.Div([

    dcc.Dropdown(id='input_data',
                 style={'display': 'none'}),
    html.Div([
        html.Div([
            html.P([html.H3('Data Table', style={"color": "#0084d6", }),
                    dcc.Markdown('''
                    The below data in the table has been used in this **dashboard**.
                    ''', style={'margin-top': '10px',
                                'color': '#ffffff',
                                'line-height': '1.2'}),
                    html.Hr(),
                    dbc.Spinner(html.Div(id='data_table', className="table-responsive text-nowrap overflow-auto",
                                         style={'height': '500px'}), color='info')])
        ], className='table_bg twelve columns')
    ], className='table_row row')

])


@app.callback(Output("data_table", "children"),
              Input("input_data", "value"))
def update_table(data):
    df = pd.read_csv('sales_data.csv')
    return dbc.Table.from_dataframe(df, striped=False, bordered=False, hover=True)
