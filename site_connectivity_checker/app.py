# give the response site is runnning or not

import urllib.request as urllib

def connectivity_checker(url):
    print("Checking the connectivity ....")
    response = urllib.urlopen(url)
    print("The response code is : ", response.getcode())


print("This is site connectivity checker .... ")
url = input("Please enter the url to check the connectivity : ")
connectivity_checker(url)
