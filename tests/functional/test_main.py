import json
from mattfemia.main.forms import ContactForm


def test_home_page(test_client):
    """
    Test GET method allowed on '/' and returns status 200
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"LabVivo, Inc." in response.data

def test_home_page_post(test_client):
    """
    Test POST method allowed on '/' and returns status 200
    """
    response = test_client.post('/')
    assert response.status_code == 200

def test_ContactForm(test_client):
    """
    GIVEN ContactForm form model
    CHECK params 
    """

    data = {
        'name': "Matt Femia", 
        'email': "mattfemia1@gmail.com", 
        'message': "Hello"
    }

    response = test_client.post('/', data=json.dumps(data),
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b"Message sent!" in response.data