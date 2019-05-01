import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly_express as px
import plotly.graph_objs as go

psi_data_df = pd.read_csv('c:/data/TEST/psi_data.csv', dtype = {'Zip_Code':'str'})
psi_data_df.index.astype(str, copy=False)
benchmark_df = pd.read_csv('c:/data/TEST/benchmark.csv')
#benchmarkh_df = pd.read_csv('c:/data/TEST/benchmarkh.csv')

#psi_data_df = psi_data_df.append(benchmark_df,ignore_index = True,sort=True)
psi_data_df = psi_data_df.drop(columns=["Address","Footnote","Start_Date","End_Date","Location"])

#psi_df = px.data.psi_data_df()


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

all_options={}
all_options = dict(psi_data_df.groupby('State')['Provider_Name'].apply(list))           
                 
app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.H1(
        children='Hospital PSI - as compared to Population',
        style={
            'textAlign':'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Select a State and Hospital', style ={
        'textAlign': 'center',
        'color': colors['text']
    }),  
                 
dcc.Graph(
    id='safety measures',
    figure = {
        'data': [
            {'x':[1],'y':[1],'type': 'bar','name': 'hospital'},
            {'x':[2],'y':[2],'type': 'bar','name': 'all'},
        ],
        'layout': {
            'title': 'Hospital Safety Measure compared to Population Benchmark'
        }
    }
),
  
dcc.Dropdown(
     id = 'state-dropdown',
     options=[{'label': k, 'value': k} for k in all_options.keys()],
     value = 'GA'
            ),

html.Hr(),

dcc.Dropdown(id='hospital-dropdown'),
html.Hr(),

html.Div(id='display-selected-values')
])                    

@app.callback(
     Output('hospital-dropdown','options'),
     [Input('state-dropdown','value')]
     )
def set_provider_options(selected_state):
    return[{'label' : i, 'value': i} for i in all_options[selected_state]]

@app.callback(
    Output('state-dropdown','value'),
    [Input('state-dropdown','options')]
)
def set_provider_values(available_options):
    return available_options[0]['value']

@app.callback(
     Output('display-selected-values','children'),
     [Input('state-dropdown','value'),
      Input('hospital-dropdown','value')]
      )
def set_display_graph(selected_state,selected_provider):
    df1 = psi_data_df[psi_data_df['Provider_Name']==selected_provider]
    results2plot_df = df1.append(benchmark_df,ignore_index=True,sort=True)

       
   
    

    
    #u'{} is a facility in {}'.format(
     #   selected_provider, selected_state,
   # )



#dcc.graph(
 #   id='example-graph',
 #   figure={
 #       'data':[
  #          {'x': [1,2,3],'y':['PSI-3','PSI-8','PSI-15'],'type': 'bar','name': 'test'},
 #           {'x': [1,2,3],'y':['PSI-3','PSI-8','PSI-15'],'type': 'bar','name': 'OVERALL POPULATION'}
  #      ]
  #  }
#)

if __name__=="__main__":
    app.run_server(debug=True, port=8050) 

