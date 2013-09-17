from interface import IBase, RenderMixin


class XMLParser(IBase, RenderMixin):
    '''XML Parser. Overrides parse_file to block exception
       raising. 
       TODO: write parse file method
       '''

    def __init__(self, file):
        super(XMLParser, self).__init__(file)

    def parse_file(self):
        '''Implements logic for XML parsing'''
        import lxml.etree as et
        from lxml import objectify as obj
        with open(self._file, 'rb') as xl:
            xml = xl.read()
            root = obj.fromstring(xml)
            for e in root.iterchildren():
                print e.tag, '=>', e.text

            title = root.service.title
            date = root.service.date
            author = root.service.author
            print title, '=>', date, '=>', author

            for el in root.data.iterchildren():
                for _ch in el.iterchildren():
                    print _ch.tag, '--->', _ch.text


            # tree = et.parse(xl)
            # root = tree.getroot()
            # print root.service.title

            # for child in root:
            #     print child.tag, child.attrib
            #     for _child in child.iterchildren():
            #         print _child.tag, _child.text

