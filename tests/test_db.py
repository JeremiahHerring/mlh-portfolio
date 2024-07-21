import unittest
from peewee import *

from app import TimelinePost
MODELS = [TimelinePost]

# use an in-memory SQLite for tests
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of 
        # all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only live 
        # for the duration of the connection, and in the next step we close
        # the connection... but a good practice all the same
        test_db.drop_tables(MODELS)

        # Close connection to db.
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2
        
        # Get timeline posts and assert they are correct
        retrieved_posts = list(TimelinePost.select().order_by(TimelinePost.id))
        assert len(retrieved_posts) == 2

        assert retrieved_posts[0].name == 'John Doe'
        assert retrieved_posts[0].email == 'john@example.com'
        assert retrieved_posts[0].content == 'Hello world, I\'m John!'

        assert retrieved_posts[1].name == 'Jane Doe'
        assert retrieved_posts[1].email == 'jane@example.com'
        assert retrieved_posts[1].content == 'Hello world, I\'m Jane!'

    def test_create_post_invalid_data(self):
        with self.assertRaises(IntegrityError):
            TimelinePost.create(name='Incomplete Post', email='incomplete@example.com')

    def test_delete_post(self):
        post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        post.delete_instance()

        # Verify that the post has been deleted
        posts = list(TimelinePost.select())
        self.assertEqual(len(posts), 0)

if __name__ == '__main__':
    unittest.main()

