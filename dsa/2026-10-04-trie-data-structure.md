# Trie Data Structure

> _2026-10-04_ | Category: **dsa**

Efficient prefix search and autocomplete.

```java
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd = false;
}

class Trie {
    TrieNode root = new TrieNode();
    
    void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int i = c - 'a';
            if (node.children[i] == null) node.children[i] = new TrieNode();
            node = node.children[i];
        }
        node.isEnd = true;
    }
    
    boolean search(String word) {
        TrieNode node = find(word);
        return node != null && node.isEnd;
    }
    
    boolean startsWith(String prefix) { return find(prefix) != null; }
    
    private TrieNode find(String s) {
        TrieNode node = root;
        for (char c : s.toCharArray()) {
            node = node.children[c - 'a'];
            if (node == null) return null;
        }
        return node;
    }
}
```

**Use cases**: Autocomplete, spell checker, IP routing, word games.
