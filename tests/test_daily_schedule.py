from files_collector import daily_schedule

def test_hello(client):
    response = client.get('/daily_schedule/')
    assert "Program dne" in response.get_data(as_text=True)
