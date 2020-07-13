#################################################################
#       Created On: 12/07/2020                                  #     
#       @author: Abhilash Gupta (abhilash.gupta22@gmail.com)    #
#                                                               #
#       This file contains code for client side UI              #     
#                                                               #
#################################################################

#Importing libraries
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc 
import dash_core_components as dcc
import dash_html_components as html


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Printing the heading
client_heading = dbc.Container([dbc.Row(
                                [html.H1("Client")]
                                , justify = "center"
                                , align = "center")])


# For adding the port
server_endpoint_input = html.Div([
                            dcc.Input(
                                    placeholder='Enter server endpoint...',
                                    type='text',
                                    size = 50,
                                    className = "mb-3",
                                    value=''
                                    ),
                                    ], 
                                    style = dict (
                                            marginTop = 50,
                                            ),)

# Connection Button
connections_button = html.Button("Check Connection", id = "btn_connect_server", n_clicks = 0,
                                 style = dict (
                                            marginTop = 50,
                                            ))

# Connection Label
connection_status_label = html.Div(id = "connections_status",
                                    style = dict (
                                            marginTop = 50,
                                            ))

# Div for connection server check
div_server_connection = html.Div([
                            dbc.Row([
                                    dbc.Col(server_endpoint_input, width = {"size":3,"offset": 1}),
                                    dbc.Col(connections_button, width = {"size":3}),
                                    dbc.Col(connection_status_label, width = {"size":3}),
                                    ]),
                                ])

# Drop down to list all the history access
dropdown_history_access = html.Div([
                            dcc.Dropdown(
                                    options=[
                                            {'label': 'New York City', 'value': 'NYC'},
                                            {'label': 'Montréal', 'value': 'MTL'},
                                            {'label': 'San Francisco', 'value': 'SF'}
                                            ],
                                    multi=True,                               
                                    value="",
                                    placeholder = "Select History Data...",
                                    ),                           
                                    ],
                                    style = dict (
                                            marginTop = 20
                                            ),)

# Create list button for History Data
create_history_model_button = html.Button("Create List", id = "btn_history_data", n_clicks = 0,
                                 style = dict (
                                            marginTop = 20,
                                            ))

# Div for history data
div_history_data = html.Div([
                        dbc.Row([
                                dbc.Col(dropdown_history_access, width = {"size":5,"offset": 1}),
                                dbc.Col(create_history_model_button, width = {"size":3}),
                                ]),
                            ])
                            
# Drop down to list all the runtime data access tab
dropdown_runtime_access = html.Div([
                            dcc.Dropdown(
                                    options=[
                                            {'label': 'New York City', 'value': 'NYC'},
                                            {'label': 'Montréal', 'value': 'MTL'},
                                            {'label': 'San Francisco', 'value': 'SF'}
                                            ],
                                    multi=True,
                                    value="",
                                    placeholder = "Select RunTime Data...",
                                    ),  
                                    ],
                                    style={'height': 30, 'margin-top' : 20, 'margin-bottom': 75},
                            )
         
# Create list button for History Data
create_runtime_model_button = html.Button("Create List", id = "btn_runtime_data", n_clicks = 0,
                                 style = dict (
                                            marginTop = 20,
                                            ))

# Div for runtime data
div_runtime_data = html.Div([
                        dbc.Row([
                                dbc.Col(dropdown_runtime_access, width = {"size":5,"offset": 1}),
                                dbc.Col(create_runtime_model_button, width = {"size":3}),
                                ]),
                            ])
   
############# Train Tab Start #############
# Heading for Training tab
train_tab_heading = dbc.Container([dbc.Row(
                                    [html.H4("Train Tab")]
                                    , justify = "center"
                                    , align = "center"
                                    )])

# For adding thecsv file path
csv_filepath_input = html.Div([
                            dcc.Input(
                                    placeholder='Enter the csv file path...',
                                    type='text',
                                    size = 50,
                                    className = "mb-3",
                                    value=''
                                    ),
                                    ], 
                                    style = dict (
                                            marginTop = 50,
                                            ),)

# Drop down for model selection
dropdown_model_selection = html.Div([
                            dcc.Dropdown(
                                    options=[
                                            {'label': 'New York City', 'value': 'NYC'},
                                            {'label': 'Montréal', 'value': 'MTL'},
                                            {'label': 'San Francisco', 'value': 'SF'}
                                            ],
                                    multi=True,
                                    value="",
                                    placeholder = "Select model to train..",
                                    ),  
                                    ],
                                    style={'height': 20, 'width': 700, 'margin-top' : 10, 'margin-bottom' : 70},
                            )
                            
