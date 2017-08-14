# A card node holds a string to copy and retype, and a type_check,
# which shows what will be unlocked
# {{
class Card_Node:
    def __init__(self, type_check, instring):
        self.repeat_me = instring
        self.type_check = type_check

    def check_against_string(self, instring):
        return (instring == self.repeat_me)
# }}
