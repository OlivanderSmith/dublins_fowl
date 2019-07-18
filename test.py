from app import app
import unittest


class FlaskTestCase(unittest.TestCase):
    # Ensure Flask was set up correctly
    # Uses response code as testing metric
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly
    # Uses data validation as testing metric
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)

    # Make sure login works correctly given correct credentials

    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username='admin', password='admin'),
            follow_redirects=True
        )
        self.assertIn(b"You&#39;re good to go!", response.data)

    # Make sure login works correctly given incorrect credentials

    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username='xdgdfg', password='zfvxdf'),
            follow_redirects=True
        )
        self.assertIn(b"Error: Invalid User Name or Password", response.data)

    # Make sure logout works correctly

    def test_logout(self):
        tester = app.test_client(self)
        tester.post(
            '/login',
            data=dict(username='admin', password='admin'),
            follow_redirects=True
        )
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b"You&#39;re logged out", response.data)

    # Make sure /name-and-shame requires login

    def test_add_data_requires_login(self):
        tester = app.test_client(self)
        response = tester.get(
            '/name-and-shame', content_type='html/text', follow_redirects=True)
        self.assertTrue(
            b'Please login to add your own Predators' in response.data)

    # Ensure posts are populated on main page

    def test_posts_show_up(self):
        tester = app.test_client(self)
        response = tester.get(
            '/'
        )
        self.assertIn(b"I&#39;m enthusiastic!", response.data)


if __name__ == '__main__':
    unittest.main()
