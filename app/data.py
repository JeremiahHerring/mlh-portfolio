# data.py

# General Information
general_info = {
    'name': 'Jeremiah Herring',
    'shortIntro': 'CS Student at CSUF',
    'longIntro': 'Jeremiah Herring from Bakersfield, CA. I am currently studying Computer Science at Cal State Fullerton. I worked as a software engineer intern for Sandia National Laboratories and Information Technology for Cal State Fullerton.',
    'email': '123fakemail@gmail.com',
    'profilepic': './static/img/profile_pic.jpg'
}

# Work Experience
work_experience = [
    {'jobTitle': 'Software Engineer', 'desc': "Artificial Intelligence, Machine Learning, Big DaTA", 'year': "2018 - Present", 'link':'./static/img/sandia.png'}
]

# Skills
skills = [
    './static/img/skillicons/html.png',
    './static/img/skillicons/css.png',
    './static/img/skillicons/javascript.png',
    './static/img/skillicons/python.png',
    './static/img/skillicons/sql.png'
]

# Education
education = [
    {'type': 'Bachelors of Computer Science', 'from': 'California State University', 'when': '2021 - Present', 'desc': 'Computers are cool!', 'link': './static/img/csuf.png'}
]

# Hobbies
hobbies = [
    {'name': 'Eating!', 'caption': 'I like meat. Pause.', 'img': './static/img/hobbies_gallery/eating_out.jpg', 'active': 'active'},
    {'name': 'Playing Video Games', 'caption': 'My favorite way to relax!', 'img': './static/img/hobbies_gallery/video_games.jpg', 'active': ''}, 
    {'name': 'Working out', 'caption': 'We go jim.', 'img': './static/img/hobbies_gallery/working_out.jpg', 'active': ''}
]

# Projects
projects = [
    [
        {'name': 'FullyHacks', 'tag': 'Website for CSUF Hackathon', 'tools': 'Next.js, TailwincCSS, Prisma, MongoDB', 'link': 'https://github.com/fullyhacks2024', 'img': './static/img/projects/fullyhacks.png'},
        {'name': 'VitaMatch', 'tag': 'Vitamin Recommendation Website', 'tools': 'HTML, CSS, JavaScript', 'link': 'github.com/jeremiahherring/vitaminapp', 'img': './static/img/projects/vitamatch.png'},
        {'name': 'QuickReadAI', 'tag': 'AI Web Content Summarizer', 'tools': 'React, CSS, JavaScript', 'link': 'github.com/jeremiahherring/quickread-ai', 'img': './static/img/projects/quickreadai.png'}
    ]
]

# Social Media
social_media = {
    'facebook': 'facebook.com',
    'github': 'github.com/jeremiahherring',
    'instagram': 'instagram.com/jeremiah.herring7',
    'linkedin': 'linkedin.com/jeremiahherring',
    'twitter': 'twitter.com'
}

# Functions to retrieve the data
def get_general_info():
    return general_info

def get_work_experience():
    return work_experience

def get_skills():
    return skills

def get_education():
    return education

def get_hobbies():
    return hobbies

def get_projects():
    return projects

def get_social_media():
    return social_media
