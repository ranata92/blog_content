from interface import IBase, RenderMixin


class JSONParser(IBase, RenderMixin):
    '''JSON Parser. Overrides parse_file from IBase
       and renders parsed data with Mixin's render page
       method'''

    def __init__(self, file):
        super(JSONParser, self).__init__(file)

    def parse_file(self):
        '''Implements logic for JSON parsing'''
        import json
        with open(self._file, 'rb') as js:
            data = json.load(js)
            context = {}
            context.update(data['service'])
            dt = {'data': data['data']}
            context.update(dt)
            from pprint import pprint
            pprint(context)
            self.render_page(context)
