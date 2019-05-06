import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly_express as px
import plotly.graph_objs as go



psi90_df = pd.read_csv('c:/data/TEST/psi_data_geo.csv')
psi90_df.index.astype(str, copy=False)

#psi_data_df = psi_data_df.append(benchmark_df,ignore_index = True,sort=True)
psi90_df = psi90_df.drop(columns=["Address","Footnote","Start_Date","End_Date"])
#Convert rate to data type float; imported as a string due to "Not Available" values
psi90_df['Rate']=pd.to_numeric(psi90_df['Rate'],errors='coerce')
psi90_df['Rate'].fillna(0,inplace = True)





external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

#button_options={}
#all_options = dict(psi_data_df.groupby('State')['Provider_Name'].apply(list))           
                 
app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.H1(
        children='Map - Hospitals above or below Composite Safety Benchmark',
        style={
            'textAlign':'center',
            'color': colors['text']
        }
    ),

    html.Div(children='PSI-90 Safety Score: Benchmark = 1.0', style ={
        'textAlign': 'center',
        'color': colors['text']
    }),  
                 
dcc.Graph(
    id='create_df_graph',
 #   figure = {
 #       'data': [
 #           {'x':[1],'y':[1],'type': 'bar','name': 'hospital'},
  #          {'x':[2],'y':[2],'type': 'bar','name': 'all'},
  #      ],
  #      'layout': {
  #          'title': 'Hospital Safety Measure compared to Population Benchmark'
  #      }
  #  }
),
  
dcc.RadioItems(
     id = 'radio-items',
     options=[{'label': i, 'value': i} for i in ['Above Benchmark','Below Benchmark']],
     value = 'Above Benchmark',
     labelStyle = {'display': 'inline-block'}

     
            ),

html.Hr(),


html.Hr(),

#html.Div(id='display-selected-values'),


])                    

@app.callback(
     Output('create_df_graph','figure'),
     [Input('radio-items','value')]
 )
def create_graph(selected_value):
       if selected_value == 'Above Benchmark':
           df=psi90_df.query('Rate > 1')
       else:
           df=psi90_df.query('Rate < 1')
       return px.scatter_geo(df,lat='Latitude',lon='Longitude',locations = 'State',locationmode='USA-states', color='Provider_Name',hover_name='Provider_Name',scope='usa')

   
    #query where safety scores worse than normal
    

   
    





    




       
   
    

    
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

