from dash import html
from dash import dcc


layout = html.Div([
    html.Div([
        html.Div([
            html.P(
                "KPI Sales Dashboard", style={"color": "#0084d6",
                                              "font-size": "20px",
                                              'margin-left': '15px',
                                              'margin-top': '15px'}
            ),
            html.P([html.P(dcc.Markdown('''Welcome to the **KPI Sales Dashboard**!''',
                                        style={"color": "#ffffff",
                                               "font-size": "15px",
                                               'margin-left': '15px',
                                               'margin-top': '15px'})),
                    html.P(dcc.Markdown(
                        '''
                        Here, I have created the dashboard using the Python library Plotly dash for data visualizations
                        and dash for web framework. I have analyzed the monthly data using the graphs and key 
                        performance indicators with drop down list. Some graphs are dynamic and some are static.
                        ''',
                        style={"color": "#ffffff",
                               "font-size": "15px",
                               'margin-left': '15px',
                               'margin-right': '15px',
                               'margin-bottom': '15px',
                               'line-height': '1.2',
                               'text-align': 'justify'}
                    )),
                    html.P([
                        'I have used here one year monthly dataset and analyzed and visualized the data using the ',
                        html.A('Plotly', href="https://plotly.com/", target="_blank", style={"color": "#0084d6"
                                                                                             ,'text-decoration': 'none'}),
                        ' for this exercise.',
                    ], style={"color": "#ffffff",
                              "font-size": "15px",
                              'margin-left': '15px',
                              'margin-right': '15px',
                              'margin-bottom': '15px',
                              'line-height': '1.2',
                              'text-align': 'justify',
                              'margin-top': '-15px'}),
                    html.P([dcc.Markdown(
                        '''
                        If you have any questions or need assistance, please don't hesitate to reach out.
                        ''',
                        style={"color": "#ffffff",
                               "font-size": "15px",
                               'margin-left': '15px',
                               'margin-right': '15px',
                               'margin-bottom': '15px',
                               'line-height': '1.2',
                               'text-align': 'justify'},
                    ),
                        html.P(
                            html.A('Mubeen Ali', href='https://www.linkedin.com/in/mubeen-ali-93a327147/',
                                   target="_blank", style={"color": "#0084d6", 'text-decoration': 'none'}),
                            style={"color": "#ffffff",
                                   "font-size": "15px",
                                   'margin-left': '15px',
                                   'margin-right': '15px',
                                   'margin-bottom': '30px',
                                   'line-height': '1.2',
                                   'text-align': 'justify',
                                   'margin-top': '-15px'}),
                    ])
                    ])
        ], className='home_bg eight columns')
    ], className='home_row row')
])
