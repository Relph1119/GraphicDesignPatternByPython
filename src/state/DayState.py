from state.State import State


class DayState(State):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(DayState, cls).__new__(cls)
        return cls._instance

    def doClouck(self, context, hour):
        from state.NightState import NightState
        if hour < 9 or 17 <= hour:
            context.changeState(NightState())

    def doUse(self, context):
        context.recordLog("使用金库（白天）")

    def doAlarm(self, context):
        context.callSecurityCenter("按下警铃（白天）")

    def doPhone(self, context):
        context.callSecurityCenter("正常通话（白天）")

    def __str__(self):
        return "[ 白天 ]"