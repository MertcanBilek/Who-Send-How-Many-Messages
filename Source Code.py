import time

print("""******************************************************************************************
*  Who Send How Many Messages in Whatsapp                                                  *
*                                                                                          *
*  How Does It Work                                                                        *
*                                                                                          *
*  1- Download Your Whatsapp Chat Back Up                                                  *
*  2- Enter the Path of Your File                                                          *
*  3- And Run Me                                                                           *
*                                                                                          *
*  In this way you can see who send how many messages in whatsapp groups or private chat.  *
******************************************************************************************
""")

time.sleep(2)


path = input("Enter Your Path Please :)\n")
def message_counter():
    line = ""
    dict1 = {}
    name = ""
    try:
        with open(path, "r+", encoding="utf-8") as file:
            for i in file:
                line += i
            for main_line in line.split("\n"):
                name = ""
                first_colon = main_line.find(":")
                second_colon = main_line[first_colon + 1:].find(":")
                end = (first_colon + second_colon + 1)
                start = main_line.find("-")
                if start > 0:
                    for letter in main_line[start + 2:end + 1]:
                        if letter != ":":
                            name += letter
                        else:
                            if name not in dict1:
                                dict1[name] = 0
                                dict1[name] += 1
                            else:
                                dict1[name] += 1
                            break

    except:
        if IndexError:
            pass
        if FileNotFoundError:
            print("The system cannot find the file, please check \nand try again...")

    for item in dict1:
        print("{} : {}".format(item, dict1[item]))
    quit = input("Press any button to quit")

    

message_counter()
