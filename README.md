<h1>Quiz Game: Which is bigger?</h1>

<p align="center">

<img src="https://github.com/grigricar/Quiz_game/blob/main/bigger_or_smaller_than.png" height="35%" width="35%"/>
<br/>
</p>

<h2>Description</h2>
The is a Python coding project done in university as a final course assignment for the year one module. The task was to build a quiz game for the user, where a number of comparisons are given to the user and they have to decide "which is bigger." The required dictionary structure of comparisons was provided. As the focus of the course was on "Problem Solving with Python" much attention was given to thinking about and planning the structure of the algorithm through decomposition before attempting to execute it in code. The decomposition is included in this repository.      
<br/>


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>GitHub </b>
- <b>Basic HTML </b>

<h2> Skills </h2>

- <b>Algorithmic Decomposition</b> 
- <b>Basic dictionary structures</b>
- <b>Functions</b>
- <b>Case splits</b>
- <b>'while' loops</b>

<h2> Reflection and Questions</h2>

The project did not draw from any external Python libraries, as such it forced us to stick to fundamentals and this was engaging. The decomposition process was unquestionably valuable. Forming the habit of breaking the problems down into subproblems, onto which recurring patterns can be mapped, is critical in tackling more complex tasks. It is also time-saving, and is one of the most valued lessons I have taken away from the course. The subproblems I identified can be found in the "decomposition" document.    
 </br>
The most challenging part of the project was to think of a way to randomise both the selection of comparisons in the dictionary pairings, and then to also randomise the ordering of the pair found in the dictionary structure. Randomising the first requirement turned out to be trivial. Switching the actual pairings was more challenging. I solved this by separating out the key and entry in the dictionary into two separate lists. Based on a random selection of 0 or 1, I was able to assign the key and entry to variables that could be switched according to the 0 or 1 outcome. 
<br>
</br>
Setting up the user-input loop so they could quit the program or ask for a new question was delt within a while loop which terminates when the user enters 'q'. This section was not a difficult as initially thought. Inserting the entire flashcard function into the input section, knowing it worked, was the moment I knew the project would achieve its aims. Including a tally of correctly answered questions presented once the user quits, was an easy problem, solved with counting variables inserted into key sections of the loop. 

<br>Key takeaways and ideas to develop include:</br>

</br>

-  <b> Could this easily be developed into a more user friendly GUI? </b>
-  <b> It was not a requirement of the task, but it is possible for comparisons to be repeated. This would have to be solved in the function by using the '.remove' method to eliminate keys and entries from the list once they have been used.  </b>
-  <b> Decomposition was essential even though parts had to be modified once adapting to code. The structure was essential. Constant revision and reflection are also required. </b>
- <b> What more efficient solutions are there? I think a clever nested loop could be used in the function and randomisation process. </b>
- <b> More case-splits could be used to deal with some of the potential user-input variety eg. ('a'.; 'A')?
  

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
