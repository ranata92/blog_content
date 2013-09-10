from interface import IBase


class XMLParser(IBase):
    def __init__(self, file):
        super(XMLParser, self).__init__(file)

    def parse_file(self):
        '''Implements logic for XML parsing'''
        pass
