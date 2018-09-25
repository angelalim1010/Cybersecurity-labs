#include <iostream>
#include <climits>
using namespace std;

int main(){
	int i ;
	int j ;
	int result;
	cout << "For this compiler: integers are: " << sizeof(int) <<  " bytes" << endl;
	cout << "The largest integer is: " << INT_MAX << endl;
    cout << "The smallest integer is: " << INT_MIN << endl;
    
    cout << "Input two integer values: " << endl;
    cin >> i >> j;
    //cin >> j >> endl;
    cout << "The integers your displayed are: " << i << "," << j << endl;
    
    //part 2 
    result = i * 10;
    cout << "Your number times ten is " << result << endl;
    result = i + j;
    cout << "The sum of your numbers is " << result << endl;
    result = i*j;
    cout << "The product of your numbers is " << result << endl;
    return 0;
}
