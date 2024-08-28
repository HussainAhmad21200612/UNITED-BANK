import os
import math
import random
import smtplib 
import time
from colorama.ansi import Back, Style
from colorama.initialise import reset_all
from prettytable import PrettyTable
from plyer import notification
from emoji import emojize
import colorama
info_table=PrettyTable()
passbook_table=PrettyTable()
info_table.field_names=["ACCOUNT NUMBER","NAME OF CUSTOMER","ADHAR NUMBER","EMAIL ID","BALANCE (Rs.)"]
NamesOFClients = []
ClientPins = []
AdminId=["HUSSAIN_77","HARDIK_68","DEVANSH_59","DEV_58"]
AdminNames=['HUSSAIN AHMAD', 'HARDIK AGRAWAL', 'DEVANSH TRIPATHI', 'DEV SIKKA']
ClientBalances = []
ClientEmail=[]
ClientAcctNo=[]
ClientAdharNo=[]
ClientDeposition = 0
ClientWithdrawal = 0
ClientBalance = 0
u = 0
passbook_table.field_names=["DAY MONTH DATE TIME(IST) YEAR: EVENT","TOTAL BALANCE (Rs.)"]
def notify_msg(msg):
    notification.notify(title="BANK OF UNITED",message=f"{time.asctime((time.localtime()))}\n{msg}",app_name="Bank Of United",timeout=30)
def write_details(file_name,message):
    with open(f"{file_name}","a") as f:
        f.write(f"{time.asctime(time.localtime())}: {message}")
        f.close()
def read_details(file_name):
    ClientPassBook=[]
    passbook_table.clear_rows()
    with open(f"{file_name}.txt","r") as f:
        line=f.readlines()
        for l in line:
            ClientPassBook.append(l.strip())
    f.close()
    for j in range(0,len(ClientPassBook)-1,2):
        passbook_table.add_row([f"{ClientPassBook[j]}",f"{ClientPassBook[j+1]}"])
    passbook_table.align["TOTAL BALANCE (Rs.)"]="l"
    passbook_table.align["DAY MONTH DATE TIME(IST) YEAR: EVENT"]="l"
def one_time_p(emailid,n):
    digits="0123456789"
    OTP=""
    if n>0:
        for i in range(6):
            OTP+=digits[math.floor(random.random()*10)]
        otp = OTP + " is your OTP"
        msg= otp
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("hussain21200612@gmail.com", "ugxbtpcqapqbrlih")
            s.sendmail('',emailid,msg)
            a = input("Enter Your OTP >>: ")
            if (a==OTP and n==1) :
                return True
            elif (a==OTP and n>1):
                print("\n EMAIL ID VERIFIED")
                return True 
            elif (a!=OTP and n>1):
                print("invalid otp")
                print(f"{n-1} attempts left")
                choice_otp=str(input("PRESS R for retry and E for exit : "))
                if(choice_otp=='R'):
                    one_time_p(emailid,n-1)
                else:
                    return False
            else:
                return False
        except:
            print(" INVALID Email Address Or Check Your Internet Connection ")
            return False
    else:
        print("no of attempts exceeded")
        return False
with open("Name_of_Clients.txt","r") as file:
    l=file.readlines()
    for line in l:
        NamesOFClients.append(line.strip())
with open("Acc_no.txt","r") as f:
    l=f.readlines()
    for line in l:
        ClientAcctNo.append(int(line.strip()))
with open("Client_pins.txt","r") as pins:
    l=pins.readlines()
    for line in l:
        ClientPins.append(line.strip())
with open("Email_id.txt","r") as email:
    l=email.readlines()
    for line in l:
        ClientEmail.append(line.strip())
with open("Client_balance.txt","r") as balance:
    l=balance.readlines()
    for line in l:
        ClientBalances.append(float(line.strip()))
with open("Client_adhar.txt","r") as adhar:
    l=adhar.readlines()
    for line in l:
        for i in range(0,len(line)):
            if (i+1)%4==0:
                ClientAdharNo.append(f"{line.strip()} ")
            ClientAdharNo.append(line.strip())
file.close()
f.close()
pins.close()
email.close()
balance.close()
adhar.close()
for i in range(0,len(NamesOFClients)):
    info_table.add_row([f"{ClientAcctNo[i]}",f"{NamesOFClients[i]}",f"{ClientAdharNo[i]}",f"{ClientEmail[i]}",f"{ClientBalances[i]}"])
