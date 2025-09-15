import os, json

# Make sure folder exists
os.makedirs("data/annotated_dataset", exist_ok=True)

# Example dataset with misconception
example_data = [
    {
        "code": "def my_function():\n    x=10\n    return x\n\nprint(x)",
        "error_types": ["NameError"],
        "misconceptions": ["variable_scope"],
        "skill_level": "beginner"
    },
    {
        "code": "def modify_list(lst):\n    lst.append(4)\n    return lst\n\noriginal=[1,2,3]\nnew_list=modify_list(original)\nprint(original)",
        "error_types": [],
        "misconceptions": ["mutability_confusion"],
        "skill_level": "intermediate"
    }
]

# Save dataset
with open("data/annotated_dataset/example.json", "w") as f:
    json.dump(example_data, f, indent=2)

print("Dataset saved to data/annotated_dataset/example.json")