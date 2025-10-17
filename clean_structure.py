#!/usr/bin/env python3

# Restore from backup first
import shutil
shutil.copy('admin.html.backup_structure_fix', 'admin.html')

with open('admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the misplaced Logen-Übersicht section (it's between tabs)
import re

# Find and remove the Logen-Übersicht that's misplaced
pattern = r'<!-- Logen-Übersicht -->.*?</div>\s*</div>\s*<!-- Präferenz-Übersicht -->'
content = re.sub(pattern, '', content, flags=re.DOTALL)

# Write the cleaned version
with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Misplaced sections removed")
