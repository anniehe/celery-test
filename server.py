from flask import Flask
from tasks import celery

# Flask app
app = Flask(__name__)


if __name__ == "__main__":
    app.debug = True
    app.run()

    # Connecting instance of Celery to Flask app
    celery.init_app(app)


# Three tabs:
# 1. python server.py
# 2. celery worker -l info --beat
# 3. redis-server
