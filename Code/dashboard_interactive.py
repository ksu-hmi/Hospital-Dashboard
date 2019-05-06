import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly_express as px
import plotly.graph_objs as go


#Read the data using pandas
psi_data_df = pd.read_csv('c:/data/TEST/psi_data.csv', dtype = {'Zip_Code':'str'})
psi_data_df.index.astype(str, copy=False)
benchmark_df = pd.read_csv('c:/data/TEST/benchmark.csv')

#Convert rate to data type float; imported as a string due to "Not Available" values
psi_data_df['Rate']=pd.to_numeric(psi_data_df['Rate'],errors='coerce')
psi_data_df['Rate'].fillna(0,inplace = True)


#Drop columns not needed
psi_data_df = psi_data_df.drop(columns=["Address","Footnote","Start_Date","End_Date","Location"])
#psi_data_df.info()



#Sets up html layout using Dash 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

#Create dictionary of items to populate dropdown
all_options={}
all_options = dict(psi_data_df.groupby('State')['Provider_Name'].apply(list))           
                 
app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.H1(
        children='Hospital PSI - as compared to Population Benchmark',
        style={
            'textAlign':'center',
            'color': colors['text']
        }
    ),

html.Div(children='Select a State and Hospital', style ={
        'textAlign': 'center',
        'color': colors['text']
    }),  



  
dcc.Dropdown(
     id = 'state-dropdown',
     options=[{'label': k, 'value': k} for k in all_options.keys()],
     value = 'GA'
            ),

html.Hr(),

dcc.Dropdown(id='hospital-dropdown'),
html.Hr(),

html.Div(id='display-selected-values'),

dcc.Graph(
    id='create-df-graph',
 
),

      



])                    


#Code to capture user choice and utilize as input for graphics and page verbiage
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
def set_display_children(selected_state,selected_provider):
     return u'{} is a facility in {}'.format(
      selected_provider, selected_state,
    )

#Reshapes df for input to graphic using user input from above

@app.callback(
    Output('create-df-graph','figure'),
     [Input('hospital-dropdown','value')]
      )
def create_df(selected_provider):
       df1 = psi_data_df[psi_data_df['Provider_Name']==selected_provider]
       results2plot_df = df1.append(benchmark_df,ignore_index=True,sort=True)
       return px.bar(results2plot_df, x='Measure_ID',y='Rate', color='Provider_Name', barmode = 'group',hover_name='Measure_Name')

      
  

if __name__=="__main__":
    app.run_server(debug=True, port=8050) 

