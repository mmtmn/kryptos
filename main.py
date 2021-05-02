# made by Thiago M Nóbrega
# to run this project: python main.py
import os

def main():
    linked_list = []
    print("hello there kryptos, I would take quite a while to make this in c")
    print("since i've already lost about 2/3 of my time trying to do it in c, I'll do it in python")
    #1/3 was attempting into creating .dll files for c
    #another 2/3 trying to remember how to do simple lists in c

    control = 0
    while control == 0:
        print("choices:\n1.search:\n2.put\n3.list\n4.remove\n5.clear\n6.first\n7.last\n8.quit")
        print("9.sort")

        while True:
            try:
                x = int(input('Your choice: '))
                break   
            except:
                print("Invalid option. Please try again.")

        # search     
        if x == 1:
            os.system('cls||clear')
            choosen_number = int(input('Your choice: '))
            linked_list[choosen_number]
            input("Press Enter to continue...")
            os.system('cls||clear')
            
            
        # put
        elif x == 2:
            os.system('cls||clear')
            choosen_number = int(input('Your choice: '))
            linked_list.append(choosen_number)
            input("Press Enter to continue...")
            os.system('cls||clear')
            
        # list
        elif x == 3:
            os.system('cls||clear')
            print(linked_list)
            input("Press Enter to continue...")
            os.system('cls||clear')

        # remove
        elif x == 4:
            os.system('cls||clear')
            choosen_number = int(input('Your choice: '))
            linked_list.pop(choosen_number)
            input("Press Enter to continue...")
            os.system('cls||clear')
            

        # clear
        elif x == 5:
            os.system('cls||clear')
            linked_list.clear()
            input("Press Enter to continue...")
            os.system('cls||clear')
                    

        # first
        elif x == 6:
            os.system('cls||clear')
            print(linked_list[0])
            input("Press Enter to continue...")
            os.system('cls||clear')
                    

        # last
        elif x == 7:
            os.system('cls||clear')
            print(linked_list[-1])
            input("Press Enter to continue...")
            os.system('cls||clear')
             

        # exit
        elif x == 8:
            control = 1
            print("thank you so much for your time and have a lovely day!")

        # only 6 mintues left when this was started
        elif x == 9:
            list_size = len(linked_list)
            organized_numbers = False
            while not organized_numbers:
                organized_numbers = True
                for x in range(0, list_size-1):
                    if linked_list[x] > linked_list[x+1]:
                        organized_numbers = False
                        linked_list[x], linked_list[x+1] = linked_list[x+1], linked_list[x]
            print(linked_list)

        # error catching
        else:
            print("")
            print("Sorry, that was not an option!")
            print("")
main()
