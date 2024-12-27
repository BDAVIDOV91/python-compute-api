import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)

# Load environment variables
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///instance/app.db")
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

logging.basicConfig(level=logging.INFO)
logging.info(f"Using database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

db = SQLAlchemy(app)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# Ensure the instance directory exists
instance_dir = os.path.join(os.getcwd(), 'instance')
if not os.path.exists(instance_dir):
    logging.info(f"Creating instance directory at {instance_dir}")
    os.makedirs(instance_dir)
else:
    logging.info(f"Instance directory exists at {instance_dir}")

# Check if the database file can be created
db_file = os.path.join(instance_dir, 'app.db')
try:
    with open(db_file, 'w') as f:
        f.write('')
    logging.info(f"Database file created at {db_file}")
except Exception as e:
    logging.error(f"Error creating database file: {e}")

with app.app_context():
    try:
        db.create_all()
        logging.info("Database tables created successfully")
    except Exception as e:
        logging.error(f"Error creating database tables: {e}")
        logging.error(f"Exception details: {e.__class__.__name__}: {e}")

if __name__ == "__main__":
    app.run(debug=True)