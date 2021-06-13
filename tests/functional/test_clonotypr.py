

def test_home_page(test_client):
    """
    Test /clonotypr/ returns status 200 
    and contains Clonotypr on render
    """
    response = test_client.get('/clonotypr/')
    assert response.status_code == 200
    assert b"Clonotypr" in response.data

def test_authors_page(test_client):
    """
    Test /clonotypr/authors returns status 200 
    """
    response = test_client.get('/clonotypr/authors')
    assert response.status_code == 200

def test_changelog_page(test_client):
    """
    Test /clonotypr/changelog returns status 200 
    """
    response = test_client.get('/clonotypr/changelog')
    assert response.status_code == 200

def test_license_page(test_client):
    """
    Test /clonotypr/license returns status 200 
    """
    response = test_client.get('/clonotypr/license')
    assert response.status_code == 200

def test_articles_page(test_client):
    """
    Test /clonotypr/articles/ returns status 200 
    """
    response = test_client.get('/clonotypr/articles/')
    assert response.status_code == 200

def test_reference_page(test_client):
    """
    Test /clonotypr/reference/ returns status 200 
    """
    response = test_client.get('/clonotypr/reference/')
    assert response.status_code == 200

def test_reference_function_page(test_client):
    """
    Test /clonotypr/reference/<function> returns status 200 
    """
    response = test_client.get('/clonotypr/reference/AnalyzeCDR3aa.html')
    assert response.status_code == 200

def test_vignettes_page(test_client):
    """
    Test /clonotypr/articles/vignette returns status 200 
    """
    response = test_client.get('/clonotypr/articles/vignette')
    assert response.status_code == 200

def test_404_page(test_client):
    """
    Test /clonotypr/404 returns status 200 
    """
    response = test_client.get('/clonotypr/404')
    assert response.status_code == 200

