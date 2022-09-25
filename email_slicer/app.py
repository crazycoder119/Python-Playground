# Collect emails and slice username(abc), host(gmail), extension(com)

def main():
    print("Welcome to email slicer")
    email_input = input("input your email address : ")
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    print("Username is : ", username)
    print("Domain is : ", domain)
    print("extension is : ", extension)

choice = input("Entert Y to start, to quit press N : ")


while (choice == "Y" or choice == "y"):
    main()
    choice = input("Entert Y to start, to quit press N : ")