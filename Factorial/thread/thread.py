from time import time
from threading import Thread
import logging
from Factorial.factorial import factorial


logging.basicConfig(
    level=logging.DEBUG,
    filename='spent_time.log',
    filemode='w',
)

t1 = Thread(target=factorial, args=(30000,))
t2 = Thread(target=factorial, args=(50000,))
t3 = Thread(target=factorial, args=(70000,))

start = time()
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
end = time()

spent_time = end - start
logging.info('spent time: %f' % spent_time)
# print('spent time:', spent_time)
