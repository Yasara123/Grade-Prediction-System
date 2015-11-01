__author__ = 'Yas'
'''
This is the class is the user class of the system.
this store the user data such as password and user names
'''
class User(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(User, cls).__new__( cls, *args, **kwargs)
        return cls._instance
    def __init__(cls, name, userName,PassWd,Subs):
         cls.Nm = name
         cls.UsrNm = userName
         cls.Pwd = PassWd
         cls.NoSubs=Subs
    def getName(cls):
        return cls.Nm
    def getPwd(cls):
        return cls.Pwd
    def getUsrNm(cls):
        return cls.UsrNm
    def getNoSub(cls):
        return cls.NoSubs

'''
if __name__ == '__main__':
    s1=User("Yasara","Yas","sri")
    s2=User("Yasara2","Yas","sri")
    print s1.getName()
    print s2.getName()
'''
