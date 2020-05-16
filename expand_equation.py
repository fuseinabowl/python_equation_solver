import argparse
import sys

from expand_equation import expand_equation

def create_arg_parser() -> argparse.ArgumentParser:
  parser = argparse.ArgumentParser()
  parser.add_argument('equation', str)
  return parser

if __name__ == '__main__':
  parser = create_arg_parser()
  args = parser.parse_args(sys.argv)
  expanded_equation = expand_equation(args.equation)
  print(expanded_equation)
  sys.exit(0)