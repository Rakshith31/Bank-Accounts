import sys
import random
import datetime
import mysql.connector
con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
cursor = con.cursor()
time = datetime.date.today()
print(time)
class transaction:
    transactionId=None
    def depositAmount(self,customerID,depositAmt):
        transactionId=random.randint(100000000,999999999);
        trans_type = "Deposit"
        tr_date=datetime.date.today()
        credit=depositAmt
        debit=0;
        con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
        cursor = con.cursor()
        amt = cursor.execute ("select customerAccountType from customer where customerID = %s"%(tempAccNo))
        row = cursor.fetchone()
        if(row[0] == "Savings"):
            con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
            cursor = con.cursor()
            trans = cursor.execute ("select customerID from transaction where customerID = %s"%(tempAccNo))
            trans1 = cursor.fetchall()
            transCount = len(trans1)
            if(transCount > 10):
                print("transaction limit reached/tryAgain next month")
            else :
                con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
                cursor = con.cursor()
                insDepo = "insert into transaction values (%s, %s, '%s', '%s', %s, %s)"\
                            %(customerID, transactionId, trans_type, tr_date, credit, debit)
                cursor.execute(insDepo)
                con.commit()
                print("Deposit successfull")
                con.close()

                con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
            cursor = con.cursor()

            cursor.execute("update customer set customerMinBalance = customerMinBalance + %s  where customerID = %s"\
                                                            %(credit,customerID))
            con.commit()
            con.close()

        elif(row[0] == "Current"):
            con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
            cursor = con.cursor()
            insDepo = "insert into transaction values (%s, %s, '%s', '%s', %s, %s)"\
                            %(customerID, transactionId, trans_type, tr_date, credit, debit)
            cursor.execute(insDepo)
            con.commit()
            print("Deposit successfull")
            con.close()

            con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
            cursor = con.cursor()

            cursor.execute("update customer set customerMinBalance = customerMinBalance + %s  where customerID = %s"\
                                                            %(credit,customerID))
            con.commit()
            con.close()
        
    def withdrawAmount(self,customerID,withdrawAmount):
        transactionId=random.randint(100000000,999999999);
        trans_type = "Withdraw"
        tr_date=datetime.date.today()
        credit=0
        debit=withdrawAmount;
        con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
        cursor = con.cursor()
        amt = cursor.execute ("select customerAccountType from customer where customerID = %s"%(tempAccNo))
        row = cursor.fetchone()
        if(row[0] == "Savings"):
            con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
            cursor = con.cursor()
            trans = cursor.execute ("select customerID from transaction where trans_type = '%s'"%(trans_type))
            trans1 = cursor.fetchall()
            transCount = len(trans1)
            if(transCount > 10):
                print("Withdrawal limit reached/tryAgain next month")
            else :
                con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
                cursor = con.cursor()
                rez1="select customerMinBalance from customer where customerID=%s"%(tempAccNo)
                rez2=cursor.execute(rez1)
                rez3=cursor.fetchone()
                if(float(tempWithdrawAmount) >= rez3[0]):
                        print("No enough money...")
                       
                else:
                    con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
                    cursor = con.cursor()
                    insDepo = "insert into transaction values (%s, %s, '%s', '%s', %s, %s)"\
                            %(customerID, transactionId, trans_type, tr_date, credit, debit)
                    cursor.execute(insDepo)
                    con.commit()
                    print("Withdrawal successfull")
                    con.close()

                    con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
                    cursor = con.cursor()

                    cursor.execute("update customer set customerMinBalance = customerMinBalance - %s  where customerID = %s"\
                                                                    %(debit,customerID))
                    con.commit()
                    con.close()

        elif(row[0] == "Current"):
            con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
            cursor = con.cursor()
            check = "select customerMinBalance from customer where customerID = %s"%(customerID)
            cursor.execute(check)
            minBal = cursor.fetchone()
            if(minBal[0]  >= 5000):
                con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
                cursor = con.cursor()
                insDepo = "insert into transaction values (%s, %s, '%s', '%s', %s, %s)"\
                            %(customerID, transactionId, trans_type, tr_date, credit, debit)
                cursor.execute(insDepo)
                con.commit()
                print("Withdrawal successfull")
                con.close()
            else:
                print("No enough balance..")

            con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
            cursor = con.cursor()

            cursor.execute("update customer set customerMinBalance = customerMinBalance - %s  where customerID = %s"\
                                                            %(debit,customerID))
            con.commit()
            con.close()
        
    def  transferAmount(self,customerID,transferAmount,receiverID):
        transactionId=random.randint(100000000,999999999);
        trans_type = "Transfer"
        tr_date=datetime.date.today()
        con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
        cursor = con.cursor()
        amt = cursor.execute ("select customerAccountType from customer where customerID = %s"%(tempAccNo))
        row = cursor.fetchone()
        if(row[0] == "Savings"):
            con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
            cursor = con.cursor()
            trans = cursor.execute ("select customerID from transaction where trans_type = '%s'"%(trans_type))
            trans1 = cursor.fetchall()
            transCount = len(trans1)
            mini = cursor.execute("select customerMinBalance from customer where customerID = %s"%(customerID))
            minBal=cursor.fetchone()
            if(transCount > 10 and minBal[0] == 0):
                print("Withdrawal limit reached/tryAgain next month")
            else :
                    con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
                    cursor = con.cursor()
                    debit = transferAmount
                    credit = 0
                    instransf1 = "insert into transaction values (%s, %s, '%s', '%s', %s, %s)"\
                            %(customerID, transactionId, trans_type, tr_date, credit, debit)
                    cursor.execute(instransf1)
                    con.commit()
                    debit = 0
                    credit = transferAmount
                    instransf2 = "insert into transaction values (%s, %s, '%s', '%s', %s, %s)"\
                            %(receiverID, transactionId, trans_type, tr_date, credit, debit)
                    cursor.execute(instransf2)
                    con.commit()
                    print("Transfer successfull")
                    con.close()

                    con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
                    cursor = con.cursor()

                    cursor.execute("update customer set customerMinBalance = customerMinBalance - %s  where customerID = %s"\
                                                                    %(transferAmount,customerID))
                    cursor.execute("update customer set customerMinBalance = customerMinBalance + %s  where customerID = %s"\
                                                                    %(transferAmount,receiverID))
                    con.commit()
                    con.close()

        elif(row[0] == "Current"):
            con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
            cursor = con.cursor()
            check = "select customerMinBalance from customer where customerID = %s"%(customerID)
            cursor.execute(check)
            minBal = cursor.fetchone()
            if(minBal[0]  >= 5000):
                con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
                cursor = con.cursor()
                debit = transferAmount
                credit = 0
                instransf1 = "insert into transaction values (%s, %s, '%s', '%s', %s, %s)"\
                            %(customerID, transactionId, trans_type, tr_date, credit, debit)
                cursor.execute(instransf1)
                con.commit()
                debit = 0
                credit = transferAmount
                instransf2 = "insert into transaction values (%s, %s, '%s', '%s', %s, %s)"\
                            %(receiverID, transactionId, trans_type, tr_date, credit, debit)
                cursor.execute(instransf2)
                con.commit()
                print("Transfer successfull")
                con.close()

                con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
                cursor = con.cursor()

                cursor.execute("update customer set customerMinBalance = customerMinBalance - %s  where customerID = %s"\
                                                            %(debit,customerID))
                cursor.execute("update customer set customerMinBalance = customerMinBalance + %s  where customerID = %s"\
                                                            %(credit,receiverID))
                con.commit()
                con.close()
            else:
                    print("No enough balance...")



    
        


