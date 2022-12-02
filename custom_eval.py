def custom_eval(inp):
  def _if_int(x):
    if "'" in x or '"' in x:
      return x.replace("'",'').replace('"','')
    else: return int(x)  
      
  op = ""
  for c in inp:
    if c in ['+','-','*','/']:
      op = c
  if op == "":
    return inp
  else:  
    cd1 = inp.split(op)[0]
    cd2 = inp.split(op)[1]
    if op == "+":
      return _if_int(cd1)+_if_int(cd2)
    if op == "-":
      return _if_int(cd1)-_if_int(cd2)
    if op == "*":
      return _if_int(cd1)*_if_int(cd2)
    if op == "/":
      return _if_int(cd1)/_if_int(cd2)
    
