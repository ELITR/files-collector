from files_collector.folder_browser import FolderBrowser
import unittest
import os

class TestFolderBrowser(unittest.TestCase):

    def test_list_folders(client):
        folder_names = ['prezentace1', 'prezentace2']
        folder_paths = ['D:\\files-collector\\tests\\read_this_folder\\prezentace1\\',
            'D:\\files-collector\\tests\\read_this_folder\\prezentace2\\']
        fd = FolderBrowser('D:\\files-collector\\tests\\read_this_folder\\')
        assert folder_names == fd.folder_names
        assert folder_paths == fd.folder_paths

    def test_nonexistent_folders(client):
        with client.assertRaises(Exception):
            fd = FolderBrowser('D:\\nonexistent')

    def test_list_files(client):
        file_names = ['prez1.pptx', 'prez2.pptx']
        fd = FolderBrowser('D:\\files-collector\\tests\\read_this_folder\\prezentace1\\')
        fd.list_files()
        assert file_names == fd.file_names

    def test_set_root_from_url(client):
        fd = FolderBrowser('D:\\prezentace\\')

        url = '/prezentace1/'
        fd.set_root_from_url(url)
        assert fd.root_folder == 'D:\\\\prezentace\\\\prezentace1\\'

        url = '/prezentace1/test/'
        fd.set_root_from_url(url)
        assert fd.root_folder == 'D:\\\\prezentace\\\\prezentace1\\test\\'

        url = '/'
        fd.set_root_from_url(url)
        assert fd.root_folder == 'D:\\\\prezentace\\\\'

    def test_get_urls_from_paths(client):
        os.mkdir("D:\\\\prezentace\\p1\\")
        os.mkdir("D:\\\\prezentace\\p2\\")
        os.mkdir("D:\\\\prezentace\\p1\\a\\")
        os.mkdir("D:\\\\prezentace\\p1\\b\\")

        fd = FolderBrowser("D:\\\\prezentace\\p1\\")
        urls = ['/presentations/p1/a/', '/presentations/p1/b/', '/presentations/p1/']
        assert fd.get_urls_from_paths() == urls

        fd = FolderBrowser("D:\\\\prezentace\\")
        urls = ['/presentations/p1/', '/presentations/p2/']
        assert fd.get_urls_from_paths() == urls
