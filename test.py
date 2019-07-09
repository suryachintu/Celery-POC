# import eventlet
# from eventlet.green import urllib2
#
#
# urls = [
#     "http://www.google.com/intl/en_ALL/images/logo.gif",
#     "http://us.i1.yimg.com/us.yimg.com/i/ww/beta/y3.gif",
# ]
#
#
# def fetch(url):
#     return urllib2.urlopen(url).read()
#
#
# pool = eventlet.GreenPool()
#
# for body in pool.imap(fetch, urls):
#     print("got body", len(body))


def countdown(n):
    while n > 0:
        yield n
        n -= 1


c = countdown(5)

from collections import deque

tsks = deque()

tsks.extend([countdown(10), countdown(5), countdown(20)])

print(tsks)


def run():
    while tsks:
        tsk = tsks.popleft()
        print(tsks)
        try:
            x = next(tsk)
            # print(x)
            tsks.append(tsk)
        except StopIteration:
            print("Task")

run()