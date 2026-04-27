# [Diamond IV] Diameter - 13326 

[문제 링크](https://www.acmicpc.net/problem/13326) 

### 성능 요약

메모리: 111636 KB, 시간: 464 ms

### 분류

그리디 알고리즘, 기하학

### 제출 일자

2023년 11월 21일 09:41:12

### 문제 설명

<p>A new city has many buildings. For an efficiency of administration, the city wants to split the buildings into two groups, red and blue ones. A diameter of a group is defined as the maximum distance of two buildings in the group, which is an important criterion to measure the geometric extent of the group. The smaller the diameter is, the easier the administration is made. The final goal of this work is to determine a partition such that the sum of the diameters of the two groups is minimized.</p>

<p>More precisely, a building is mapped to a point in the plane. The distance between two points is the Euclidean distance between them. Note that the diameter of a point set is the maximum distance of two points in the set. Given a set P of n distinct points in the plane, you partition P into two subsets P<sub>1</sub> and P<sub>2</sub> such that P<sub>1</sub> ≠ ∅, P<sub>2</sub> ≠ ∅, P<sub>1</sub> ∪ P<sub>2</sub> = P, P<sub>1</sub> ∩ P<sub>2</sub> = ∅, and the sum of the diameters of P<sub>1</sub> and P<sub>2</sub> is minimized. If a subset consists of only one point, then its diameter is zero. You write a program to compute the minimum diameter sum for P.</p>

<p>For example, nine points with integer coordinates are given in the plane as in Figure 1(a). There are many redblue partitions. If you partition the points as in Figure 1(b), then the diameter of the blue points is \(\sqrt{4^2+3^2} = 5\), and the diameter of the red points is \(\sqrt{5^2+1^2} = \sqrt{26}\), thus their sum is \(5 + \sqrt{26}\). The partition in Figure 1(c) has the sum of the diameters of \(4 + \sqrt{34}\), which is a bit smaller than the sum in Figure 1(b).</p>

<p style="text-align:center"><img alt="" src="" style="height:217px; width:586px"></p>

<p style="text-align:center">Figure 1. (a) Input points. (b), (c) Two red-blue partitions where the point pair determining the diameter of each group is marked with a line segment with same color of the group.</p>

### 입력 

 <p>Your program is to read from standard input. The input starts with a line containing an integer, n (2 ≤ n ≤ 5,000), where n is the number of points. In the following n lines, each of the n points in P is given line by line. Each point is represented by two numbers separated by a single space, which are the x-coordinate and the y-coordinate of the point, respectively. The coordinate is an integer between 0 and 10,000, inclusively. </p>

### 출력 

 <p>Your program is to write to standard output. Print exactly one line for the input. The line should contain the minimum diameter sum. The output is judged as a correct answer if it is within an absolute error of 10<sup>−3</sup>.</p>

