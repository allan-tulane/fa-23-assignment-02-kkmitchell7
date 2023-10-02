# CMPS 2200 Assignment 2

**Name:** Kailen Mitchell

In this assignment we'll work on applying the methods we've learned to analyze recurrences, and also see their behavior
in practice. As with previous
assignments, some of of your answers will go in `main.py` and `test_main.py`. You
should feel free to edit this file with your answers; for handwritten
work please scan your work and submit a PDF titled `assignment-02.pdf`
and push to your github repository.


1. Derive asymptotic upper bounds of work for each recurrence below.
  * $W(n)=2W(n/3)+1$
.  
.  w(n) = O(n)
.  
.  
.  
  * $W(n)=5W(n/4)+n$
.  
.  w(n) = O(n^log4(5)) = O(n^1.16...)
.  
.  
.  
  * $W(n)=7W(n/7)+n$
.  
.  w(n) = O(n*log(n))
.  
.  
.  
  * $W(n)=9W(n/3)+n^2$
.  
.  w(n) = O(n^2*log(n))
.  
.  
.  
  * $W(n)=8W(n/2)+n^3$
.  
.  w(n) = O(n^3*log(n))
.  
.  
.  
  * $W(n)=49W(n/25)+n^{3/2}\log n$
.  
.  
.  w(n) = O(n^(3/2)*log(n)*log(n))
.  
.  
  * $W(n)=W(n-1)+2$
.  
.  w(n) = O(n)
.  
.  
.  
  * $W(n)= W(n-1)+n^c$, with $c\geq 1$
.  
.  w(n) = O(n^c)
.  
.  
.  
  * $W(n)=W(\sqrt{n})+1$
.
.  w(n) = O(log(log(n)))
.
.


2. Suppose that for a given task you are choosing between the following three algorithms:

  * Algorithm $\mathcal{A}$ solves problems by dividing them into
      five subproblems of half the size, recursively solving each
      subproblem, and then combining the solutions in linear time.
    
  * Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively solving two subproblems of size $n-1$ and then
      combining the solutions in constant time.
    
  * Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into nine subproblems of size $n/3$, recursively solving
      each subproblem, and then combining the solutions in $O(n^2)$
      time.

    What are the asymptotic running times of each of these algorithms?
    Which algorithm would you choose?

    A: w(n) = 5*w(n/2)+n

    leaf dominated, so w(n) = O(n^log2(5)) = O(n^2.3...)

    B: w(n) = 2w(n-1)+1

    balanced, so w(n) = O(n)

    C: w(n) = 9w(n/3)+n^2

    balanced, so w(n) = O(n^log3(9)*log(n)) = O(n^2*log(n))

    
    B is the best because it has the best runtime


3. Now that you have some practice solving recurrences, let's work on
  implementing some algorithms. In lecture we discussed a divide and
  conquer algorithm for integer multiplication. This algorithm takes
  as input two $n$-bit strings $x = \langle x_L, x_R\rangle$ and
  $y=\langle y_L, y_R\rangle$ and computes the product $xy$ by using
  the fact that $xy = 2^{n/2}x_Ly_L + 2^{n/2}(x_Ly_R+x_Ry_L) +
  x_Ry_R.$ Use the
  stub functions in `main.py` to implement Karatsaba-Ofman algorithm algorithm for integer
  multiplication: a divide and conquer algorithm that runs in
  subquadratic time. Then test the empirical running times across a
  variety of inputs in `test_main.py` to test whether your code scales in the manner
  described by the asymptotic runtime. Please refer to Recitation 3 for some basic implementations, and Eqs (7) and (8) in the slides https://github.com/allan-tulane/cmps2200-slides/blob/main/module-02-recurrences/recurrences-integer-multiplication.ipynb
 
n*2

n=1 0.0050067901611328125

n=10 0.08177757263183594

n=100 0.11086463928222656

n=1000 0.2079010009765625

n=10000 0.2288818359375

n=100000 0.21004676818847656

Run time should be w(n) = O(n^(log2(3))) = O(n^1.585)
The graph is similar

