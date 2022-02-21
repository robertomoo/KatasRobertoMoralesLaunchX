#def main():
#    open("/path/to/mars.jpg")
#
#if __name__ == '__main__':
#    main()


#def main():
#    try: 
#        configuration = open('config.txt')
#    except FileNotFoundError:
#        print("Could not find the config.txt file !")
#
#if __name__ == '__main__':
#    main()

def main():
    try: 
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Could not find the config.txt file !")

if __name__ == '__main__':
    main()