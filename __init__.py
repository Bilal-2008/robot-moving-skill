from mycroft import MycroftSkill, intent_file_handler


class RobotMoving(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('moving.robot.intent')
    def handle_moving_robot(self, message):
        self.speak_dialog('moving.robot')


def create_skill():
    return RobotMoving()

