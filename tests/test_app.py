from app.app import app, is_sanitized
import pytest

@pytest.fixture
def client():
    """
    Fixture to set up a Flask test client for testing.

    Returns:
        Flask test client: The Flask test client.
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_is_sanitized():
    """
    Test the is_sanitized function.

    - Check if a sample input is sanitized.
    - Check if an input with SQL SELECT statement is not sanitized.
    - Check if an input with SQL INSERT statement is not sanitized.
    """
    assert is_sanitized("sample input") == True
    assert is_sanitized("SELECT * FROM users") == False
    assert is_sanitized("INSERT INTO users (name) VALUES ('testuser')") == False

def test_sanitize_input(client):
    """
    Test the sanitize_input route.

    - Check if a valid input returns a sanitized result.
    - Check if an input with SQL SELECT statement returns an unsanitized result.
    - Check if a request with an invalid payload returns a 400 status code.
    """
    response = client.post('/v1/sanitized/input/', json={"input": "valid input"})
    assert response.get_json() == {"result": "sanitized"}

    response = client.post('/v1/sanitized/input/', json={"input": "SELECT * FROM users"})
    assert response.get_json() == {"result": "unsanitized"}

    response = client.post('/v1/sanitized/input/', json={"invalid_key": "invalid input"})
    assert response.status_code == 400