class Customer:
    customerID=None        #auto generate 5 digit
    customerFirstName=None
    customerLastName=None
    customerCity=None
    customerDistrict=None
    customerState=None
    customerCountry=None
    customerAddressL1=None
    customerAddressL2=None
    customerPincode=None  
    customerPassword=None
    customerAccountType=None
    customerAccountIsClosed=None
    customerMinBalance=None
    balance=None
    def __init__(self,customerID,
                customerFirstName,
                customerLastName,
                customerCity,
                customerDistrict,
                customerState,
                customerCountry,
                customerAddressL1,
                customerAddressL2,
                customerPincode,
                customerPassword,
                customerAccountType,
                customerAccountIsClosed,
                customerMinBalance,
                balance):
        self.customerID=customerID
        self.customerFirstName=customerFirstName
        self.customerLastName=customerLastName
        self.customerCity=customerCity
        self.customerDistrict=customerDistrict
        self.customerState=customerState
        self.customerCountry=customerCountry
        self.customerAddressL1=customerAddressL1
        self.customerAddressL2=customerAddressL2
        self.customerPincode=customerPincode
        self.customerPassword=customerPassword
        self.customerAccountType=customerAccountType
        self.customerAccountIsClosed=customerAccountIsClosed
        self.customerMinBalance=customerMinBalance
        self.balance=balance

