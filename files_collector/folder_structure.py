import os, platform, unicodedata
from .paths import Paths

class FolderStructure(object):

    def __init__(self, daily_schedule_file):
        self.file = daily_schedule_file
        self.contents = self.get_file_content(self.file)

    def get_file_content(self, file):
        contents = []
        try:
            with open(file, encoding='utf-8-sig', mode='r') as f:
                for line in f:
                    contents.append(line)
        except UnicodeDecodeError: #Czech symbols files need to be saved as utf8
            raise Exception("IncorrectEncoding") #Tell user to change encoding

        return contents

    def create_folders(self):
        paths = self.get_paths()
        for path in paths:
            try:
                os.mkdir(path)
            except FileExistsError:
                continue

    def get_paths(self):
        slots = self.get_slots()
        root = Paths().documents_path

        paths = []
        for slot in slots:
            path = root + self.utf_to_ascii(slot) #URLS/file names in ascii
            paths.append(path)

        return paths

    def get_slots(self):
        slots = []
        for line in self.contents:
            line = line.split('\t')
            slots.append(line[0])

        return slots

    def utf_to_ascii(self, name):
        name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore')
        name =  name.decode('utf-8')
        return name.replace(' ', '_').lower()
