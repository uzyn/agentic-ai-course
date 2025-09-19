from .singapore_time import singapore_time
from .singapore_weather import singapore_weather
from .singapore_news import singapore_news


def test_print_all():
    print(singapore_time())
    print("\n" + singapore_weather())
    print("\n" + singapore_news())
