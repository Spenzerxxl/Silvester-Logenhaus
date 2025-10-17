#!/usr/bin/env python3

with open('admin.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Finde die Logen-Übersicht und verschiebe sie ans Ende vor dem Script-Tag
new_lines = []
logen_section = []
in_logen_section = False
logen_depth = 0

for i, line in enumerate(lines):
    if '<!-- Logen-Übersicht -->' in line:
        in_logen_section = True
        logen_section.append(line)
        # Track div depth to know when section ends
        logen_depth = 0
        continue
    
    if in_logen_section:
        logen_section.append(line)
        if '<div' in line:
            logen_depth += line.count('<div')
        if '</div>' in line:
            logen_depth -= line.count('</div>')
        
        # Section ends when we're back at depth 0 after having content
        if logen_depth == 0 and len(logen_section) > 10:
            in_logen_section = False
            # Add closing divs for the container structure
            new_lines.append('        </div>\n')  # Close tab container
            new_lines.append('    </div>\n')  # Close dashboard
            new_lines.append('\n')
            # Now add the Logen section
            new_lines.extend(logen_section)
            logen_section = []
        continue
    
    if not in_logen_section:
        new_lines.append(line)

# Write the fixed version
with open('admin.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Tab-Struktur korrigiert")
