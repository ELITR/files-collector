from files_collector.folder_browser import FolderBrowser
import unittest

class TestFolderBrowser(unittest.TestCase):

    def test_list_folders(client):
        folder_names = ['prezentace1', 'prezentace2']
        folder_paths = ['D:\\files-collector\\tests\\read_this_folder\\prezentace1\\',
            'D:\\files-collector\\tests\\read_this_folder\\prezentace2\\']
        fd = FolderBrowser('D:\\files-collector\\tests\\read_this_folder\\')
        assert folder_names == fd.folder_names
        assert folder_paths == fd.folder_paths

    def test_list_folders(client):
        with client.assertRaises(Exception):
            fd = FolderBrowser('D:\\nonexistent')
