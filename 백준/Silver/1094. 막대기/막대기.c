#include <stdio.h>
//백준 1094
int main() {
	int x;
	int  stick;
	int i;
	int sum = 0;
	int num = 0;

	scanf("%d", &x);

	stick = 0;
	for (i = 64; i > 0; i /= 2) { 
		if (i > x) {
			continue; //for문의 처음
		}
		else if (i == x) {
			stick = 1;
			break;
		}
		if (sum + i <= x) {
			sum += i;
			stick++;
		}

	}
	printf("%d", stick);
	return 0;
}