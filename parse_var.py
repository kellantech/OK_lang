import parse_func
def parse_var(val):
  if val.startswith("'") or val.startswith('"'):
        return val
  elif val[0] == "[":
    
    return f"#{val}"
  elif val.startswith("func"):
     return (parse_func.parse_func_def(val)) 
  elif val.startswith("evalpy"):
        val = val.replace("evalpy(","")[:-2][1:]
        evv = eval(val)
        if evv is int:
          return evv
        else:  
          return f'"{evv}"'
  elif '.' in val:
        return float(val)
  
  else:
        return int(val)
  
