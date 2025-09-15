import os

def create_structure():
    dirs = [
        "data/raw_code_samples",
        "data/annotated_dataset",
        "src",
        "notebooks",
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print("📁 Created:", d)

if __name__ == "__main__":
    create_structure()
    print("Project setup complete")