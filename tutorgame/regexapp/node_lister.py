from regexapp import regex_maker, card_nodes
import random

class Node_Lister():
    my_regexer = regex_maker.Regexer()
    #Build node list
    # {{
    active_node = None
    nodelist = []
    digit_node = card_nodes.Card_Node('digit', 'In regex, \d catches a single digit.')
    nodelist.append(digit_node)
    single_char_node = card_nodes.Card_Node('single_char', 'In regex, [a-zA-Z] catches a single letter, uppercase or lowercase.')
    nodelist.append(single_char_node)
    space_node = card_nodes.Card_Node('space', 'In regex, \s catches a space')
    nodelist.append(space_node)
    
    def choose_node(self):
        self.active_node = random.choice(self.nodelist)
        return self.active_node.type_check
    # }}

    def request_homework(self):
        return self.active_node.repeat_me

    def check_homework(self, instring):
        return (instring == self.active_node.repeat_me)

    def get_test_question(self):
        return self.my_regexer.regex_question()


