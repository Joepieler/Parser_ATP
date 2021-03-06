import enum

########################################################################################################################
#
# LEXER
#
########################################################################################################################



class Token_Types(enum.Enum):
    VARIABLE = None
    SUMPLUS = 'addiere'
    SUMMIN = 'zähle'
    MULTIPLUCATION = 'multiplizieren'
    DIVISION = 'teilen'
    IS = 'ist'
    IF = 'wenn'
    ELSE = 'sonst'
    END = 'ende'
    SMALER = 'kleiner'
    LARGER = 'größer'
    SAME = 'gleichwie'
    WHILE = 'solange'
    INTEGER = type(int)
    PRINT = "abdrucken"
    PRINTALL = "alle_variable_drucken"



class Token():
    def __init__(self, token_types: Token_Types, value):
      self.type = token_types
      self.value = value

    def __repr__(self):
      return "Token(Type {}, Value\"{}\")".format(self.type.name, self.value)

    def __str__(self):
      return "Token(Type {}, Value\"{}\")".format(self.type.name, self.value)

def put_line_in_list(lines: str)->list:
  return lines.rstrip('\n')


def split_lines_word(lines: str)->list:
  return lines.split(" ")

def put_in_head_teal_list(l: list, index:int = 0)->list:
  if index == len(l) - 1:
    return [l[index], None]
  else:
    return [l[index]] + [put_in_head_teal_list(l, index + 1)]



#function on a normal list [1,2,3]
def Put_tokens_on_list(token_function, l: list, i: int = 0)->list:
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
    if string == Token_Types.SUMPLUS.value:     # Plus
        return Token(Token_Types.SUMPLUS, string)
    elif string == Token_Types.SUMMIN.value:    # min
        return Token(Token_Types.SUMMIN, string)
    elif string == Token_Types.MULTIPLUCATION.value:# Multiply
        return Token(Token_Types.MULTIPLUCATION, string)
    elif string == Token_Types.DIVISION.value:  # Devide
      return Token(Token_Types.DIVISION, string)
    elif string == Token_Types.IS.value:        # Is
        return Token(Token_Types.IS, string)
    elif string == Token_Types.IF.value:        # If
        return Token(Token_Types.IF, string)
    elif string == Token_Types.ELSE.value:      # Else
        return Token(Token_Types.ELSE, string)
    elif string == Token_Types.WHILE.value:     # While
        return Token(Token_Types.WHILE, string)
    elif string == Token_Types.END.value:       # End
        return Token(Token_Types.END, string)
    elif string == Token_Types.SMALER.value:    # Smaller then
        return Token(Token_Types.SMALER, string)
    elif string == Token_Types.LARGER.value:    # Larger then
        return Token(Token_Types.LARGER, string)
    elif string == Token_Types.SAME.value:      # Same as
        return Token(Token_Types.SAME, string)
    elif string.isdigit():                      # Integer
        return Token(Token_Types.INTEGER, int(string))
    elif string == Token_Types.PRINT.value:     # Print
        return Token(Token_Types.PRINT, string)
    elif string == Token_Types.PRINTALL.value:  # Print all
        return Token(Token_Types.PRINTALL, string)
    else:                                       # Variable
        return Token(Token_Types.VARIABLE, string)

########################################################################################################################
#
# AST
#
########################################################################################################################


#Base Node
class Node(object):
  pass


#Node for Numbers
class NumberNode(Node):
  def __init__(self, value: int):
    self.value = value

  def __repr__(self):
    return f'{self.value}'

  def __str__(self):
    return f'{self.value}'


#Node For variable
class VariableNode(Node):
  def __init__(self, token: Token, value: int = None):
    self.token = token
    self.value = value

  def __repr__(self):
    return f'{self.token} = [{self.value}]'

  def __str__(self):
    return f'{self.token} = [{self.value}]'


#Note for Operators
class OperationNode(Node):
  def __init__(self, left: Node, token: Token, right: Node):
    self.left = left
    self.token = token
    self.right = right

  def __repr__(self):
    return f'{self.left}, {self.token}, {self.right}'

  def __str__(self):
    return f'{self.left}, {self.token}, {self.right}'


