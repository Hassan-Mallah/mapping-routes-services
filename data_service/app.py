from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/mapping-routes-services" # local
app.config['SQLALCHEMY_DATABASE_URI']= "postgres://postgres:postgres@postgres:5432" # docker
db = SQLAlchemy(app)

x = db.session.execute('select 1 as is_alive;').fetchall()
print(x)

@app.route('/')
def hello_world():
    return {
        'data': 50,
        'message': 'This is data service',
        'db_connection': str(x)
    }

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, host='0.0.0.0')
    # app.run(threaded=True, port=5055)