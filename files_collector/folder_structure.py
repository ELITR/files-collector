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
