from datetime import datetime,timedelta
from selenium.webdriver.common.keys import Keys
import time


def get_begin_day(delta_days):
    today = datetime.today()
    begin_day = today + timedelta(int(delta_days))
    begin_day_str = begin_day.strftime("%d%m%Y")
    return begin_day_str


def enter_address_cdi(element, address):
    element.send_keys(address)
    time.sleep(1)
    element.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    element.send_keys(Keys.ENTER)
    time.sleep(1)


class InvalidLanguageException(Exception):
    pass