# [Gold II] 원 이동하기 1 - 22946 

[문제 링크](https://www.acmicpc.net/problem/22946) 

### 성능 요약

메모리: 65928 KB, 시간: 1384 ms

### 분류

깊이 우선 탐색, 기하학, 그래프 이론, 그래프 탐색, 정렬, 트리

### 문제 설명

<p>좌표평면에 $N$개의 원이 존재한다.</p>

<p>$N$개의 원 중 임의의 두개의 원을 선택했을 때 내접, 외접 등 교점이 존재하지 않도록 존재한다. 하나의 원이 다른 원 안에 포함될 수는 있다.</p>

<p>하나의 원 내부에서 다른 원의 내부로 이동하려고 한다. 원 내부는 <strong>단 한 번만 방문 할 수 있으며</strong> 두 번 이상 방문을 할 수 없다.</p>

<p>문제 편의상 좌표평면을 원점이 (0, 0)이고 반지름이 무수히 큰 하나의 원이라고 가정하자.</p>

<p>좌표평면에 두 원 A, B만 존재한 상황에서 원 A 내부에서 원 B 내부로 올바르게 이동하는 경우는 아래와 같다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/bb24a122-acb9-4aa4-a619-c1ebaac3a086/-/crop/1358x768/281,155/-/preview/" style="height: 283px; width: 500px;"></p>

<p style="text-align: center;">1. 원 A와 원 B가 서로 포함관계가 아니고 만나지 않는 경우</p>

<p>첫 번째 경우는 원 A 내부 $\rightarrow$ 좌표평면 $\rightarrow$ 원 B 내부로 이동하였다. 이 경우를 제외한 올바른 경로는 존재하지 않는다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/cda92dcb-b2c6-4c91-a99c-7dcf8ae73e74/-/crop/840x833/542,126/-/preview/" style="height: 298px; width: 300px;"></p>

<p style="text-align: center;">2. 원 B가 원 A안에 존재하는 경우</p>

<p>두 번째 경우는 원 A 내부 $\rightarrow$ 원 B 내부로 이동하였다. 이 경우를 제외한 올바른 경로는 존재하지 않는다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/4a0e9613-390c-4b58-854f-5e37511f1315/-/crop/828x823/545,131/-/preview/" style="height: 298px; width: 300px;"></p>

<p style="text-align: center;">3. 원 A가 원 B안에 존재하는 경우</p>

<p>세 번째 경우도 원 A 내부 $\rightarrow$ 원 B 내부로 이동하였다. 이 경우를 제외한 올바른 경로는 존재하지 않는다.</p>

<p>아래 경우는 원 A 내부에서 원 B로 올바르게 이동하지 않은 경우들이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/b175d26f-3ff9-47a6-acff-36aded60f42e/-/crop/1361x773/281,155/-/preview/" style="height: 284px; width: 500px;"></p>

<p style="text-align: center;">4. 좌표평면 위에 원 A, B, C가 존재하고 서로 포함관계가 아니면서 만나지 않는 경우</p>

<p>이 경우는 원 A 내부 $\rightarrow$ 좌표평면 $\rightarrow$ 원 C 내부 $\rightarrow$ 좌표평면 $\rightarrow$ 원 B 내부로 이동한 경로이다. 좌표평면을 2번 방문하였기 때문에 올바르게 이동한게 아니다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/f2dff913-6138-43ec-b8ab-d0b6ea21834a/-/crop/1462x907/230,88/-/preview/" style="height: 310px; width: 500px;"></p>

<p style="text-align: center;">4. 좌표평면 위에 원 A, B가 존재하고 원 B가 원 A의 내부에 있을 경우</p>

<p>이 경우는 원 A 내부 $\rightarrow$ 좌표평면 $\rightarrow$ 원 A 내부 $\rightarrow$ 원 B 내부로 이동한 경로이다. 원 A 내부를 2번 방문하였기 때문에 올바르게 이동한게 아니다.</p>

<p>좌표평면에서 임의의 두 원을 골랐을 때 하나의 원 내부에서 다른 원 내부로 이동할 때 방문한 원의 최대 개수를 구하시오.</p>

### 입력 

 <p>첫 번째 줄에는 원의 개수 $N$이 주어진다.</p>

<p>두 번째 줄부터 $N + 1$번째 줄까지 원의 좌표 $x$, $y$와 반지름 $R$이 공백으로 구분되어 주어진다.</p>

<ul>
</ul>

### 출력 

 <p>임의의 두 원을 선택했을 때 하나의 원에서 다른 원으로 이동할 때 방문한 원의 최대 개수를 출력한다.</p>

