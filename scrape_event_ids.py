import logging

import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
import time


def get_driver():
    chromedriver_path = '/Users/leopoldpfeiffer/WebDriver/chromedriver'  # change path as needed

    service = Service(executable_path=chromedriver_path)

    options = Options()
    options.add_argument('--disable-notifications')
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(20)
    driver.set_script_timeout(20)
    return driver


def scrape_ids(driver: WebDriver, event_ids: list[tuple[str, str]]):
    driver.get("https://results.hyrox.com/season-8/")

    time.sleep(10)

    driver.find_element(by=By.ID, value='restricted-consent-give').click()

    events = driver.find_element(by=By.ID, value='default-lists-event_main_group')
    all_event_options = Select(events).options
    event_option_values = [opt.get_attribute("value") for opt in all_event_options]

    for event_name in event_option_values[21:]:
        driver.find_element(By.CSS_SELECTOR, f"option[value^='{event_name}']").click()

        time.sleep(1)

        default_submit_btn = driver.find_element(by=By.ID, value="default-submit")
        default_submit_btn.click()

        time.sleep(1)

        reload_button = driver.find_element(By.CSS_SELECTOR, "a[href^='?event=']")
        reload_button.click()

        time.sleep(1)

        try:
            event_id = driver.current_url.split("?event=")[1].split("&")[0].split("_")[1]
            event_ids.append((event_name, event_id))
            print(f"{event_id} – {event_name}")
        except Exception:
            logging.error(f"Could not get event ID for {event_name}")

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
    print(event_ids)
    write_csv(event_ids)
    driver.quit()