info_table.align["ADHAR NUMBER"]="l"
info_table.align["NAME OF CUSTOMER"]="l"


info_table.align["EMAIL ID"]="l"
disk2=len(ClientAcctNo)
u=disk2
os.system("cls")
while True:
    os.system("cls")
    print(colorama.Fore.LIGHTMAGENTA_EX)
    print("$**********************************************************$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(colorama.Fore.LIGHTWHITE_EX)
    print("$**********************************************************$")
    print("$==========     WELCOME TO BANK OF UNITED ",emojize(":bank:"),"  ===========$")
    print("$**********************************************************$")
    print("$=========    (a). ADMIN MODE                   ===========$")
    print("$=========    (u). USER MODE                    ===========$")
    print("$**********************************************************$")
    print(colorama.Fore.LIGHTMAGENTA_EX)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$**********************************************************$")
    print(colorama.Style.RESET_ALL)
    select_choice=input("ENTER MODE OPTION YOU WANT TO ACCESS : ").lower()
    if select_choice=="a":
        input_id=input("ENTER YOUR ADMIN ID : ")
        w=-1
        for i in AdminId:
            w=w+1
            if input_id == i:
                print("\n")
                print(colorama.Fore.GREEN)
                print("$**********************************************************$")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print(colorama.Style.RESET_ALL)
                print(f"*********** WELCOME TO ADMIN MODE {AdminNames[w]} ************")
                print("$**********************************************************$")
                print("$=========  PRESS b for Checking Clients & Balance  =======$")
                print("$=========  PRESS q to Quit                         =======$")
                print(colorama.Fore.GREEN)
                print("$**********************************************************$")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print(colorama.Style.RESET_ALL)
                select_ch = input("ENTER YOUR CHOICE : ").lower()
                if select_ch == "b":
                    print("Letter b is selected by the admin")
                    print("Client account number , name list ,email id and balances mentioned below : ")
                    print("\n")
                    print("\n")
                    print(colorama.Fore.MAGENTA)
                    print("***********************************************************************************")
                    print("***********************************************************************************")
                    print("***********************************************************************************")
                    info_table.del_column("BALANCE (Rs.)")
                    info_table.add_column("BALANCE (Rs.)",ClientBalances)
                    print(colorama.Fore.LIGHTWHITE_EX)
                    print(info_table.get_string(title="BANK OF UNITED",border=True))
                    print(colorama.Fore.MAGENTA)
                    print("***********************************************************************************")
                    print("***********************************************************************************")
                    print("***********************************************************************************")
                    print(colorama.Style.RESET_ALL)
                    print("\n")
                    print("\n")
                    break
                elif select_ch == "q":
                    print("letter q is selected by the admin")
                    print("\n")
                    break
                else:
                    print("Invalid option selected by the admin")
                    print("Please Try again!")
                    break
        else:
            print(" INVALID USER ID")

        mainMenu = input("Press Enter Key to go Back to Main Menu to Conduct Another operation or Quit_")
        os.system('cls')
    elif select_choice=='u':
        print(colorama.Fore.LIGHTMAGENTA_EX)
        print("$**********************************************************$")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(colorama.Fore.LIGHTWHITE_EX)
        print("$==========     WELCOME TO  USER  MODE          ===========$")
        print("$**********************************************************$")
        print("$=========    (o). Open New Client Account      ===========$")
        print("$=========    (b). Check Client Balance         ===========$")
        print("$=========    (w). The Client Withdraw a Money  ===========$")
        print("$=========    (d). The Client Deposit a Money   ===========$")
        print("$=========    (p). Print your passbook          ===========$")
        print("$=========    (q). Quit                         ===========$")
        print(colorama.Fore.LIGHTMAGENTA_EX)
        print("$**********************************************************$")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(colorama.Style.RESET_ALL)
        EnterLetter = input("Select a Letter from the Above Box menu : ").lower()
        if EnterLetter == "o":
            print(" Letter o is Selected by the Client")
            NumberOfClient = int(input("Number of Clients : "))
            disk1=0
            u = u + NumberOfClient
            while disk1 < NumberOfClient:
                disk1 = disk1 + 1
                name = input("Write Your Fullname : ").upper()
                adhar_no=input("ENTER 12 DIGIT ADHAR NUMBER without ANY SPACES: ")
                if len(adhar_no)==12:
                    if adhar_no not in ClientAdharNo:
                        email = str(input("Enter your emailID for verification : "))
                        print(colorama.Fore.RED)
                        print("\nEmail verification started stay put  ",emojize(":fast-forward_button:"),emojize(":fast-forward_button:"),emojize(":fast-forward_button:"),colorama.Style.RESET_ALL)
                        if one_time_p(email,3):
                            NamesOFClients.append(name)
                            ClientDeposition = float(input("Please Insert a Money to Deposit to Start an Account : "))                        
                            ClientBalances.append(ClientDeposition)
                            ClientEmail.append(email)
                            while (True):
                                Acc_no = random.randint(2000100100000, 9999999999999)
                                if Acc_no not in ClientAcctNo:
                                    break 
                            pin = str(input("Please Write a Pin to Secure your Account : "))
                            ClientPins.append(pin)
                            print(colorama.Fore.RED)
                            ClientAcctNo.append(Acc_no)
                            print("\nName=", end=" ")
                            print(NamesOFClients[disk2])
                            print("Balance=", "Rs.", end=" ")
                            print(ClientBalances[disk2], end=" ")
                            print("Account Number =",end=" ")
                            print(ClientAcctNo[disk2], end=" ")
                            print(colorama.Style.RESET_ALL)
                            ClientAdharNo.append(adhar_no)
                            f = open(f"{name}{Acc_no}.txt", "x")
                            f.close()
                            notify_msg("SUCCESSFULLY CREATED")
                            print(ClientAcctNo,disk1,disk2)
                            info_table.add_row([f"{ClientAcctNo[disk2]}",f"{NamesOFClients[disk2]}",f"{ClientAdharNo[disk2]}",f"{ClientEmail[disk2]}",f"{ClientBalances[disk2]}"])
                            write_details(f"{NamesOFClients[disk2]}{ClientAcctNo[disk2]}.txt",f"ACCOUNT OPENED SUCCESSFULLY\nTOTAL BALANCE = Rs.{ClientBalances[disk2]}\n")
                            f=open("Name_of_Clients.txt","a")

                            f.write(f"{name}\n")
                            f.close()
                            f=open("Email_id.txt","a")
                            f.write(f"{email}\n")
                            f.close()
                            f=open("Client_pins.txt","a")
                            f.write(f"{pin}\n")
                            f.close()
                            f=open("Acc_no.txt","a")
                            f.write(f"{str(Acc_no)}\n")
                            f.close()
                            f=open("Client_adhar.txt","a")
                            f.write(f"{adhar_no}")
                            f.close()
                            f=open("Client_balance.txt","w")
                            for i in ClientBalances:
                                f.write(f"{str(i)}\n")
                            f.close()
                            disk2 = disk2 + 1
                        else:
                            print("\n")
                            pass
                    else:
                        print("CUSTOMER OF THIS ADHAR NUMBER  ALREADY EXISTS IN THIS BANK")
                        pass
                else:
                    print("INVALID ADHAR NUMBER ")
                    pass
            mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
            os.system('cls')
        elif EnterLetter == "w":
                v = 0
                print(" letter w is Selected by the Client ",emojize(":ATM_sign:"),"\n")
                while v < 1:
                    w = -1
                    name = input("Please Insert a name : ").upper()
                    pin = input("Please Insert a pin : ")
                    while w < len(NamesOFClients) - 1:
                        w = w + 1
                        if name == NamesOFClients[w]:
                            if pin == ClientPins[w]:
                                v = v + 1
                                print("Your Current Balance:", "Rs.", end=" ")
                                print(ClientBalances[w], end=" ")
                                print("\n")
                                ClientBalance = ClientBalances[w]
                                ClientWithdrawal = float(input("Insert value to Withdraw : "))
                                if ClientWithdrawal > ClientBalance:
                                    notify_msg("Transaction Failed Not Enough Balance")
                                    # nn=11
                                else:
                                    print(colorama.Fore.RED)
                                    print("\nEmail verification started stay put  ",emojize(":fast-forward_button:"),emojize(":fast-forward_button:"),emojize(":fast-forward_button:"),colorama.Style.RESET_ALL)
                                    print("\n")
                                    if one_time_p(ClientEmail[w],1):
                                        ClientBalance = ClientBalance - ClientWithdrawal
                                        print("-\n")
                                        ClientBalances[w] = ClientBalance
                                        notify_msg(f"----Withdraw Successfully!----\nCurrent Balance: Rs.{ClientBalance}")
                                        write_details(f"{NamesOFClients[w]}{ClientAcctNo[w]}.txt",f" Rs.{ClientWithdrawal}  Withdraw Successfully\nTOTAL BALANCE = Rs.{ClientBalance}\n")
                                        print("\n\n")
                                        f=open("Client_balance.txt","w")
                                        for i in ClientBalances:
                                            f.write(f"{str(i)}\n")
                                        f.close()
                                    else:
                                        print(colorama.Fore.RED)
                                        print("\n TRANSACTION FAILED")
                                        print(colorama.Style.RESET_ALL)
                    if v < 1:
                        print("Your name and pin does not match!\n")

                        break
                mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
                os.system('cls')
        elif EnterLetter=="b":
            print("Letter b selected\n")
            acc_no=int(input("ENTER your Account Number : "))
            if acc_no in ClientAcctNo:
                pin=input("ENTER your PIN : ")
                if pin in ClientPins:
                    x=ClientAcctNo.index(acc_no)
                    print("BALANCE : ",ClientBalances[x])
                else:
                    print("INVALID PIN\n")
                    pass
            else:
                print("INVALID ACCOUNT NUMBER\n")
                pass
            mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
            os.system('cls')
        elif EnterLetter == "d":
            print("Letter d is selected by the Client")
            x = 0
            while x < 1:
                w = -1
                account_no = int(input("Please Enter Your Account Number : "))
                account_no_again = int(input("Please Re-Enter Your Account Number : "))
                for i in ClientAcctNo:
                    w = w + 1
                    if account_no == i and account_no_again == i:
                            x = x + 1
                            print("Customer Name : ", NamesOFClients[w])
                            choice = input("Press C to confirm else E : ").upper()
                            if (choice == 'E'):
                                pass
                            else:
                                print("Your Current Balance: ", "Rs.", end=" ")
                                print(ClientBalances[w], end=" ")
                                ClientBalance = ClientBalances[w]
                                print("\n")
                                ClientDeposition = float(input("Enter the value you want to deposit : "))
                                ClientBalance = ClientBalance + ClientDeposition
                                ClientBalances[w] = ClientBalance
                                print("\n")
                                notify_msg(f"----Deposition successful!----\nYour New Balance: Rs.{ClientBalance}")
                                write_details(f"{NamesOFClients[w]}{ClientAcctNo[w]}.txt",f" Rs.{ClientDeposition}  DEPOSITED Successfully\nTOTAL BALANCE = Rs.{ClientBalance}\n")
                                print("\n")
                                f=open("Client_balance.txt","w")
                                for i in ClientBalances:
                                    f.write(f"{str(i)}\n")
                                f.close()
                if x==0:                
                    print("Account Number does not exist!\n")
                    break
            mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
            os.system('cls')

        elif EnterLetter == "p":
            print("Letter p is selected\n")
            acc_of=int(input("Enter your account number : "))
            w=-1
            x=0
            while w<len(ClientAcctNo)-1:
                w=w+1
                if ClientAcctNo[w] == acc_of:
                    x=x+1
                    read_details(f"{NamesOFClients[w]}{ClientAcctNo[w]}")
                    print(colorama.Fore.LIGHTRED_EX)
                    print(passbook_table.get_string(title=f"{NamesOFClients[w]}",border=True))
                    print(colorama.Style.RESET_ALL)
            if (x==0):
                print("CLIENT does not exists ")

            mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_ ")
            os.system('cls')

        elif EnterLetter == "q":
            print("letter q is selected by the client")
            print("\n\n")
            print(colorama.Fore.LIGHTRED_EX)
            print("Thank you for using our banking system!",emojize(":smiling_face_with_smiling_eyes:"))
            print("WEAR YOUR MASK",emojize(":face_with_medical_mask:")," AND GET VACCINATED ",emojize(":syringe:"),"    ")
            print("#WE_ARE_IN_THIS_TOGETHER",emojize(":folded_hands:"))
            print("BANK OF UNITED",emojize(":bank:"))
            print(colorama.Style.RESET_ALL)
            print("\n")
            break
        else:
            print("Invalid option selected by the Client")
            print("Please Try again!")
            mainMenu = input("Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
            os.system('cls')
    else:
        print("ENTER A VALID CHOICE ")
        mainMenu = input("Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
        os.system('cls')