#include <stdio.h>

long long int A, B, C;

long long int prob(long long int n)
{
	if (n == 1)
		return A % C;
	if (n % 2 == 0)
	{
		long long int a = prob(n / 2);
		return a * a % C;
	}
	else
	{
		long long int a = prob(n / 2);
		return a * a * A % C;
	}
}

int main()
{
	if(scanf("%lld %lld %lld", &A, &B, &C) != 3) return 0;
	printf("%lld\n", prob(B));
	return 0;
}