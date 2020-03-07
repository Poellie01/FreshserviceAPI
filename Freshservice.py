import requests
import pprint
import webbrowser
import sys
import json
from pyfiglet import Figlet

headers = {
    'Content-Type': 'application/json',
}

api_baseURLTicket = "https://XXXXXXXXX.com/helpdesk/tickets/"
api_baseURL = "https://XXXXXXXX.com/"
api_key = "XXXXXXXXX"


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Freshservice_banner = Figlet(font='big')
print(Freshservice_banner.renderText('Freshservice'))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

choice = input(
    "What do you wanna do? [1-5] 1: View a Ticket | 2: View list of tickets | 3: Show list of assets | 4: Show all contracts | 5: Create an Ticket ")
choice = int(choice)


def web_filesave():
    saveFile = input("Do you want to save the results to a file? (y/n)")
    if saveFile == "y" or saveFile == "yes":
        saveFile = input(
            "Name of the file (Put the extension behind it, filename.txt, filename.json)")
        saveFile = str(saveFile)
        with open(saveFile, 'w') as json_file:
            json.dumps(pprint.pprint(response.json(), json_file))
    openWeb = input("Do you want to open the ticket in the web browser?")
    if openWeb == "yes" or openWeb == "y":
        webbrowser.open(api_baseURLTicket + ticketID)
    printFile = input("Want to print out the output?")
    if printFile == "y" or printFile == "yes":
        pprint.pprint(response.json())


# View a ticket
if choice == 1:
    ticketID = input("What ticket ID?")
    ticketID = str(ticketID)
    response = requests.get(api_baseURLTicket + ticketID + ".json",
                            headers=headers, auth=('api_key', 'cmdX'))
    web_filesave()

# View list of tickets
elif choice == 2:
    tickets = input("How much tickets do you wanna see? (max 20)")
    tickets = str(tickets)
    response = requests.get(api_baseURLTicket + "filter/all_tickets?format=json&page=" +
                            tickets, headers=headers, auth=('api_key', 'X'))
    web_filesave()

# View assets.
elif choice == 3:
    response = requests.get(api_baseURL + "cmdb/items.json",
                            headers=headers, auth=('api_key', 'X'))

# View all the contracts
elif choice == 4:
    response = requests.get(api_baseURL + "cmdb/contracts.json",
                            headers=headers, auth=('api_key', 'X'))
    web_filesave()

elif choice == 5:
    catogory = "helpdesk_ticket"
    descr = str(input("What is the description? "))
    subj = str(input("What is the subject? "))
    email = str(input("what is your email? "))
    prio = int(input("What is the priority? [1-3] 1 = Highest"))
    ccmail = input("Want to put emails in the cc?")
    if ccmail == "y" or ccmail == "yes":
        ccmail = input("What are the mails? ")
    response = requests.get(api_baseURL + "/helpdesk/tickets.json",
                            headers=headers, auth=('api_key', 'X'))
    printFile = input("Want to print out the output?")
    if printFile == "y" or printFile == "yes":
        pprint.pprint(response.json())
