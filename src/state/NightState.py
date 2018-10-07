from state.State import State

class NightState(State):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(NightState, cls).__new__(cls)
        return cls._instance

    def doClouck(self, context, hour):
        from state.DayState import DayState
        if 9 <= hour < 17:
            context.changeState(DayState())

    def doUse(self, context):
        context.callSecurityCenter("紧急：晚上使用金库！")

    def doAlarm(self, context):
        context.callSecurityCenter("按下警铃（晚上）")

    def doPhone(self, context):
        context.recordLog("晚上的通话录音")

    def __str__(self):
        return "[ 晚上 ]"