import argparse
def load_args():
  argparser = argparse.ArgumentParser(prog = '',description = 'a simple programing language')
  argparser.add_argument('file')
  argparser.add_argument('-d', '--debug',action='store_true')  
  argparser.add_argument('--allow_inf_loop',action='store_true')  
  argparser.add_argument('-l', '--loop_limit',default=1000000,type=int)      
  cli_args = argparser.parse_args()
  lpbrk = not (cli_args.allow_inf_loop)
  if lpbrk:
    LOOPLIMIT = cli_args.loop_limit
  
  else: LOOPLIMIT = 0;
  debug = cli_args.debug
  return cli_args.file, lpbrk , LOOPLIMIT, debug  
