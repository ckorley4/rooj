from config import app, migrate

from models import db

def welcome_screen():
    print("Hello World!")
if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    welcome_screen()
    # remove pass and write your cli logic
