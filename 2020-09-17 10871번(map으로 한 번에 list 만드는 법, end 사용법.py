"""
1. 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.

N,X=input().split()
N=int(N)
X=int(X)
대신에 이렇게 할 수 있다
"""
N,X=map(int,input().split())
"""
이런 방법으로 수열 A처럼 한 번에 받아야되서 for문으로 하면 엔터로 받아야되서 컴파일 오류라 뜨는거 같음 이럴때도 마찬가지로
리스트에 map을 쓰면 한 번에 리스트 안에 받을 수 있음
"""
MyList=list(map(int,input().split()))
for i in range(1,N+1):
    num=MyList[i-1]
    if num<X:
        print(num,end=" ")
    else:
        pass
# for문에서 한 개씩 출력할 때 print로 하면 한 줄씩 띄어진 채로 출력되지만 end를 지정하면 한 줄에 출력도 가능하다