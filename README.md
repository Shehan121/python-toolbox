# python-toolbox

Small, dependency-free Python utilities. Every module is pure standard library,
and every public function carries a doctest that doubles as its example.

## Install

There is nothing to install. Copy the module you need, or clone the repo and
import from `toolbox`.

```python
from toolbox.levenshtein import levenshtein
from toolbox.intervals import merge
```

## Modules

| Module | What it provides |
| --- | --- |
| `binary_search` | `binary_search`, `bisect_left` over sorted sequences |
| `bloom` | `BloomFilter` — probabilistic membership, no false negatives |
| `intervals` | `merge`, `intersect`, `total_length` for closed intervals |
| `iterutils` | `flatten`, `chunked`, `unique` — lazy iterator helpers |
| `levenshtein` | `levenshtein` edit distance, `similarity` ratio |
| `lru` | `LRUCache` — fixed-capacity cache with O(1) get/put |
| `memoize` | `memoize` decorator with an optional TTL |
| `quicksort` | `quicksort` — in place, median-of-three pivot |
| `retry` | `retry` decorator with exponential backoff and jitter |
| `rle` | `encode` / `decode` run-length encoding |
| `roman` | `to_roman` / `from_roman` numeral conversion |
| `sieve` | `primes_below`, `factorise` |
| `stats` | `mean`, `median`, `stdev`, `percentile` |
| `toposort` | `toposort` with `CycleError` detection |
| `trie` | `Trie` — prefix tree with prefix enumeration |
| `union_find` | `UnionFind` — disjoint sets with path compression |

## Running the tests

```bash
python run_doctests.py
```

This imports every module under `toolbox/` and runs its doctests, exiting
non-zero if any fail.

## Design notes

- **No dependencies.** Nothing here imports outside the standard library.
- **Doctests as documentation.** The example in a docstring is the test, so the
  documentation cannot drift from the behaviour.
- **Bounded recursion.** Recursive algorithms recurse into the smaller half
  where it matters, keeping stack depth logarithmic.

## Licence

MIT.
