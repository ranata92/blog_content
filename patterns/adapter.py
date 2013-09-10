class ParseAdapter(object):
    def __init__(self, parser):
        self._parser = parser

    def parse(self):
        return self._parser.parse_file()
