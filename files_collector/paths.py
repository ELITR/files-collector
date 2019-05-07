import platform

class Paths(object):

    def __init__(self):
        self._root = self.get_system_root()
        self.delimiter = self.get_system_delimiter()

        self.documents_path = self.set_documents_path()
        self.schedule_backup_path = self.set_schedule_backup_path()
        self.config_path = self.set_config_path()

    def set_config_path(self):
        return self._root + 'files-collector' + self.delimiter + 'tests' + self.delimiter + 'config.conf'

    def set_schedule_backup_path(self):
        return self._root + 'program_dne' + self.delimiter

    def set_documents_path(self):
        return self._root + 'prezentace' + self.delimiter

    def get_system_root(self):
        if platform.system() == 'Windows':
            return 'D:\\\\'
        else:
            return '/home/master/'

    def get_system_delimiter(self):
        if platform.system() == 'Windows':
            return '\\'
        else:
            return '/'
