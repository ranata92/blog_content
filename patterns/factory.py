def parser_factory(data=None):
#    if not data:
#        raise Exception("No data to operate!")  ##requres file to operate

    import re
    from interface import IBase
    from adapter import ParseAdapter as Parser


    Base = IBase(data)
    m = re.match(r".+\.(?P<ext>[a-z]{2,4})$", data)
    ext = m.group('ext')
    if ext in ['js', 'jsn', 'json']:
        from jsonparser import JSONParser
        Base = JSONParser(data)
    if ext in ['xml', 'rxml']:
        from xmlparser import XMLParser
        Base = XMLParser(data)

    return Parser(Base)


parser = parser_factory('data.json').parse()

#try:
#    _parser = parser_factory().parse()   ##if no file is given
#except Exception as e:
#    print e

