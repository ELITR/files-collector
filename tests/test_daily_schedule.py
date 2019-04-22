from files_collector import daily_schedule
from io import BytesIO
import os

def test_response(client):
    response = client.get('/daily_schedule/')
    assert "Program dne" in response.get_data(as_text=True)

def test_upload_file(client):
    file = open('D:\\files-collector\\tests\\utf8_program_dne_2019-04-01.txt', 'rb')
    data = {
        'file': (file, 'program_dne.txt')
    }
    res = client.post('/daily_schedule/', data=data)
    assert res.status_code == 200
    os.remove('D:\\program_dne\\program_dne.txt') #Does not exist -> Exception
    os.rmdir('D:\\\\prezentace\\prednaska_1')
    os.rmdir('D:\\\\prezentace\\prednaska_2')

def test_incorrect_file(client):
    file = open('D:\\files-collector\\tests\\ascii_program_dne_2019-04-01.txt', 'rb')
    data = {
        'file': (file, 'program_dne.txt')
    }
    res = client.post('/daily_schedule/', data=data)
    assert res.status_code == 200
    assert "Prosím nastavte kódování souboru na utf a zopakujte" in res.get_data(as_text=True)

def test_word_file(client):
    file = open('D:\\files-collector\\tests\\program_dne_2019-04-01.docx', 'rb')
    data = {
        'file': (file, 'program_dne.docx')
    }
    res = client.post('/daily_schedule/', data=data)
    assert res.status_code == 200
    assert "Prosím vkládejte pouze textové soubory (ne word, excel apod.)" in res.get_data(as_text=True)

def test_sidebar(client):
    file = open('D:\\files-collector\\tests\\utf8_program_dne_2019-04-01.txt', 'rb')
    data = {
        'file': (file, 'program_dne.txt')
    }
    res = client.post('/daily_schedule/', data=data)
    assert res.status_code == 200
    assert "prednaska_1" in res.get_data(as_text=True)
    assert "prednaska_1" in res.get_data(as_text=True)
    os.remove('D:\\program_dne\\program_dne.txt') #Does not exist -> Exception
    os.rmdir('D:\\\\prezentace\\prednaska_1')
    os.rmdir('D:\\\\prezentace\\prednaska_2')
