from configparser import ConfigParser
class Configuration:
    def __init__(self,filename):
        configparserobj=ConfigParser()
        configparserobj.read(filename)
        self._parser=configparserobj
        self.filename=filename
    def __getattr__(self,name):
        if name in self._parser.sections():
            return Section(name,self._parser)
        else:
            return None
    def __str__(self):
        p=self._parser
        result= []
        result.append('<configuration from %s>' %self.filename)
        #understand this carefully
        for s in p.sections():
            result.append('[%s]' % s)
            for o in p.options(s):
                result.append('%s=%s' % (o, p.get(s, o)))
        return '\n'.join(result)
                
        
class Section:
    def __init__ (self, name, parser):
        self.name = name
        self.__parser = parser
    def __getattr__ (self, name):
        return self.__parser.get(self.name, name)