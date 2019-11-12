from time import time
from multiprocessing import Pool
import logging
from Factorial.factorial import factorial


logging.basicConfig(
    level=logging.DEBUG,
    filename='spent_time.log',
    filemode='w',
)

pool = Pool(processes=3)

start = time()
p1 = pool.apply_async(factorial, [30000])
p2 = pool.apply_async(factorial, [50000])
p3 = pool.apply_async(factorial, [70000])
pool.close()
pool.join()
end = time()

spent_time = end - start
logging.info('spent time: %f' % spent_time)
# print('spent time:', spent_time)
