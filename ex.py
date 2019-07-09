from tasks import add, app

print(app.conf)

for i in range(250):
    add.delay(i, 1)

# res = app.AsyncResult('a9fd2d78-023b-4f4d-aeb0-2f07a112f530')
# print(res.ready())
# import time
#
# import eventlet
#
# urls = [
#     "http://www.google.com/intl/en_ALL/images/logo.gif",
#     "https://wiki.secondlife.com/w/images/secondlife.jpg",
#     "http://us.i1.yimg.com/us.yimg.com/i/ww/beta/y3.gif",
# ]
#
#
# def fetch(url):
#     time.sleep(5)
#     return 'A' + url
#
#
# pool = eventlet.GreenPool()
#
# for body in pool.imap(fetch, urls):
#     print("got body", len(body))