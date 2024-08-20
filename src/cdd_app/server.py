from dash import Dash,html,dcc,Input,Output


from src.cdd_app.ui.layout import create_layout
from src.cdd_app.callbacks.disease_predict import disease_predict_callbacks


def create_dash():
    app=Dash(__name__)
    app.layout=create_layout(app)
    disease_predict_callbacks(app)
    return app

