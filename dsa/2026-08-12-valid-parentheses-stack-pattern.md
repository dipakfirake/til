# Valid Parentheses - Stack Pattern

> _2026-08-12_ | Category: **dsa**

Classic stack problem.

```java
public boolean isValid(String s) {
    Stack<Character> stack = new Stack<>();
    Map<Character,Character> pairs = Map.of(')', '(', '}', '{', ']', '[');
    
    for (char c : s.toCharArray()) {
        if (pairs.containsValue(c)) {
            stack.push(c); // opening bracket
        } else if (pairs.containsKey(c)) {
            if (stack.isEmpty() || stack.pop() != pairs.get(c)) return false;
        }
    }
    return stack.isEmpty();
}

// Examples:
// "([])" → true
// "([)]" → false
// "{}" → true
```

### Stack Pattern Problems
- Valid parentheses
- Next greater element
- Min stack
- Evaluate reverse polish notation
- Largest rectangle in histogram

**Key Takeaway**: Whenever you need to match pairs, or track "nearest previous", think Stack.