def pinInput():
    flag=1
    while flag==1:
        number = input()
        if len(number)==6:
            try:
                number=int(number)
                flag=0
            except:
                print ("You must enter valid input try again")
                sys.exit()
            finally:
                return number
        else :
            print("enter 6 digit number")

quit=False


depo = transaction()
while(quit==False):
    print("Main Menu")
    print("1)Sign Up \n2)Sign in\n3)Admin Sign In\n4)Quit\nEnter your choice")
    option=input()

    
    
    if option==1:
        while True:
            passWordLengthFlag=True
            print(" >--Sign Up-->")
            customerID=random.randint(100000000,999999999)
            ##print("Enter password(minimum 8 charecter/digit)")
            while passWordLengthFlag:
                customerPassword=raw_input("Enter password(minimum 8 charecter/digit):")
                if (len(customerPassword)>=8):
                    passWordLengthFlag=False
                else :
                    print("Enter minimun length atleast 8")
            print("SelectAccount type:\n1)Savings\n2)Current(more than or 5000)")
            while True:
                selectAccountType=input()
                if(selectAccountType== 1 ):
                    customerAccountType="Savings"
                    break
                elif(selectAccountType== 2 ):
                    customerAccountType="Current"
                    break
                else:
                    print("select valid option")
            print("Enter minimum amount to deposit ")
            while True:
                if customerAccountType=="Savings":
                    customerMinBalance=int(input())
                    break;
                elif customerAccountType=="Current":
                    customerMinBalance=int(input())
                    if customerMinBalance>=5000:
                        break
                    else :
                        print("Minimum balance must be greater than 5000")
            customerFirstName=raw_input(" Enter FirstName:")
            customerLastName=raw_input(" Enter LastName:")
            customerAddressL1=raw_input(" Enter Address Line 1:")
            customerAddressL2=raw_input(" Enter Address Line 2:")
            customerCity=raw_input("Enter city:")
            customerDistrict=raw_input("Enter District:")
            customerState=raw_input("Enter State:")
            customerCountry=raw_input("Enter country:")
            customerPincode=raw_input("Enter Pincode:")
            customerAccountIsClosed=0
            balance=customerMinBalance
            newCustomer=Customer(customerID,
                                customerFirstName,
                                customerLastName,
                                customerCity,
                                customerDistrict,
                                customerState,
                                customerCountry,
                                customerAddressL1,
                                customerAddressL2,
                                customerPincode,
                                customerPassword,
                                customerAccountType,
                                customerAccountIsClosed,
                                customerMinBalance,
                                balance)
            ins = "insert into customer values(%s,'%s','%s','%s','%s','%s','%s','%s','%s',%s,'%s','%s',%s,'%s')"\
                    %(customerID,customerFirstName,customerLastName,customerAddressL1,customerAddressL2,customerCity,customerDistrict,\
                    customerState,customerCountry,customerPincode,customerAccountType,customerPassword,customerMinBalance,customerAccountIsClosed)
            cursor.execute(ins)
            con.commit()
            det1 = "select customerID from customer where customerID=%s"%(customerID)
            det11=cursor.execute(det1)
            det111=cursor.fetchone()
            acno=int(det111[0])
            det2 = "select customerAccountType from customer where customerID=%s"%(customerID)
            det12=cursor.execute(det2)
            det222=cursor.fetchone()
            acty=str(det222[0])
            det3 = "select customerMinBalance from customer where customerID=%s"%(customerID)
            det13=cursor.execute(det3)
            det333=cursor.fetchone()
            acmi=int(det333[0])
            print('You have been successfully signed up...')
            print("Account number:%s")%(acno)
            print("Account type:%s")%(acty)
            print("Account balance:%s")%(acmi)
            
            con.close()
            break;
        
    elif option==2:
        print(">--Sign In-->")
        l=0;
        while True:
            if l==1:
                    break;
            l=0;
            flagS = 0
            print("  Enter account number:")
            tempAccNo=input()
            con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
            cursor = con.cursor()
            rez = "select customerAccountIsClosed from customer where customerID = %s"%(tempAccNo)
            res = cursor.execute(rez)
            resu = cursor.fetchone()
            comp = '1'
            if(resu[0] == comp):
                print("Account is closed...")
                break;
            else:
                con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
                cursor = con.cursor()
                custName = ("select customerID from customer")
                result = cursor.execute(custName)
                row = cursor.fetchall()
                l = len(row)
                if any(tempAccNo in row[i] for i in range(0,l)):
                    wrongCount=0
                    while True:
                        if l==1:
                               break;
                        l=0;
                        tempPassWord=raw_input("Enter password:")
                       
                        custPass = ("select customerPassword from customer where customerID=%s")%(tempAccNo)
                        result = cursor.execute(custPass)
                        row = cursor.fetchone()
                        h = len(row)
                        if (tempPassWord == row[0]) :
                            accountTypeFlag=None;
                            print("  --Login Successfull--")
                            while True:
                                    
                                    if l==1:
                                         break;
                                    l=0;
                                    flagS=1
                                    
                                    while True:
                                        print("    Select operation:\n    1)Address change\n    2)Money Deposit\n    3)Money Withdrawal\n    4)Print Statment\n    5)TransferMoney\n    6)CloseAccount\n    7)Customer Logout")
                                        subMenueSlect=input()
                                        if subMenueSlect==1:
                                            print("Enter New Address")
                                            customerAddressL1=raw_input(" Enter Address Line 1:")
                                            customerAddressL2=raw_input(" Enter Address Line 2:")
                                            customerCity=raw_input("Enter city:")
                                            customerDistrict=raw_input("Enter District:")
                                            customerState=raw_input("Enter State:")
                                            customerCountry=raw_input("Enter country:")
                                            customerPincode=raw_input("Enter Pincode:")
                                            con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
                                            cursor = con.cursor()
                                            address = ("update customer set customerAddressL1 = '%s',customerAddressL2 = '%s',customerCity = '%s',customerDistrict = '%s',\
                                                        customerState = '%s',customerCountry = '%s',customerPincode = %s where customerID=%s"\
                                                       %(customerAddressL1,customerAddressL2,customerCity,customerDistrict,customerState,customerCountry,customerPincode,tempAccNo))
                                            cursor.execute(address)
                                            con.commit()
                                            print("Address updated...")
                                            con.close()
                                            break;
                                        elif subMenueSlect==2:
                                                print("Money Deposit>>")
                                                tempDepositAmount=raw_input("Enter The Amount:")
                                                depo.depositAmount(tempAccNo, tempDepositAmount)
                                                break;
                                            
                                        elif subMenueSlect==3:
                                                print("Money Withdrawal>>")
                                                tempWithdrawAmount=raw_input("Enter The Amount:")
                                                depo.withdrawAmount(tempAccNo, tempWithdrawAmount)
                                                break;
                                        elif subMenueSlect==4:
                                            print("--Transaction history--")
                                            print("Enter the start date(""YYYY-MM-DD""):")
                                            sdate=input()
                                            print("Enter the end date(""YYYY-MM-DD""):")
                                            edate=input()
                                            print("customer ID \t Transaction ID \t Transaction Type \t Date \t Credit \t Debit")
                                            top = ("select * from transaction where customerID = %s and tr_date between '%s' and '%s'"%(tempAccNo,sdate,edate))
                                            result = cursor.execute(top)
                                            row = cursor.fetchall()
                                            for i in row:
                                                print('%s'+"\t"+'%s'+"\t\t"+'%s'+"\t\t"+'%s'+"\t"+'%s'+"\t"+'%s')%(str(i[0]),str(i[1]),str(i[2]),str(i[3]),str(i[4]),str(i[5]))
                                            break;
                                        elif subMenueSlect==5:
                                            print("Enter the Customer ID you want to send money")
                                            tempRecieverID=input()
                                            if(tempAccNo == tempRecieverID):
                                                print("Not possible to transfer to same account number..")
                                                break;
                                            else:
                                                print("Enter the amount")
                                                tempAmount=input()
                                                con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
                                                cursor = con.cursor()
                                                rez1="select customerMinBalance from customer where customerID=%s"%(tempAccNo)
                                                rez2=cursor.execute(rez1)
                                                rez3=cursor.fetchone()
                                                if(float(tempAmount)>=rez3[0]):
                                                    print("No enough money...")
                                                    break
                                                else:
                                                    depo.transferAmount(tempAccNo,tempAmount,tempRecieverID)
                                                    break;
                                        elif subMenueSlect==6:
                                                print("are you sure..?? enter 1 to accept and 0 to decline")
                                                tempAccCloseChoice=input()
                                                if tempAccCloseChoice==1:
                                                    
                                                    con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',
                                                    database='test1')
                                                    cursor = con.cursor()
                                                    customerAccountIsClosed=1
                                                    result = cursor.execute("select customerAccountIsClosed from customer where  customerID = %s"%(tempAccNo))
                                                    row = cursor.fetchone()
                                                    print(row[0])
                                                    if(row[0] == '0'):
                                                        cursor.execute("update customer set customerAccountIsClosed = '%s'  where customerID = %s"\
                                                                        %(tempAccCloseChoice,tempAccNo))
                                                        con.commit()
                                                        print("Your account has been closed")
                                                    else:
                                                        print("Your account is already closed")
                                                break;
                                        elif subMenueSlect==7:
                                            if flagS==1:
                                                flagS=0
                                                l=1;
                                                print("Logged Off")
                                                break;
                                                con.close()

                        else :
                                 wrongCount=wrongCount+1
                                 print("Password is wrong enter again")
                                 if wrongCount>=3 :
                                     print("All attempts done....")
                                     sys.exit()
                else :
                    print("user Id not available try again");                     
                     
    elif option==3:     
        print(">--Admin Sign In-->>")
        con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',
                              database='test1')
        cursor = con.cursor()
        print("Enter the id:")
        tempAdminId=input()
        tempAdminPassword=raw_input("Enter the password:")
        while True:
            name = ("select admin_id from admins")
            result = cursor.execute(name)
            row = cursor.fetchone()
            if(row[0]== tempAdminId):
                passwrd = ("select admin_passwd from admins")
                password = cursor.execute(passwrd)
                row1 = cursor.fetchone()
                if(row1[0] == tempAdminPassword):##compare with original password from db
                    print("--Login Successfull--")
                while True:
                    print("setect the operation:-\n1)closed account details\n2)Logout ")
                    adminChoice=input()
                    if adminChoice==1:
                        print("closed account details:")
                        con = mysql.connector.connect(user='root',password='#I@mshreyas1997',host='127.0.0.1',database='test1')
                        cursor = con.cursor()
                        result=cursor.execute("select customerID,customerFirstName,customerLastName,customerAddressL1,customerAddressL2,customerCity,customerDistrict,\
                customerState,customerCountry,customerPincode,customerAccountType,customerPassword,customerMinBalance from customer where customerAccountIsClosed='1';")
                        row=cursor.fetchall()
                        for i in row:
                            print('%s'+"\t"+'%s'+"\t"+'%s'+"\t"+'%s'+"\t"+'%s'+"\t"+'%s'+"\t"+'%s'+"\t"+'%s'+"\t"+'%s'+"\t"+'%s'+"\t"+'%s'+"\t"+'%s'+"\t"+'%s')%(str(i[0]),str(i[1]),str(i[2]),str(i[3]),str(i[4]),str(i[5]),str(i[6]),str(i[7]),str(i[8]),str(i[9]),str(i[10]),str(i[11]),str(i[12]))
                    elif adminChoice==2:
                        print("thank you")
                        sys.exit()
                    else :
                        print("wrong choice")

            else :
                wrongCount=wrongCount+1
                if wrongCount>3:
                    print("Try again")
                    sys.exit()
        sys.exit();
        con.close()
    elif option==4:
        print("<<<----------Thank you---------->>>");
        sys.exit();
    else:
        print("----Wrong choice try again---")
        sys.exit()
            
        
        
