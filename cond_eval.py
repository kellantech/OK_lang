from  custom_eval import custom_eval
def eval_cond(cnd):
  op =  ""
  for chr in cnd:
    if chr in ["=","<",">","!","~"]:
      op=chr
      break
  if op == "=":
    ev1 = custom_eval(cnd.split("=")[0].strip())
    ev2 = custom_eval(cnd.split("=")[1].strip())
    if ev1 == ev2: return True
    else: return False
  elif op == "<":
      ev1 = custom_eval(cnd.split("<")[0].strip())
      ev2 = custom_eval(cnd.split("<")[1].strip())
      if ev1 < ev2: return True
      else: return False  
  elif op == ">":
      ev1 = custom_eval(cnd.split(">")[0].strip())
      ev2 = custom_eval(cnd.split(">")[1].strip())
      if ev1 > ev2: return True
      else: return False  
  elif op == "!":
      ev1 = custom_eval(cnd.split("!")[0].strip())
      ev2 = custom_eval(cnd.split("!")[1].strip())
      if ev1 != ev2: return True
      else: return False  
  elif op == "~":
      ev1 = eval_cond(cnd.strip()[1:])
      if ev1 == False:
        return True
      else:
        return False

