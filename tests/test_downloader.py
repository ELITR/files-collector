from files_collector import downloader
import os

def test_incorrect_download(client):
    file = open('D:\\files-collector\\tests\\utf8_program_dne_2019-04-01.txt', 'rb')
    data = {
        'file': (file, 'program_dne.txt')
    }
    client.post('/daily_schedule/', data=data)
    res = client.get('/a/testovaci_prezentace.pptx/')
    assert res.status_code == 404

    res = client.get('/prednaska_1/testovaci_prezentace.pptx/404')
    assert res.status_code == 404

def test_download(client):
    path = 'D:\\prezentace\\prez1\\'
    os.mkdir(path)

    file = open('D:\\files-collector\\tests\\testovaci_prezentace.pptx', 'rb')
    data = {
        'file': (file, 'test_download_file.pptx')
    }
    res = client.post('/prez1', data=data)
    assert res.status_code == 200
    assert "test_download_file.pptx" in res.get_data(as_text=True)

    res = client.get('/prez1/a/')
    assert res.status_code == 404

    with client.get('/prez1/test_download_file.pptx/') as res:
        assert res.status_code == 200
