from files_collector import daily_schedule

def test_hello(client):
    response = client.get('/daily_schedule/')
    assert response.data == b'Hello daily schedule'
