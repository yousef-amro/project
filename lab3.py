# Function 1: Unique In Order

def unique_in_order(values):
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


print("Function 1")
print(unique_in_order([3, 1, 3, 2, 1]))
print(unique_in_order("banana"))
print()


# Function 2: Word Frequencies

def word_frequencies(text):
    counts = {}
    for word in text.lower().split():
        word = word.strip(".,;:!?")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


print("Function 2")
print(word_frequencies("The cat. the HAT!"))
print(word_frequencies(""))
print()


# Function 3: Top K

def top_k(frequencies, k):
    ordered = sorted(frequencies.items(), key=lambda pair: (-pair[1], pair[0]))
    return ordered[:k]


print("Function 3")
print(top_k({"b": 2, "a": 3, "c": 5}, 2))
print()


# Function 4: Transpose

def transpose(matrix):
    if not matrix:
        return []
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


print("Function 4")
print(transpose([[1, 2, 3], [4, 5, 6]]))
print(transpose([]))
print()


# Function 5: Invert

def invert(mapping):
    result = {}
    for key, value in mapping.items():
        result.setdefault(value, []).append(key)
    for keys in result.values():
        keys.sort()
    return result


print("Function 5")
print(invert({"a": 1, "b": 2, "c": 1}))
print()


# Function 6: Common Elements

def common_elements(first, second):
    return sorted(set(first) & set(second))


print("Function 6")
print(common_elements([3, 1, 2, 3], [3, 4, 1]))
print()


# Function 7: Group By Length

def group_by_length(words):
    groups = {}
    for word in words:
        groups.setdefault(len(word), []).append(word)
    return groups


print("Function 7")
print(group_by_length(["hi", "sun", "to", "sky"]))
print()


# Function 8: Bag

class Bag:
    def __init__(self, items=()):
        self._counts = {}
        self._size = 0
        for item in items:
            self.add(item)

    def add(self, item):
        self._counts[item] = self._counts.get(item, 0) + 1
        self._size += 1

    def remove(self, item):
        if item not in self._counts:
            raise KeyError(item)
        self._counts[item] -= 1
        if self._counts[item] == 0:
            del self._counts[item]
        self._size -= 1

    def count(self, item):
        return self._counts.get(item, 0)

    def distinct(self):
        return len(self._counts)

    def __len__(self):
        return self._size

    def __contains__(self, item):
        return item in self._counts

    def __iter__(self):
        for item, times in self._counts.items():
            for _ in range(times):
                yield item

    def __eq__(self, other):
        if not isinstance(other, Bag):
            return NotImplemented
        return self._counts == other._counts

    def __repr__(self):
        return f"Bag({sorted(self)!r})"


print("Function 8")
b = Bag(["a", "b", "a"])
print(len(b))
print(b.count("a"))
print(b.count("z"))
print("b" in b)
b.add("z")
b.remove("a")
print(b.distinct())
print(sorted(b))
print(Bag("aab") == Bag("aba"))
print(repr(Bag()))
print(b)
print()


# Function 9: Countdown

def countdown(n):
    while n > 0:
        yield n
        n -= 1


print("Function 9")
print(list(countdown(3)))
print(list(countdown(0)))
print()


# Function 10: Chunks

def chunks(values, size):
    if size < 1:
        raise ValueError("size must be at least 1")
    for start in range(0, len(values), size):
        yield values[start:start + size]


print("Function 10")
print(list(chunks([1, 2, 3, 4, 5], 2)))
