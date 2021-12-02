from app import app
from flask import render_template, request
from models.events_list import events, add_new_event
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', events = events)

@app.route('/events', methods=['POST'])
def add_event():
    event_name = request.form['title']
    event_desc = request.form['description']
    event_no_of_people = request.form['title']
    event_date = request.form['title']
    new_event = Event(event_name, event_desc, event_no_of_people, event_date)
    add_new_event(new_event)
    return render_template('index.html', events = events)
