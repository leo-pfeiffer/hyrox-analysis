from enum import Enum


class Division(Enum):
    open = "H"
    pro = "HPRO"
    elite = "HE"
    doubles = "HD"
    relay = "HMR"
    goruck = "HG"
    goruck_doubles = "HDG"


class Gender(Enum):
    male = "M"
    female = "W"
