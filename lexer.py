import enum

file = "sum.gmm"

file = open(file, "r", encoding="utf-8")
lines = file.readlines()




class Token_Types(enum.Enum):
    VALUE = None
    SUMPLUS = 'addiere'
    SUMMIN = ''
    IS = 'ist'
    IF = 'wenn'
    ELSE = 'sonst'
    END = 'ende'
    SMALER = 'kleiner'
    LARGER = 'größer'
    SAME = 'gleichwie'
    WHILE = 'solange'
    INTEGER = type(int)


class Token():
    def __init__(self, Token_Types, value=None):
        self.type = Token_Types
        self.value = value

    def __repr__(self):
        if self.value != None:
            return "|{} {}|".format(self.type, self.value)

        else:
            return "|{}|".format(self.type)


def split_l(lines: list, i: int):
  if i == len(lines) - 1:
    if lines[i] != '\n':
      return [lines[i].rstrip('\n'), None]
  else:
    if lines[i] != '\n':
      return [lines[i].rstrip('\n')] + [split_l(lines, i + 1 )]
    else:
      return split_l(lines, i + 1 )


def split_lines_words(l :list)->list:
    if l[1] == None:
        return [l[0].split(" "), None]
    else:
        return [l[0].split(" ")] + [split_lines_words(l[1])]


#function on a normal list [1,2,3]
def Put_tokens_on_list(token_function, l: list, i: int)->list:
    if i == len(l) - 1:
        return [token_function(l[i])]
    else:
        return [token_function(l[i])] + Put_tokens_on_list(token_function, l, i+1)

## for list of inf size like [1,[2,[3,None]]]
def Put_tokens_on_head_tail_list(loop_fuction ,token_function, l: list)->list:
    if l[1] == None:
        return [loop_fuction(token_function, l[0], 0), None]
    else:
        return [loop_fuction(token_function, l[0], 0)] + [Put_tokens_on_head_tail_list(loop_fuction,token_function, l[1])]


def get_token(string : str) ->Token:
    if string == Token_Types.SUMPLUS.value:
        return Token(Token_Types.SUMPLUS)
    elif string == Token_Types.IS.value:
        return Token(Token_Types.IS)
    elif string == Token_Types.IF.value:
        return Token(Token_Types.IF)
    elif string == Token_Types.ELSE.value:
        return Token(Token_Types.ELSE)
    elif string == Token_Types.WHILE.value:
        return Token(Token_Types.WHILE)
    elif string == Token_Types.END.value:
        return Token(Token_Types.END)
    elif string == Token_Types.SMALER.value:
        return Token(Token_Types.SMALER)
    elif string == Token_Types.LARGER.value:
        return Token(Token_Types.LARGER)
    elif string == Token_Types.SAME.value:
        return Token(Token_Types.SAME)

    elif string.isdigit():
        return Token(Token_Types.INTEGER, int(string))
    else:
        return Token(Token_Types.VALUE, string)



lines = split_l(lines, 0)
lines = split_lines_words(lines)
tokenlist = Put_tokens_on_head_tail_list(Put_tokens_on_list, get_token, lines)
print(tokenlist)
