from files_collector import file_slot
import os

def test_correct_url(client):
    file = open('D:\\files-collector\\tests\\utf8_program_dne_2019-04-01.txt', 'rb')
    data = {
        'file': (file, 'program_dne.txt')
    }
    client.post('/daily_schedule/', data=data)
    res = client.get('/prednaska_1')
    assert res.status_code == 200
    assert "Na tomhle místě jsou soubory:" in res.get_data(as_text=True)
    os.remove('D:\\program_dne\\program_dne.txt') #Does not exist -> Exception
    os.rmdir('D:\\\\prezentace\\prednaska_1')
    os.rmdir('D:\\\\prezentace\\prednaska_2')

def test_incorrect_url(client):
    file = open('D:\\files-collector\\tests\\utf8_program_dne_2019-04-01.txt', 'rb')
    data = {
        'file': (file, 'program_dne.txt')
    }
    client.post('/daily_schedule/', data=data)
    res = client.get('/prednaska_3')
    assert res.status_code == 404
    os.remove('D:\\program_dne\\program_dne.txt') #Does not exist -> Exception
    os.rmdir('D:\\\\prezentace\\prednaska_1')
    os.rmdir('D:\\\\prezentace\\prednaska_2')

def test_list_files(client):
    path = 'D:\\prezentace\\prez1\\'
    os.mkdir(path)
    open(path + 'file.pptx', 'a').close()

    res = client.get('/prez1')
    assert res.status_code == 200
    assert "file.pptx" in res.get_data(as_text=True)

    os.remove('D:\\prezentace\\prez1\\file.pptx')
    os.rmdir('D:\\\\prezentace\\prez1')
