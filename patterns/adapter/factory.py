def parser_factory(data=None):
    '''Simple factory to construct Parser Adapter
       depending on file extension. '''

    import re
    from interface import IBase
    from adapter import ParseAdapter as Parser


    Base = IBase(data)
    m = re.match(r".+\.(?P<ext>[a-z]{2,4})$", data)
    ext = m.group('ext')
    if ext in ['js', 'jsn', 'json']:
        from jsonparser import JSONParser
        Base = JSONParser(data)
    if ext in ['xml', 'rxml', 'xl']:
        from xmlparser import XMLParser
        Base = XMLParser(data)

    return Parser(Base)


parser = parser_factory('data.xml').parse()

