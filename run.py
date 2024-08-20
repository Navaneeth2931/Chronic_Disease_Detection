

from src.cdd_app.server import create_dash

if __name__ == '__main__':
    app=create_dash()
    app.run_server(debug=True,jupyter_mode='external',port=8142)

