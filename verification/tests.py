"""
TESTS is a dict with all you tests.
Keys for this will be categories" names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it"s using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [1],
            "answer": 1,
            "explanation": [1],
        },
        {
            "input": [3],
            "answer": 2, 
            "explanation": [2, 1, 0],
        },
        {
            "input": [5],
            "answer": 3, 
            "explanation": [3, 1, 1, 0, 0, 0],
        },
        {
            "input": [10],
            "answer": 6,
            "explanation": [3, 2, 2, 1, 1, 1],
        },
    ],
    "Extra": [
        {
            "input": [18],
            "answer": 8,
            "explanation": [4, 3, 3, 2, 2, 2, 1, 1, 0, 0],
        },
        {
            "input": [27],
            "answer": 10,
            "explanation": [5, 4, 4, 3, 3, 3, 2, 1, 1, 1, 0, 0, 0, 0, 0],
        },
        {
            "input": [40],
            "answer": 15,
            "explanation": [6, 5, 5, 4, 4, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        },
        {
            "input": [40],
            "answer": 15,
            "explanation": [6, 5, 5, 4, 4, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        },
        {
            "input": [53],
            "answer": 18,
            "explanation": [6, 5, 5, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0],
        },
        {
            "input": [64],
            "answer": 21,
            "explanation": [7, 6, 6, 5, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        },
        {
            "input": [74],
            "answer": 21,
            "explanation": [7, 6, 6, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        },
        {
            "input": [85],
            "answer": 28,
            "explanation": [8, 6, 6, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        },
        {
            "input": [90],
            "answer": 28,
            "explanation": [8, 7, 7, 6, 6, 6, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        },
        {
            "input": [102],
            "answer": 28,
            "explanation": [8, 7, 7, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        },
        {
            "input": [117],
            "answer": 33,
            "explanation": [8, 7, 7, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0],
        },
        {
            "input": [124],
            "answer": 36,
            "explanation": [9, 8, 8, 7, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        },
        {
            "input": [134],
            "answer": 36,
            "explanation": [9, 8, 8, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        },
        {
            "input": [148],
            "answer": 36,
            "explanation": [9, 8, 8, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        },
        {
            "input": [152],
            "answer": 36,
            "explanation": [9, 8, 8, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        },
        {
            "input": [161],
            "answer": 41,
            "explanation": [9, 8, 8, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        },
        {
            "input": [179],
            "answer": 45,
            "explanation": [10, 9, 9, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 5, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        },
        {
            "input": [190],
            "answer": 45,
            "explanation": [10, 9, 9, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        },
        {
            "input": [198],
            "answer": 45,
            "explanation": [10, 9, 9, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        },
        {
            "input": [10000],
            "answer": 741,
        },
        {
            "input": [99999],
            "answer": 3486,
        },
    ]
}
