def parse_func_def(c):
  
  c = c.replace("func","")
  c_args =  c[c.index("(") + 1 : c.index(")")].split(",")
  c_code = c[c.index("{") + 1 : c.index("}")]
  return {"args":c_args,"code":c_code}
