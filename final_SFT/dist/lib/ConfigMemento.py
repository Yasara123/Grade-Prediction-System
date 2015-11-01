__author__ = 'Yas'
'''
This class is for the restoring function in the design patter memento
This keeps the passwords History
'''
class RestorePointDoesNotExist():
    pass
class Memento(object):
    """Memento class"""
    def __init__(self, state):
        self.__state = state

    def get_state(self):
        """Returns the state object."""
        return self.__state

class CareTaker(object):
    """CareTaker class."""
    def __init__(self):
        self.__states = []
    def save(self, memento):
        """Save the memento object"""
        self.__states.append(memento)

    def restore(self):
        """Restore the originator state"""
        if self.__states:
            return self.__states.pop()
        raise RestorePointDoesNotExist
    def size(self):
        return int(len(self.__states))


class Originator(object):
    def __init__(self, state):
        self.state = state

    def save_to_momento(self):
        return Memento(self.state)

    def restore_from_momento(self, memento):
        self.state = memento.get_state()
        return self.state

class Pw_RollBack():
    def __init__(cls):
        cls.caketaker = CareTaker()
        cls.originator = Originator("Initialized")
    def addState(cls,State):
        cls.originator.state = str(State)
        # save the actual state
        cls.caketaker.save(cls.originator.save_to_momento())
        # modify the originator state
    def getState(cls):
        #if cls.caketaker.size()==3:
           # for x in range(0,2):
              #print cls.originator.restore_from_momento(cls.caketaker.restore())
        cls.originator.restore_from_momento(cls.caketaker.restore())
        return str(cls.originator.restore_from_momento(cls.caketaker.restore()))
