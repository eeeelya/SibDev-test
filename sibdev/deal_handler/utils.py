import csv


def prepare_deals(file):
    file = file.read().decode("utf-8").splitlines()
    result = csv.DictReader(file, fieldnames=("customer", "item", "total", "quantity", "date"))
    next(result)

    return result
