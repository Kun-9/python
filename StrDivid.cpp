#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <typeinfo>
using namespace std;

 
vector<string> split(string str, char Delimiter) {
    istringstream iss(str);             // istringstream에 str을 담는다.
    string buffer;                      // 구분자를 기준으로 절삭된 문자열이 담겨지는 버퍼
 
    vector<string> result;
 
    // istringstream은 istream을 상속받으므로 getline을 사용할 수 있다.
    while (getline(iss, buffer, Delimiter)) {
        result.push_back(buffer);               // 절삭된 문자열을 vector에 저장
    }
 
    return result;
}
 
int main() {
 
    string str="3 5 7 0 0 0,40 50 20 0 0 0,1 0 1 0 0 0";
 
    vector<string> result = split(str, ',');
 
    int source_info[3][6];

    for (int i = 0; i < 3; i++) {
        // cout << result[i] << "\n";

        vector<string> temp = split(result[i], ' ');
        for(int k = 0; k < 6; k++) {
            // cout << stoi(string(temp[k])) << "\n";
            
            int a = stoi(string(temp[k]));
            source_info[i][k] = a;
            
        }
    }

    for (int i = 0; i < 3; i++)
    {
        for (int k = 0; k < 6; k++)
        {
            cout << source_info[i][k] <<"\n";
        }
    }
    

    return 0;
}
