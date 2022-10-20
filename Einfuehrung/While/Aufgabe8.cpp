#include <iostream>

using namespace std;

int collatz(int n) {
	int count=0;
	while (n>1) {
		if (n%2==0) {
			n=n/2;
		} else {
			n = 3*n+1;
		};
		count += 1;
	};
	return count;
};

int longestCollatz(int n) {
	int longest = 1;
	for (n; n>0; n--) {
		int tmp = collatz(n);
		if (tmp > longest) {
			longest = n;
		}	
	};
	return longest;
};

int main() {
	cout << "Enter a number: ";
	int n;
	cin >> n;
	cout << longestCollatz(n) << endl;
	return 0;
};
