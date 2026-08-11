# RULES
- Think always about simple solution first
- Check if sorting or reversing makes it easy to solve
- Think when to use For loop and when to use While loop 
    - If you know when you will get answer -- got for For loop.
    - If using for loop can help avoiding writting if/else to return or assign values -- go for for loop. 
    - If you don't know where to stop/when you will get the result -- go for While loop
- If you find a problem with more than one loop -- always think if there exist any Greedy way to solve it or not?
- TRY to connect the question with real world Scenarios (MOST IMPORTANT POINT)
- NEVER assume that if the loops are nested it's O(n^2), The trick is to see weather for every i, we are visisting atmost n elements (if yes it's O(n^2)), if we don't revisit or backtrack same index i, it's O(n) -- See 45. Jump Game II Solution to understand this.