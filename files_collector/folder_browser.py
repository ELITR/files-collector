import os
from .paths import Paths

class FolderBrowser(object):
    def __init__(self, folder):
        self.root_folder = self.set_root_folder(folder)
        self.folder_paths = []
        self.folder_names = []
        self.file_names = []
        self.list_folders()

    def set_root_folder(self, folder):
        try:
            return folder
        except FileNotFoundError:
            raise Exception("FolderNotFound")

    def set_root_from_url(self, url):
        delimiter = Paths().delimiter
        documents_path = Paths().documents_path

        url = url.replace("data-collector/presentations", "")
        url = url.split("/")
        url = [delimiter + x for i,x in enumerate(url) if i > 1]
        path = ''.join(url)
        path = documents_path + path
        self.root_folder = path

    def get_urls_from_paths(self):
        urls = []
        for path in self.folder_paths:
            urls.append(self.get_url(path))

        if self.root_folder != Paths().documents_path:
            urls.append(self.get_url(self.root_folder))

        return urls

    def get_url(self, path):
        url = path.replace(Paths().documents_path, '')
        url = url.replace(Paths().delimiter, '/')
        return '/data-collector/presentations/' + url

    def list_files(self):
        for file in os.listdir(self.root_folder):
            file_path = self.root_folder + file
            if os.path.isfile(file_path):
                self.file_names.append(file)

    def list_folders(self):
        self.folder_names = []
        for file in os.listdir(self.root_folder):
            file_path = self.root_folder + file + Paths().delimiter
            if os.path.isdir(file_path):
                self.folder_paths.append(file_path)
                self.folder_names.append(file)
