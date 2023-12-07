import dash
from dash import dcc, html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(name=__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Hello Dash'),
    html.Div('Dash: Web Dashboards with Python'),
])


if __name__ == '__main__':
    app.run_server(debug=True)
