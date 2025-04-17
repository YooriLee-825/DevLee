# **C++ Essentials: OOP, Building Blocks, and Compilation Process**

## **Introduction**

- **Object-Oriented Programming (OOP)** is a programming method that solves problems using objects and their relationships.
- Objects are designed independently and can be reused in different programs with similar needs.
- OOP is especially suitable for large-scale software development.

## **Main Concepts of OOP**

### **1. Encapsulation**

- Encapsulation is the process of combining **data** and **methods** that manipulate the data into a single unit.
- **Strong Encapsulation**: Data is protected with `private` access and cannot be accessed directly.
- **Weak Encapsulation**: Data and methods are together, but data protection is not strict.

**Example:**
```cpp
class Rectangle
{
private:
    double width;
    double height;

public:
    void setDimensions(double w, double h)
    {
        width = w;
        height = h;
    }
    double getArea()
    {
        return width * height;
    }
};
```

### **2. Inheritance**

- Inheritance allows a class to acquire **properties** and **methods** from another class.
- It increases code reusability and expresses relationships between classes.

**Example:**
```cpp
class Animal
{
public:
    void eat()
    {
        // Eating action
    }
};

class Dog : public Animal
{
public:
    void bark()
    {
        // Barking action
    }
};
```

### **3. Polymorphism**

- Polymorphism allows the same method to behave differently depending on the object's type.
- It increases flexibility and extensibility of programs.

**Example:**
```cpp
class Shape
{
public:
    virtual void draw()
    {
        // Default drawing
    }
};

class Circle : public Shape
{
public:
    void draw() override
    {
        // Drawing a circle
    }
};

class Square : public Shape
{
public:
    void draw() override
    {
        // Drawing a square
    }
};

// Usage example
Shape* shape1 = new Circle();
Shape* shape2 = new Square();

shape1->draw(); // Draws a circle
shape2->draw(); // Draws a square
```

## **Modularity in OOP**

- **Modules** are independent units of code that contain classes and their implementations.
- Easy to manage and maintain code.
- Only modified modules need to be recompiled, which is efficient.

## **Basic Elements of OOP Languages**

- **Values**: Values that objects hold.
- **Objects**: Instances created from classes.
- **Variables**: Named objects.
- **References**: Alternative names pointing to objects.
- **Functions**: Blocks of code that perform tasks.
- **Types**: Define kinds of data and possible operations.
- **Class Members**: Variables and methods inside classes.
- **Templates**: Blueprints for generic programming.
- **Namespaces**: Spaces that prevent name conflicts.

## **Types and Declarations**

### **Types**

- The type of an object determines what data it can store and what operations it can perform.

**Types:**

- **Fundamental Types**: Basic types like `int`, `char`.
- **User-Defined Types**: Programmer-defined classes or structs.

### **Declarations and Scope**

- **Declaration**: Introduces a name and type of a variable or function.
- **Scope**: The region where a name is valid.

**Scopes:**

- **Local Scope**: Inside functions or blocks.
- **Class Scope**: Inside a class.
- **Global Scope**: Entire program.

**Example:**
```cpp
int globalVar; // Global scope

class MyClass
{
public:
    int classVar; // Class scope

    void myFunction()
    {
        int localVar; // Local scope
    }
};
```

## **Role of Compilers**

- The **compiler** translates source code into binary code.
- Performs **type checking** to detect errors early.
- Error detection occurs during **compile-time**, **link-time**, and **run-time**.

## **Static vs Dynamic Allocation**

### **Static Allocation**

- Memory size is determined at compile time.
- Allocated in the **stack**.
- Fast but fixed in size.

### **Dynamic Allocation**

- Memory size is determined at run time.
- Allocated in the **heap**.
- Flexible but requires manual management.

**Example:**
```cpp
int* arr = new int[10]; // Allocate array of 10 integers in heap
// Use the array
delete[] arr; // Free memory
```

## **Memory Organization**

- **Code Segment**: Stores program code.
- **Data Segment**: Stores global/static variables.
- **Stack Segment**: Stores function call data and local variables.
- **Heap Segment**: Stores dynamically allocated memory.

```
-----------------
|     Stack     |
-----------------
|               |
|     Heap      |
|               |
-----------------
|  Data Segment |
-----------------
|  Code Segment |
-----------------
```

---

# **C++ Building Blocks**

## **Overview**

- Introduces C++ basic components and syntax.
- These components include **values, variables, objects, references, functions, types, class members, templates, namespaces**.

## **Declarations and Definitions**

- **Declaration**: Introduces a name to the program.
- **Definition**: Gives meaning to a declared name.

## **One Definition Rule (ODR)**

- Every entity must have exactly one definition in the whole program.

## **Scope and Shadowing**

- **Block Scope**: Name valid inside `{}`.
- **Class Scope**: Name valid inside class.
- **Global Scope**: Name valid everywhere.
- **Shadowing**: Inner name hides outer name.

## **Linkage**

- **External Linkage**: Visible across modules using `extern`.
- **Internal Linkage**: Visible only inside the file using `static`.

## **Type and Type Definition**

- `typedef` defines type aliases.

**Example:**
```cpp
typedef const int constInt;
```

## **Namespaces**

- Groups names to avoid conflicts.

**Example:**
```cpp
namespace myNamespace
{
    int x;
}

myNamespace::x = 5;
```

## **Lifetime in Memory**

- **automatic**: Disappears when out of scope.
- **static**: Exists during whole program.
- **dynamic**: Managed by `new` and `delete`.
- **thread**: Exists during thread's life.

## **Static Duration Example**

```cpp
#include <iostream>

void display()
{
    static int n = 1;
    std::cout << "n is " << n++ << std::endl;
}

int main()
{
    display(); // n is 1
    display(); // n is 2
}
```

---

# **C++ Compilation Process and Evaluation Techniques**

## **1. Compilation Process**

- **Pre-Processing**: Insert headers, replace macros.
- **Compilation**: Create binary files.
- **Linking**: Combine binaries into executable.
- **Execution**: OS loads and runs executable.

## **2. Platforms and Compilers**

- **Windows**: `cl` compiler.
- **Linux**: `g++` compiler.

### **Compiler Options**

- `/c` or `-c`: Compile only.
- `/E` or `-E`: Pre-process only.
- `/Wall`: Show all warnings.

## **3. Interface with OS**

**Main function:**
```cpp
int main(); // No arguments
int main(int argc, char *argv[]); // With command-line arguments
```

**Example Command:**
```bash
my_prg Assignments Workshops Tests Exam
```

**Output:**
```
Application: my_prg
- Assignments
- Workshops
- Tests
- Exam
```

## **4. Compile-time Evaluations**

### **Constant Expressions**

**Example:**
```cpp
constexpr int N = 8;
constexpr int factorial(int i)
{
    return i > 1 ? i * factorial(i - 1) : 1;
}
```

### **Static Assertions**

**Example:**
```cpp
constexpr int N = 0;

int main()
{
    static_assert(N > 0, "N must be greater than 0");
    static_assert(N < 20, "N must be less than 20");
}
```

---