"""
1. 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
N=int(input())
for i in range(1,N+1):
    star="*"
    star*=i
    print(star)
2. 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
N=int(input())
for i in range(1,N+1):
    star="*"
    space=" "
    star*=i
    space*=N-i
    print(space+star)

3. 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.
"""
N,X=input().split()
N=int(N)
X=int(X)
for i in range(1,N+1):
    num=int(input())
    if num<X:
        print(num)
    else:
        pass