# Custom_Interpreter
Created a custom interpreter for a small imperative language

There are five types of tokens in our language, defined by the following regular expressions<br>
<li>
  <ul>IDENIFIER=([a-z] | [A-Z])([a-z] | [A-Z] | [0-9])*</ul>
  <ul>NUMBER=[0-9]+</ul>
  <ul>PUNCTUATION=\+  |  \-  |  \*|  /  |  \(  |  \)  |  :=  |  ;</ul>
  <ul>KEYWORD=if  |  then  |  else  |  endif  |  while  |  do|  endwhile  |  skip</ul>
</li>
  
Grammar of the language is defined as follows:<br>
<li>
  <ul>statement→basestatement{;basestatement}</ul>
  <ul>basestatement→assignment|ifstatement|whilestatement|skip</ul>
  <ul>assignmet→IDENTIFIER :=expression</ul>
  <ul>ifstatement→ if expression then statement else statement endif</ul>
  <ul>whilestatement→ while expression do statement endwhile</ul>
  <ul>expression→term{+term}</ul>
  <ul>term→factor{-factor}</ul>
  <ul>factor→piece{/piece}</ul>
  <ul>piece→element{*element}</ul>
  <ul>element→(expression)|NUMBER|IDENTIFIER</ul>
</li>
  
Command to run the evaluator:<br>
<strong><i>py interpreter.py input.txt output.txt</i></strong>

where input.txt is a file to be interpreted like the one shown.
