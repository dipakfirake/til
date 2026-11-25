# Go Basics - Syntax and Types

> _2026-11-25_ | Category: **go**

Fast, compiled, statically typed.

```go
package main

import "fmt"

func main() {
    // Variables
    var name string = "Dipak"
    age := 25 // Short declaration, infers type
    
    // Arrays (fixed) & Slices (dynamic)
    arr := [3]int{1, 2, 3}
    slice := []int{1, 2, 3, 4}
    slice = append(slice, 5)
    
    // Maps
    ages := map[string]int{"Alice": 30, "Bob": 25}
    ages["Charlie"] = 35
    
    // Loops (only 'for' exists in Go)
    for i := 0; i < 5; i++ {
        fmt.Println(i)
    }
    
    // Range loop
    for key, val := range ages {
        fmt.Printf("%s is %d\n", key, val)
    }
}
```
