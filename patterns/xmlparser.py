from interface import IBase


class XMLParser(IBase):
    '''XML Parser. Overrides parse_file to block exception
       raising. 
       TODO: write parse file method
       '''

    def __init__(self, file):
        super(XMLParser, self).__init__(file)

    def parse_file(self):
        '''Implements logic for XML parsing'''
        pass
