#!/usr/bin/env python
# coding:utf-8
import os


def break_tail(path: str, keys):
    if not isinstance(keys, bytes):
        keys = bytes(keys, encoding = "utf8")
    tail_lenth = len(keys)
    file_lenth = os.path.getsize(path)
    pointer = file_lenth - tail_lenth
    assert(pointer >= 0)
    with open(path,"rb+") as file:
        file.seek(pointer)
        tail = file.read(tail_lenth)
        tail_broken = _break(tail, keys)
        file.seek(pointer)
        file.write(tail_broken)

def recover_tail(path: str, keys):
    if not isinstance(keys, bytes):
        keys = bytes(keys, encoding = "utf8")
    tail_lenth = len(keys)
    file_lenth = os.path.getsize(path)
    pointer = file_lenth - tail_lenth
    assert(pointer >= 0)
    with open(path,"rb+") as file:
        file.seek(pointer)
        tail = file.read(tail_lenth)
        tail_recover = _recover(tail, keys)
        file.seek(pointer)
        file.write(tail_recover)
        
def break_head(path: str, keys):
    if not isinstance(keys, bytes):
        keys = bytes(keys, encoding = "utf8")
    head_lenth = len(keys)
    with open(path,"rb+") as file:
        head = file.read(head_lenth)
        head_broken = _break(head, keys)
        file.seek(0)
        file.write(head_broken)

def recover_head(path: str, keys):
    if not isinstance(keys, bytes):
        keys = bytes(keys, encoding = "utf8")
    head_lenth = len(keys)
    with open(path,"rb+") as file:
        head = file.read(head_lenth)
        head_recover = _recover(head, keys)
        file.seek(0)
        file.write(head_recover)

        

def _break(heads: bytes, keys: bytes):
    '''
    heads 和 keys 对应字节两两相加
    '''
    assert(len(heads) == len(keys))
    data = [ (heads[index] + keys[index])&0xff for index in range(len(keys))]
    return bytes(data)
    
    
def _recover(heads: bytes, keys: bytes):
    '''
    heads 和 keys 对应字节两两相减
    '''
    assert(len(heads) == len(keys))
    data = [ (heads[index] + 256 - keys[index])&0xff for index in range(len(keys))]
    return bytes(data)
    
if __name__ == '__main__':
    # main()
    file = r'D:\Workspace\NiceLeee-FFmpeg.zip'
    #file = r'D:\Workspace\PythonWorkspace\HeadBreaker\test.txt'

    keys = '3.14151111111111111111111111111111111111111111111111111111111111111111'
    
    break_head(file, keys)
    break_tail(file, keys)
    #recover_head(file, keys)  
    #recover_tail(file, keys)
    