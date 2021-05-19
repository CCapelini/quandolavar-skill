from mycroft import MycroftSkill, intent_file_handler


class Quandolavar(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('quandolavar.intent')
    def handle_quandolavar(self, message):
        self.speak_dialog('quandolavar')


def create_skill():
    return Quandolavar()

