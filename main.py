import sys
from get_args import load_args
from parse_var import parse_var
import custom_eval,parse_if

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
  lines = code.split("\n")
  
  for tkn in lines:
    if tkn.startswith('var'):
      splt = tkn.split(" ",1)[1]
      name = (splt.split('=',1)[0].strip())
      val= (splt.split('=',1)[1].strip())
      pv = parse_var(val)
      if pv is None: continue
      if isinstance(pv,dict):
        
        funcs[name] = pv
        
      elif isinstance(pv,str) and pv.startswith("#"):
        
        v = pv[2:][:-1]
        for k,va in vars_.items():
          v = v.replace(f"${k}",str(va))
        setvar(name,custom_eval.custom_eval(v))
      else:
        setvar(name,pv)
    elif tkn.startswith("if "):
      s = tkn
      for vn,vv in vars_.items():
        s = s.replace(f"${vn}",str(vv))
      
      r = parse_if.parse(s)
      
      if r != "":
        
        for l in r.split(";"):
          run(l)
    elif tkn.startswith("import"):
      nm = tkn.split(" ")[1]
      with open(f"{nm}.ok",'r') as imp:
        run(imp.read())
    elif tkn.startswith("call"):
      fnname =  tkn[tkn.index("call ")+4: tkn.index("(")].strip()
      args = tkn[tkn.index("(")+1: tkn.index(")")].split(',')
      
      cd = funcs[fnname]["code"]
      fn_args = funcs[fnname]["args"]
      for ar in range(len(fn_args)):
        arg = fn_args[ar]
        cd = cd.replace("$"+arg,args[ar])
      for vrn,vrv in vars_.items():
        cd = cd.replace(f"${vrn}",str(vrv))  
      run(cd.replace(";","\n"))
      
      
run(cde)
