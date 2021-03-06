import json

def main():
    jsonFileName = "data.json"
    fileContents = ReadJsonFile(jsonFileName)
    fileData = fileContents["data"]
    
    #Calcualte Revenue
    revenueFilter = [{"account_category":["revenue"]}]
    revenueData =  FilterData(revenueFilter,fileData)
    revenueTotal = CalcualteTotalValue(revenueData)
    print("Revenue: " + FormatValue("money",revenueTotal))
    #Calculate Expenses
    expensesFilter = [{"account_category":["expense"]}]
    expensesData = FilterData(expensesFilter,fileData)
    expensesTotal = CalcualteTotalValue(expensesData)

    print("Expenses: " + FormatValue("money",expensesTotal))

    #Calculate Gross Profit Margin
    gpmAccountFilter = [{"account_type":["sales"]}]
    gpmValueFilter = [{"value_type":["debit"]}]

    gpmAccountData = FilterData(gpmAccountFilter,fileData)
    gpmValueData = FilterData(gpmValueFilter,fileData)

    gpmPercent = (CalcualteTotalValue(gpmAccountData) + CalcualteTotalValue(gpmValueData)) / revenueTotal
    print("Gross Profit Margin: " + FormatValue("percentage",gpmPercent))
    
    #Calculate Net Profit Margin
    npmValue = (revenueTotal - expensesTotal) / revenueTotal
    print("Net Profit Margin: " + FormatValue("percentage",npmValue))

    #Calcuate Working Capital Ratio
    wcrAssetsDebitFilter = [{"account_category":["assets"]},
    {"value_type":["debit"]},
    {"account_type":["current","bank","current_accounts_receivable"]}]
    wcrAssetsCreditFilter = [{"account_category":["assets"]},
    {"value_type":["credit"]},
    {"account_type":["current","bank","current_accounts_receivable"]}]
    wcrLiabilitiesCreditFilter = [{"account_category":["liability"]},
    {"value_type":["debit"]},
    {"account_type":["current","current_accounts_payable"]}]
    wcrLiabilitiesDebitFilter = [{"account_category":["liability"]},
    {"value_type":["credit"]},
    {"account_type":["current","current_accounts_payable"]}]

    wcrAssetsDebitData = FilterData(wcrAssetsDebitFilter,fileData)
    wcrAssetsCreditData = FilterData(wcrAssetsCreditFilter,fileData)
    wcrLiabilitiesCreditData = FilterData(wcrLiabilitiesCreditFilter,fileData)
    wcrLiabilitiesDebitData = FilterData(wcrLiabilitiesDebitFilter,fileData)

    wcrAssetsTotal = CalcualteTotalValue(wcrAssetsDebitData) - CalcualteTotalValue(wcrAssetsCreditData)
    wcrLiabilitiesTotal = CalcualteTotalValue(wcrLiabilitiesCreditData) - CalcualteTotalValue(wcrLiabilitiesDebitData)

    wcrValue = (wcrAssetsTotal / wcrLiabilitiesTotal)

    print("Working Capital Ratio: " + FormatValue("percentage",wcrValue))

def ReadJsonFile(jsonFile):
    with open('data.json') as f:
        return json.load(f)

#Return filtered data relevant to paramaters provided
def FilterData(filterOptions,dataList):
    filteredList = list()
    for dataDict in dataList:
        correctlyFiltered = True
        for filterOption in filterOptions:
            #Get a list of values from the filter options and check if the data matches if it meet all condtions add it to the filtered data list
            dictValue = dataDict[list(filterOption.keys())[0]]
            filterValues = list(filterOption.values())[0]
            if not (dictValue in filterValues):                
                correctlyFiltered = False
                break
        if correctlyFiltered:
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

def FormatValue(formatType,value):
    if (formatType == "money"):
        return  f"{value:,}"
    elif (formatType == 'percentage'):
        return "{:.1%}".format(value)


main()