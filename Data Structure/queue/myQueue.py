#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# data structure: Queue
# author: @ljx

class MyQueue(object):

    def __init__(self, length):
        super(MyQueue, self).__init__()
        self.length = length
        self.data = [None] * length
        self.head = 0
        self.tail = 0
        
    def enQueue(self, x):
        if not self.isFull():
            self.data[self.tail] = x
            self.tail += 1
            return True
        else:
            return False

    def deQueue(self):
        if not self.isEmpty():
            self.data.append(None)
            self.data = self.data[1:]
            self.tail -= 1
            return True
        else:
            return False

    def isEmpty(self):
        return self.head == self.tail

    def isFull(self):
        return self.tail - self.head == self.length


if __name__ == '__main__':
    mq = MyQueue(3)
    mq.enQueue(3)
    mq.enQueue(2)
    print('enqueue:', mq.enQueue(9))
    print('data now:', mq.data)
    print('enqueue when queue is full:', mq.enQueue(0))

    mq.deQueue()
    mq.deQueue()
    print('dequeue:', mq.deQueue())
    print('data now:', mq.data)
    print('dequeue when queue is empty:', mq.deQueue())

    print('Is queue full?', mq.isFull())
    print('Is queue empty?', mq.isEmpty())
