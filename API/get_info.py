import requests
import logging
from threading import Thread
from time import time


logging.basicConfig(
    level=logging.DEBUG,
    filename='jobs.log',
    filemode='w',
)


PAGE_COUNT = 2
BASE_URL = 'https://jobs.github.com/positions.json'
JOBS = ['python', 'ruby', 'java']


def get_response(job: str, page: int):
    resp = requests.get(BASE_URL, params={'description': job, 'page': page})
    logging.info(f'(Job:{job}|Page:{page}) => {resp.content})\n\n')


threads = list()
for job in JOBS:
    for page_num in range(1, PAGE_COUNT+1):
        threads.append(Thread(target=get_response, args=(job, page_num)))


start = time()
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
end = time()

spent_time = end - start
logging.info('spent time: %f' % spent_time)
