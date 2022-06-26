from datetime import datetime
import pathlib

nuevadireccion = "./02-Generador de contratos"
# Obtengo la ruta absoluta
path = pathlib .Path( __file__ ) .parent .absolute()

def replaceText(text):
    filters = [["[COMPANY_NAME]", "Company Name"],
                   ["[EMPLOYEE_NAME]", "Employee Name"],
                   ["[PRICE]", "Price"],
                   ["[CITY]", "City"],
                   ["[COUNTRY]", "Country"]
               ]
    for filter in filters:
        print("What is the " + filter[1] + "?")
        txtInput = input()
        text = text.replace(filter[0], txtInput)

    return text.replace("[CURRENT_DATE]", datetime.today().strftime('%Y-%m-%d'))

contractFile = open(str( path ) + "/contract.txt", "r", encoding='utf8')
result = ""


for row in contractFile:
    result += row
result = replaceText(result)

with open(f"{nuevadireccion}/contract_processed.txt", "w", encoding='utf8') as textFile:
    textFile.write(result)


#  [CURRENT_DATE] [COMPANY_NAME] [EMPLOYEE_NAME] [CITY] [COUNTRY] [PRICE]