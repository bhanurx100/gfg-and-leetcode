#include <iostream>
using namespace std;

int main() {
    int T; 
    cin >> T;
    while(T--)
    {
	int N; cin >> N;
	int arr[N];
	for(int i = 0; i < N; i++)
	    cin >> arr[i];
    for(int i = N - 1; i >= 0; i--)
        cout << arr[i] << " ";
    cout << "\n";
    }
	return 0;
}