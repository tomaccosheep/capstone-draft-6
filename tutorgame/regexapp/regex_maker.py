import random
import string
import re

class Regexer:
    # This is a list of types and matching regex. This dictionary is used
    # to create the regex string and the findme string
    # {{
    regex_dict = {'digit': '\d', 'single_char': '[a-zA-Z]', 'space': '\s'}
    # }}


    # This is a list of all opened types of regex
    # {{
    open_regex = ['digit', 'single_char', 'space']
    # }}

    # This creates the Regexer object with args representing
    # regex types that could be in the open_regex list
    # {{
    def __init__(self, *args):
        for arg in args:
            if arg not in open_regex:
                open_regex.append(arg)
    # }}

    # This takes in a regex type and outputs characters that
    # correspond for that type. Used for building answer strings
    # {{
    def regex_step_function(self, func_key):
        if func_key == 'single_char':
            return random.choice(string.ascii_letters)
        elif func_key == 'digit':
            return str(random.randrange(0,10,1))
        elif func_key == 'space':
            return ' '
    # }}

    # This takes in a regex_list and shortens it, so that
    # two instances will return one instance with a coefficient
    # {{
    def compress_indicies(self, regex_list):
        regex_string = ''
        regex_list_compressed = []
        how_many_indicies = 1
        compress_to_do = False
        print(str(regex_list))
        for i in range(0, len(regex_list)):
            if i == (len(regex_list) - 1):
                if compress_to_do:
                    compressed_string = regex_list[i] + '{' + str(how_many_indicies) + '}'
                    regex_list_compressed.append(compressed_string)
                else:
                    regex_list_compressed.append(regex_list[i])
            elif regex_list[i] != regex_list[i+1]:
                if compress_to_do:
                    compressed_string = regex_list[i] + '{' + str(how_many_indicies) + '}'
                    regex_list_compressed.append(compressed_string)
                    how_many_indicies = 1
                    compress_to_do = False
                else:
                    regex_list_compressed.append(regex_list[i])
            else:
                how_many_indicies += 1
                compress_to_do = True
        return regex_list_compressed
    # }}

    def regex_gen(self):
        match_num = random.randrange(2, 5, 1)
        selectme_string_list = []
        for i in range(0, match_num):
            selectme_string_list.append("")
        regex_list = []
        for i in range(0,9):
            regex_step = random.choice(self.open_regex)
            regex_list.append(self.regex_dict[regex_step])
            for i in range(0, match_num):
                selectme_string_list[i] += self.regex_step_function(regex_step)
        return self.compress_indicies(regex_list), selectme_string_list



    def regex_nonselect_gen(self, selectme_string_list):
        nonselect_string_list = []
        for i in range(0, len(selectme_string_list) + 1):
            nonselect_string_list.append('')
            for j in range(0, random.randrange(2,10,1)):
                nonselect_string_list[i] += self.regex_step_function(random.choice(list(self.regex_dict)))
        return nonselect_string_list

    def regex_question(self):
        regexed = 1
        selectme_string_list = 0
        while regexed != selectme_string_list:
            regex_list, selectme_string_list = self.regex_gen()
            nonselect_string_list = self.regex_nonselect_gen(selectme_string_list)
            full_string = ''
            for i in range(0, len(selectme_string_list)):
                full_string += nonselect_string_list[i]
                full_string += selectme_string_list[i]
            full_string += nonselect_string_list[-1]
            regex_string = ''
            for i in regex_list:
                regex_string += i
            regexed = re.findall(regex_string, full_string)
        return [nonselect_string_list, selectme_string_list, regex_string, full_string]

































