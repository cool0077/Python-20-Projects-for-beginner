def main():
    print("Welcome to email slicer")
    print("")
    
    email_slicer = input("enter your email address")
    (username,domain) = email_slicer.split("@")
    (domain, extension) = domain.split(".")
    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)
main()