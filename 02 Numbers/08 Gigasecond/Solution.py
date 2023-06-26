from datetime import date, timedelta

gigasecond = 10 ** 9

def add(moment):
    return moment + timedelta(seconds=gigasecond)
