# Logic-satisfiability
Satisfiability of logic formula written in ONP (Reverse Polish Notation)
More about satisfiability [here](https://en.wikipedia.org/wiki/Method_of_analytic_tableaux)
<br>
More about the Metoda tablic semantycznych (Semantic tableaux method) used in this example is available [here (in Polish)](http://www.cs.put.poznan.pl/jjozefowska/wyklady/lo/W4_MTS__handouts.pdf)

## Technologies
language: Python 3.6 <br>
libraries: copy

## Launch
1. Have all the files in one folder
2. Run the rules_connector.py file
    1. Enter the formula for which you want to check satisfiability 
        * Use CAPITAL LETTERS
        * The formula must be entered in [Reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) (postfix notation)
        * Use A,B,C,D,E,F for constants
        * Use p, q for predicates. p/1 is used for predicate "p" with 1 argument. q/3 is a predicate named "q" with 3 arguments
        * Use X, Y, Z for variables
        * available logic expressions: EXISTS, ∀, FORALL, ∃, AND, OR, XOR, IMPLIES, ⊕, ↔, IFF, →, ∨, ∧, &, | 
    2. Declare constants, split them using space " "
    
## Test cases
To better understand input I provide you with sample test cases, listed below:

1.  A B C p/3 B p/1 C p/1 IMPLIES OR C p/1 E F p/2 E p/1 AND XOR OR NOT
1.  X X p/1 Y p/1 AND FORALL
1.  X X p/1 Y p/1 AND EXISTS NOT
1.  C A B C p/3 B p/1 C p/1 IMPLIES OR C p/1 E F p/2 E p/1 AND XOR OR NOT FORALL
1.  B A p/1 B p/1 C p/1 AND NOT IMPLIES EXISTS NOT
1.  B A p/1 B p/1 IFF C p/1 D p/1 AND AND NOT EXISTS NOT
1.  X X Y p/2 FORALL B p/1 C p/1 AND NOT IMPLIES NOT
1.  X X p/1 Y Y p/1 C p/1 IMPLIES EXISTS OR NOT FORALL
1.  Z Z q/1 FORALL X X p/1 X q/1 AND FORALL IMPLIES NOT
1.  X Y X p/1 Y q/1 IMPLIES NOT EXISTS FORALL
