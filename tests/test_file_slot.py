from files_collector import file_slot
import os

def test_correct_url(client):
    file = open('D:\\files-collector\\tests\\utf8_program_dne_2019-04-01.txt', 'rb')
    data = {
        'file': (file, 'program_dne.txt')
    }
    client.post('/daily_schedule/', data=data)
    res = client.get('/presentations/prednaska_1/')
    assert res.status_code == 200
    assert "There aren't any files in this directory" in res.get_data(as_text=True)
    os.remove('D:\\program_dne\\program_dne.txt') #Does not exist -> Exception
    os.rmdir('D:\\\\prezentace\\prednaska_1')
    os.rmdir('D:\\\\prezentace\\prednaska_2')

def test_incorrect_url(client):
    file = open('D:\\files-collector\\tests\\utf8_program_dne_2019-04-01.txt', 'rb')
    data = {
        'file': (file, 'program_dne.txt')
    }
    client.post('/daily_schedule/', data=data)
    res = client.get('/presentations/prednaska_4/')
    assert res.status_code == 404
    assert 'This folder does not exist' in res.get_data(as_text=True)
    os.remove('D:\\program_dne\\program_dne.txt') #Does not exist -> Exception
    os.rmdir('D:\\\\prezentace\\prednaska_1')
    os.rmdir('D:\\\\prezentace\\prednaska_2')

def test_list_files(client):
    path = 'D:\\prezentace\\prez1\\'
    os.mkdir(path)
    open(path + 'file.pptx', 'a').close()

    res = client.get('/presentations/prez1/')
    assert res.status_code == 200
    assert "file.pptx" in res.get_data(as_text=True)

    os.remove('D:\\prezentace\\prez1\\file.pptx')
    os.rmdir('D:\\\\prezentace\\prez1')

def test_upload_file(client):
    path = 'D:\\prezentace\\prez1\\'
    os.mkdir(path)

    file = open('D:\\files-collector\\tests\\testovaci_prezentace.pptx', 'rb')
    data = {
        'file': (file, 'testovaci_prezentace.pptx')
    }
    res = client.post('/presentations/prez1/', data=data)
    assert res.status_code == 200
    assert "testovaci_prezentace.pptx" in res.get_data(as_text=True)

    os.remove('D:\\prezentace\\prez1\\testovaci_prezentace.pptx')
    os.rmdir('D:\\\\prezentace\\prez1')
