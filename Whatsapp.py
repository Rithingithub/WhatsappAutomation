
import pywhatkit

print("""

 ________ __           __                            _______         __                         __   __              
|  |  |  |  |--.---.-.|  |_.-----.---.-.-----.-----.|   _   |.--.--.|  |_.-----.--------.---.-.|  |_|__|.-----.-----.
|  |  |  |     |  _  ||   _|__ --|  _  |  _  |  _  ||       ||  |  ||   _|  _  |        |  _  ||   _|  ||  _  |     |
|________|__|__|___._||____|_____|___._|   __|   __||___|___||_____||____|_____|__|__|__|___._||____|__||_____|__|__|
                                       |__|  |__|                                                                    


""")


class WTPythonSwitch:
    def msg(self, Automation):
        default = "Error !"

        return getattr(self, 'case_' + str(Automation), lambda: default)()

    def case_1(self):
        a = input('Enter number with country code : ')
        b = input('Enter message : ')
        c = input('Hour :')
        d = input('Minute : ')
        return pywhatkit.sendwhatmsg(a, b, int(c), int(d), True, 2)

    def case_2(self):
        e = input('Enter number with country code : ')
        f = input('Enter image file location : ')
        return pywhatkit.sendwhats_image(e, f)

    def case_3(self):
        g = input('Enter group name : ')
        h = input('Image file location : ')
        i = input('Enter caption : ')
        return pywhatkit.sendwhats_image(g, h, i)

    def case_4(self):
        j = input('Enter whatsapp group name : ')
        k = input('Enter message : ')
        l = input('Enter Hour : ')
        m = input('Enter minute : ')
        return pywhatkit.sendwhatmsg_to_group(j, k, int(l), int(m))

    def case_5(self):
        n = input('Enter the group name : ')
        o = input('Enter message : ')
        return pywhatkit.sendwhatmsg_to_group_instantly(n, o)

    def case_6(self):
        return exit(0)



what_switch = WTPythonSwitch()

print("1. Send message to number\n"
      "2. Send image to a number\n"
      "3. Send image to group\n"
      "4. Send message to group\n"
      "5. Send instant message to group\n"
      "6. Exit")
z = input(print('Choose the number : '))
print(what_switch.msg(z))

