import re

with open('index.html', 'r') as f:
    content = f.read()

changes = 0

def patch(old, new, label):
    global content, changes
    if old in content:
        content = content.replace(old, new)
        print(f"✓ {label}")
        changes += 1
    else:
        print(f"✗ {label} — pattern non trouvé")

# ── Ajoute tes patches ici ──────────────────────────────────
# patch("ancien texte", "nouveau texte", "description")
# ────────────────────────────────────────────────────────────

with open('index.html', 'w') as f:
    f.write(content)

print(f"\n{changes} modification(s) appliquée(s)")
