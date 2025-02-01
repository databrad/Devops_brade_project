def test_health_check(client):
    """
    Test the /health endpoint to ensure the application is functional.
    """
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
