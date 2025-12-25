import os
import re

BASE = "pattern_problems"

def cpp_filename(title):
    return re.sub(r'[^a-zA-Z0-9]+', '_', title).strip('_') + ".cpp"

def cpp_template(link):
    return f"""// {link}

class Solution {{
public:
}};
"""

PATTERNS = {
    "Arrays & Strings": [
        ("Two Sum", "https://leetcode.com/problems/two-sum/"),
        ("Move Zeroes", "https://leetcode.com/problems/move-zeroes/"),
        ("Rotate Image", "https://leetcode.com/problems/rotate-image/"),
        ("Sort Colors", "https://leetcode.com/problems/sort-colors/"),
        ("Trapping Rain Water", "https://leetcode.com/problems/trapping-rain-water/"),
        ("Container With Most Water", "https://leetcode.com/problems/container-with-most-water/"),
        ("Subarray Sum Equals K", "https://leetcode.com/problems/subarray-sum-equals-k/"),
        ("Maximum Subarray", "https://leetcode.com/problems/maximum-subarray/"),
        ("Longest Substring Without Repeating Characters", "https://leetcode.com/problems/longest-substring-without-repeating-characters/"),
        ("Maximum Points You Can Obtain from Cards", "https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/")
    ],

    "Linked List": [
        ("Reverse Linked List", "https://leetcode.com/problems/reverse-linked-list/"),
        ("Merge Two Sorted Lists", "https://leetcode.com/problems/merge-two-sorted-lists/"),
        ("Merge k Sorted Lists", "https://leetcode.com/problems/merge-k-sorted-lists/"),
        ("Linked List Cycle II", "https://leetcode.com/problems/linked-list-cycle-ii/")
    ],

    "Stack & Queue": [
        ("Min Stack", "https://leetcode.com/problems/min-stack/"),
        ("Sliding Window Maximum", "https://leetcode.com/problems/sliding-window-maximum/"),
        ("Task Scheduler", "https://leetcode.com/problems/task-scheduler/"),
        ("Daily Temperatures", "https://leetcode.com/problems/daily-temperatures/")
    ],

    "Binary Search & Greedy": [
        ("First Bad Version", "https://leetcode.com/problems/first-bad-version/"),
        ("Jump Game II", "https://leetcode.com/problems/jump-game-ii/"),
        ("Cheapest Flights Within K Stops", "https://leetcode.com/problems/cheapest-flights-within-k-stops/"),
        ("Maximum Profit in Job Scheduling", "https://leetcode.com/problems/maximum-profit-in-job-scheduling/"),
        ("Furthest Building You Can Reach", "https://leetcode.com/problems/furthest-building-you-can-reach/")
    ],

    "Trees & Graphs": [
        ("Number of Islands", "https://leetcode.com/problems/number-of-islands/"),
        ("Course Schedule II", "https://leetcode.com/problems/course-schedule-ii/"),
        ("Clone Graph", "https://leetcode.com/problems/clone-graph/"),
        ("Diameter of Binary Tree", "https://leetcode.com/problems/diameter-of-binary-tree/"),
        ("Convert Sorted Array to Binary Search Tree", "https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/"),
        ("Unique Binary Search Trees II", "https://leetcode.com/problems/unique-binary-search-trees-ii/"),
        ("Distribute Coins in Binary Tree", "https://leetcode.com/problems/distribute-coins-in-binary-tree/"),
        ("Trim a Binary Search Tree", "https://leetcode.com/problems/trim-a-binary-search-tree/"),
        ("Binary Tree Maximum Path Sum", "https://leetcode.com/problems/binary-tree-maximum-path-sum/"),
        ("Delete Nodes And Return Forest", "https://leetcode.com/problems/delete-nodes-and-return-forest/"),
        ("Populate Next Right Pointers in Each Node II", "https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/"),
        ("Reconstruct Itinerary", "https://leetcode.com/problems/reconstruct-itinerary/")
    ],

    "Heaps & Priority Queues": [
        ("Top K Frequent Elements", "https://leetcode.com/problems/top-k-frequent-elements/"),
        ("Process Tasks Using Servers", "https://leetcode.com/problems/process-tasks-using-servers/"),
        ("Stock Price Fluctuation", "https://leetcode.com/problems/stock-price-fluctuation/"),
        ("Car Pooling", "https://leetcode.com/problems/car-pooling/"),
        ("Bus Routes", "https://leetcode.com/problems/bus-routes/")
    ],

    "Dynamic Programming & Backtracking": [
        ("Combination Sum", "https://leetcode.com/problems/combination-sum/"),
        ("Coin Change II", "https://leetcode.com/problems/coin-change-ii/"),
        ("Word Search II", "https://leetcode.com/problems/word-search-ii/"),
        ("Longest Increasing Subsequence", "https://leetcode.com/problems/longest-increasing-subsequence/"),
        ("Longest Increasing Path in a Matrix", "https://leetcode.com/problems/longest-increasing-path-in-a-matrix/")
    ],

    "Tries & Advanced Structures": [
        ("Implement Trie Prefix Tree", "https://leetcode.com/problems/implement-trie-prefix-tree/"),
        ("Group Anagrams", "https://leetcode.com/problems/group-anagrams/"),
        ("Maximum Profit in Job Scheduling", "https://leetcode.com/problems/maximum-profit-in-job-scheduling/"),
        ("Maximum Points You Can Obtain from Cards", "https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/"),
        ("Stock Price Fluctuation", "https://leetcode.com/problems/stock-price-fluctuation/")
    ]
}

os.makedirs(BASE, exist_ok=True)

# README
with open(os.path.join(BASE, "README.md"), "w") as readme:
    readme.write(
"""# Pattern-Based LeetCode Problems

Here’s the list I wish someone gave me earlier — so you don’t waste time like I did.

This collection focuses on **patterns**, not random problem solving.
If you master these, most interview problems will feel familiar.

---

## How to Use This List
- Solve **pattern-wise**, not problem-wise
- Identify the underlying technique
- Revisit this list before interviews

---

"""
    )

    count = 1
    for pattern, problems in PATTERNS.items():
        readme.write(f"## {pattern}\n")
        for title, link in problems:
            readme.write(f"{count}. [{title}]({link})\n")
            count += 1
        readme.write("\n")

# CPP files
for problems in PATTERNS.values():
    for title, link in problems:
        with open(os.path.join(BASE, cpp_filename(title)), "w") as cpp:
            cpp.write(cpp_template(link))

print("Pattern problems folder generated successfully.")
