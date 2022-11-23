import parse_func
def parse_var(val):
  if val.startswith("'") or val.startswith('"'):
        val = val[1:][:-1]
        return val
  elif '.' in val:
        return float(val)
  elif val.startswith("func"):
     return (parse_func.parse_func_def(val))
  else:
        return int(val)
  
