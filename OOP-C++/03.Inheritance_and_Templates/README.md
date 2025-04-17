# **C++ Essentials: Inheritance, Polymorphism, and Templates**

---

## **Part 1: Inheritance & Inclusion Polymorphism**

### **1. Inheritance Basics**

- **Inheritance** lets one class (Derived) inherit features from another class (Base).
- This models **generalization (Base)** and **specialization (Derived)** in object-oriented programming.

#### **Abstract Base Class**

- A class with at least one **pure virtual function** (defined with `= 0`) is abstract.
- Cannot create instances from abstract classes.
- They serve as a **common interface** for derived classes.

```cpp
class Shape {
public:
    virtual double volume() const = 0;  // Pure virtual function
};
```

#### **Concrete Classes**

- A concrete class **implements all pure virtual functions** from the abstract class.
- You can create objects from concrete classes.

```cpp
class Cube : public Shape {
    double len;
public:
    Cube(double l) : len{ l } {}
    double volume() const override {
        return len * len * len;
    }
};

class Sphere : public Shape {
    double rad;
public:
    Sphere(double r) : rad{ r } {}
    double volume() const override {
        return 4.18879 * rad * rad * rad;
    }
};
```

---

### **2. Inclusion Polymorphism**

- **Polymorphism** allows different objects to respond differently to the same function call.
- The base class method must be marked `virtual`.
- Behavior depends on the **dynamic type** of the object at runtime.

```cpp
void displayVolume(const Shape* shape) {
    if (shape)
        std::cout << shape->volume() << std::endl;
    else
        std::cerr << "ERROR!" << std::endl;
}
```

---

### **3. Copying Operations with Polymorphism**

- To copy polymorphic objects correctly, use a `clone()` method.
- Each derived class should implement `clone()` to return a copy of its type.

```cpp
class Shape {
public:
    virtual Shape* clone() const = 0;
};

class Cube : public Shape {
public:
    Shape* clone() const override {
        return new Cube(*this);
    }
};
```

---

### **4. Liskov Substitution Principle (LSP)**

- If a function works with a base class pointer/reference, it should work properly with any derived class.
- Design based on **behavior** for functions and **properties** for data.

#### ✅ Correct Design

```cpp
class Square {
    double width;
public:
    void setWidth(double w) { width = w; }
    double getWidth() const { return width; }
};

class Rectangle : public Square {
    double height;
public:
    void setHeight(double h) { height = h; }
    double getHeight() const { return height; }
};
```

#### ❌ Problematic Design (violates LSP)

```cpp
class Rectangle {
    double width;
    double height;
public:
    virtual void setWidth(double w) { width = w; }
    virtual void setHeight(double h) { height = h; }
    double getWidth() const { return width; }
    double getHeight() const { return height; }
};

class Square : public Rectangle {
public:
    void setWidth(double s) {
        Rectangle::setWidth(s);
        Rectangle::setHeight(s);
    }

    void setHeight(double s) {
        Rectangle::setWidth(s);
        Rectangle::setHeight(s);
    }
};
```

- The derived `Square` forces equal width and height, which breaks the behavior expected from `Rectangle`.

---

### **5. Summary**

- Inheritance and polymorphism help create reusable and maintainable object-oriented code.
- Abstract interfaces and cloneable objects provide flexibility in design.

---

## **Part 2: Templates in C++**

### **1. What are Templates?**

- Templates let you **reuse code** for different types.
- Supports **generic programming** — write one version that works for any type.

---

### **2. Template Syntax**

```cpp
template <typename T>
void swap(T& a, T& b) {
    T temp = a;
    a = b;
    b = temp;
}
```

#### Example:

```cpp
int a = 10, b = 20;
double x = 1.1, y = 2.2;

swap(a, b);  // int
swap(x, y);  // double
```

---

### **3. Template Parameter Types**

- **Type Parameter**: generic type (e.g., `typename T`)
- **Non-Type Parameter**: constant values (e.g., array size)

```cpp
template <typename T, int SIZE>
class Array {
    T arr[SIZE];
public:
    void displaySize() const {
        std::cout << "Array size: " << SIZE << "\\n";
    }
};
```

#### Example:

```cpp
Array<int, 10> arr1;
Array<double, 20> arr2;
arr1.displaySize();  // Output: 10
arr2.displaySize();  // Output: 20
```

---

### **4. Function Templates**

```cpp
template <typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}
```

#### Example:

```cpp
std::cout << max(10, 20);       // int
std::cout << max(10.5, 7.5);    // double
std::cout << max('a', 'z');     // char
```

---

### **5. Class Templates**

```cpp
template <typename T>
class Array {
    T data[10];
public:
    void set(int index, T value) { data[index] = value; }
    T get(int index) const { return data[index]; }
};
```

#### Example:

```cpp
Array<int> intArray;
Array<double> doubleArray;

intArray.set(0, 42);
doubleArray.set(0, 3.14);

std::cout << intArray.get(0);     // Output: 42
std::cout << doubleArray.get(0);  // Output: 3.14
```

---

### **6. Template Specialization**

```cpp
template <typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}

// Specialized for const char*
template <>
const char* max(const char* a, const char* b) {
    return (strcmp(a, b) > 0) ? a : b;
}
```

#### Example:

```cpp
std::cout << max(5, 10);               // uses general template
std::cout << max("apple", "banana");  // uses specialization
```

---

### **7. Template Inheritance**

```cpp
template <typename T>
class Container {
protected:
    T value;
public:
    Container(T val) : value(val) {}
    T getValue() const { return value; }
};

template <typename T>
class NumberContainer : public Container<T> {
public:
    NumberContainer(T val) : Container<T>(val) {}
    void display() const {
        std::cout << "Value: " << this->value << "\\n";
    }
};
```

#### Example:

```cpp
NumberContainer<int> intBox(42);
intBox.display();  // Output: Value: 42
```

---
