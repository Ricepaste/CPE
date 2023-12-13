
first_double = True

while True:
    try:
        temp = input()
        sent_output = ""
        for i in temp:
            if (i == "\""):
                if (first_double):
                    sent_output += "``"
                    first_double = False
                else:
                    sent_output += "''"
                    first_double = True
            else:
                sent_output += i
        print(sent_output)
    except:
        break
