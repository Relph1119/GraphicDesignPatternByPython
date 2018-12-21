class Context(object):
    @classmethod
    def setClock(cls, hour):
        raise NotImplementedError

    @classmethod
    def changeState(cls, state):
        raise NotImplementedError

    @classmethod
    def callSecurityCenter(cls, msg):
        raise NotImplementedError

    @classmethod
    def recordLog(cls, msg):
        raise NotImplementedError
