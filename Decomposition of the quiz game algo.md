### **Decomposition of the quiz game algorithm**





**> Set up the question bank**

&nbsp;	Set the values of the question bank to a dictionary which contains the predefined comparisons.



**> Engage the user in an interactive loop**

&nbsp;		Set the score count to zero

&nbsp;		Set exit to False

&nbsp;		Repeat while exit is False

&nbsp;			Set user\_input to ‘Enter “s” to show a flashcard and “q” to quit

&nbsp;			If the user\_input equals ‘q’

&nbsp;				Set exit to True

&nbsp;				Print “Number of correct answers” followed by the scorecount

&nbsp;			Otherwise if the user\_input equals ‘s’

&nbsp;			**>>Result equals show\_flashcard**

&nbsp;			If the result equals True

&nbsp;				Score\_count must equal score\_count plus 1.

&nbsp;				Print ‘Correct’

&nbsp;			Else:

&nbsp;				Print ‘Incorrect’



&nbsp;			**>> Show\_flashcard function**



&nbsp;				**>>> Randomise the order of pairs from the question\_bank**

&nbsp;				Set big\_item equal to a random key from question\_bank

&nbsp;				Set small\_item to the object value of the selected key.

&nbsp;	

&nbsp;				**>>> Randomise the order of the pair selected**

&nbsp;				Set random\_number to a random choice of 0 or 1

&nbsp;					If random\_number equals 0

&nbsp;						Set first\_random to big\_item

&nbsp;						Set second\_random to small\_item

&nbsp;					Otherwise if random\_number equals 1

&nbsp;						Set first\_random to small\_item

&nbsp;						Set second\_random to big\_item



&nbsp;				**>>> Ask for user input and determine if it is correct or not.**

&nbsp;				Display the question ‘Which is bigger?” and the required randomised pair.

&nbsp;				Collect user\_input to ‘Enter your guess A. or B. >’

&nbsp;					If the user\_input is A

&nbsp;						Then set A to first\_random.

&nbsp;					Otherwise if user\_input is B,

&nbsp;						Set user\_input to second\_random

&nbsp;					If user\_input is equal to big\_item

&nbsp;						The function must return True





