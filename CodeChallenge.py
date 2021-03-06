import json

def main():
    jsonFileName = "data.json"
    fileContents = ReadJsonFile(jsonFileName)
    fileData = fileContents["data"]
    
    
    revenueFilteredData =  FilterData("account_category","revenue",fileData)
    expensesFilteredData = FilterData("account_category","expense",fileData)


def ReadJsonFile(jsonFile):
    with open('data.json') as f:
        return json.load(f)

#Return filtered data relevant to paramaters provided
def FilterData(key,value,dataList):
    filteredList = list()
    for dataDict in dataList:
        if dataDict[key] == value:
            filteredList += [dataDict]
    return filteredList


main()