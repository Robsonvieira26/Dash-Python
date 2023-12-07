import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(name=__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H6("Inicianco com callbacks"),
    html.Div(children=[
        "Entrada: ",
        dcc.Input(id="input-1", value='', type='text'),
    ]),
    html.Br(),
    html.Div(id="div-1"),
])


@app.callback(
    Output(component_id='div-1', component_property='children'),
    [Input(component_id='input-1', component_property='value')]
    # []
)
def update_output_div(input_value):
    if input_value != '':
        return "Saida: {}".format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
