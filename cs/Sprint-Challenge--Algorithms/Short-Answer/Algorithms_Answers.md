#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n). The loop runs O(n) times and does O(1) work per iteration. Therefore, as the size if the input increases, the runtime space used will grow at the same rate. 


b) O(n*log(n)). The outer loop for i in range(n): adds a runtime complexity of O(N). The inner loop of while j < n: j*=2 will run for O(log(n)) times. This is because as N grows larger, J will increment, but at a logarithmic rate since J grows multiplicatively but n grows linearly. 


c) Consider a base case of n=0, the algorithim will recursively build a stack of n-1 until the base case is reached. So for every N values, the function will be called N times to arrive at an answer. For N=3, it will call f(3)=2+f(2)=4+f(1)=f(0)=6. N+1, or O(N)

## Exercise II

The most efficient way to determine what floor an egg can be dropped from without breaking would be a binary search. This can be done because the floors in our apartment building are already sorted. Floor 0 is the ground floor, and the top floor N-1. Binary search has a runtime complexity of 0(log(n)) 

high = n low = 0 while abs(high-low) <=1

middle = (high-low)/2

drop egg from middle if egg breaks high = middle else low = middle

When the difference between the previous middle and new middle is less than or equal to one floor, we have identified f floor.

As this is binary search sort, the run time complextity is O(log n)