#Note for Conditions
class ConditionNode(Node):
  def __init__(self, left: Node, token: Token, right: Node):
    self.left = left
    self.token = token
    self.right = right

  def __repr__(self):
    return f'{self.left.value}, {self.token}, {self.right.value}'

  def __str__(self):
    return f'{self.left.value}, {self.token}, {self.right.value}'



#Note for If statments
class IfNode(Node):
  def __init__(self, condition: ConditionNode):
    self.value = condition

  def __repr__(self):
    return f'{self.value}'

  def __str__(self):
    return f'{self.value}'



#Node for While loops
class WhileNode(Node):
  def __init__(self, condition: ConditionNode):
    self.value = condition

  def __repr__(self):
    return f'{self.value}'

  def __str__(self):
    return f'{self.value}'



class EndNode(Node):
  def __repr__(self):
    return f'EndNode'

  def __str__(self):
    return f"EndNode"
  pass


class PrintNode(Node):
  def __init__(self, value: Node):
    self.left = value

  def __repr__(self):
    return f'Print({self.left})'

  def __str__(self):
    return f'Print({self.left})'


class PrintAllNode(Node):
  pass



#Main parser function
def parser(tokens: list, index: int=0, node: Node=None)->Node:
  # The end of a line can only be an integer or a variable
  if index == len(tokens) - 1:
    if tokens[index].type == Token_Types.INTEGER: # Integer
      return NumberNode(tokens[index].value)
    elif tokens[index].type == Token_Types.VARIABLE: # Variable
      return VariableNode(tokens[index], tokens[index].value)
    elif tokens[index].type == Token_Types.END:
      return EndNode()
    elif tokens[index].type == Token_Types.PRINTALL:
      return PrintAllNode()
  else:
    if tokens[index].type == Token_Types.INTEGER: # Intergers
      return  parser(tokens, index + 1, NumberNode(tokens[index].value))
    elif tokens[index].type == Token_Types.VARIABLE: # Variables
      return parser(tokens, index + 1, VariableNode(tokens[index], tokens[index].value))
    elif tokens[index].type in (Token_Types.MULTIPLUCATION, Token_Types.DIVISION, Token_Types.SUMMIN, Token_Types.SUMPLUS): # Operations
      return OperationNode(node, tokens[index], parser(tokens, index + 1))
    elif tokens[index].type in (Token_Types.SMALER, Token_Types.LARGER, Token_Types.SAME): # Conditions
      return ConditionNode(node, tokens[index], parser(tokens, index + 1))
    elif tokens[index].type == Token_Types.WHILE: # While loops
      return WhileNode(parser(tokens, index +1))
    elif tokens[index].type == Token_Types.IF:# If statements
      return IfNode(parser(tokens, index + 1))
    elif tokens[index].type == Token_Types.IS:# Is operator
      return VariableNode(node.token, parser(tokens, index + 1))
    elif tokens[index].type == Token_Types.PRINT: # printing variable or int
      return PrintNode(parser(tokens, index + 1))

#Run parser function on every line of the code
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



#Get the left and right child
def Get_left_and_right(node, state):
  left = None
  right = None
  if type(node) in (WhileNode, IfNode, VariableNode):
    if type(node.value) in (OperationNode, ConditionNode):
      if type(node.value.left) == VariableNode:
        left = state[node.value.left.value]
      else:
        left = node.value.left.value
      if type(node.value.right) == VariableNode:
        right = state[node.value.right.value]
      else:
        right = node.value.right.value
  elif type(node) == PrintNode:
    if type(node.left) == VariableNode:
      left = state[node.left.value]
    else:
      left = node.left.value
  return [left, right]



#returns the result of a operation in int
def do_operation(node, states)->int:
  childs = Get_left_and_right(node, states)
  if node.value.token.type == Token_Types.SUMPLUS:
    return childs[0] + childs[1]
  elif node.value.token.type == Token_Types.SUMMIN:
    return childs[0] - childs[1]
  elif node.value.token.type == Token_Types.MULTIPLUCATION:
    return childs[0] * childs[1]
  elif node.value.token.type == Token_Types.DIVISION:
    if childs[1] != 0:
      return int(childs[0] / childs[1])



