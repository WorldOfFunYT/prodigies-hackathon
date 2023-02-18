import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import random


def getClient():
    data = pd.read_csv(
        'ReportingBehaviour.csv')

    Source = []
    SourceScore = []

    for x in data['Source']:
        Source.append(x)

    for x in data['PC_Transactions']:
        SourceScore.append(x)

    Device = ["mobile", "desktop", "tablet"]
    DeviceScore = [0.56, 1.54, 0.71]

    UserType = ["new_visitor", "returning_visitor"]
    UserTypeScore = [0.70, 1.47]

    BrowserData = pd.read_csv(
        'browser_data.csv')
    # BrowserData = pd.read_csv(
    #     r'C:\\Users\\Student\\Desktop\\hackhaton\\home.html\\browser_data.csv')

    Browser = []
    BrowserScore = []

    for x in BrowserData['Browser']:
        Browser.append(x)

    for x in BrowserData['PC_Transactions']:
        BrowserScore.append(x)

    CustomerType = []
    BrowserType = []
    SourceType = []
    DeviceType = []
    VisitorType = []

    CustomerScore = []
    BrowserRate = []
    SourceRate = []
    DeviceRate = []
    VisitorRate = []

    for a in UserType:
        for b in Device:
            for c in Browser:
                for d in Source:
                    add = a + "," + b + "," + c + "," + d
                    CustomerType.append(add)
                    BrowserType.append(c)
                    SourceType.append(d)
                    VisitorType.append(a)
                    DeviceType.append(b)

    for a in UserTypeScore:
        for b in DeviceScore:
            for c in BrowserScore:
                for d in SourceScore:
                    add = a + b + c + d
                    CustomerScore.append(add)
                    BrowserRate.append(c)
                    SourceRate.append(d)
                    DeviceRate.append(b)
                    VisitorRate.append(a)

    data = {'VisitorType': [CustomerType],
            'VisitorScore': [CustomerScore]}

    CentralDataFrame = pd.DataFrame(CustomerType)
    CentralDataFrame['CustomerScore'] = CustomerScore

    CentralDataFrame['VisitorType'] = VisitorType
    CentralDataFrame['DeviceType'] = DeviceType
    CentralDataFrame['BrowserType'] = BrowserType
    CentralDataFrame['SourceType'] = SourceType

    CentralDataFrame['VisitorRate'] = VisitorRate
    CentralDataFrame['DeviceRate'] = DeviceRate
    CentralDataFrame['BrowserRate'] = BrowserRate
    CentralDataFrame['SourceRate'] = SourceRate

    CentralDataFrame.to_csv("CentralFile.csv")

    response = CentralDataFrame['CustomerScore'].describe()
    return response
