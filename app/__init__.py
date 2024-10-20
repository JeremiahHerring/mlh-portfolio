from flask import Flask, render_template, request
from app.views import views
import os
import datetime
from .data import get_general_info, get_social_media
from peewee import *
from playhouse.shortcuts import model_to_dict
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    if not all([os.getenv("MYSQL_DATABASE"), os.getenv("MYSQL_USER"), os.getenv("MYSQL_PASSWORD"), os.getenv("MYSQL_HOST")]):
        raise ValueError("Database configuration is missing in environment variables")

    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                         user=os.getenv("MYSQL_USER"),
                         password=os.getenv("MYSQL_PASSWORD"),
                         host=os.getenv("MYSQL_HOST"),
                         port=3306
                         )

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

@views.route('/timeline')
def timeline():
    general_info = get_general_info()
    social_media = get_social_media()

    return render_template('timeline.html', 
    title="Timeline",
    posts = get_time_line_post(), 
    url=os.getenv("URL"),
    email=general_info['email'], 
    facebook = social_media['facebook'], 
    instagram = social_media['instagram'],
    github=social_media['github'], 
    linkedin=social_media['linkedin'], 
    twitter = social_media['twitter'])

@views.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    if name == "":
        return "Invalid name", 400
    elif not "@" in email:
        return "Invalid email", 400
    elif content == "":
        return "Invalid content", 400
    else:
        timeline_post = TimelinePost.create(name=name, email=email, content=content)
        return model_to_dict(timeline_post)

@views.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in
TimelinePost.select().order_by(TimelinePost.created_at.desc())
    ]
    }

@views.route('/api/timeline_post/<int:id>', methods=['DELETE'])
def delete_time_line_post(id):
    try:
        post = TimelinePost.get(TimelinePost.id == id)
        post.delete_instance()
        return {'message': 'Post deleted successfully'}
    except TimelinePost.DoesNotExist:
        return {'error': 'Post not found'}, 404

app.register_blueprint(views)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
