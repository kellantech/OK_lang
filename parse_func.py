def parse_func_def(c):
  c = c.replace("func","")
  c_args =  c[c.index("(") + 1 : c.index(")")].split(",")
  c_code = c[c.index("{") + 1 : c.index("}")]
  print(c_code)
  return {"args":c_args,"code":c_code}
