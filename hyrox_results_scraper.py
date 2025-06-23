from hyrox.enums import Division, Gender
from hyrox.hyrox import HyroxEvent
from multiprocessing import Pool
import logging


output_dir = 'data/'

events_2025 = [
    HyroxEvent(event_id="LR3MS4JIA19", season=8),  # houston
    HyroxEvent(event_id="LR3MS4JIB91", season=8),  # nyc
    HyroxEvent(event_id="LR3MS4JIA79", season=8),  # atlanta
    HyroxEvent(event_id="LR3MS4JIAA3", season=8),  # miami
    HyroxEvent(event_id="LR3MS4JIA40", season=8),  # dc
    HyroxEvent(event_id="JGDMS4JI9A1", season=8),  # las vegas
    HyroxEvent(event_id="LR3MS4JIB56", season=8),  # cardiff
    HyroxEvent(event_id="LR3MS4JIB7D", season=8),  # riga
    HyroxEvent(event_id="LR3MS4JIB69", season=8),  # rimini
    HyroxEvent(event_id="LR3MS4JIB41", season=8),  # bangkok
    HyroxEvent(event_id="LR3MS4JIAF1", season=8),  # berlin
    HyroxEvent(event_id="LR3MS4JIB19", season=8),  # incheon
    HyroxEvent(event_id="LR3MS4JIACA", season=8),  # herenveen
    HyroxEvent(event_id="LR3MS4JIAB7", season=8),  # london
    HyroxEvent(event_id="LR3MS4JIADD", season=8),  # mumbai
    HyroxEvent(event_id="LR3MS4JIAA2", season=8),  # barcelona
    HyroxEvent(event_id="LR3MS4JIA69", season=8),  # paris
    HyroxEvent(event_id="LR3MS4JIA55", season=8),  # cologne
    HyroxEvent(event_id="LR3MS4JIA65", season=8),  # sharjah
    HyroxEvent(event_id="LR3MS4JIA3F", season=8),  # taipei
    HyroxEvent(event_id="LR3MS4JIA66", season=8),  # warsaw
    HyroxEvent(event_id="LR3MS4JIA54", season=8),  # belgium
    HyroxEvent(event_id="LR3MS4JIA52", season=8),  # monterrey
    HyroxEvent(event_id="LR3MS4JIA3E", season=8),  # shanghai
    HyroxEvent(event_id="LR3MS4JIA29", season=8),  # malaga
    HyroxEvent(event_id="LR3MS4JIA1A", season=8),  # glasgow
    HyroxEvent(event_id="LR3MS4JIA15", season=8),  # copenhagen
    HyroxEvent(event_id="LR3MS4JIA01", season=8),  # valencia
    HyroxEvent(event_id="LR3MS4JI9DA", season=8),  # brisbane
    HyroxEvent(event_id="JGDMS4JI9A0", season=8),  # johannesburg
    HyroxEvent(event_id="LR3MS4JI9C5", season=8),  # karlsruhe
    HyroxEvent(event_id="JGDMS4JI99C", season=8),  # rotterdam
    HyroxEvent(event_id="JGDMS4JI999", season=8),  # vienna
    HyroxEvent(event_id="JGDMS4JI98D", season=8),  # katowice
    HyroxEvent(event_id="JGDMS4JI976", season=8),  # bilbao
    HyroxEvent(event_id="JGDMS4JI9A3", season=8),  # guadalajara
    HyroxEvent(event_id="JGDMS4JI998", season=8),  # st. gallen
    HyroxEvent(event_id="JGDMS4JI9B1", season=8),  # toulouse
    HyroxEvent(event_id="JGDMS4JI98E", season=8),  # aukland
    HyroxEvent(event_id="JGDMS4JI996", season=8),  # maastricht
    HyroxEvent(event_id="JGDMS4JI992", season=8),  # manchester
]

