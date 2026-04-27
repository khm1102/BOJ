# [Gold III] :rightplant: - 31631 

[문제 링크](https://www.acmicpc.net/problem/31631) 

### 성능 요약

메모리: 110548 KB, 시간: 124 ms

### 분류

애드 혹, 해 구성하기

### 제출 일자

2024년 3월 22일 12:32:14

### 문제 설명

<p>$1$부터 $N$까지의 서로 다른 정수 높이를 가진 $N$개의 빌딩이 일렬로 놓여 있습니다. 왼쪽에서 $i$번째 빌딩의 높이는 $H_i$입니다.</p>

<p>높이 $h$의 빌딩에서 가지를 오른쪽으로 발사하면, 가지는 높이 $h$ 이하인 빌딩들의 위를 통과하여 날아갑니다. 가지가 높이 $h$ 초과인 빌딩에 부딪히면 부딪힌 빌딩의 높이를 $1$ 줄이고 진행 방향을 반대로 바꿉니다.</p>

<p style="display:flex;flex-direction:column;align-items:center;"><img src="" style="max-height:12em;max-width:100%"><span style="text-align:center;">높이 $h$인 빌딩에서 오른쪽으로 날아가는 가지가 높이 $h$ 미만인 빌딩의 위를 통과하여 날아가는 모습</span></p>

<p style="display:flex;flex-direction:column;align-items:center;"><img src="" style="max-height:12em;max-width:100%"><span style="text-align:center;">높이 $h$인 빌딩에서 오른쪽으로 날아가는 가지가 높이 $h$인 빌딩의 위를 통과하여 날아가는 모습</span></p>

<p style="display:flex;flex-direction:column;align-items:center;"><img src="" style="max-height:12em;max-width:100%"><span style="text-align:center;">높이 $h$인 빌딩에서 오른쪽으로 날아가는 가지가 높이 $h$ 초과인 빌딩에 부딪혀서 방향을 바꾸는 모습</span></p>

<p>왼쪽에서 $i$번째 빌딩에서 가지를 오른쪽으로 발사한 이후, 발사한 가지가 맨 왼쪽 혹은 오른쪽 빌딩을 통과하여 날아갈 때까지 가지가 진행 방향을 바꾼 횟수를 $B_i$라 합시다. $B_1 + B_2 + \dots + B_N$의 값이 최대가 되도록 하는 수열 $H$를 구해 봅시다.</p>

### 입력 

 <p>첫 번째 줄에 정수 $N$이 주어집니다. $(2 \le N \le 5\,000)$</p>

### 출력 

 <p>첫 번째 줄에 $B_1 + B_2 + \dots + B_N$의 값이 최대가 되도록 하는 수열 $H$의 원소 $H_1, H_2, \dots, H_N$을 공백으로 구분하여 출력합니다. 가능한 답이 여러 가지라면 아무거나 출력합니다.</p>

