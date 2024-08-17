from abc import ABC 
# Here i use Liskov’s Substitution Principle that i find a parent class and let the whole other classes extends it 
# In other way the other classes inherits it 
class paymentMethod(ABC):
    """ Abstract base class for all payment methods. """
    @abstractmethod
    def ValidationProcess(self):
        pass 
# Here I use the Single Responsibility Principle Each class is responsibile for one payment method
# also I use Open/Closed Principle by use abstract method and rather than
# modifying the original class directly.


# Strategy Method is used here by adding a new class called order 
class order:
    """ Detrmine the needed Strategy """
    def __init__(self,amount,strategy=None):
        self.amount = amount
        self.strategy =strategy
    
class CreditCard(paymentMethod):
    def __init__(self,cardNumber):
        self.cardNumber=cardNumber
    """ I use my one way to check the validity also i get help from intrnet how th check (test the Implementation)"""
    def ValidationProcess(self):
        return len(self.cardNumber) == 16

class PayPal(paymentMethod):
    def __init__(self, Number):
        self.Number = Number
    """ I use my one way to check the validity also i get help from intrnet how th check (test the Implementation)"""
    def ValidationProcess(self):
        return 0 < self.Number < 9

class Cryptocurrency(paymentMethod):
    def __init__(self, walletAddress):
        self.walletAddress = walletAddress
    """ I use my one way to check the validity also i get help from intrnet how th check (test the Implementation)"""
    def ValidationProcess(self):
        return len(self.walletAddress) > 10

# also here i did not use a class dicount with the payment method becouse it will go wrong the Responsibility Principle
# that it work with more than one Responsibie so divide it to anther class
# i use mutiple principle such as Substitution Principle and open/closed 
class Discount(ABC):
    def __init__(self,amounts):
        pass
    """Abstract base class for all discount types."""
    @abstractmethod
    def FunPay(self,amount):
        pass 
        
class percentageMethod(Discount):
    def __init__(self,percentage):
        self.percentage=percentage
# Here i did not put the percentage becouse i want my code to be flexible and can be easily extended in the future.
    def FunPay(self,amount):
        return amount-(amount*self.percentage/100)

class FixedAmount(Discount):
    def __init__(self,amount):
        self.amount=amount
    def FunPay(self,amount):
        return amount-self.amount

# Single Responsibility Principle (SRP)
class CurrencyConversion:
    def __init__(self,USA,JOR):
        self.USA=USA 
        self.JOR=JOR
# Should take a String value 
    def Convert(self,amount,fromC):
        if self.USA== fromC:
            amount=amount*3.5
            return amount
        elif self.JOR==fromC:
            amount=amount*5.5
            return amount
        else :
            return amount

class MetaSingleton(type):
    _instance={}
    def __call__ (cls,*args,**kwargs):
# If an instance does not exist, create one
        if cls not in cls._instance:
            cls._instance[cls]=super(MetaSingleton,cls).__call__(*args,**kwargs)
        return cls._instance

class logger(metaclass=MetaSingleton):
    def __init__(self):
        self.file = open("C:\Users\omar.DESKTOP-4KRKGQT\Downloads\DesignP_skyProject\SingletonLogger.txt", "w")
# Choose x becouse of Opens a file for writing, creates the file if it does not exist
    def loging(self,Message):
        self.file.write(Message)
    def Close(self):
        self.file.close()

log1=logger()
log2=logger()

log1.loging("first log")
log2.loging("second log")
print(log1 is log2)
log1.loging("Order processed with Credit Card.")
# the both are the same 
log1.close()
# log1 closes the file for both log1 and log2

# Creating the object from each class and let them connect with each other 
"""Payment Methods"""
cre_card=CreditCard("1234567891234567")
pay_pal=PayPal(7)
cre_cur=Cryptocurrency("AS23SSDSD432223Bb0")

order_amount=500
order_cret_card = order(amount=order_amount, strategy=cre_card)
order_pay_pal = order(amount=order_amount, strategy=pay_pal)
order_cre_cur = order(amount=order_amount, strategy=cre_cur)

currency_converter = CurrencyConversion(USA="USD", JOR="JOD")
converted_amount = currency_converter.Convert(order_amount, fromC="USD")
print(f"Converted Amount: {converted_amount}")

# Extensibility the code is designed to be extended and other payment method by not adding the discount methed at each 
# payment method insted i made a parent class and have abstact methed and make override at these functions 
