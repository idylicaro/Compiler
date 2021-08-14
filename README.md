# Compiler
Python compiler for (Perl)

#### Sumário

1. [Installation and execution](https://github.com/idylicaro/Compiler#Installation-and-execution)
2. [BNF Grammar](https://github.com/idylicaro/Compiler#BNF-Grammar)
3. [Team](https://github.com/idylicaro/Compiler#Team)

#### Installation and execution

1. Clone the repository

    ```bash
	$ git clone https://github.com/idylicaro/Compiler.git
	$ cd application
    ```

2. Install the dependencies
    - Creating virtual environment in Mac/Linux
    ```bash
    $ python3 -m venv env
    ```
    - Creating virtual environment in Windows
    ```bash
    $ py -m venv env
    ```
    - install requirements
    ```bash
    $ pip install -r requirements.txt
    ```
    
3. Execute the **syntactic.py**:

    ```bash
    $ cd src
	$ python syntactic.py
    ```

#### BNF Grammar
```python
# What is capitalized is TOKEN

init : command init
        | command
        | function init
        | function

blockcode : command
    | blockcode command

command : interations
    | IF LPAREN exp RPAREN if_statement
    | exp SEMICOLON
    | RETURN exp SEMICOLON
    | BREAK SEMICOLON
    | CONTINUE SEMICOLON

if_statement :  LBRACE blockcode RBRACE
        | LBRACE blockcode RBRACE ELSE LBRACE blockcode RBRACE
        | LBRACE blockcode RBRACE elsif

elsif : ELSIF LPAREN exp RPAREN LBRACE blockcode RBRACE
    | ELSIF LPAREN exp RPAREN LBRACE blockcode RBRACE elsif2

elsif2 : elsif
    | ELSE LBRACE blockcode RBRACE

interations : FOR LPAREN for_assignments SEMICOLON exp SEMICOLON for_assignments RPAREN LBRACE blockcode RBRACE
    | DO LBRACE blockcode RBRACE WHILE LPAREN exp RPAREN
    | WHILE LPAREN exp RPAREN LBRACE blockcode RBRACE
    | WHILE LPAREN exp RPAREN LBRACE RBRACE

for_assignments : exp
    | exp COMMA for_assignments

function : SUB ID LPAREN RPAREN LBRACE blockcode RBRACE
    | SUB ID LPAREN function_assignments RPAREN LBRACE blockcode RBRACE

function_assignments : exp
    | exp COMMA function_assignments

call : ID LPAREN RPAREN
    | ID LPAREN function_assignments RPAREN

exp : ID_SC EQUALS exp_lor
    | ID_LI EQUALS exp_lor
    | ID_SC MINUSEQUAL exp_lor
    | ID_SC PLUSEQUAL exp_lor
    | ID_SC MODEQUAL exp_lor
    | ID_SC DIVEQUAL exp_lor
    | ID_SC TIMESEQUAL exp_lor
    | exp_lor


exp_lor : exp_lor LOR exp_land
    | exp_land

exp_land : exp_land LAND exp_or
    | exp_or

exp_or : exp_or OR exp_and
    | exp_and

exp_and : exp_and AND exp_comp
    | exp_comp_eq

exp_comp_eq : exp_comp_eq EQ exp_comp
    | exp_comp_eq NE exp_comp
    | exp_comp_eq SEQ exp_comp
    | exp_comp_eq SNE exp_comp
    | exp_comp_eq CMP exp_comp
    | exp_comp

exp_comp : exp_comp GT exp_plusminus
    | exp_comp LT exp_plusminus
    | exp_comp GE exp_plusminus
    | exp_comp LE exp_plusminus
    | exp_comp SLT exp_plusminus
    | exp_comp SGT exp_plusminus
    | exp_comp SGE exp_plusminus
    | exp_comp SLE exp_plusminus
    | exp_plusminus


exp_plusminus : exp_plusminus PLUS exp_times_divides
    | exp_plusminus MINUS exp_times_divides
    | exp_times_divides


exp_times_divides : exp_times_divides TIMES exp_lnot
    | exp_times_divides DIVIDE exp_lnot
    | exp_times_divides MODULO exp_lnot
    | exp_lnot


exp_lnot : XOR exp_lnot
    | exp_decrement_increment


exp_decrement_increment : INCREMENT  ID_SC
    | DECREMENT ID_SC
    | ID_SC INCREMENT
    | ID_SC DECREMENT
    | exp_lastlayer

exp_lastlayer : LPAREN exp RPAREN
    | ID_SC
    | ID_LI
    | NUMBER
    | call
    | TRUE
    | FALSE

```
#### Team

######  Advisor
* [Andre Luis Meneses Silva](https://github.com/andreluisms)

###### Developers
* [Antonio Frauzo Santos Moura](https://github.com/truef)
* [Idyl Icaro dos Santos](https://github.com/idylicaro)

###### Copyright © 2021 [Compiler](https://github.com/idylicaro/Compiler)  - Licensed by MIT LICENSE.
