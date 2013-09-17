class ParseAdapter(object):
    '''Class implements Adapter pattern 
       to create unified interface to 
       many types of parser'''
    def __init__(self, parser):
        self._parser = parser

    def parse(self):
        return self._parser.parse_file()
