# views.py
from flask import Blueprint, render_template, request
import os
from .data import get_general_info, get_work_experience, get_skills, get_education, get_hobbies, get_projects, get_social_media

views = Blueprint('views', __name__, template_folder='templates')

@views.route('/')
def index():
    general_info = get_general_info()
    work_experience = get_work_experience()
    skills = get_skills()
    education = get_education()
    social_media = get_social_media()
    
    return render_template('index.html', 
        title='MLH Fellow', 
        url=os.getenv('URL'), 
        name=general_info['name'],
        shortIntro=general_info['shortIntro'], 
        longIntro=general_info['longIntro'], 
        work=work_experience, 
        skills=skills,
        education=education, 
        email=general_info['email'], 
        facebook=social_media['facebook'], 
        instagram=social_media['instagram'],
        github=social_media['github'], 
        linkedin=social_media['linkedin'], 
        twitter=social_media['twitter'], 
        profilepic=general_info['profilepic']
    )

@views.route('/hobbies')
def hobbies():
    hobbies = get_hobbies()
    general_info = get_general_info()
    social_media = get_social_media()
    
    return render_template('hobbies.html', 
        title="Hobbies", 
        url=os.getenv("URL"),
        hobbies=hobbies,
        email=general_info['email'], 
        facebook=social_media['facebook'], 
        instagram=social_media['instagram'],
        github=social_media['github'], 
        linkedin=social_media['linkedin'], 
        twitter=social_media['twitter']
    )

@views.route('/projects')
def projects():
    projects = get_projects()
    general_info = get_general_info()
    social_media = get_social_media()
    
    return render_template('projects.html', 
        title="Projects", 
        url=os.getenv("URL"),
        project_rows=projects,
        email=general_info['email'], 
        facebook=social_media['facebook'], 
        instagram=social_media['instagram'],
        github=social_media['github'], 
        linkedin=social_media['linkedin'], 
        twitter=social_media['twitter']
    )
