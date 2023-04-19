# your task is to create all permutations of a non-empty input string and remove duplicates, if present.

# Create as many "shufflings" as you can!

# Examples:

# With input 'a':
# Your function should return: ['a']

# With input 'ab':
# Your function should return ['ab', 'ba']

# With input 'abc':
# Your function should return ['abc','acb','bac','bca','cab','cba']

# With input 'aabb':
# Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
# Note: The order of the permutations doesn't matter.
def permutations(s):
    seen = set()
    if len(s) <= 1:
        yield s
    else:
        for i, c in enumerate(s):
            for p in permutations(s[:i] + s[i+1:]):
                perm = c + p
                if perm not in seen:
                    seen.add(perm)
                    yield perm