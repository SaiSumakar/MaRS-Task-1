#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

// class to store details of a person and actions of a person:communicate
class Person {
private:
    string name;
    int level;
public:
    Person(string n, int l) : name(n), level(l) {}

    string getName() const {
        return name;
    }

    int getLevel() const {
        return level;
    }
    //communicate only if a persons level is higher than the second person
    void communicate(const Person& another) const {
        if (level >= another.level) {
            cout << name << " communicates with " << another.name << endl;
        } else {
            cout << "Insufficient level to communicate with " << another.name << endl;
        }
    }
};

//organization: collection of people basically
class Organization {
private:
    vector<Person> people;
public:
    //function to add a person
    void addPerson(const Person& p) {
        people.push_back(p);
    }

    //function to check for communication between people
    void communicate(const string& person1, const string& person2) const {
        Person p1("", 0), p2("", 0);
        for (const Person& p : people) {
            if (p.getName() == person1) {
                p1 = p;
            } else if (p.getName() == person2) {
                p2 = p;
            }
        }
        if (p1.getName() != "" && p2.getName() != "") {
            p1.communicate(p2);
        } else {
            cout << "Person not found" << endl;
        }
    }

    //function to display the heirarchy level of a organization in ascending order
    void display_hierarchy() const {
        vector<Person> sorted_people = people;
        sort(sorted_people.begin(), sorted_people.end(), [](const Person& p1, const Person& p2) {
            return p1.getLevel() < p2.getLevel();
        });
        cout << "Hierarchy:" << endl;
        for (const Person& p : sorted_people) {
            cout << p.getName() << " - Level " << p.getLevel() << endl;
        }
    }
};

int main() {
    Organization org;

    // Adding people to the organization
    org.addPerson(Person("Alice", 3));
    org.addPerson(Person("Bob", 2));
    org.addPerson(Person("Charlie", 4));

    // Communicating between people
    org.communicate("Alice", "Bob");
    org.communicate("Bob", "Alice");
    org.communicate("Charlie", "Alice");
    org.communicate("Alice", "Charlie");
    org.communicate("Bob", "Charlie");
    org.communicate("Charlie", "Bob");
    org.communicate("Dave", "Eve");

    // Display hierarchy
    org.display_hierarchy();

    return 0;
}
