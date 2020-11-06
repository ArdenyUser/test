print("----------")
print("Welcome to WebDiFine!")
print("This site can only be accessed on WebDiFine Servers.")
print("1: Data 2: Emulate 3: Branches 4: Exit 5: Web Browse 6: Make Account")
x = input("@User: ")
if x == "1":
    print("WebDiFine is a program used to view the web in Non-GUI.")
    x = input("")
    print("It has many branches! Like the official WebXPython.")
    x = input("")
    print("Most branches are closed due to a web server problem.")
    x = input("")
    print("WebDiFine will shutdown on 05/07/2021")
    x = input("")
    print("")
    print("To help, donate to WebXPython.")
    x = input("")
    print("Also, many sites are not working on WebDiFine anymore because")
    x = input("")
    print("of the shutdown soon, many devs have quit too.")
    x = input("")
    import webdifinecom
if x == "2":
    print("WebDiFine has been converting sites to Non-GUI.")
    x = input("")
    print("To use sites, use a branch. Like the")
    x = input("")
    print("official WebXPython and WebXWindows.")
    x = input("")
    print("WebXPython uses WebDiFine Python Versions.")
    x = input("")
    import webdifinecom
if x == "3":
    print("404 Page Not Found")
    x = input("")
    import webdifinecom
if x == "4":
    print("Exiting...")
    import WEBDIFINE
if x == "5":
    import c2
if x == "6":
    print("Make/Edit Account:")
    print("Enter 'Web Name':")
    webn = input("@User: ")
    file = open('name.config', 'w')
    file.write(webn)
    file.close()
    print("Enter 'ID/Password':")
    webp = input("@User: ")
    file = open('id.config', 'w')
    file.write(webp)
    file.close()
    import webdifinecom
    