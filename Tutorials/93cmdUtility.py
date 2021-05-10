# python .\93cmdUtility.py --x 4 --y 8 --o add
# OR
# python .\93cmdUtility.py --x 4 --y 8 --o mul 

import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'sub':
        return args.x - args.y
    elif args.o == 'div':
        return args.x / args.y
    else:
        return "Something went Wrong!"


if __name__ == "__main__":
    p = argparse.ArgumentParser()

    p.add_argument('--x', type=float, default=1.0, 
    help="Enter First Number. This Utility is created by ARS...")

    p.add_argument('--y', type=float, default=2.0, 
    help="Enter Second Number. This Utility is created by ARS...")

    p.add_argument('--o', type=str, default='add', 
    help="Add the Entered number. This Utility is created by ARS...")

    args = p.parse_args()
    sys.stdout.write(str(calc(args)))
