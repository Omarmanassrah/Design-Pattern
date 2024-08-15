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
