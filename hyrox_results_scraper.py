from hyrox.enums import Division, Gender
from hyrox.hyrox import HyroxEvent
from multiprocessing import Pool
import logging
import csv

OUTPUT_DIR = 'data/'


def scrape_event(event):
    hyrox_event = event.copy()
    try:
        hyrox_event.get_info(divisions=[Division.open], genders=[Gender.male])
        hyrox_event.save(directory=OUTPUT_DIR)
    except Exception as e:
        logging.error(f"Error getting event {hyrox_event.event_id}")
        logging.error(e)


def read_event_ids(
    event_name_filter: list[str] | None,
    file_name: str
):
    _event_ids = []

    def _filter(event_name: str, event_name_filter: list[str] | None) -> bool:
        if event_name_filter:
            return any(list(filter(lambda f: f in event_name, event_name_filter)))
        return True

    with open(file_name, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            event_name, event_id = row
            if _filter(event_name, event_name_filter):
                _event_ids.append(event_id)

    return _event_ids


if __name__ == '__main__':

    event_ids = read_event_ids(
        event_name_filter=["2023", "2022", "2021"],
        file_name=OUTPUT_DIR + "event_ids.csv"
    )

    events = [
        HyroxEvent(event_id=event_id, season=8)
        for event_id in event_ids
    ]

    with Pool(5) as p:
        print(p.map(scrape_event, events))
