import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)  # Instanciando o Dash

# Cria um DataFrame
df = pd.DataFrame({
    'Cidade': ['São Paulo', 'Nova York', 'Londres', 'Tóquio', 'Sydney'],
    'População': [12325232, 8623000, 8982000, 9273000, 5230000],
    'País': ['Brasil', 'Estados Unidos', 'Reino Unido', 'Japão', 'Austrália']
})

fig = px.bar(df, x='Cidade', y='População', color='País', barmode='group')

# === Layout ===
app.layout = html.Div(children=[
    html.H1(children='Dash Exemplo 1'),

    html.Div(children='''
        Exemplo de Dash com Plotly Express.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )

])
if __name__ == '__main__':
    app.run_server(debug=True)
