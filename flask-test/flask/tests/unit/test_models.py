# /flask/tests/unit/test_models.py
"""
Tests /app/models.py
"""

def test_new_user(new_user):
    """
    Given a User model
    When testing User is created
    Then checks the email, hashed_password, authenticated and role fields are defined correctly
    """

    assert new_user.email == 'joabaj88@gmail.com'
    assert new_user.hashed_password != 'FlaskIsAwesome'
    assert not new_user.authenticated
    assert new_user.role == 'user'

def test_setting_password(new_user):
    """
    GIVEN an existing user
    WHEN  the password for the user is set
    THEN  check the password is stored correctly
    """
    new_user.set_password('MyNewPassword')
    assert new_user.hashed_password != 'MyNewPassword'
    assert new_user.is_correct_password('MyNewPassword')
    assert not new_user.is_correct_password('MyNewPassword2')
    assert not new_user.is_correct_password('FlaskIsAwesome')

def test_user_id(new_user):
    """
    GIVEN an existing user
    WHEN  the ID of the user is defined to a variable
    THEN  check the user ID returns a string (and not an integer) as needed by Flask-WTF
    """
    new_user.id = 17
    assert isinstance(new_user.get_id(), str)
    assert not isinstance(new_user.get_id(), int)
    assert new_user.get_id() == '17'
