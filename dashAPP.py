import dash
# from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

df = px.data.tips()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button("Rotate", id='button', n_clicks=0),
    html.Div(id="output", children=[])
])


@app.callback(
    Output('output', 'children'),  # The output will be displayed in  html.Div(id="output)
    [Input("button", "n_clicks")])
def rotate_figure(n_clicks):
    fig = px.histogram(df, x="sex", height=500)
    fig.update_xaxes(tickangle=n_clicks * 45)

    # The plotly figure is saved as HTML in a variable
    html_data = fig.to_html(full_html=False, include_plotlyjs='cdn')

    # The variable is then displayed as a plot using Iframe from dash_html_components
    html_plot = html.Iframe(srcDoc=html_data,
                            style={"height": "1000px",
                                   "width": "1000px",
                                   "display": "flex",
                                   "align-items": "center",
                                   "justify-content": "center"}
                            )

    # Now you can return the Iframe as a children of a Div
    return html_plot


app.run_server(debug=True)
