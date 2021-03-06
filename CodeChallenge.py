import json

def main():
    jsonFileName = "data.json"
    fileContents = readJsonFile(jsonFileName)

def readJsonFile(jsonFile):
    with open('data.json') as f:
        return json.load(f)

main()