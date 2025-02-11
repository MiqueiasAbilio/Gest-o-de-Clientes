from flask import Flask
from configurações import configure_all

app = Flask(__name__)

configure_all(app)

app.run(debug=True)