#include <iostream>

using namespace std;

int main() {
	while (true) {
		srand((unsigned int)time(NULL));
		int rand1 = rand() % 100;
		int rand2 = rand() % 100;
		cout << rand1 << " + " << rand2 << endl;
		int answ;
		cin >> answ;
		if (answ != rand1 + rand2 && answ != 111) {break;}
	}
	
}
