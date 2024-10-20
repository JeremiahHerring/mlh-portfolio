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
    {
        'jobTitle': 'Software Engineer Intern',
        'desc': (
            "Refactored a tool that allowed for the addition of notes to a set of source code differences, "
            "providing analysts to add commentary about specific changes in code without modifying either version of the code being compared.\n"
            "Finetuned an LLM that could scan and sort project abstract reports based on relevance to sponsor interests, "
            "which sped up the manual review methods by 80% and allowed for 500+ projects to be reviewed simultaneously."
        ),
        'year': "May 2025 - Present",
        'link': './static/img/sandia.png'
    },
    {
        'jobTitle': 'Production Engineer Fellow',
        'desc': (
            "Secured position in the production engineering fellowship with Meta placing in the top 2% of applications.\n"
            "Collaborated closely with 2 Meta engineers and 12 other fellows to build individual projects integrating principles such as automated testing, scripting, containers, continuous integration and development, and troubleshooting."
        ),
        'year': "July 2025 - September 2025",
        'link': './static/img/meta.png'
    },
    {
        'jobTitle': 'Information Technology Specialist',
        'desc': (
            "Resolved over 100 hardware and software issues for health center staff, leading to a 20% improvement in operational efficiency and reducing downtime across daily tasks.\n"
            "Managed a large employee database that was critical for tracking staff and patient records, ensuring accurate and efficient record-keeping for the health center’s operations."
        ),
        'year': "November 2024 - May 2025",
        'link': './static/img/csuf.png'
    },
]


# Skills
skills = [
    './static/img/skillicons/html.png',
    './static/img/skillicons/css.png',
    './static/img/skillicons/javascript.png',
    './static/img/skillicons/python.png',
    './static/img/skillicons/express.png',
    './static/img/skillicons/figma.png',
    './static/img/skillicons/flask.png',
    './static/img/skillicons/github.png',
    './static/img/skillicons/graphql.png',
    './static/img/skillicons/mongodb.png',
    './static/img/skillicons/react.png',
]

# Education
education = [
    {'type': 'Bachelors of Computer Science', 'from': 'California State University', 'when': '2021 - Present', 'desc': 'Magna Cum Laude. President of Association of Computing Machinery', 'link': './static/img/csuf.png'}
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
        {'name': 'FullyHacks', 'tag': 'Website for CSUF Hackathon!', 'tools': 'Next.js, TailwincCSS, Prisma, MongoDB', 'link': 'https://github.com/fullyhacks2024', 'img': './static/img/projects/fullyhacks.png'},
        {'name': 'VitaMatch', 'tag': 'Vitamin Recommendation Website', 'tools': 'HTML, CSS, JavaScript', 'link': 'github.com/jeremiahherring/vitaminapp', 'img': './static/img/projects/vitamatch.png'},
        {'name': 'QuickReadAI', 'tag': 'AI Web Content Summarizer', 'tools': 'React, CSS, JavaScript', 'link': 'github.com/jeremiahherring/quickread-ai', 'img': './static/img/projects/quickreadai.png'}
    ]
]

# Social Media
social_media = {
    'facebook': 'facebook.com',
    'github': 'github.com/jeremiahherring',
    'instagram': 'instagram.com/jeremiah.herring7',
    'linkedin': 'linkedin.com/in/jeremiahherring',
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
