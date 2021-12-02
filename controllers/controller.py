from app import app
from flask import render_template
from models.events_list import Event
from models.events_list import events

@app.route('/events')
def index():
    return render_template('index.html', events = events)