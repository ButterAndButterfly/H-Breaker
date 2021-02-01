<p align="center">
      <strong>
        <a href="https://github.com/ButterAndButterfly/H-Breaker" target="_blank">Head-Breaker 爆头者</a>
      </strong>  针对文件恶意扫描解析而生  
  <br>
      源自<strong>
        <a href="https://github.com/ButterAndButterfly" target="_blank">ButterAndButterfly</a><br>
      </strong>  
        Butter, 寓意宅男; Butterfly, 寓意美好的事物。 
        <br/> 美好的世界由我们创造!  
</p>


## 技术原理  
#### 可读性破坏  
+ 当我们解析某类文件(比如`.mp4`/`.jpg`)时，往往需要根据该类文件约定俗成的规范进行读取。  
而不论哪种规范，头部往往是关键。在大多数情况下，更改头部(必要的时候加上尾部)的寥寥几个几十个字节即可使得文件完全无法解析。  
    + **当然文本除外，缺失几个字节对文本后续阅读基本上没有影响**  
    + **针对某些压缩算法(尤其是不带密码的)，因为有一定的冗余的修复信息，一般密钥需要更长一点，且最好对尾部进行一定的破坏**  

#### 可还原性  
本项目根据密钥字符串的字节长度，读取文件相应长度的头/尾部，采用逐字节做加法取模的方法进行加密破坏。  
相应的，自然可以采用逐字节做减法取模的方法进行解密还原。  

#### 转换速度  
相比较于各种压缩/加密算法，由于我们只针对密钥长度的文件部分进行破坏/还原，无论文件有多大，速度低于秒级，快的飞起。  

  
## 如何安装  
```
pip install --upgrade h-breaker

或者克隆本项目后
pip setup.py install
```
或者前往[Release](https://github.com/ButterAndButterfly/H-Breaker/releases)页面下载`exe`文件

## 如何使用  
```
usage: h-breaker [-h] [-breaks | -recover] [-all | -only_tail] path key

version 1.0.0 : 文件头破坏者，用于简单加密文件头/尾部

positional arguments:
  path             待处理的文件路径
  key              密钥

optional arguments:
  -h, --help       show this help message and exit
  -breaks, -b      破坏文件
  -recover, -r     恢复文件
  -all, -a         同时破坏文件头+文件尾
  -only_tail, -ot  仅破坏尾巴
```

#### 举例
+ 破坏文件`test.mp4`，口令字符串为`3.1415926`  
```
h-breaker ./test.mp4 3.1415926
```

+ 还原文件`test.mp4`(假设已经被破坏，相应的口令字符串为`3.1415926`)  
```
h-breaker ./test.mp4 3.1415926 -r
```

+ 破坏文件`test.zip`，口令字符串为(需要足够长)`12345678901234567890123456789012345678901234567890`  
```
h-breaker ./test.zip 12345678901234567890123456789012345678901234567890 -a
```

+ 还原文件`test.zip`(假设已经被破坏，相应的口令字符串为`12345678901234567890123456789012345678901234567890`)  
```
h-breaker ./test.zip 12345678901234567890123456789012345678901234567890 -a -r
```

## **重要的话**
+ 为了提高处理速度，我们直接对原文件进行读写操作，而不是再copy一个副本，在进行操作之前请确认文件已经备份！！！   
+ 如果不小心误操作了，不用慌，记住密钥，使用**相反**操作即可还原。

## LICENSE
MIT 


