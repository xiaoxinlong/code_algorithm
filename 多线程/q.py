#coding=utf-8
from queue import Queue
import threading
import time

from queue import Queue


def job(l, q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    q.put(l)
    print(q.queue)


def multithreading():
    q = Queue()
    threads = []
    data = [[1, 2, 3], [3, 4, 5], [4, 4, 4], [5, 5, 5]]
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))  # Thread首字母要大写，被调用的job函数没有括号，只是一个索引，每次传进去data的一行
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)

if __name__== '__main__':
    multithreading()