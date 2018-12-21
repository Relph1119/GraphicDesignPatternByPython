class State(object):
    @classmethod
    def doClouck(cls, context, hour):
        raise NotImplementedError

    @classmethod
    def doUse(cls, context):
        raise NotImplementedError

    @classmethod
    def doAlarm(cls, context):
        raise NotImplementedError

    @classmethod
    def doPhone(cls, context):
        raise NotImplementedError
