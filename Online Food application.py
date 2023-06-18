l=[]
pre_food={1:'Asian food',2:'Chinese food',3:'Italy food'}
pre_pay_platform={1:'gpay'}
class user_profiles:
    print("Welcome to my app!!!!\n")
    def __init__(self,user_id,user_name,user_emailid,user_phno):      #Constractor
        self.user_id=user_id
        self.user_name=user_name
        self.user_emailid=user_emailid
        self.phno=user_phno
class login(user_profiles):      #single Inheritance
    def __init__(self,user_id,user_name,user_emailid,user_phno,user_password):
        self.password=user_password
        user_profiles.__init__(self,user_id,user_name,user_emailid,user_phno)
        l.append(self.user_emailid)
        l.append(user_password)
    def sign_in(self):
        email=input("Enter the email id: \t")
        l.append(email)
        password=input("Enter the password: \t")
        l.append(password)
        print("Successfully Sign in!\t")
    def check(self,password,user_email_id):
        for i in range(len(l)):
            if(l[i-1]==password and l[i]==self.user_emailid):
                print("Sussfull login!\t")
                break
            else:
                print("Please sign in with your email id and valid password!!\t")
                self.sign_in()
                break
class online_payment:
    def gpay(self):
        s='044-789-283'
        print('Please enter the name in your gpay : '+s+'\t')
        l=input('Once you finished click ok : \t')
        if(l=='ok'):
            print('Please enter your valid UPI pin \t')
            k=input('After Please click enter : \t')
            if(k=='enter'):
                print('Please pay '+self.to+'\t')
                self.f=int(input('Enter total payment : '))
                if(self.f==self.t):
                    print('Successfully payed\t')
                else:
                    print('Please pay correctly\t')
                    self.gpay()
            else:
                self.gpay()
        else:
            self.gpay()
class pay:
    def payment(self,l):
        if(l==1):
            s=self.f1.price
            print(s)
            q=int(input('Please enter how many biriyani to you want : \t'))
            r=self.f1.price[1:]
            self.t=q*int(r)
            self.to='$'+str(self.t)
        elif(l==2):
            s=self.f2.price
            print(s)
            q=int(input('Please enter how many biriyani to you want : \t'))
            r=self.f2.price[1:]
            self.t=q*int(r)
            self.to='$'+str(self.t)
        elif(l==3):
            s=self.f3.price
            print(s)
            q=int(input('Please enter how many biriyani to you want : \t'))
            r=self.f3.price[1:]
            self.t=q*int(r)
            self.to='$'+str(self.t)
        else:
            print('Not available food!!!\n Please enter valid food number : \t')
            self.p()
        a=input('If you sure for your select then press Yes : \t')
        if(a=='Yes'):
            print('Total amount is '+self.to+'\t')
            print('Please select prefer pay money !!!\t')
            print(pre_pay_platform)
            self.b=int(input())
            if(self.b==1):
                self.gpay()             
            else:
                print('Only transition pay to gpay !!!\t')
                self.b()
        
class food(pay,online_payment):
    def __init__(self,food_id=None,food_name=None,price=None,quantity=None):
        self.food_id=food_id
        self.food_name=food_name
        self.price=price
        self.quantity=quantity
    def choice(self):
        print(pre_food)
        sel_choice=int(input("Select your prefer food: \t"))
        if(sel_choice==1):
            self.f1=food(1,'Biriyani','$400')
            self.f2=food(2,'Paneer Dikka','$250')
            self.f3=food(3,'Idly','$10')
            print("Available Asian food are: \n")
            print(self.f1.food_id,':',self.f1.food_name,'\t')
            print(self.f2.food_id,':',self.f2.food_name,'\t')
            print(self.f3.food_id,':',self.f3.food_name,'\t')
            p=int(input("Select your prefer food : \t"))
            print('This food price is : \t')
            self.payment(p)      
        elif(sel_choice==2):
            self.f1=food(1,'Fried Rice','$600')
            self.f2=food(2,'Kung Pao Chicken','$900')
            self.f3=food(3,'Sweet and sour pork','$500')
            print("Available Chinese food are: \n")
            print(self.f1.food_id,':',self.f1.food_name,'\t')
            print(self.f2.food_id,':',self.f2.food_name,'\t')
            print(self.f3.food_id,':',self.f3.food_name,'\t')
            p=int(input("Select your prefer food : \t"))
            print('This food price is : \t')
            self.payment(p)
        elif(sel_choice==3):
            self.f1=food(1,'Pizza','$400')
            self.f2=food(2,'Risotto','$950')
            self.f3=food(3,'Pasta','$500')
            print("Available Asian food are: \t")
            print(self.f1.food_id,':',self.f1.food_name,'\t')
            print(self.f2.food_id,':',self.f2.food_name,'\t')
            print(self.f3.food_id,':',self.f3.food_name,'\t')
            p=int(input("Select your prefer food : \t"))
            print('This food price is : \t')
            self.payment(p)
class address:
    def valid_add(self):
        addr=input('Please enter current address: \t')
        p=input('Ones you finished click enter : \t')
        if(p=='enter'):
            print('Thank you\t')
            print('Please logout\t')
        else:
            self.valid_add()
if __name__=="__main__":
    l1=login(1,'priya','priya@gmail.com','8072649175','Priya*2003')
    l1.check('Priya*20033','priya@gmail.com')
    m1=food()
    m1.choice()
    a1=address()
    a1.valid_add()
    
