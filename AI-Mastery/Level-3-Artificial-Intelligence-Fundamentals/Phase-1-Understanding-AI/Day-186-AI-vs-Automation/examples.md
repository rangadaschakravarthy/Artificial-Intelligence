# Day 186 Worked Examples: AI vs Automation

## Example 1 — Practical: Automated File Backup vs AI File Router
```python
# Automation: Fixed Cron-style File Backup
def backup_files(source, dest):
    print(f"Copying all files from {source} to {dest} rigidly.")

# AI: Adaptive Content-Aware Classifier Router
def ai_route_file(file_content):
    if "invoice" in file_content.lower():
        return "Finance_Folder"
    elif "resume" in file_content.lower():
        return "HR_Folder"
    else:
        return "General_Folder"

print("AI File Router Destination:", ai_route_file("Candidate Resume Details"))
```
