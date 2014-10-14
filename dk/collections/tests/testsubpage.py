# -*- coding: utf-8 -*-

from django import template

def _render(templ, page):
    t = template.Template(templ)
    return t.render(template.Context(page))

class _sentinel(object):
    def __init__(self, fn, *args):
        self.fn = fn
        self.args = args

    def __call__(self):
        return self.fn(*self.args)
    

class pageproperty(object):
    """`@property`-like decorator for properties on sub-classes of page.
    """

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, pageobj, pageclass=None):
        #print "PROPERTY_GET from", repr(pageobj)
        import pprint
        #pprint.pprint(dir(pageclass))
        #print "  Name:", self.fget.__name__
        if pageobj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        val = self.fget(pageobj)
        #print "  VAL:", repr(val)
        return _sentinel(self.fget, pageobj)
        return val

    def __set__(self, obj, value):
        print "__SET__"

class page(dict):
    def __init__(self):
        self['_'] = "empty-is-false"
        
#     def __getattribute__(self, key):
#         print "GETATTRIBUTE:", key
#         attr = object.__getattribute__(self, key)
#         print "ATTR:", type(attr), repr(attr)
#         return attr

    def __iter__(self):
        print "ITER"

    def __copy__(self):
        print "COPY"

    def update(self, other):
        print "UPDATE", other

    def keys(self):
        print "KEYS"

    def new(self, values=None):
        print "NEW:", values

    def items(self):
        print "ITEMS"
    
    def __getattr__(self, key):
        print "GETATTR:", key

    def __setattr__(self, key, val):
        print "SETATTR:", key, repr(val)
        self[key] = val
        
    def has_key(self, key):
        print "HAS_KEY", key

    def get(self, key, default):
        print "GET", key

    def _ownsattr(self, key):
        return hasattr(self, key) and not hasattr(super(page, self), key)
    
    def __contains__(self, key):
        print "CONTAINS", key
        print "HASATTR:", hasattr(self, key)
        print "SUPERHAS:", hasattr(super(page, self), key)
        print "TYPE:", type(getattr(self, key))
        return super(page, self).__contains__(key) or self._ownsattr(key)

    def __getitem__(self, key):
        print "GETITEM", key
        if super(page, self).__contains__(key):
            return super(page, self).__getitem__(key)
        elif self._ownsattr(key):
            return getattr(self, key)

    def __setitem__(self, key, val):
        print "SETITEM", key, repr(val)
        super(page, self).__setitem__(key, val)

    def __delitem__(self, key):
        print "DELITEM:", key

    def push(self):
        print "PUSH"

    def pop(self):
        print "POP"

class Subpage(page):
    @pageproperty
    def foo(self):
        return 'foo'


if __name__ == "__main__":
    p = Subpage()
    #p = page()
    #getattr(p, 'foo')
    
    #p['foo'] = 'foo'
    #p.asdf = 'asdf'
    #print p.foo
    #print p.bar
    #print "render [%s]" % _render('{{ foo }} {{ asdf }}', p)

    print "render [%s]" % _render('{{ foo }}', p)

    #p.bar = 'bar'
    #print "render [%s]" % _render('{{ bar }}', p)

    #p.foo
