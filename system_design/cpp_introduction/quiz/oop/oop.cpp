#include <iostream>
#include <vector>
#include <memory>  // for smart pointers
using namespace std;

// =======================================================
// 1. Object-Oriented Programming (OOP): organizing code into objects
// =======================================================

// 11. Interface (in C++, achieved via pure virtual class)
// Interface only contains pure virtual methods
class Flyable {
public:
    virtual void fly() = 0;  // pure virtual method
};

// 10. Abstract class (cannot be instantiated)
class Animal {
private:
    // 6. Encapsulation — private data
    string name;
    int age;

protected:
    // Protected: accessible to subclasses
    string color;

public:
    static int animalCount; // 19. Static member shared by all objects

    // 17. Constructor
    Animal(string name, int age, string color) : name(name), age(age), color(color) {
        animalCount++;
    }

    // 18. Destructor
    virtual ~Animal() {
        cout << name << " has been destroyed." << endl;
    }

    // Getter and Setter (Encapsulation)
    string getName() const { return name; }
    void setName(const string &n) { name = n; }

    int getAge() const { return age; }

    // 8. Abstraction — abstract behavior
    virtual void makeSound() = 0;

    // 26. Virtual function — supports polymorphism
    virtual void sleep() {
        cout << name << " is sleeping..." << endl;
    }

    // 14. Method hiding (static)
    static void info() {
        cout << "Animals are living beings." << endl;
    }

    // 16. final keyword (C++11): prevent overriding
    virtual void breathe() final {
        cout << name << " is breathing." << endl;
    }
};

// Initialize static member
int Animal::animalCount = 0;

// =======================================================
// 4–5. Inheritance and its types
// =======================================================
class Bird : public Animal, public Flyable { // Multiple inheritance (Animal + Flyable)
private:
    double wingSpan;

public:
    // 21. Constructor chaining: calling another constructor
    Bird(string name, int age, string color, double wingSpan)
        : Animal(name, age, color), wingSpan(wingSpan) {}

    // Overloaded constructor (calls another)
    Bird(string name) : Bird(name, 1, "gray", 0.5) {}

    // 13. super keyword equivalent = calling base class constructor above

    // 7. Polymorphism (method overriding)
    void makeSound() override {
        cout << getName() << " chirps!" << endl;
    }

    // Implementing interface (Flyable)
    void fly() override {
        cout << getName() << " flies with wingspan " << wingSpan << " meters!" << endl;
    }

    // Method overloading (compile-time polymorphism)
    void fly(string direction) {
        cout << getName() << " flies toward " << direction << "." << endl;
    }

    // 12. this keyword
    void showThis() {
        cout << "This bird's name is " << this->getName() << endl;
    }

    // 14. Method hiding (static)
    static void info() {
        cout << "Birds are a type of Animal that can often fly." << endl;
    }
};

// 5. Hierarchical inheritance: another subclass of Animal
class Dog : public Animal {
public:
    Dog(string name, int age, string color) : Animal(name, age, color) {}

    void makeSound() override {
        cout << getName() << " barks!" << endl;
    }

    void fetch() {
        cout << getName() << " is fetching a ball." << endl;
    }
};

// 22. Composition (Zoo "has-a" list of animals)
class Zoo {
private:
    vector<shared_ptr<Animal>> animals;  // smart pointers manage memory automatically

public:
    void addAnimal(shared_ptr<Animal> a) {
        animals.push_back(a);
    }

    void showAllAnimals() {
        for (auto &a : animals) {
            a->makeSound();  // 24. Dynamic method dispatch (runtime polymorphism)
        }
    }
};

// 25. Shallow vs Deep Copy demonstration
class DogClone {
public:
    string breed;

    DogClone(string breed) : breed(breed) {}

    // Shallow copy constructor
    DogClone(const DogClone &other) {
        breed = other.breed;
    }

    // Deep copy would clone nested data (not shown here)
};

