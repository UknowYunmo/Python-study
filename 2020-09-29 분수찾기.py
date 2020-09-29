"""
3. 이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로
차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
"""
N=int(input())
range=0
sum=0
cnt=0
sum2=0
while sum<N:
    sum2=sum
    range+=1
    sum+=range
    cnt+=1
#print(cnt)
#print(N-sum2)

if (cnt%2)==0: #행이 짝수일때
    print(str(N-sum2)+"/"+str(cnt-(N-sum2)+1))
    #몇 번째 수인지 + 몇 번째 행 - (몇번째 수인지 +1) -- 예를들어 3번째 행의 첫번째 수면 3이 나와야하기 때문
else: #행이 홀수일때
    print(str(cnt-(N-sum2)+1)+"/"+str(N-sum2))
    #거꾸로
"""
어제는
1행을 1
2행을 1,2,3,2,1
3행을 1,2,3,4,5,4,3,2,1
이렇게 잡았었는데 이렇게하면 올랐다가 중간 지점에서 다시 감소해야되니까 한 행한 안에 조건식을 또 달아야됨.
그래서 일단 행을 
1행은 1
2행은 1,2
3행은 3,2,1
4행은 1,2,3,4
5행은 5,4,3,2,1
으로 바라봤다.
이렇게 하니까 편해진게 1행은 1개 2행은 2개 3행은 3개 이런 식으로 행 이름이랑 개수가 똑같아지는걸 확인.
그래서 예를 들어 10을 넣으면 4행의 4번째 숫자라는걸 알 수 있고 4를 의미한다는 걸 알수 있다는걸 깨달음
그렇기 때문에 가장 먼저 알아야되는건 N을 넣었을때 몇번째 행의 몇번째 숫자인지 파악하는거임.
행을 알아야되는 이유는 행 숫자가 짝수 일때는 1부터 증가하지만, 행 숫자가 홀수 일때는 행 수부터 1씩 감소하기 때문.
즉, 행이 몇 행인지도 알아야한다.

일단 몇번째 행인지 파악하는법
1행은 1개, 2행은 2개, 3행은 3개 이렇게 행이 증가할 수록 그 행 안의 들어가는 숫자는 1개씩 늘어남
즉 행 안의 들어가는 숫자를 range라고 하고, while문으로 range를 1씩 늘리고,
또 그 range를 계속 더해서 저장하는 sum이라는 변수에 저장했다.
그리고 sum이 업데이트 될때마다 cnt를 1씩 더했다
그렇다면 sum이랑 cnt의 의미는 무엇이냐.
sum값은 그 이전 행에 들어간 어떤 수의 최대값을 의미함
즉, 만약 N에 20을 넣었을때 range는 1,2,3,4,5,6 이렇게 증가하고
sum은 1,3,6,10,15,21 이렇게 증가함
그리고 sum2는 이전 sum을 저장하는 공간으로, 만약 sum이 21이면 sum2는 15임
그리고 cnt는 몇 행인지 나타냄.
"""
