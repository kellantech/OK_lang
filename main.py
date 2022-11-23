import sys
from get_args import load_args
from parse_var import parse_var
from parse_ep import parse_ep

file,lpbrk,LOOPLIMIT, debug  = load_args()

def stop(msg):
  print(msg)
  sys.exit()

with open(file,'r') as file:
  cde = file.read()
vars_ = { }  
funcs = { }
def setvar(name,val):
  vars_[name] = val
def getvar(name):
  return vars_[name]
def run(code):
  tokens = code.split("\n")
  for tkn in tokens:
    if tkn.startswith('var'):
      splt = tkn.split(" ",1)[1]
      name = (splt.split('=')[0].strip())
      val= (splt.split('=')[1].strip())
      
      if isinstance(parse_var(val),dict):
        funcs[name] = parse_var(val)
      else:
        setvar(name,parse_var(val))
    if tkn.startswith('execpy'):    
      c = parse_ep(tkn) 
      if c[0] == '$':
        exec(getvar(c[1:]))
        
      else:
        exec(c)
    
run(cde)
