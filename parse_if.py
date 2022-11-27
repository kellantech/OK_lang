import cond_eval
def parse(st):
  st = st[3:].strip()
  cond = st[st.index("(") + 1 : st.index(")")]
  stat = st[st.index("{")+1:-1]
  if cond_eval.eval_cond(cond) == True:
    return stat
  else:
    return ""
