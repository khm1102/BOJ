# [Platinum V] Wall construction - 10903 

[문제 링크](https://www.acmicpc.net/problem/10903) 

### 성능 요약

메모리: 21368 KB, 시간: 308 ms

### 분류

볼록 껍질, 기하학

### 제출 일자

2023년 11월 14일 01:42:04

### 문제 설명

<p>세계적인 거부 홍준이에게 매일 매일은 공허하기 짝이 없었다. 그러다 어느 날 홍준이는 예술에 눈을 떴다. 자신의 마음 속에 내재되어 있던 예술에 대한 갈망을 발견하였다. 그렇기에 썩어 넘치게 많은 그의 돈으로 미술관을 짓기로 했다.</p>

<p>미술관의 바닥은 평평하게 만들기로 했다. 그리고 미적인 이유로 바닥에 수직하게 서 있는 원기둥을 N개 만들기로 했다. 또한 특이하게 모든 기둥의 반지름을 동일하게 만들 것이다. 이제 홍준이는 두께가 없다고 할 수 있을 정도의 매우 얇은 유리를 이용해 미술관의 외벽을 만들기로 했으며, 외벽도 미술관 바닥과 수직하게 만들어서 미술관을 위쪽에서 바라볼 경우 외벽은 아름다운 폐곡선을 이뤄야 한다. 홍준이는 미니멀리즘을 추구하기 위해 가장 최소한의 유리 벽을 사용하여 외벽을 만들고자 한다. 또한 외벽은 모든 기둥을 포함해야 한다. 홍준이가 만들게 될 미술관 외벽 둘레의 길이는 얼마가 될까?</p>

### 입력 

 <p>첫 번째 줄에는 두 개의 자연수 N, R (1 ≤ R ≤ 100)이 공백으로 구분되어 주어진다. N은 기둥의 개수이며, R은 기둥의 반지름으로 모든 기둥은 같은 반지름을 가진다.</p>

<p>이후 N개의 줄에는 미술관의 바닥을 xy평면으로 볼 때 각 기둥 중심이 위치하는 좌표를 의미하는 두 정수 x, y(-10<sup>4</sup> ≤ x, y ≤ 10<sup>4</sup>)가 공백으로 구분되어 주어진다. 주어진 기둥 중에 어떤 두 기둥이 겹쳐져 있거나 접해있는 경우는 없다.</p>

<p>2 ≤ N ≤ 1,000을 만족하는 입력이 주어진다.</p>

### 출력 

 <p>주어진 기둥을 모두 포함하는 외벽 둘레 길이의 최솟값을 출력한다. 절대오차 혹은 상대오차가 정답과 10<sup>-8</sup>이하인 경우 정답으로 인정된다.</p>

