class IBase(object):
    '''Base class for any parser.
       Implements virtual parse_file method
       to be overriden in ancestors.'''
    
    def __init__(self, file):
        self._file = file

    def parse_file(self):
        raise NotImplementedError()


class RenderMixin(object):
    '''Mixin class for any parser 
       to render parsed data into html page.'''

    def _build_context(self, kwargs):
        from datetime import date
        import getpass

        _title = kwargs.pop('title', "Parsed file")
        _date = kwargs.pop('date', str(date.today()))
        _author = kwargs.pop('author', getpass.getuser())
        service = dict([('title', _title), 
                ('date', _date), ('author', _author)])
        data = {}
        data.update(kwargs)
        # from pprint import pprint
        # pprint(service)
        # pprint(data)

        return service, data

    def render_page(self, kwargs):
        service, parsed_data = self._build_context(kwargs)
        
        from jinja2 import Environment, FileSystemLoader

        _loader = FileSystemLoader('templates/')
        env = Environment(loader=_loader)
        template = env.get_template('page_template.html')
        # pprint(service)
        # pprint(parsed_data)
        with open('templates/parsed_page.html', 'wb') as t:
            t.write(
                template.render(service=service,
                parsed_data=parsed_data)
                )
            t.close()


