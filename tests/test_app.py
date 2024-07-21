import unittest
import os
from app import app

os.environ['TESTING'] = 'true'

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn('<h1>Jeremiah Herring</h1>', html)  
        self.assertIn('<h2>About Myself:</h2>', html)
        self.assertIn('<h2>Education</h2>', html)
        self.assertIn('<h2>Skills:</h2>', html)
        self.assertIn('<h2>Experience:</h2>', html) 
        self.assertIn('<a class="link-1" href="/">Home</a>', html)
        self.assertIn('<a href="/hobbies">Hobbies</a>', html)
        self.assertIn('<a href="/projects">Projects</a>', html)
    
    def test_hobbies(self):
        response = self.client.get("/hobbies")
        self.assertEqual(response.status_code, 200)
        hobbies_html = response.get_data(as_text=True)
        self.assertIn('<ol class="carousel-indicators">', hobbies_html)
        for hobby in ['Eating!', 'Playing Video Games', 'Working out']:
            self.assertIn(f'<h5>{hobby}</h5>', hobbies_html)
        self.assertIn('<a class="link-1" href="/">Home</a>', hobbies_html)
        self.assertIn('<a href="/hobbies">Hobbies</a>', hobbies_html)
        self.assertIn('<a href="/projects">Projects</a>', hobbies_html)
        self.assertIn('<img class="d-block w-100 rounded" src="./static/img/hobbies_gallery/eating_out.jpg"', hobbies_html)
        self.assertIn('<img class="d-block w-100 rounded" src="./static/img/hobbies_gallery/video_games.jpg"', hobbies_html)
        self.assertIn('<img class="d-block w-100 rounded" src="./static/img/hobbies_gallery/working_out.jpg"', hobbies_html)
         
    def test_projects(self):
        response = self.client.get('/projects')
        projects_html = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('<h2>Projects:</h2>', projects_html)
        self.assertIn('<div class="card" id="map-title">', projects_html)
        self.assertIn('<h2>Places I Have Been:</h2>', projects_html)

    def test_timeline_page(self):
        response = self.client.get('/timeline')
        self.assertEqual(response.status_code, 200)
        timeline_html = response.get_data(as_text=True)

        # Test form presence
        self.assertIn('<form id="timeline-form" method="POST">', timeline_html)
        self.assertIn('<input type="text" name="name" id="name" placeholder="Name" required />', timeline_html)
        self.assertIn('<input type="text" name="email" id="email" placeholder="Email" required />', timeline_html)
        self.assertIn('<textarea name="content" id="content" cols="30" rows="10" placeholder="Body" required></textarea>', timeline_html)
        self.assertIn('<input class="button submit" type="submit" value="Add Timeline Post" />', timeline_html)

        # Test timeline posts section
        self.assertIn('<div id="timeline-posts">', timeline_html)
        self.assertIn('<h2>Timeline</h2>', timeline_html)

    def test_timeline_api_get(self):
        response = self.client.get('/api/timeline_post')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        json_data = response.get_json()
        self.assertIn('timeline_posts', json_data)
        self.assertIsInstance(json_data['timeline_posts'], list)

if __name__ == '__main__':
    unittest.main()