// =======================================================
// Main — demonstrating all concepts
// =======================================================
int main() {
    // 3. Object creation
    shared_ptr<Bird> parrot = make_shared<Bird>("Polly", 2, "green", 0.7);
    shared_ptr<Dog> dog = make_shared<Dog>("Buddy", 3, "brown");

    // Using methods
    parrot->makeSound();
    parrot->fly();
    parrot->fly("north");
    parrot->showThis();

    dog->makeSound();
    dog->fetch();

    // 20. instanceof operator equivalent: dynamic_cast
    cout << boolalpha;
    cout << "(parrot is Bird): " << (dynamic_cast<Bird*>(parrot.get()) != nullptr) << endl;
    cout << "(dog is Animal): " << (dynamic_cast<Animal*>(dog.get()) != nullptr) << endl;
    cout << "(dog is Flyable): " << (dynamic_cast<Flyable*>(dog.get()) != nullptr) << endl;

    // 22. Composition
    Zoo zoo;
    zoo.addAnimal(parrot);
    zoo.addAnimal(dog);
    zoo.showAllAnimals();

    // 16. final keyword demonstration (breathe can't be overridden)
    parrot->breathe();

    // 19. Static member
    cout << "Total animals created: " << Animal::animalCount << endl;

    // 25. Shallow copy
    DogClone d1("Beagle");
    DogClone d2 = d1;
    cout << "Copied dog breed: " << d2.breed << endl;

    // 14. Method hiding
    Animal::info();
    Bird::info();

    // 27. Liskov Substitution Principle (all derived classes can replace Animal)
    vector<shared_ptr<Animal>> animals = { parrot, dog };
    for (auto &a : animals) a->sleep();

    return 0;
}

/// Page 2: Quiz 2
#include <iostream>
#include <vector>
using namespace std;

class Bank {
public:
    vector<long long>& balance_ref;
    // Initialize the Bank with an array of account balances by reference
    Bank(vector<long long>& balance) : balance_ref(balance) {
        // doing nothing
    }
   
    // Transfers money from account1 to account2
    bool transfer(int account1, int account2, long long money) {
        /* Your code for the transfer function starts here from account1 to account2 */
        if (account1 < 1 || account1 > balance_ref.size() || account2 < 1 || account2 > balance_ref.size()) {
            return false;
        }

        int idx1 = account1 - 1;
        int idx2 = account2 - 1;

        if (balance_ref[idx1] >= money && money >= 0) {
            balance_ref[idx1] -= money;
            balance_ref[idx2] += money;
            return true;
        }

        return false;
        /* Your code for the transfer function ends here */
    }
   
    // Deposits money into the specified account
    bool deposit(int account, long long money) {
        /* Your code for the deposit function starts here */
        if (account < 1 || account > balance_ref.size() || money < 0) {
            return false;
        }
        int idx = account - 1;
        balance_ref[idx] += money;
        return true;
        
        /* Your code for the deposit function ends here */
    }
   
    // Withdraws money from the specified account
    bool withdraw(int account, long long money) {
        /* Your code for the withdraw function starts here */
        if (account < 1 || account > balance_ref.size() || money < 0) {
            return false;
        }
        int idx = account - 1;

        if (balance_ref[idx] < money && money > 0) {
            return false;
        }

        if (balance_ref[idx] >= money) {
            balance_ref[idx] -= money;
            return true;
        }
        return false;

        /* Your code for the withdraw function ends here */
    }

};

int main() {
    vector<long long> balance = {10, 100, 20, 50, 30};
    Bank bank(balance);
   
    cout << bank.withdraw(3, 10) << endl;     // Output: true
    cout << bank.transfer(5, 1, 20) << endl;  // Output: true
    cout << bank.deposit(5, 20) << endl;      // Output: true
    cout << bank.transfer(3, 4, 15) << endl;  // Output: false
    cout << bank.withdraw(10, 50) << endl;    // Output: false
    return 0;
}