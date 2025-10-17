#!/usr/bin/env python3

with open('admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Entferne die überflüssigen schließenden divs nach dem E-Mail-Tab
# Der E-Mail-Tab sollte nur mit einem </div> enden
content = content.replace("""            </div>

                    
        </div>
    </div>

                    
                
           </div>
        </div>""", """            </div>""")

# Speichere die korrigierte Version
with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML-Struktur korrigiert")
