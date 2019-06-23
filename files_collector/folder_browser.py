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

        url = url.replace("/presentations", "")
        url = url.split("/")
        url = [x + delimiter for i,x in enumerate(url) if i > 0 and x != '']
        path = ''.join(url)
        path = documents_path + path
        self.root_folder = path

    def get_urls_from_paths(self):
        urls = []
        for path in self.folder_paths:
            urls.append(self.get_url(path))


        parrent_url = self.get_parrent_url(self.root_folder)
        if parrent_url != Paths().file_slot_url:
            urls.append(parrent_url)
        else: #top level folders
            urls.append('/')

        return urls

    def get_url(self, path):
        url = path.replace(Paths().documents_path, '')
        url = url.replace(Paths().delimiter, '/')
        return Paths().file_slot_url + url

    def get_parrent_url(self, path):
        url = self.get_url(path)
        index = url.rfind('/', 0, len(url) - 1)
        parrent_url = url[:index + 1]
        return parrent_url

    def get_last_url_part(self):
        urls = self.get_urls_from_paths()
        parrent_url = self.get_parrent_url(self.root_folder)
        for index, url in enumerate(urls):
            i = url.rfind('/')
            j = url[:i-1].rfind('/') + 1
            if url == parrent_url or url == '/':
                urls[index] = '/..'
            else:
                urls[index] = './' + url[j:i]

        return urls

    def list_files(self):
        self.file_names = []
        for file in os.listdir(self.root_folder):
            if file == 'config.conf':
                continue

            file_path = self.root_folder + file
            if os.path.isfile(file_path):
                self.file_names.append(file)

    def list_folders(self):
        self.folder_names = []
        self.folder_paths = []
        for file in os.listdir(self.root_folder):
            file_path = self.root_folder + file + Paths().delimiter
            if os.path.isdir(file_path):
                self.folder_paths.append(file_path)
                self.folder_names.append(file)
