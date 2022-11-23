def parse_ep(token):
  tkn = token.replace("execpy(","")[:-1].strip()
  if tkn[0] == '"' or tkn[0] == "'":
    return (tkn[1:][:-1])
  else:
    return tkn
    
