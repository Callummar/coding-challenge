import json

def main():
    jsonFileName = "data.json"
    fileContents = ReadJsonFile(jsonFileName)
    fileData = fileContents["data"]
    
    
    revenueFilteredData =  FilterData("account_category","revenue",fileData)
    expensesFilteredData = FilterData("account_category","expense",fileData)

    #print(CalcualteTotalValue(revenueFilteredData))
    #print(CalcualteTotalValue(expensesFilteredData))

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

#Sum all Total_values based on data provided
def CalcualteTotalValue(dataList):
    totalValue = 0
    for data in dataList:
        try:
            totalValue += int(data["total_value"])
        except:
            totalValue += 0
    return totalValue

main()