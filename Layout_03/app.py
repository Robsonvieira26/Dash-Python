import dash
from dash import dcc, html


app = dash.Dash(name=__name__)

app.layout = html.Div([
    html.Div(children=[
        html.Label('Dropdown'),
        dcc.Dropdown(
            id="dp-1",
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'San Francisco', 'value': 'SF'},
            ],
            value='SF'
        ),], style={'margin': '10px 10px 10px 10px'}),

    html.Div(children=[
        html.Label('Slider'),
        dcc.Slider(
             id="slider-1",
             min=0,
             max=9,
             marks={i: 'Label {}'.format(i) if i == 1 else str(i)
                    for i in range(1, 6)},
             value=5,
             ),], style={'margin': '20px 10px 10px 10px'}),
    html.Div(children=[
        html.Label('Checklist'),
        dcc.Checklist(
            id="checklist-1",
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'San Francisco', 'value': 'SF'},
            ],
            value=['SF']
        ),], style={'margin': '20px 10px 10px 10px'}),

    html.Div(children=[
        html.Label('Input Text'),
        dcc.Input(id="input-1", value='', type='text')
    ], style={'margin': '20px 10px 10px 10px'}),
])


if __name__ == '__main__':
    app.run_server(debug=True)
