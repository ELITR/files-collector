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

def test_download_no_conf(client):
    path = 'D:\\prezentace\\prez1\\'
    os.mkdir(path)

    file = open('D:\\files-collector\\tests\\testovaci_prezentace.pptx', 'rb')
    data = {
        'file': (file, 'test_download_file.pptx')
    }
    res = client.post('/presentations/prez1/', data=data)
    assert res.status_code == 200
    assert "test_download_file.pptx" in res.get_data(as_text=True)

    res = client.get('/presentations/prez1/a/')
    assert res.status_code == 404

    os.rename("D:\\files-collector\\tests\\config.conf",
              "D:\\files-collector\\tests\\config2.conf")
    with client.get('/presentations/prez1/test_download_file.pptx/') as res:
        assert res.status_code == 200
    os.rename("D:\\files-collector\\tests\\config2.conf",
              "D:\\files-collector\\tests\\config.conf")

def test_download_no_auth(client):
    path = 'D:\\prezentace\\prez1\\'
    os.mkdir(path)

    file = open('D:\\files-collector\\tests\\testovaci_prezentace.pptx', 'rb')
    data = {
        'file': (file, 'test_download_file.pptx')
    }
    res = client.post('/presentations/prez1/', data=data)
    assert res.status_code == 200
    assert "test_download_file.pptx" in res.get_data(as_text=True)

    res = client.get('/presentations/prez1/a/')
    assert res.status_code == 404

    with client.get('/presentations/prez1/test_download_file.pptx/') as res:
        assert res.status_code == 200

def test_download_with_auth(client):
    path = 'D:\\prezentace\\prednaska_1\\'
    os.mkdir(path)

    file = open('D:\\files-collector\\tests\\testovaci_prezentace.pptx', 'rb')
    data = {
        'file': (file, 'test_download_file.pptx')
    }
    res = client.post('/presentations/prednaska_1/', data=data)
    assert res.status_code == 200
    assert "test_download_file.pptx" in res.get_data(as_text=True)

    res = client.get('/presentations/prednaska_1/a/')
    assert res.status_code == 404

    with client.get('/presentations/prednaska_1/test_download_file.pptx/') as res:
        assert res.status_code == 401
