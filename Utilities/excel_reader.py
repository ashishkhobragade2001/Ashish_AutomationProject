import pandas as pd


def get_login_data():
    filepath = "C://Ashish_Automation//TestData//login_data.xlsx"
    df = pd.read_excel(filepath)
    return df.values.tolist()


def get_registration_data():
    filepath = "C://Ashish_Automation//TestData//registration_data.xlsx"
    df = pd.read_excel(filepath)
    return df.values.tolist()
