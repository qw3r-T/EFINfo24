#include <iostream>

using namespace std;

void evil_arithmetic_trainer(int n) {
	while (n>0) {
		srand((unsigned int)time(NULL));
		int rand1 = rand()%10+1;
		int rand2 = rand()%10+1;
		cout << rand1 << " * " << rand2 << endl;
		int answ;
		cin >> answ;
		if (answ==rand1*rand2) {
			n-=1;
		} else {
			int i = 2;
			while (i>0) {
				cout << "Wrong!" << endl;
				cin >> answ;
				if (answ==rand1*rand2) {n -= 1; break;} 
				i -= 1;
				};
			cout << "Next exercise" << endl;
		};
	};
};

int main() {
	cout << "How many exercises do you wanna solve? ";	
	int a;
	cin >> a;
	evil_arithmetic_trainer(a);
}
