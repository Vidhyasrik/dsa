"""
LeetCode#1189
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" 
as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.
"""
# Method#1
from collections import defaultdict, Counter
def maxNumberOfBalloons(text: str):
    counter = defaultdict(int)
    balloon = "balloon"

    for c in text:
        if c in balloon:
            counter[c] += 1
    if any(c not in counter for c in balloon):
        return 0
    else:
        return min(counter["b"], counter["a"], counter["l"] // 2, counter["o"] // 2, counter["n"])
print(maxNumberOfBalloons("loonbalxballpoon"))  # Output: 2

# Method#2

def maxNumberOfBalloons(text: str):
    balloon_counts = Counter("balloon")  # Counts of characters in "balloon"
    text_counts = Counter(text)        # Counts of characters in the input text
    print(f"balloon_counts:=>{balloon_counts}")
    print(f"text_counts:=>{balloon_counts}")
    print(f"div:=>{[text_counts[c] // balloon_counts[c] for c in balloon_counts]}")
    return min(text_counts[c] // balloon_counts[c] for c in balloon_counts)

print(maxNumberOfBalloons("loonbalxballpoon"))  # Output: 2


