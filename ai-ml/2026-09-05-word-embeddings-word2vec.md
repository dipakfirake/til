# Word Embeddings (Word2Vec)

> _2026-09-05_ | Category: **ai-ml**

Representing words as numbers.

Machine learning models only understand numbers.
- **One-hot encoding**: [0,0,1,0...] (Sparse, no semantic meaning).
- **Embeddings**: Dense vectors where distance represents semantic similarity.

If "King" is [0.9, 0.1, 0.5], "Man" is [0.8, 0.1, 0.4].
Famous vector math: `King - Man + Woman ≈ Queen`

**Key Takeaway**: Embeddings capture meaning. Modern models generate context-aware embeddings (the embedding for "bank" depends on if it's "river bank" or "bank account").
