def test_home_page(test_web_client):
    """
    GIVEN a flask application
    WHEN  the route is '/'
    THEN  check that the response is valid
    """
    response = test_web_client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Flask User Management Example!" in response.data
    assert b"Need an account?" in response.data
    assert b"Existing user?" in response.data

def test_home_page_post(test_web_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is is posted to (POST)
    THEN check that a '405' status code is returned
    """
    response = test_web_client.post('/')
    assert response.status_code == 405
    assert b"Welcome to the Flask User Management Example!" not in response.data


def test_login_page(test_web_client):
    """
    GIVEN a Flask application
    WHEN the '/login' page is requested (GET)
    THEN check the response is valid
    """
    response = test_web_client.get('/login')
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data


def test_valid_login_logout(test_web_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_web_client.post('/login',
                                data=dict(email='patkennedy79@gmail.com', password='FlaskIsAwesome'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"Thanks for logging in, patkennedy79@gmail.com!" in response.data
    assert b"Welcome patkennedy79@gmail.com!" in response.data
    assert b"Flask User Management" in response.data
    assert b"Logout" in response.data
    assert b"Login" not in response.data
    assert b"Register" not in response.data

    """
    GIVEN a Flask application
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_web_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b"Goodbye!" in response.data
    assert b"Flask User Management" in response.data
    assert b"Logout" not in response.data
    assert b"Login" in response.data
    assert b"Register" in response.data


def test_invalid_login(test_web_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/login' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = test_web_client.post('/login',
                                data=dict(email='patkennedy79@gmail.com', password='FlaskIsNotAwesome'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"ERROR! Incorrect login credentials." in response.data
    assert b"Flask User Management" in response.data
    assert b"Logout" not in response.data
    assert b"Login" in response.data
    assert b"Register" in response.data


def test_valid_registration(test_web_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/register' page is posted to (POST)
    THEN check the response is valid and the user is logged in
    """
    response = test_web_client.post('/register',
                                data=dict(email='patkennedy79@yahoo.com',
                                          password='FlaskIsGreat',
                                          confirm='FlaskIsGreat'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"Thanks for registering, patkennedy79@yahoo.com!" in response.data
    assert b"Welcome patkennedy79@yahoo.com!" in response.data
    assert b"Flask User Management" in response.data
    assert b"Logout" in response.data
    assert b"Login" not in response.data
    assert b"Register" not in response.data

    """
    GIVEN a Flask application
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_web_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b"Goodbye!" in response.data
    assert b"Flask User Management" in response.data
    assert b"Logout" not in response.data
    assert b"Login" in response.data
    assert b"Register" in response.data


def test_invalid_registration(test_web_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/register' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = test_web_client.post('/register',
                                data=dict(email='patkennedys79@hotmail.com',
                                          password='FlaskIsGreat',
                                          confirm='FlskIsGreat'),   # Does NOT match!
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"Thanks for registering, patkennedy79@hotmail.com!" not in response.data
    assert b"Welcome patkennedy79@hotmail.com!" not in response.data
    assert b"[This field is required.]" not in response.data
    assert b"Flask User Management" in response.data
    assert b"Logout" not in response.data
    assert b"Login" in response.data
    assert b"Register" in response.data

