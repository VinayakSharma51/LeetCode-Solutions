import os
import re

README_FILE = "README.md"

# Count problems by difficulty
counts = {
    "Easy": 0,
    "Medium": 0,
    "Hard": 0
}

# Walk through all folders
for root, _, files in os.walk("."):
    folder = os.path.basename(root)

    if folder in counts:
        for file in files:
            if file.endswith(".py"):
                counts[folder] += 1

total = counts["Easy"] + counts["Medium"] + counts["Hard"]

# New markdown table
progress_table = f"""| Difficulty | Solved |
|------------|-------:|
| 🟢 Easy | {counts['Easy']} |
| 🟡 Medium | {counts['Medium']} |
| 🔴 Hard | {counts['Hard']} |
| **Total** | **{total}** |"""

# Read README
with open(README_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Replace content between markers
pattern = r"<!-- START_PROGRESS -->.*?<!-- END_PROGRESS -->"

replacement = f"""<!-- START_PROGRESS -->

{progress_table}

<!-- END_PROGRESS -->"""

updated = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Write back
with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(updated)

print("✅ README updated successfully!")
print(f"Easy   : {counts['Easy']}")
print(f"Medium : {counts['Medium']}")
print(f"Hard   : {counts['Hard']}")
print(f"Total  : {total}")
