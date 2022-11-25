import string
def custom_eval(ex):
  global rm
  rm = True
  for c in ex:
    
    if c == "\"" or c == "'":
      rm = not rm
    elif rm:
      if c in string.ascii_uppercase or c in string.ascii_lowercase:
        ind = ex.index(c)
        ex = ex[:ind] + ex[ind + 1:]
  
  return eval(ex)

