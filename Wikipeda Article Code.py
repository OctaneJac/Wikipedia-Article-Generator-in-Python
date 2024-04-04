import requests 
from bs4 import BeautifulSoup
import webbrowser

usr_title = input("What kind of article do you want on Wikipedia?: ").strip()

while True:
    main_url = "https://en.wikipedia.org/wiki/{}".format(usr_title)
    get = requests.get(main_url)
    soup = BeautifulSoup(get.content, 'html.parser')
    title = soup.find(class_ = "firstHeading").text
    print(title + "\nDo You want to view it? (Y/N/T -to exit)")
    ans = str(input(""))
    
    if (ans.lower() == "y"):
        url = 'https://en.wikipedia.org/wiki/%s' %title
        webbrowser.open(url)
        break
    
    elif (ans.lower() == "n"):
        print("ok\nEnter a different article name!")
        usr_title = input("What kind of article do you want on Wikipedia?: ").strip()
        continue
    
    elif (ans.lower() == "t"):
        break
    
    else:
        print("Bad Input!")
        ans = str(input("Do you want to try again? (Y/N) "))
    
    if (ans.lower() == "y"):
        usr_title = input("Enter something more specific:").strip()
        continue
    
    elif( ans.lower() == "n"):
        print("Terminating the program.")
        break  