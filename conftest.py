import pytest
import sys
print(sys.path)

@pytest.fixture(scope='session')
def test_client():
    
    from mattfemia import create_app
    flask_app = create_app()
    flask_app.config.from_object('config.DevelopmentConfig')

    # Create a test client using the Flask application
    with flask_app.test_client() as testing_client:
        
        # Establish an application context
        with flask_app.app_context():
            yield testing_client 