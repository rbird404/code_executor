from executors import (
    GoExecutor,
    CppExecutor,
    PythonExecutor
)

# EXAMPLES
code = '''
n = input()
print(n)
'''

result = PythonExecutor(code).execute("Hello world!")
print(f"output = {result.output}")
print(f"errors = {result.errors}")


code = '''
package main

import "fmt"

func main() {
    fmt.Print("Enter text: ")
    var input string
    fmt.Scanln(&input)
    fmt.Print(input)
}
'''

result = GoExecutor(code).execute("Hello world!")
print(f"output = {result.output}")
print(f"errors = {result.errors}")


code = '''
#include <iostream>

int main() {
    std::cout << "Hello World!";
    return 0;
}
'''

result = CppExecutor(code).execute()
print(f"output = {result.output}")
print(f"errors = {result.errors}")
