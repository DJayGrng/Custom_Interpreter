# Custom_Interpreter
Created a custom interpreter for a small imperative language

There are five types of tokens in our language, defined by the following regular expressions
  * IDENIFIER=([a-z] | [A-Z])([a-z] | [A-Z] | [0-9])*
  * NUMBER=[0-9]+
  * PUNCTUATION=\+  |  \-  |  \*|  /  |  \(  |  \)  |  :=  |  ;
  * KEYWORD=if  |  then  |  else  |  endif  |  while  |  do|  endwhile  |  skip
  
Grammar of the language is defined as follows:
  * statement→basestatement{;basestatement}
  * basestatement→assignment|ifstatement|whilestatement|skip
  * assignmet→IDENTIFIER :=expression
  * ifstatement→ if expression then statement else statement endif
  * whilestatement→ while expression do statement endwhile
  * expression→term{+term}
  * term→factor{-factor}
  * factor→piece{/piece}
  * piece→element{*element}
  * element→(expression)|NUMBER|IDENTIFIER
  
Command to run the evaluator:<br>
<strong>py interpreter.py input.txt output.txt</strong>

where input.txt is a file to be interpreted like the one shown.
