from ganzhi.gan_list import Gan
from ganzhi.zhi_list import Zhi


def gan_zhi():
    for year in range(0, 60):
        print(f"第{year + 1}年 {Gan[year % 10]}{Zhi[year % 12]}")


def gan_zhi_year(year_number: int) -> str:
    gan = Gan[(year_number - 3) % 10 - 1]
    zhi = Zhi[(year_number - 3) % 12 - 1]

    return f"{year_number}年是{gan}{zhi}年"
