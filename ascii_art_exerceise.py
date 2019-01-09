import pyfiglet, termcolor
while True:
    ss = input("Type something good!!\n")
    cc = input("Choose the color you want to display\n")
    if ss:
        try:
            pyfiglet.print_figlet(ss, font="standard", colors=cc.upper())
        except:
            pyfiglet.print_figlet(ss, font="standard")
        if ss.lower() == 'quit':
            break