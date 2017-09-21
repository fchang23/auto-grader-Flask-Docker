#include <iostream>
using std::cin;
using std::cout;
#include <string> 
using std::string;
int main() 
{
string name1,name2;
std::cout << "Enter a name:";
getline(std::cin,name1);
std::cout << "Enter a name:";
getline(std::cin,name2);
std::cout << name1 + " and " + name2 + " went for a walk.\n" ;
}
