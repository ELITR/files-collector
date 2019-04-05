import unittest
from files_collector.folder_structure import FolderStructure

class TestFolderStructure(unittest.TestCase):
    def test_utf8_file(client):
        file_contents = ['\ufeffpřednáška 1\tdalší info\tdalší info\n', 'přednáška 2\tdalší info\tdalší info']
        f = FolderStructure('D:\\files-collector\\tests\\utf8_program_dne_2019-04-01.txt')
        assert  file_contents == f.contents

    def test_ascii_file(client):
        with client.assertRaises(Exception):
            f = FolderStructure('D:\\files-collector\\tests\\ascii_program_dne_2019-04-01.txt')

    def test_nonexistent_file(client):
        with client.assertRaises(FileNotFoundError):
            f = FolderStructure('D:\\files-collector\\tests\\nonexistent.txt')
