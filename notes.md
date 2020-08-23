
# C++ Notes

## Pointers

* Pointers are used to point to a place in memory where a value is being held
* References are used to refer to a value in memory, but are not equivalent to a pointer!

## Classes

* Used to group data & functions together

```cpp
#include <iostream>

class Player 
{
  public:
    int x, y;
    int speed;

    void Move(int xa, int ya)
    {
      x += xa * speed;
      y += ya * speed;
    }
};

int main() 
{
  // Player object
  Player player;
  player.move(1, -1);

  cin.get();
}
```

### Writing a basic logging class

> This literally is not how you would write any type of loggin class,
> but is used to represent a class in a simple manner.

```cpp
#include <iostream>

using namespace std;

class Log
{
  public:
    const int LogLevelError = 0;
    const int LogLevelWarning = 1;
    const int LogLevelInfo = 2;
  private:
    int m_LogLevel = LogLevelInfo;
  public:
    void SetLevel(int level)
    {
      m_LogLevel = level;
    }

    void Err(const char* message)
    {
      if (m_LogLevel >= LogLevelError)
        cout << "[Error]: " << message << endl;
    }

    void Info(const char* message)
    {
      if (m_LogLevel >= LogLevelInfo)
        cout << "[Info]: " << message << endl;
    }

    void Warn(const char* message)
    {
      if (m_LogLevel >= LogLevelWarning)
        cout << "[Warn]: " << message << endl;
    }

};

int main() 
{
  Log log;
  log.SetLevel(log.LogLevelError);
  log.Err("oof!");
  cin.get();
}
```


## Classes vs Structs

* Structs and classes are basically the same, except for some visibility differences.
* A class is private by default, whereas a struct is public by default.

## Static Keyword

### Outside of classes or structs

* Without the static keywords, global variables cannot share the same name
* If they do, you must use the ```extern``` keyword to refer to the original variable.

Static.cpp
```cpp
static int s_Variable = 5;

static void Function() 
{
  //
}
```

Main.cpp
```cpp
#include <iostream>

using namespace std;

int s_Variable = 10;

void Function()
{
  //
}

int main()
{
  cout << s_Variable << endl;
  cin.get();
}
```


## Enums

* A method of giving a name to a set of values.
* Allows restriction of assignment when using the enum as a type.

```cpp
#include <iostream>

// You can assign enum's specific types
enum Example : unsigned char
{
  A, B, C
};

int main()
{
  Example value = B;

  if (value == B)
  {
    // Do something
  }
}
```

## Arrays

* A collection of values assigned as a single variable.
* Data is stored contiguously (one after the other).
* Is actually an integer pointer to a collection of values. 

```cpp
#include <iostream>

int main()
{
  // Declare array
  int example[5];
  int* ptr = example;

  // Access array
  example[0] = 5;

  // Print value from array
  cout << example[0] << endl;

  // For loops are useful for arrays
  for (int i = 0; i < 5; ++i) {
    cout << example[i] << endl;
  }

  example[2] = 5;

  // An array can also be accessed using pointer arithmetics.
  *(ptr + 2) = 6;

  cin.get();
}
```

## Strings

* A method of grouping characters to be represented as text.
* A character is represented in 1 byte.
* A wide string is represented in 2 bytes.
* A string is basically an array of characters.
* Termination char is ``'\0'``.

```cpp
#include <iostream>
#include <string>

int main()
{
  // The old school C method.
  const char* name = "Bob";

  // The new cool C++ method.
  string name2 = "Bob";

  // Find if the string contains certain chars.
  bool contains = name2.find("ob") != string.npos;
}
```

### String Literals

* A string literal is a series of characters in between double quotes
* String literals are stored in read-only memory.

```cpp
int main() 
{
  // This is a const char[]
  "Bob";
}
```

## Const

* A keyword to specify a variable is non-modifiable.

```cpp
int main()
{
  // You CANNOT change the value of a const.
  const int MAX_AGE = 99;
  const int* age = 20;

  *a = 2;
}
```

## Ternary Operators

* A quick alternative to if statements

```cpp
int main()
{
  int speed = 10;
  int level = 5;

  if (level > 10) {
    speed = 5;
  }
  else {
    speed = 10;
  }

  // This does the above
  speed = level > 10 ? 5 : 10;

  // Used for simple assignment
  string rank = level > 10 ? "Master" : "Beginner";
}
```

## Smart Pointers

* Smart pointers are used to automatically assign and delete heap memory

### Unique Pointer

* A scoped pointer that is destroyed once out of scope.
* Will automatically delete itself once out of scope.
* You cannot copy unique pointers.

```cpp
#include <memory>

int main()
{
  {
    // Exclusive to this scope!
    unique_ptr<Entity> entity = make_unique<Entity>();
  }
  // Cannot access the above as it is outside of its scope
  cout << entity << endl;
}
```

## Arrow Operator

* A shortcut for calling functions from pointers

```cpp
int main()
{
  Entity e;
  e.Print();

  Entity* ptr = &e;

  ptr->Print();
}
```

## Namespacing

* You don't have to use ``namespace std;``

```cpp
#include <iostream>

using std::cout;
using std::cin;
using std::endl;

int main()
{
  int a = 1;

  cout << a << endl;
}
```
