import sys,os
from get_args import load_args
from parse_var import parse_var
import custom_eval,parse_if,cond_eval
global lpbrk
from OKDIR import OKLANG_DIR

file,lpbrk_,LOOPLIMIT, debug  = load_args()
ABSPATH = os.popen("pwd").read().replace("\n","")

def stop(msg):
  print(msg)
  sys.exit()

with open(f"{ABSPATH}/{file}",'r') as file:
  cde = file.read()
vars_ = { }  
funcs = { }
def setvar(name,val):
  vars_[name] = val
def getvar(name):
  return vars_[name]
  
def run(code):
  global lpbrk
  lpbrk = lpbrk_
  if debug:
    print("variables",end=":   ")
    for _vn_,_vv_ in vars_.items():
      print(f"{_vn_}:{_vv_}")
    print()  
    print("functions",end=":  ")
    for _vn2_,_vv2_ in funcs.items():
      print(f"{_vn2_}:{_vv2_}")
    print()  
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
    elif tkn.startswith("while "):
      st = tkn[tkn.index("{") + 1 : tkn.index("}")]
      cond = tkn[tkn.index("(") + 1 : tkn.index(")")]
      lpctr = 0
      while True:
        if lpbrk and lpctr > LOOPLIMIT-1:break
        
        for vn,vv in vars_.items():
          c2 = cond
          c2 = c2.replace(f"${vn}",str(vv))
          
        if cond_eval.eval_cond(c2):
          for l2 in st.split(";"):
            run(l2)
          lpctr += 1
        else:
          break
      
    elif tkn.startswith("if "):
      s = tkn
      
      
      r,c = parse_if.parse(s)
      for vn,vv in vars_.items():
        c = c.replace(f"${vn}",str(vv))
      if cond_eval.eval_cond(c):
        for l in r.split(";"):
          run(l)
    elif tkn.startswith("import"):
      nm = tkn.split(" ")[1]
      try:
        pth = os.path.join(ABSPATH,f"{nm}.ok")
        with open(f"{pth}",'r') as imp:
          run(imp.read())
      except FileNotFoundError:
        pth2 = os.path.join(OKLANG_DIR,"stdlib",f"{nm}.ok")
        with open(pth2,'r') as imp2:
          run(imp2.read())
    elif tkn.startswith("call"):
      fnname =  tkn[tkn.index("call ")+4: tkn.index("(")].strip()
      args = tkn[tkn.index("(")+1: tkn.index(")")].split(',')
      
      cd = funcs[fnname]["code"]
      fn_args = funcs[fnname]["args"]
      for ar in range(len(fn_args)):
        arg = fn_args[ar]
        if arg == '': continue
        cd = cd.replace("$"+arg,args[ar])
      
      
      for vrn,vrv in vars_.items():
        cd = cd.replace(f"${vrn}",str(vrv))  
      run(cd.replace(";","\n"))
      
run(cde)
