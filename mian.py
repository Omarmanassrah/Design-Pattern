from abc import ABC 
# Here i use Liskov’s Substitution Principle that i find a parent class and let the whole other classes extends it 
# In other way the other classes inherits it 
class paymentMethod(ABC):
    @abstractmethod
    def ValidationProcess(self):
        pass 
# Here I use the Single Responsibility Principle Each class is responsibile for one payment method
# also I use Open/Closed Principle by use abstract method and rather than
# modifying the original class directly.


# Strategy Method is used here by adding a new class called order 
class order:
    def __init__(self,amount,strategy=None):
        self.amount = amount
        self.strategy =strategy
    
class CreditCard(paymentMethod):
    def __init__(self,cardNumber):
        self.cardNumber=cardNumber

    def ValidationProcess(self):
        return len(self.cardNumber) == 16

class PayPal(paymentMethod):
    def __init__(self, Number):
        self.Number = Number

    def ValidationProcess(self):
        if self.Number>0 and self.Number<9:
            return True
        else :
            return False 

class Cryptocurrency(paymentMethod):
    def __init__(self, walletAddress):
        self.walletAddress = walletAddress

    def ValidationProcess(self):
        return len(self.walletAddress) > 10

# also here i did not use a class dicount with the payment method becouse it will go wrong the Responsibility Principle
# that it work with more than one Responsibie so divide it to anther class
# i use mutiple principle such as Substitution Principle and open/closed 
class Discount(ABC):
    def __init__(self,amounts):
        pass
    @abstractmethod
    def FunPay(self):
        pass 
        
class percentageMethod(Discount):
    def __init__(self,percentage):
        self.percentage=percentage
# Here i did not put the percentage becouse i want my code to be flexible and can be easily extended in the future.
    def FunPay(self,amount1):
        return amount1-(amount1*self.percentag/100)

class FixedAmount(Discount):
    def __init__(self,amount2):
        self.amount2=amount2
    def FunPay(self,amount):
        return amount-self.amount2
# Extensibility the code is designed to be extended and other payment method by not adding the discount methed at each 
# payment method insted i made a parent class and have abstact methed and make override at these functions 
