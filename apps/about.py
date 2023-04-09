from dash import html


layout = html.Div([

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Mubeen Ali', style={"color": "#0084d6",
                                                 'margin-left': '15px',
                                                 'margin-top': '15px'}),
                    html.P('Data scientist with 1+ years experience in building data-intensive applications in Python '
                           'programming, overcoming complex challenges, proficient in predictive data'
                           ' modeling, processing, visualizing, dashboards, and extracting actionable insights from '
                           'data.',
                           style={"color": "#ffffff",
                                  "font-size": "15px",
                                  'margin-left': '15px',
                                  'margin-right': '15px',
                                  'margin-top': '15px',
                                  'margin-bottom': '15px',
                                  'line-height': '1.2',
                                  'text-align': 'justify'
                                  }
                           ),
                    html.Div([
                        html.A(href='https://github.com/Mubeen31', target='_blank',
                               children=[html.Img(src='/assets/github.png', height="30px",
                                                  style={"margin-top": '15px',
                                                         'margin-left': '15px',
                                                         'margin-bottom': '15px'})]),
                        html.A(href='https://community.plotly.com/u/jawabutt/summary', target='_blank',
                               children=[html.Img(src='/assets/plotly.ico', height="30px",
                                                  style={"margin-top": '20px',
                                                         'margin-left': '15px',
                                                         'margin-bottom': '15px',
                                                         "background-color": "#35384b"})]),
                        html.A(href='https://www.linkedin.com/in/mubeen-ali-93a327147/', target='_blank',
                               children=[html.Img(src='/assets/linkedin.png', height="30px",
                                                  style={"margin-top": '20px',
                                                         'margin-left': '15px',
                                                         'margin-bottom': '15px',
                                                         "background-color": "#35384b"})]),
                    ])
                ], className='first_text_column'),
                html.Div([
                    html.Img(src='/assets/programmer.gif', className='gif_image')
                ], className='gif_column')
            ], className='gif_row')
        ], className='about_bg eight columns')
    ], className='about_row row')

])
