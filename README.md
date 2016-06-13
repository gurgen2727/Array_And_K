# Array_And_K
Sum of binomial coefficients

Chef has an array A consisting of N integers. He also has an intger K.

Chef wants you to find out number of different arrays he can obtain from array A by applying the following operation exactly K times.

Pick some element in the array and multiply it by -1
As answer could be quite large, print it modulo 109 + 7.

Input

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space separated integers N, K as defined above.
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.
Output

For each test case, output a single line containing an integer corresponding to the number of different arrays Chef can get modulo 109 + 7.
Constraints

1 ≤ T ≤ 10
1 ≤ N, K ≤ 105
-106 ≤ Ai ≤ 106
Subtasks

Subtask #1 (10 points) : N, K ≤ 10
Subtask #2 (30 points) : N, K ≤ 100
Subtask #3 (60 points) : N, K ≤ 105
Example

Input:
3
1 3
100
3 1
1 2 1
3 2
1 2 1

Output:
1
3
4
Explanation

Example case 1.
Chef has only one element and must apply the operation 3 times to it. After applying the operations, he will end up with -100. That is the only array he will get.

Example case 2.
Chef can apply operation to one of three elements. So, he can obtain three different arrays.

Example case 3.
Note that other than applying operation to positions (1, 2), (1, 3), (2, 3), Chef can also apply the operation twice on some element and get the original.

In summary, Chef can get following four arrays.

[1, 2, 1]
[-1, -2, 1]
[-1, 2, -1]
[1, -2, -1]

Solution: It is used Fermat's little theorem to pre-compute factorials and inverses, because there is prime P=1000000007

There is no need to use Lucas' Theorem as well because N and K (items of bionomial coefficient) themself are less than <P.

generally solution is: find the near NINDEX index by doing -2 till it less than N, then if there is '0' in list. Needs to count:
Sum of CN(0) + CN(1) + ... + CN(K), where N is numbet of not zero elemends, and K is min of not_zero_count and NINDEX

Otherwise solutions is:
sum of cn(NINDEX) + cn(NINDEX-2) + cn(NINDEX-4) + ... + cn(0) or cn(1) depending NINDEX % 2 is even or odd

It should be each 2, because by doing * -1 it becomes the same number.

Reffer to : http://fishi.devtail.com/weblog/2015/06/25/computing-large-binomial-coefficients-modulo-prime-non-prime/
Also the PDF file with this project.
