import time
import logging

import Actions.GenericActions


def loop_until(start_time, f, test_flag, until):
    remain = 5
    while remain > 0 and time.time() < start_time + until:
        f()
        if test_flag:
            remain -= 1
            logging.info('Test RUN, %i loops remain.' % remain)
        else:

            logging.info('Loop action until %dm%ds' % divmod(until, 60))


def browser_url_loop_until(start_time, urls, a: Actions.GenericActions.GenericActions, test_flag, until):
    remain = 5
    while remain > 0 and time.time() < start_time + until:
        url = urls.popleft()
        urls.append(url)
        if 'search' in url:
            url = url.replace('search:', '')
            a.browser_search(url)
        else:
            a.browser_new_tab(url)
        a.browser_browse()
        if test_flag:
            logging.info('Test RUN browser, %i loops remain.' % remain)
            remain -= 1
        else:
            logging.info('Loop browser action until %dm%ds' % divmod(until, 60))


def wait_until(start_time, test_flag, until):
    until = time.time() + 30 if test_flag else until
    logging.info('Will wait until %dm%ds' % divmod(until, 60))
    while time.time() < start_time + until:
        time.sleep(1)
