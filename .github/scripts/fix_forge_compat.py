from pathlib import Path

root = Path("source/Masterme4aClient-Forge-1.17.1/src/main/java/com/masterme4a/client")

def edit(name, replacements):
    path = root / name
    text = path.read_text(encoding="utf-8")
    for old, new in replacements:
        if old not in text:
            raise SystemExit(f"Expected code not found in {name}: {old!r}")
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")

edit("ClientKeybinds.java", [
    ("import net.minecraftforge.client.ClientRegistry;", "import net.minecraftforge.fmlclient.registry.ClientRegistry;")
])

edit("FriendsScreen.java", [
    (" nameField.setHint(new TextComponent(\"Ник игрока\"));", ""),
    ("rebuildWidgets();", "clearWidgets(); init();")
])

edit("ClientRadar.java", [
    ("player.yRot", "player.getYRot()")
])

print("Applied Forge 1.17.1 compatibility fixes.")
