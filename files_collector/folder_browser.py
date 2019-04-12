import os

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

    def list_files(self):
        for file in os.listdir(self.root_folder):
            file_path = self.root_folder + file
            if os.path.isfile(file_path):
                self.file_names.append(file)

    def list_folders(self):
        self.folder_names = []
        for file in os.listdir(self.root_folder):
            file_path = self.root_folder + file + '\\'
            if os.path.isdir(file_path):
                self.folder_paths.append(file_path)
                self.folder_names.append(file)