# Heading for train PB
train_pb_heading = dbc.Container([dbc.Row(
                                    [html.H4("Train PB")]
                                    , justify = "center"
                                    , align = "center"
                                    )])                          
                            
# Drop down for trained model
dropdown_trained_model= html.Div([
                            dcc.Dropdown(
                                    options=[
                                            {'label': 'New York City', 'value': 'NYC'},
                                            {'label': 'Montréal', 'value': 'MTL'},
                                            {'label': 'San Francisco', 'value': 'SF'}
                                            ],
                                    multi=True,
                                    value="",
                                    placeholder = "Trained model list..",
                                    ),  
                                    ],
                                    style={'height': 20, 'width': 700, 'margin-top' : 10},
                            )     
                            
# Save selected model button
save_selected_model_button = html.Button("Save Model", id = "btn_save_model", n_clicks = 0,
                                   style={'height': 30, 'width': 120, 'margin-top' : 50, 'margin-left':350},                                       
                                         )

# Div for row for Train Tab
div_train_tab = html.Div([
                        dbc.Row(train_tab_heading),
                        dbc.Row(csv_filepath_input),
                        dbc.Row(dropdown_model_selection),
                        dbc.Row(train_pb_heading),
                        dbc.Row(dropdown_trained_model),
                        dbc.Row(save_selected_model_button)])


############ Train Tab End ###########
       
########### Deployment Tab Start ############
# Heading for deployment tab
train_tab_heading = dbc.Container([dbc.Row(
                                    [html.H4("Deploy Tab")]
                                    , justify = "center"
                                    , align = "center"
                                    )])

# Drop down for deployment model selection
dropdown_deploy_model= html.Div([
                            dcc.Dropdown(
                                    options=[
                                            {'label': 'New York City', 'value': 'NYC'},
                                            {'label': 'Montréal', 'value': 'MTL'},
                                            {'label': 'San Francisco', 'value': 'SF'}
                                            ],
                                    multi=True,
                                    value="",
                                    placeholder = "Deployment model list..",
                                    ),  
                                    ],
                                    style={'height': 20, 'width': 1000, 'margin-top' : 20},
                            )  

# Graph for deployment tab
deployment_graph = dcc.Graph(
        figure=dict(
                data=[
                        dict(
                            x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                               2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                            y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                               350, 430, 474, 526, 488, 537, 500, 439],
                            name='Rest of world',
                            marker=dict(
                                    color='rgb(55, 83, 109)'
                                    )
                            ),
                       dict(
                           x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                              2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                           y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                              299, 340, 403, 549, 499],
                              name='China',
                              marker=dict(
                                      color='rgb(26, 118, 255)'
                                      )
                              )
                      ],
                        layout=dict(
                                title='US Export of Plastic Scrap',
                                showlegend=True,
                                legend=dict(
                                        x=0,
                                        y=1.0
                                        ),
                                        margin=dict(l=40, r=0, t=40, b=30)
                                        )
                                ),
                                style={'height': 400, 'width': 1000, 'margin-top' : 50},
                                id='deployment_graph'
                          )

# Div for row for deployment Tab
div_deploy_tab = html.Div([
                        dbc.Row(train_tab_heading),
                        dbc.Row(dropdown_deploy_model),
                        dbc.Row(deployment_graph)])

###########  Deployment Tab End  ############

###########  Final Div for Deployment and Train Tab ###########
div_train_deploy_tab = html.Div([
                        dbc.Row([
                                dbc.Col(div_train_tab, width = {"size":5,"offset": 1}),
                                dbc.Col(div_deploy_tab, width = {"size":5}),
                                ]),
                            ])          
# Adding the background                            
client_app = dash.Dash(external_stylesheets = [dbc.themes.SUPERHERO])

client_app.layout = html.Div([client_heading, div_server_connection,
                              div_history_data, 
                              div_runtime_data,
                              div_train_deploy_tab])



# Callback for connection state
@client_app.callback(Output('connections_status', 'children'),
              [Input('btn_connect_server', 'n_clicks')])

def Check_Connection_State(btn1):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'btn_connect_server' in changed_id:
        msg = 'It will display the connection status'
    return html.Div(msg)


# Starting the server
client_app.run_server(debug=False, port = '8050')