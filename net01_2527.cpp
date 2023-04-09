// BOJ 2527

/*
직사각형 판정 조건을 잘 생각해본다.
꼭짓점의 좌표가 우리에게 많은 힌트를 준다.
*/

#include <cstdio>
int main() {
	for (int a, s, d, f, q, w, e, r; ~scanf("%d%d%d%d%d%d%d%d", &a, &s, &d, &f, &q, &w, &e, &r);) {
		if ((a == e || q == d) && (s == r || w == f)) printf("c");
		else if (e < a || d < q || r < s || f < w) printf("d");
		else if (a == e || q == d || s == r || w == f) printf("b");
		else printf("a");
		printf("\n");
	}
}