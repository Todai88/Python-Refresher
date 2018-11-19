import pytest
from app import create_application, db
from app.models import User


@pytest.fixture(scope="module")
def new_user():
    user = User('joabaj88@gmail.com', 'FlaskIsAwesome')
    return user


@pytest.fixture(scope="module")
def test_web_client():
    # taken from /instance
    flask_app = create_application('flask_test.cfg')

    testing_web_client = flask_app.test_client()

    # create context
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_web_client

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    db.create_all()

    # Insert user data
    user1 = User(email='patkennedy79@gmail.com', plaintext_password='FlaskIsAwesome')
    user2 = User(email='kennedyfamilyrecipes@gmail.com', plaintext_password='PaSsWoRd')
    db.session.add(user1)
    db.session.add(user2)

    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()
