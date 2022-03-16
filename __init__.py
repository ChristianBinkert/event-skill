from mycroft import MycroftSkill, intent_file_handler


class Event(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('event.intent')
    def handle_event(self, message):
        self.speak_dialog('event')


def create_skill():
    return Event()

