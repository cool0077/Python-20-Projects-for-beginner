import urllib.request as urllib

def main(url):
    print("Checking connectivity ")
    
    response = urllib.urlopen(url)
    print("Connected to ", url, "Sucessfully")
    print("This response code was: ", response.getcode())

print("This is a site connectivity checker program")
input_url = input("Enter the url of the site you wanna check: ")

main(input_url)