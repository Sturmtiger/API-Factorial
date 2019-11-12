from time import time
import logging
from Factorial.factorial import factorial


logging.basicConfig(
    level=logging.DEBUG,
    filename='spent_time.log',
    filemode='w',
)

start = time()
factorial(30000)
factorial(50000)
factorial(70000)
end = time()

spent_time = end - start
logging.info('spent time: %f' % spent_time)
# print('spent time:', spent_time)
