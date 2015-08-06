class Accessors(object):
    def __init__(self):
        self.width = 0
        self.height = 0 
        self.ee = 0
    def __getattribute__(self, name):
        print 'getattribute Here', name
        return object.__getattribute__(self, name)
       
    def __getattr__(self, name):
        print 'getattr Here', name
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError
#         elif name == 'test':
#             return self.ee
     
    def __setattr__(self, name, value):
        print 'setattr', name
        if name == 'size':
            self.width, self.height = value
        elif name == "test":
            self.ee = value
        else:
            self.__dict__[name] = value
             
#     def __iter__(self):
#         return self
#      
#     def next(self):
#         print 'here'
#         self.width += 1
#         return self.width



if __name__ == "__main__":
    """Print testing"""
#     print __name__
#     print locals()
#     print globals()
#     print 'test'
#     print type(Accessors)
    a = Accessors()
    #print a.product
    
    for i in a:
        print 'test'
#     a.size = (10,12)
#     a.test  = 20
#     print a.__dict__
#     for i in a:
#         print i
#         if i >= 100:
#             break
    