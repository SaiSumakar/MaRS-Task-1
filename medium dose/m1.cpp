#include <iostream>
#include <string>
using namespace std;

// Define your custom data type using a struct
struct custom_data {
    int i;
    double d;
    string s;
    float f;
    bool b;
};

int main() {
    //Creating a struct variable
    custom_data my_data = {10, 3.14159265359, "Hello", 2.71828, 1};

    // Defining a lambda function 
    auto display_custom_data = [](const custom_data& data) {
        cout << "Integer Value: " << data.i << endl;
        cout << "Double Value: " << data.d << endl;
        cout << "String Value: " << data.s << endl;
        cout << "Float Value: " << data.f << endl;
        cout << "Bool Value: " << data.b << endl;
    };

    //calling the lambda function to display the values 
    display_custom_data(my_data);

    return 0;
}