#returns a bool of the result
def do_condition(node, states)->bool:
  childs = Get_left_and_right(node, states)
  if node.value.token.type == Token_Types.SAME:
    return childs[0] == childs[1]
  elif node.value.token.type == Token_Types.SMALER:
    return childs[0] < childs[1]
  elif node.value.token.type == Token_Types.LARGER:
    return childs[0] > childs[1]



#adds a value to the state dir and returns tje dir
def Is(node: Node, state:dict )->dict:
  if type(node.value) == NumberNode:
    state[node.token.value] = node.value.value

  #Call opperators
  if type(node.value) == OperationNode:
    state[node.token.value] = do_operation(node, state)
  elif type(node.value) == ConditionNode:
    state[node.token.value] = do_condition(node, state)

  #Get value for variable
  elif type(node.value) == VariableNode:
    if node.value.token in state:
      state[node.token.value] = state[node.value.token]
  return state



#Finds the first end en returns the rest of the parserser
def FindEnd(parserlist, skipend: int = 0):
  if parserlist == None:
    return [EndNode, None]
  if parserlist[0] != None:
    if skipend > 0:
      if type(parserlist[0]) == EndNode:
        return FindEnd(parserlist[1], skipend -1)
      elif type(parserlist[0]) in (IfNode, WhileNode):
        return FindEnd(parserlist[1], skipend + 1)
      else:
        return FindEnd(parserlist[1], skipend)
    else:
      if type(parserlist[0]) == EndNode:
        return parserlist[1]
      elif type(parserlist[0]) in (IfNode, WhileNode):
        return FindEnd(parserlist[1], skipend + 1)
      else:
        return FindEnd(parserlist[1], skipend)
  else:
   return [EndNode, None]



#Returns the loop
def GetLoop(parserlist: list, whilenode: WhileNode, state: dir, skipped:int = 0)->list:
  if type(parserlist[0]) == EndNode:
    if skipped == 0:
      return [EndNode(), None]
    else:
      skipped -= 1
  else:
    if type(parserlist[0]) in (IfNode, WhileNode):
      skipped += 1
    return [parserlist[0]] + [GetLoop(parserlist[1], whilenode, state, skipped)]



#The while loop function returns the state
def While(parserList: list, node: Node, state: dir, whilenode: WhileNode = None):
  if whilenode == None:
    if do_condition(node, state):
      parserlist = GetLoop(parserList[1], node, state)
      state = run(parserlist, state)
      return While(parserlist, node, state, node)
    else:
      return state
  else:
    if type(node) == WhileNode:
      if do_condition(whilenode, state):
        return While(parserList, node, run(parserList, state), whilenode)
      else:
        return state



#The if statement function it returns the state
def If(parserList: list, node , state: dir):
  if do_condition(node, state):
    return run(parserList[1], state)
  else:
    return state



#The Print function that retuns the state
def Print( node, state: dir):
  print(Get_left_and_right(node, state)[0])
  return state



def PrintRegister(state):
  list(map(print, state))
  return state



#The main run function
def run(parsedFuctions: list, state: dir):
  if parsedFuctions != None:
    if type(parsedFuctions[0]) == IfNode:
      return run(FindEnd(parsedFuctions[1]), If(parsedFuctions, parsedFuctions[0], state))
    elif type(parsedFuctions[0]) == WhileNode:
      return run(FindEnd(parsedFuctions[1]), While(parsedFuctions, parsedFuctions[0], state))
    elif type(parsedFuctions[0]) == VariableNode:
      return run(parsedFuctions[1], Is(parsedFuctions[0], state))
    elif type(parsedFuctions[0]) == PrintNode:
      return run(parsedFuctions[1], Print(parsedFuctions[0], state))
    elif type(parsedFuctions[0]) == PrintAllNode:
      return run(parsedFuctions[1], PrintRegister(state))
    elif type(parsedFuctions[0]) == EndNode:
      return state
  return state




def start_compiling(filename: str):
  file = open(filename, "r", encoding="utf-8")
  lines = file.readlines()
  lines = put_in_head_teal_list(list(map(split_lines_word, list(map(put_line_in_list, lines)))))
  tokenlist = Put_tokens_on_head_tail_list(Put_tokens_on_list, get_token, lines)
  tree = parser_on_multiline(parser, tokenlist)
  run(tree, {})



########################################################################################################################
#
# -----
#
########################################################################################################################


file = "sum.gmm"
start_compiling(file)