events_2024 = [
    HyroxEvent(event_id="JGDMS4JI964", season=8),  # frankfurt
    HyroxEvent(event_id="JGDMS4JI962", season=8),  # melbourne
    HyroxEvent(event_id="JGDMS4JI93E", season=8),  # anaheim
    HyroxEvent(event_id="JGDMS4JI917", season=8),  # marseille
    HyroxEvent(event_id="JGDMS4JI93C", season=8),  # stockholm
    HyroxEvent(event_id="JGDMS4JI939", season=8),  # london
    HyroxEvent(event_id="JGDMS4JI8D9", season=8),  # hongkong
    HyroxEvent(event_id="JGDMS4JI925", season=8),  # dallas
    HyroxEvent(event_id="JGDMS4JI8B7", season=8),  # beijing
    HyroxEvent(event_id="JGDMS4JI918", season=8),  # chicago
    HyroxEvent(event_id="JGDMS4JI8B1", season=8),  # dublin
    HyroxEvent(event_id="JGDMS4JI8B0", season=8),  # manchester
    HyroxEvent(event_id="JGDMS4JI913", season=8),  # mexico city
    HyroxEvent(event_id="JGDMS4JI914", season=8),  # paris
    HyroxEvent(event_id="JGDMS4JI901", season=8),  # poznan
    HyroxEvent(event_id="JGDMS4JI8AE", season=8),  # hamburg
    HyroxEvent(event_id="JGDMS4JI8FD", season=8),  # birmingham
    HyroxEvent(event_id="JGDMS4JI8EA", season=8),  # madrid
    HyroxEvent(event_id="JGDMS4JI871", season=8),  # incheon
    HyroxEvent(event_id="JGDMS4JI8D6", season=8),  # milan
    HyroxEvent(event_id="JGDMS4JI8B5", season=8),  # amsterdam  todo
    HyroxEvent(event_id="JGDMS4JI8C1", season=8),  # nice
    HyroxEvent(event_id="JGDMS4JI89A", season=8),  # toronto
    HyroxEvent(event_id="JGDMS4JI872", season=8),  # stuttgart
    HyroxEvent(event_id="JGDMS4JI85E", season=8),  # perth
    HyroxEvent(event_id="JGDMS4JI885", season=8),  # cape town
    HyroxEvent(event_id="JGDMS4JI860", season=8),  # singapore
    HyroxEvent(event_id="JGDMS4JI85D", season=8),  # brisbane
    HyroxEvent(event_id="JGDMS4JI849", season=8),  # sidney
    HyroxEvent(event_id="JGDMS4JI80F", season=8),  # singapore
    HyroxEvent(event_id="JGDMS4JI551", season=8),  # nice world champs
    HyroxEvent(event_id="JGDMS4JI7E7", season=8),  # new york
    HyroxEvent(event_id="JGDMS4JI80E", season=8),  # rimini
    HyroxEvent(event_id="JGDMS4JI7FB", season=8),  # gdansk
    HyroxEvent(event_id="JGDMS4JI7E8", season=8),  # taipei
    HyroxEvent(event_id="JGDMS4JI7D1", season=8),  # anaheim
    HyroxEvent(event_id="JGDMS4JI7E5", season=8),  # doha
    HyroxEvent(event_id="JGDMS4JI7AA", season=8),  # london
    HyroxEvent(event_id="JGDMS4JI759", season=8),  # bordeaux
    HyroxEvent(event_id="JGDMS4JI781", season=8),  # berlin
    HyroxEvent(event_id="JGDMS4JI76F", season=8),  # mexico city
    HyroxEvent(event_id="JGDMS4JI771", season=8),  # cologne
    HyroxEvent(event_id="JGDMS4JI75A", season=8),  # malaga
    HyroxEvent(event_id="JGDMS4JI747", season=8),  # rotterdam
    HyroxEvent(event_id="JGDMS4JI731", season=8),  # copenhagen
    HyroxEvent(event_id="JGDMS4JI748", season=8),  # houston
    HyroxEvent(event_id="JGDMS4JI745", season=8),  # karlsruhe
    HyroxEvent(event_id="JGDMS4JI70C", season=8),  # glasgow
    HyroxEvent(event_id="JGDMS4JI52E", season=8),  # dc
    HyroxEvent(event_id="JGDMS4JI709", season=8),  # fort lauderdale
    HyroxEvent(event_id="JGDMS4JI70A", season=8),  # katowice
    HyroxEvent(event_id="JGDMS4JI6CD", season=8),  # bilbao
    HyroxEvent(event_id="JGDMS4JI6CE", season=8),  # dubai
    HyroxEvent(event_id="JGDMS4JI530", season=8),  # vienna
    HyroxEvent(event_id="JGDMS4JI6AB", season=8),  # turin
    HyroxEvent(event_id="JGDMS4JI6AA", season=8),  # maastricht
]

events = events_2024 + events_2025


def scrape_event(event):
    hyrox_event = event.copy()
    try:
        hyrox_event.get_info(divisions=[Division.open], genders=[Gender.male])
        hyrox_event.save(directory=output_dir)
    except Exception as e:
        logging.error(f"Error getting event {hyrox_event.event_id}")
        logging.error(e)


if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(scrape_event, events))
