from .folder_browser import FolderBrowser

class Sidebar(object):

    def __init__(self, current_folder):
        self._folder_browser = current_folder
        self.menu = self.set_sidebar_data()

    def set_sidebar_data(self):
        paths = self._folder_browser.get_urls_from_paths()
        names = self._folder_browser.get_last_url_part()
        return zip(paths, names)
