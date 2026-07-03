# Go Channels

> _2026-07-04_ | Category: **go**

Communicate between goroutines safely.

```go
package main
import "fmt"

func sum(s []int, c chan int) {
    sum := 0
    for _, v := range s {
        sum += v
    }
    c <- sum // send sum to channel
}

func main() {
    s := []int{7, 2, 8, -9, 4, 0}
    
    // Create an unbuffered channel of ints
    c := make(chan int)
    
    go sum(s[:len(s)/2], c)
    go sum(s[len(s)/2:], c)
    
    // Receive from channel (blocks until data is ready)
    x, y := <-c, <-c 
    
    fmt.Println(x, y, x+y)
}
```

**Go Proverb**: "Don't communicate by sharing memory; share memory by communicating." Channels avoid race conditions by passing data.
