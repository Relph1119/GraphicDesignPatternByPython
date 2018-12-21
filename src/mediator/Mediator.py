class Mediator(object):
    @classmethod
    def createColleagues(cls):
        raise NotImplementedError

    @classmethod
    def colleagueChanged(cls):
        raise NotImplementedError
