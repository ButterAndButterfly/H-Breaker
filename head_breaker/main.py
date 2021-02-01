import argparse
import os
import sys
from head_breaker import breaker
from head_breaker import version

args = None

def arg_parser():
    parser = argparse.ArgumentParser(prog='h-breaker', description="version %s : %s"%(version.__version__, version.__descriptrion__))
    parser.add_argument("path", help="待处理的文件路径")
    parser.add_argument("key", help="密钥")
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument("-breaks", '-b', help="破坏文件", required=False, action='store_true', default=True)
    group1.add_argument("-recover", '-r', help="恢复文件", required=False, action='store_true', default=False)
    group2 = parser.add_mutually_exclusive_group()
    group2.add_argument("-all", '-a', help="同时破坏文件头+文件尾", required=False, action='store_true', default=False)
    group2.add_argument("-only_tail", '-ot', help="仅破坏尾巴", required=False, action='store_true', default=False)

    
    global args
    args = parser.parse_args()

    
def main():
    arg_parser()
    path = args.path
    key = args.key
    is_break = args.breaks
    is_recover = args.recover
    if not os.path.exists(path):
        print(path, "文件不存在！")
        sys.exit()  
      
    if not is_recover:
        if args.all:
            breaker.break_head(path, key)
            breaker.break_tail(path, key)
            print("文件头尾部破坏成功，请记住key: ", key)
        elif args.only_tail:
            breaker.break_tail(path, key)
            print("文件尾破坏成功，请记住key: ", key)
        else:
            breaker.break_head(path, key)
            print("文件头破坏成功，请记住key: ", key)
    else:
        if args.all:
            breaker.recover_head(path, key)
            breaker.recover_tail(path, key)
            print("文件头尾部恢复成功，key: ", key)
        elif args.only_tail:
            breaker.recover_tail(path, key)
            print("文件尾恢复成功，key: ", key)
        else:
            breaker.recover_head(path, key)
            print("文件头恢复成功，key: ", key)

    
if __name__ == '__main__':
    main()