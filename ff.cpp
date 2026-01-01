#include <iostream>
using namespace std;
int main ()
{
    int x;
    int factoriel =1 ;
    cout << "enter a number : ";
    cin >> x;
    for ( int i = 1 ; i<=x ; i++){
        factoriel = factoriel * i ;
    }
        cout << factoriel;
    return 0;
}