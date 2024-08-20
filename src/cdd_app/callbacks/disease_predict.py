from dash import Input,Output,State
import pandas as pd
import numpy as np


from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.compose import make_column_selector
from sklearn.preprocessing import StandardScaler, OneHotEncoder

import joblib


def disease_predict_callbacks(app):
    @app.callback(
        Output(component_id='output', component_property='children'),
        [
        State(component_id='gender-dropdown', component_property='value'),
        State(component_id='race-dropdown', component_property='value'),
        State(component_id='country-dropdown', component_property='value'),
        State(component_id='supplements-dropdown', component_property='value'),
        State(component_id='access-dropdown', component_property='value'),
        State(component_id='age', component_property='value'),
        State(component_id='rftp', component_property='value'),
        State(component_id='aeik', component_property='value'),
        State(component_id='asig', component_property='value'),
        State(component_id='adfig', component_property='value'),
        State(component_id='aveimcg', component_property='value'),
        State(component_id='avaimcg', component_property='value'),
        State(component_id='avb1img', component_property='value'),
        State(component_id='avb2img', component_property='value'),
        State(component_id='avb6img', component_property='value'),
        State(component_id='avb12img', component_property='value'),
        State(component_id='addedvb6img', component_property='value'),
        State(component_id='avcimg', component_property='value'),
        State(component_id='avdimg', component_property='value'),
        State(component_id='avkimg', component_property='value'),
        State(component_id='acalcimg', component_property='value'),
        State(component_id='acaffimg', component_property='value'),
        State(component_id='apr', component_property='value'),
        State(component_id='bmi', component_property='value'),
        State(component_id='cmgpdL', component_property='value'),
        State(component_id='wbcc', component_property='value'),
        State(component_id='rbcc', component_property='value'),
        State(component_id='hgpdL', component_property='value'),
        State(component_id='aadpd', component_property='value'),
        State(component_id='acpd', component_property='value'),
        State(component_id='edpw', component_property='value'),
        State(component_id='vwdpw', component_property='value'),
        ],

        Input(component_id='submit-val', component_property='n_clicks'),
        
    
        )

    def disease_predict(gender,race,country,supp,access,age,rftp,aeik,asig,adfig,aveimcg,
                    avaimcg,avb1img,avb2img,avb6img,avb12img,addedvb6img,avcimg,avdimg,
                    avkimg,acalcimg,acaffimg,apr,bmi,cmgpdL,wbcc,rbcc,hgpdL,aadpd,acpd,edpw,vwdpw,n_clicks):
        
        
        # The additional data is populated such that to binary converted categorical variables that are prodcued
        # from one hot encoding and are part of the building of the model
        new_data={'Gender':['Male','Female','Male','Male','Male','Male',gender], 
                'Race':['Non-Hispanic Asian','Non-Hispanic Black','Non-Hispanic White','Other Hispanic','Other','Mexican American',race],
                'Country':['US','US','Non_US','US','US','US',country], 'supplements_taken':['Yes','No','Yes','Yes','Yes','Yes',supp],
        'access_to_healthcare':['Yes','No','Yes','Yes','Yes','Yes',access], 'Age':[0,0,0,0,0,0,age], 'Ratio_Famincome_to_Pov':[0,0,0,0,0,0,rftp],
        'avgday_Energy_in_kcal':[0,0,0,0,0,0,aeik], 'avgday_sug_in_gm':[0,0,0,0,0,0,asig], 'avgday_diet_fib_in_gm':[0,0,0,0,0,0,adfig],
        'avgday_Vitamin_E_in_mcg':[0,0,0,0,0,0,aveimcg], 'avgday_Vitamin_A_in_mcg':[0,0,0,0,0,0,avaimcg],
        'avgday_Vitamin_B1_in_mg':[0,0,0,0,0,0,avb1img], 'avgday_Vitamin_B2_in_mg':[0,0,0,0,0,0,avb2img], 'Vitamin_B6_mg':[0,0,0,0,0,0,avb6img],
        'Vitamin_B12_mg':[0,0,0,0,0,0,avb12img], 'added_Vitamin_B6_mg':[0,0,0,0,0,0,addedvb6img], 'Vitamin_C_mg':[0,0,0,0,0,0,avcimg],
        'avgday_Vitamin_D_in_mg':[0,0,0,0,0,0,avdimg], 'avgday_Vitamin_K_in_mg':[0,0,0,0,0,0,avkimg],
        'avgday_calcium_in_mg':[0,0,0,0,0,0,acalcimg], 'avgday_caffeine_in_mg':[0,0,0,0,0,0,acaffimg], 'avg_pulse_rate':[0,0,0,0,0,0,apr],
        'body_mass_index':[0,0,0,0,0,0,bmi], 'tot_cholestrol_mgperdL':[0,0,0,0,0,0,cmgpdL], 'white_blood_cell_count':[0,0,0,0,0,0,wbcc],
        'red_blood_cell_count':[0,0,0,0,0,0,rbcc], 'hemoglobin_gperdL':[0,0,0,0,0,0,hgpdL], 'avg_alc_drinks_per_day':[0,0,0,0,0,0,aadpd],
        'avg_cig_per_day':[0,0,0,0,0,0,acpd], 'exercise_days_per_week':[0,0,0,0,0,0,edpw],
        'vigorous_workdays_per_week':[0,0,0,0,0,0,vwdpw]}
        
        dash_data=pd.DataFrame(new_data)
        #print(dash_data.dtypes)
        
        race_map={'Mexican American':'MexA','Other Hispanic':'OHP','Non-Hispanic White':'NHW','Non-Hispanic Black':'NHB','Non-Hispanic Asian':'NHA','Other':'others'}
        gender_map={'Male':'M','Female':'F'}
        dash_data['Race']=dash_data['Race'].map(race_map)
        dash_data['Gender']=dash_data['Gender'].map(gender_map)
        

        preprocessor=make_pipeline(make_column_transformer((OneHotEncoder(drop='first'),make_column_selector(dtype_include=object)),
            (StandardScaler(),make_column_selector(dtype_include=np.number)),
                              remainder='passthrough'))






        dash_data_transformed=preprocessor.fit_transform(dash_data).round(2)
        encoded_column_names = preprocessor.named_steps['columntransformer'].named_transformers_['onehotencoder'].get_feature_names_out()
        
        transformed_column_names = list(encoded_column_names) + list(dash_data.select_dtypes(include=np.number).columns)
        dash_data_prep=pd.DataFrame(dash_data_transformed,columns=transformed_column_names)
        
        lgr_model_3=joblib.load('./models/lgr_model_3.pkl')


        if n_clicks>0:
            State_df=pd.DataFrame(dash_data_prep.iloc[[5]])
            out=lgr_model_3.predict(State_df)
            return out[0]