import datetime

from ganzhi.gan_zhi import gan_zhi_year

if __name__ == "__main__":
    this_year = datetime.date.today().year

    print(gan_zhi_year(this_year))
