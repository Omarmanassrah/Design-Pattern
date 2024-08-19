Payment Processing System:
This project is a simple payment processing system implemented in Python. It demonstrates key software design principles, such as the SOLID principles, and uses various design patterns like Strategy, Singleton, and Template Method.

Features:
Payment Method Validation: The system supports multiple payment methods, including Credit Card, PayPal, and Cryptocurrency. Each payment method has its own validation logic.

Discounts: The system supports applying discounts using either a percentage or a fixed amount.

Currency Conversion: Convert amounts between different currencies.

Singleton Logger: Log messages using a singleton logger to ensure only one instance of the logger is created.

Design Principles and Patterns Used:

Liskov Substitution Principle: A parent class (paymentMethod) is defined and inherited by other payment methods (CreditCard, PayPal, Cryptocurrency), ensuring they can be substituted without affecting the correctness of the program.
Single Responsibility Principle: Each class has a single responsibility. For instance, each payment method class is responsible for handling the validation process of that particular payment method.
Open/Closed Principle: The system is open for extension but closed for modification. New payment methods or discounts can be added without modifying the existing code by leveraging abstract base classes and inheritance.
Strategy Pattern: The order class uses a strategy pattern to determine which payment method to use.
Singleton Pattern: The logger class ensures that only one instance of the logger exists, preventing multiple loggers from being created and writing to the same file.

How to run :
git clone https://github.com/Omarmanassrah/Design-Pattern.git
cd Design-Pattern


<!-- This is extra Description For the project that relate directly for what is written in the code  -->
Single Responsibility Principle (SRP):
Is used in multiple postion that is declared in the code as (#)
That i did not let any class handle more than one Responsibile

Open/Closed Principle (OCP):
I did not change on the content of some method insted of this i made new class that extend the parent one and implement the absract method in the parent class
such as :the method ValidationProcess i let each class implement his own validtion technique and that let the code be more Extensibile


Liskov’s Substitution Principle (LSP):
Also i use this principle in the code that i made a new class that extendes the original one rather than
modifying the original class directly. 
such as Discount for the both case (fixed ,percentage )


Strategy Pattern :
Is used in creating a new class called order Whyyyy?
Becouse of the application needed to support multiple pay method  strategies,
complicating its maintenance and scalability.
As i can add i new strategies as i want.

The CurrencyConversion class is responsible for handling currency conversions, keeping this responsibility
separate from payment processing.

Singleton pattern implementation:
Class has only one instance and provides a global point of access to that instance.

In the Method ValidationProcess i use a if statment that act as a unit test that will let me sure that the applection work as I want.

 In the Singleton Principle it match the case that say if i create many object they share the same instances
 or i create only a one object 
 I put "print(log1 is log2)" to ensure that they share the same id 

