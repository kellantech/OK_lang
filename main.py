import sys
try:prg = sys.argv[1]
except: prg = input('Enter program name: ')

def stop(msg,tkn="unspecified"):
  print(msg,'\n'+'token',tkn)
  sys.exit()

with open(f'{prg}', 'r') as f:
  c = f.read()

vars_ = {}
fns = {}
PI = 3.14159
E = 2.71828
SQRT2 = 1.41421
def run(txt):
  global vars_
  tokens = txt.replace("\n",';').split(';')
  for _ in range(len(tokens)):
      tokens[_] = tokens[_].strip().replace('\n', '').replace('$$PI',f'{PI}').replace("$$E",f'{E}').replace("$$SQRT2",f'{SQRT2}')
  tkno = 0
  for tk in tokens:
    tkno+=1
    tk2 = tk.split(':',1)
    if tk2[0].startswith('import'):
      p_n = tk2[0][7:]
      try:
        with open(f"{p_n}.ok",'r') as fil:
          p = fil.read()
          run(p)
      except FileNotFoundError:
        stop(f"File {p_n}.ok not found",tkno)
    elif tk2[0].startswith('call'):
      p_n = tk2[0].split(' ')[1]
    
      try:
        with open(f"{p_n}.ok",'r') as fil:
          p = fil.read()
          run(p)
      except FileNotFoundError:
        stop(f"File {p_n}.ok not found",tkno)
    elif tk2[0] == ('set'):
      tk3 = tk2[1].split('=')
      if tk3[1][0] == "i":
        vars_[tk3[0]] = int(tk3[1][1:])
      elif  tk3[1][0]== "f":
        vars_[tk3[0]] = float(tk3[1][1:])
      elif tk3[1][0]== "'": vars_[tk3[0]] = tk3[1][1:][:-1]
      elif tk3[1][0]== "\"": vars_[tk3[0]] = tk3[1][1:][:-1]
      elif tk3[1][0]== "(":
        s = (tk3[1])[1:][:-1]
        for ke,va in vars_.items():
          s = s.replace(f"${ke}",str(va))
        vars_[tk3[0]] = eval(s)
      elif tk3[1][0] == "." :
        ty = tk3[1][1]
        val = input()
        if ty == "i":
          val = int(val)
        if ty == "f":
          val = float(val)
        if ty== "'" or ty == '"':
          pass
        vars_[tk3[0]] = val
      else:
        stop("expected type idenifier",tkno)
     
    elif tk2[0] == "print":
      if tk2[1][0] == "&":
        print()
      elif tk2[1][0] == "@":print(" ",end="")  
      elif tk2[1][0] == "$": 
        try:
          print(vars_[tk2[1][1:]],end='')
        except KeyError:
          stop("variable not found "+tk2[1][1:],tkno)
      else:
        print(tk2[1],end='')
          
    elif tk2[0] == "": pass
    elif tk2[0][0] == "<":
      exp = tk2[0][1:][:-1]
      for ke,va in vars_.items():
          exp = exp.replace(f"${ke}",str(va))
      try: eval(exp)
      except SyntaxError:
        stop("variable not found",tkno)
      if (eval(exp)):
        cd = tk2[1][1:][:-1].split('|')
        for c in cd:
          run(c)
    elif tk2[0][0] == "{":
      exp = tk2[0][1:][:-1]
      for ke,va in vars_.items():
          exp = exp.replace(f"${ke}",str(va))
      co = tk2[1][1:][:-1].split('|')
      while True:
        if (eval(exp)):
          for c2 in co:
            run(c2)
          exp = tk2[0][1:][:-1]
          for ke,va in vars_.items():
            exp = exp.replace(f"${ke}",str(va))
        else:break
    elif tk2[0][0] == "%":
      nm = tk2[0][1:]
      cd3 = tk2[1][1:][:-1]
      fns[nm]= cd3
    elif tk2[0][0].startswith("*"):
      nm = tk2[0][1:]
      for cd4 in fns[nm].split("|"):
        run(cd4)
    else:
      print(f"unknown statement: {tk2[0]}")
      break
  

run(c)
