import logging

import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
import time

IGNORE = {
    "2024 Doha All Women's Race"  # not available
}


def get_driver():
    chromedriver_path = '/Users/leopoldpfeiffer/WebDriver/chromedriver'  # change path as needed

    service = Service(executable_path=chromedriver_path)

    options = Options()
    options.add_argument('--disable-notifications')

    _driver = webdriver.Chrome(service=service, options=options)
    _driver.implicitly_wait(20)
    _driver.set_script_timeout(20)
    return _driver


def scrape_ids(driver: WebDriver, event_ids: list[tuple[str, str]]):
    driver.get("https://results.hyrox.com/season-8/")

    time.sleep(10)

    driver.find_element(by=By.ID, value='restricted-consent-give').click()

    events = driver.find_element(by=By.ID, value='default-lists-event_main_group')
    all_event_options = Select(events).options
    event_option_values = [opt.get_attribute("value") for opt in all_event_options]

    for event_name in event_option_values:

        if event_name in IGNORE:
            continue

        driver.find_element(By.CSS_SELECTOR, f"option[value^=\"{event_name}\"]").click()

        time.sleep(1)

        default_submit_btn = driver.find_element(by=By.ID, value="default-submit")
        default_submit_btn.click()

        time.sleep(1)

        reload_button = driver.find_element(By.CSS_SELECTOR, "a[href^='?event=']")
        reload_button.click()

        time.sleep(1)

        event_id = driver.current_url.split("?event=")[1].split("&")[0].split("_")[1]
        event_ids.append((event_name, event_id))
        print(f"{event_id} – {event_name}")

        driver.back()
        driver.back()


def write_csv(event_ids: list[tuple[str, str]], filename='event_ids.csv'):
    with open(filename, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(event_ids)


if __name__ == '__main__':
    driver = get_driver()
    event_ids = []
    try:
        scrape_ids(driver, event_ids)
    except Exception as e:
        logging.error(e)
        logging.error(e.__traceback__)
    write_csv(event_ids)
    driver.quit()
