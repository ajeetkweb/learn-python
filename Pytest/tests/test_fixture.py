# Importing the math and pytest libraries
import math
import pytest


""" Autouse Fixtures """

# An autouse=True fixture runs automatically for all tests without needing to be explicitly used.

@pytest.fixture(autouse=True)
def setup_and_teardown():
    print("\n[SETUP] Before test")
    yield
    print("\n[TEARDOWN] After test")


# Creating the common function for input
@pytest.fixture
def input_value():
   input = 8
   return input

@pytest.fixture
def sample_data():
    return {"name": "John", "age": 30}


# Using Fixtures for Setup and Teardown
@pytest.fixture
def db_connection():
    print("\n[SETUP] Connecting to DB")
    connection = {"db": "test_db", "status": "connected"}  # Mock DB connection
    yield connection
    print("\n[TEARDOWN] Closing DB connection")
    connection["status"] = "disconnected"




# Creating first test case
def test_check_difference(input_value):
   assert 99-93==input_value

# Creating second test case
def test_check_square_root(input_value):
   assert input_value==math.sqrt(64)


def test_sample_data(sample_data):
    assert sample_data["name"] == "John"
    assert sample_data["age"] == 30

def test_db_connection(db_connection):
    assert db_connection["status"] == "connected"



""" Using Fixtures with Dependency Injection """

@pytest.fixture
def user_data():
    return {"username": "test_user", "email": "test@example.com"}

@pytest.fixture
def authenticated_user(user_data):
    user_data["authenticated"] = True
    return user_data

def test_authenticated_user(authenticated_user):
    assert authenticated_user["authenticated"] is True


"""" Parametrizing Fixtures """

@pytest.fixture(params=[("admin", "admin123"), ("user", "user123"), ("guest", "guest123")])
def user_credentials(request):
    return request.param  # Tuple of (username, password)

def test_login(user_credentials):
    username, password = user_credentials
    assert isinstance(username, str)
    assert isinstance(password, str)