import enum

########################################################################################################################
#
# LEXER
#
########################################################################################################################


#TODO
#while loop
#if statement
#programma state
#raise weghalen




class Token_Types(enum.Enum):
    VALUE = None
    SUMPLUS = 'addiere'
    SUMMIN = 'zähle'
    MULTIPLUCATION = 'multiplizieren'
    DIVISION = 'Teilen'
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
    def __init__(self, Token_Types, value):
        self.type = Token_Types
        self.value = value

    def __repr__(self):
        return "Token(Type {}, Value\"{}\")".format(self.type.name, self.value)


def split_l(lines: list, i: int=0)->list:
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
def Put_tokens_on_list(token_function, l: list, i: int=0)->list:
    if i == len(l) - 1:
        return [token_function(l[i])]
    else:
        return [token_function(l[i])] + Put_tokens_on_list(token_function, l, i+1)

## for list of inf size like [1,[2,[3,None]]]
def Put_tokens_on_head_tail_list(loop_fuction ,token_function, l: list)->list:
    if l[1] == None:
        return [loop_fuction(token_function, l[0]), None]
    else:
        return [loop_fuction(token_function, l[0])] + [Put_tokens_on_head_tail_list(loop_fuction,token_function, l[1])]


def get_token(string: str)->Token:
    if string == Token_Types.SUMPLUS.value:
        return Token(Token_Types.SUMPLUS, string)
    elif string == Token_Types.MULTIPLUCATION.value:
        return Token(Token_Types.MULTIPLUCATION, string)
    elif string == Token_Types.IS.value:
        return Token(Token_Types.IS, string)
    elif string == Token_Types.IF.value:
        return Token(Token_Types.IF, string)
    elif string == Token_Types.ELSE.value:
        return Token(Token_Types.ELSE, string)
    elif string == Token_Types.WHILE.value:
        return Token(Token_Types.WHILE, string)
    elif string == Token_Types.END.value:
        return Token(Token_Types.END, string)
    elif string == Token_Types.SMALER.value:
        return Token(Token_Types.SMALER, string)
    elif string == Token_Types.LARGER.value:
        return Token(Token_Types.LARGER, string)
    elif string == Token_Types.SAME.value:
        return Token(Token_Types.SAME, string)
    elif string.isdigit():
        return Token(Token_Types.INTEGER, int(string))
    else:
        return Token(Token_Types.VALUE, string)

########################################################################################################################
#
# AST
#
########################################################################################################################

class Node(object):
  pass

class NumberNode(Node):
  def __init__(self, value: int):
    self.value = value

  def __repr__(self):
    return f'{self.value}'

class VariableNode(Node):
  def __init__(self, token: Token, value:int = None):
    self.token = token
    self.value = value

  def __repr__(self):
    return f'{self.token} = [{self.value}]'

class BinairyOperationNode(Node):
  def __init__(self, left, token, right):
    self.left = left
    self.token = token
    self.right = right

  def __repr__(self):
    return f'{self.left}, {self.token}, {self.right}'

  def __str__(self):
    return f'{self.left.value}, {self.token.type}, {self.right.value}'

class ConditionNode(Node):
  def __init__(self, left:Node , token: Token, right:Node):
    self.left = left
    self.token = token
    self.right = right

  def __repr__(self):
    return f'{self.left.value}, {self.token}, {self.right.value}'

class IfNode(Node):
  def __init__(self, condition: ConditionNode):
    self.condition = condition

  def __repr__(self):
    return f'{self.condition}'

class WhileNode(Node):
  def __init__(self, condition):
    self.condition = condition

  def __repr__(self):
    return f'{self.condition}'


def parser(tokens: list, index: int=0, node: Node=None)->Node:
  if index == len(tokens) - 1:
    if tokens[index].type == Token_Types.INTEGER:
      return NumberNode(tokens[index].value)
    elif tokens[index].type == Token_Types.VALUE:
      return VariableNode(tokens[index], tokens[index].value)
    else:
      raise Exception("operator has no right side")
  else:
    if tokens[index].type == Token_Types.INTEGER:
      return  parser(tokens, index + 1, NumberNode(tokens[index].value))
    elif tokens[index].type == Token_Types.VALUE:
      if tokens[index].value != None:
        return parser(tokens, index + 1, VariableNode(tokens[index], tokens[index].value))
    elif tokens[index].type in (Token_Types.MULTIPLUCATION, Token_Types.DIVISION, Token_Types.SUMMIN, Token_Types.SUMPLUS):
      return BinairyOperationNode(node, tokens[index], parser(tokens, index + 1))
    elif tokens[index].type in (Token_Types.SMALER, Token_Types.LARGER, Token_Types.SAME):
      return ConditionNode(node, tokens[index], parser(tokens, index + 1))
    elif tokens[index].type == Token_Types.WHILE:
      return WhileNode(parser(tokens, index +1))
    elif tokens[index].type == Token_Types.IF:
      return IfNode(parser(tokens, index + 1))
    elif tokens[index].type == Token_Types.IS:
      return VariableNode(node.token, parser(tokens, index + 1))
    else:
      raise Exception("geen operator")


def parser_on_multiline(parser_function, tokens_list: list)->list:
  if tokens_list[1] == None:
    return [parser_function(tokens_list[0]), None]
  else:
    return [parser_function(tokens_list[0])] + [parser_on_multiline(parser_function, tokens_list[1])]

########################################################################################################################
#
# Run
#
########################################################################################################################

def do_operation(token_type, left, right)->int:
  if token_type == Token_Types.SUMPLUS:
    return left + right
  elif token_type == Token_Types.SUMMIN:
    return left - right
  elif token_type == Token_Types.MULTIPLUCATION:
    return left * right
  elif token_type == Token_Types.DIVISION:
    if right != 0:
      return left / right
    else:
      raise Exception("cannot divide by zero")

def do_condition(token_type, left, right)->bool:
  if token_type == Token_Types.SAME:
    return left == right
  elif token_type == Token_Types.SMALER:
    return left < right
  elif token_type == Token_Types.LARGER:
    return left > right



def Is(node: Node, state:dict )->dict:
  if type(node.value) == NumberNode:
    state[node.token.value] = node.value.value

  if type(node.value) in (BinairyOperationNode, ConditionNode):
    if type(node.value.left) == VariableNode:
      left = state[node.value.left.value]
    else:
      left = node.value.left.value
    if type(node.value.right) == VariableNode:
      right = state[node.value.right.value]
    else:
      right = node.value.right.value
    if type(node.value) == BinairyOperationNode:
      state[node.token.value] = do_operation(node.value.token.type, left, right)
    elif type(node.value) == ConditionNode:
      state[node.token.value] = do_condition(node.value.token.type, left, right)

  elif type(node.value) == VariableNode:
    if node.value.token in state:
      state[node.token.value] = state[node.value.token]
    else:
      raise Exception("variable does not exist")
  return state



def run(parsedFuctions: list, state: dir):
  if parsedFuctions[1] == None:
    if type(parsedFuctions[0]) == VariableNode:
      return Is(parsedFuctions[0], state)
  else:
    return run(parsedFuctions[1], Is(parsedFuctions[0], state))


########################################################################################################################
#
# -----
#
########################################################################################################################

file = "sum.gmm"

file = open(file, "r", encoding="utf-8")
lines = file.readlines()

states = {}

lines = split_l(lines)
lines = split_lines_words(lines)
tokenlist = Put_tokens_on_head_tail_list(Put_tokens_on_list, get_token, lines)
#print(tokenlist)
tree = parser_on_multiline(parser, tokenlist)
#print(tree)
states = run(tree, states)
print(states)
