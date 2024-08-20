from dash import html,dcc



def create_layout(app):

    layout=html.Div([
        html.H1(children=["Chronic Disease Risk Predictor"],style={'font-weight': 'bold', "text-align": "center"}),
    html.Div([
            html.Label('Gender:', style={'font-weight': 'bold'}),
            dcc.Dropdown(options=['Male', 'Female'], value="Male", id='gender-dropdown')
        ], style={'margin-bottom': '10px'}),

        html.Div([
            html.Label('Race:', style={'font-weight': 'bold'}),
            dcc.Dropdown(options=['Mexican American', 'Other Hispanic', 'Non-Hispanic White', 'Non-Hispanic Black', 'Non-Hispanic Asian', 'Other'], value='Other', id='race-dropdown')
        ], style={'margin-bottom': '10px'}),

        html.Div([
            html.Label('Country:', style={'font-weight': 'bold'}),
            dcc.Dropdown(options=['US', 'Non_US'], value="US", id='country-dropdown')
        ], style={'margin-bottom': '10px'}),

        html.Div([
            html.Label('Supplements Taken:', style={'font-weight': 'bold'}),
            dcc.Dropdown(options=['Yes', 'No'], value="Yes", id='supplements-dropdown')
        ], style={'margin-bottom': '10px'}),

        html.Div([
            html.Label('Access To Healthcare:', style={'font-weight': 'bold'}),
            dcc.Dropdown(options=['Yes', 'No'], value="Yes", id='access-dropdown')
        ], style={'margin-bottom': '10px'}),

        html.Div([
            html.Label('Age:', style={'font-weight': 'bold'}),
            dcc.Input(id="age", type="number")
        ], style={'margin-bottom': '10px'}),

        html.Div([
            html.Label('Ratio of Family Income to Poverty:', style={'font-weight': 'bold'}),
            dcc.Input(id="rftp", type="number")
        ], style={'margin-bottom': '10px'}),
        html.Div([
            html.Label(['Average Energy Intake in Kcal per day:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="aeik", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Average Sugar Intake in gm per day:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="asig", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Average Dietary Fibres Intake in gm per day:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="adfig", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Average Vitamin E Intake in mcg per day:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="aveimcg", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Average Vitamin A Intake in mcg per day:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="avaimcg", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Average Vitamin B1 Intake in mg per day:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="avb1img", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Average Vitamin B2 Intake in mcg per day:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="avb2img", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Average Vitamin B6 Intake in mg per day:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="avb6img", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Average Vitamin B12 Intake in mg per day:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="avb12img", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Average added Vitamin B6 Intake in mg per day:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="addedvb6img", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Average Vitamin C Intake in mg per day:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="avcimg", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Average Vitamin D Intake in mg per day:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="avdimg", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Average Vitamin K Intake in mg per day:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="avkimg", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Average Calcium Intake in mg per day:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="acalcimg", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Average Caffeine Intake in mg per day:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="acaffimg", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Average Pulse Rate:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="apr", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Body Mass Index:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="bmi", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Cholestrol mgperdL:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="cmgpdL", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['White Blood Cell Count:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="wbcc", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Red Blood Cell Count:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="rbcc", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Hemoglobin gperdL:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="hgpdL", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Average Alcoholic Drinks per day:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="aadpd", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Average Cigarettes per day:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="acpd", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Exerise Days per Week:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="edpw", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Label(['Vigorous Work days per Week:'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Input(id="vwdpw", type="number")
        ], style={'margin-bottom': '10px'}),
        
        html.Div([
        html.Button('Predict Disease', id='submit-val', n_clicks=0)
        ], style={'margin-bottom': '10px',"align": "center","text-align": "center","color":"blue"}),
        
        
        html.Div([
        html.Label(['The Disease predicted:'], style={'font-weight': 'bold', "text-align": "center"}),
        ], style={'margin-bottom': '30px',"align": "center"}),    
        
        html.Div(id='output',style={'margin-bottom': '30px',"align": "center"}),
        
    ])

    return layout