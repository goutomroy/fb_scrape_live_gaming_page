import logging
from faktory import Worker
from main.tasks import live_see_all, parse_profile, parse_posts
from utils.utils import URL_FACTORY
import multiprocessing

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    concurrency = multiprocessing.cpu_count()
    w = Worker(faktory=URL_FACTORY, queues=['default', 'busy'], concurrency=1)
    # w.register('gaming_home', gaming_home)
    w.register('live_see_all', live_see_all)
    w.register('parse_profile', parse_profile)
    w.register('parse_posts', parse_posts)
    # w.register('parse_profile_about', parse_profile_about)
    w.run()

