#!/usr/bin/python
# encoding:utf-8


import time


def consumer():
    r = ''
    while True:
        # consumer通过yield拿到消息，处理，又通过yield把结果传回
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'


def produce(c):
    # c.next启动生成器
    c.next()
    n = 0
    while n < 3:
        n += 1
        print('[PRODUCER] Producing %s...' % n)
        # 通过c.send(n)切换到consumer执行
        r = c.send(n)
        # produce拿到consumer处理的结果，继续生产下一条消息
        print('[PRODUCER] Consumer return: %s' % r)
    # produce决定不生产了，通过c.close()关闭consumer，整个过程结束
    c.close()


if __name__ == '__main__':
    c = consumer()  # c是生成器
    produce(c)
