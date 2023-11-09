import re

my_string = "Place of delivery of goods or place of performance of work or provision of services: 82172, Ukraine, Lviv Region, Stebnyk, str. Doroshenko, 1 Deadline for delivery of goods, performance of works or provision of services: 31.12.2023"


if __name__ == '__main__':
    data = {
        'country': re.search(r'(?<=\d{5}\,\s)\w*', my_string).group(),
        'region': re.search(r'(?<=\d{5}\,\s\w{7}\,\s)\w*\s\w*', my_string).group(),
        'city': re.search(r'\w*(?=\,\s\w*\.)', my_string).group(),
        'postal': re.search(r'\d{5}', my_string).group(),
        'address': re.search(r'\w*\.\s\w*\,\s\d', my_string).group(),
        'deadline': re.search(r'\d*\.\d*\.\d*$', my_string).group(),
    }
    print(data)

