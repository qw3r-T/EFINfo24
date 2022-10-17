#include <iostream>

using namespace std;

void collatz(int n) {
	while (n>1) {
		cout << n << endl;
		if (n%2==0) {n=n/2;} else {n = 3*n+1;};
	};
};

int main() {
	cout << "Enter a number: ";
	int n;
	cin >> n;
	collatz(n);	
	return 0;
};
