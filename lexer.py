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
            return "[{} {}]".format(self.type, self.value)

        else:
            return "[{}]".format(self.type)


def split_l(lines: list, i: int):
  if i == len(lines) - 1:
    return [lines[i].rstrip('\n')]
  else:
    return [lines[i].rstrip('\n')] + split_l(lines, i + 1 )


def split_lines_words(l :list, i :int)->list:
    if i == len(l) - 1:
        return list(l[i].split(" "))
    else:
        return list(l[i].split(" ")) + list(split_lines_words(l, i+1))


def fucntion_on_list(f , l: list, i)->list:
    if i == len(l) - 1:
        return [f(l[i])]
    else:
        return [f(l[i])] + fucntion_on_list(f, l, i+1)


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
print(split_lines_words(lines,0))
print(fucntion_on_list(get_token, split_lines_words(lines,0),0))
