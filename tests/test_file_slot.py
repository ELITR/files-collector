from files_collector import file_slot

def test_correct_url(client):
    res = client.get('/prednaska_1')
    assert res.status_code == 200
    assert "Na tomhle místě jsou soubory:" in res.get_data(as_text=True)
