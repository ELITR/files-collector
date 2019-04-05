import unittest
from files_collector.folder_structure import FolderStructure

class TestFolderStructure(unittest.TestCase):
    def test_utf8_file(client):
        file_contents = ['přednáška 1\tdalší info\tdalší info\n', 'přednáška 2\tdalší info\tdalší info']
        f = FolderStructure('D:\\files-collector\\tests\\utf8_program_dne_2019-04-01.txt')
        assert  file_contents == f.contents

    def test_ascii_file(client):
        with client.assertRaises(Exception):
            f = FolderStructure('D:\\files-collector\\tests\\ascii_program_dne_2019-04-01.txt')

    def test_nonexistent_file(client):
        with client.assertRaises(FileNotFoundError):
            f = FolderStructure('D:\\files-collector\\tests\\nonexistent.txt')

    def test_get_slots(client):
        slots = ['přednáška 1', 'přednáška 2']
        f = FolderStructure('D:\\files-collector\\tests\\utf8_program_dne_2019-04-01.txt')
        assert slots == f.get_slots()

    def test_get_paths(client):
        paths = ['D:\\\\prezentace\\prednaska_1', 'D:\\\\prezentace\\prednaska_2']
        f = FolderStructure('D:\\files-collector\\tests\\utf8_program_dne_2019-04-01.txt')
        assert paths == f.get_paths()

    def test_utf_to_ascii(self):
        f = FolderStructure('D:\\files-collector\\tests\\utf8_program_dne_2019-04-01.txt')
        text = 'Náhodný český text'
        text_url = 'nahodny_cesky_text'
        assert text_url == f.utf_to_ascii(text)
