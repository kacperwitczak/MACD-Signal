import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read("config.txt")
    data_length = config.getint("DEFAULT", 'data_length')
    data_path = config.get("DEFAULT", 'data_path')
    price_column = config.get("DEFAULT", 'prices_column')
    company_name = config.get("DEFAULT", 'company_name')
    date_column = config.get("DEFAULT", 'date_column')
    return data_length, data_path, price_column, company_name, date_column
