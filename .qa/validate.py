from pathlib import Path
from html.parser import HTMLParser
import json, re
p = Path(__file__).parent.parent / "ai-assisted-development.html"
s = p.read_text(encoding="utf-8")
data = json.loads(re.search(r'<script id="slide-data" type="application/json">(.*?)</script>',s,re.S).group(1))
assert len(data) == 42
assert all(x["notes"] for x in data)
assert data[30]["title"] == "Discussion & Questions"
assert data[31]["title"] == "Connect & Materials"
assert data[31]["html"].count("data:image/png;base64,") == 3
assert len([x for x in data if x["kind"]=="deep"]) == 6
class ExternalRuntime(HTMLParser):
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag in ["script","img","iframe","audio","video","source"] and a.get("src") and not a.get("src").startswith("data:"):
            raise AssertionError((tag,a))
        if tag=="link" and a.get("rel") in ["stylesheet","preload","modulepreload"]:
            raise AssertionError((tag,a))
ExternalRuntime().feed(s)
assert not re.search(r'fetch\(|XMLHttpRequest|WebSocket|@import|url\(\s*https?://',s)
script=re.findall(r"<script>(.*?)</script>",s,re.S)[0]
(p.parent/".qa"/"runtime.js").write_text(script,encoding="utf-8")
print("PASS: 42 slides, complete notes, Questions/QR closing sequence, six supplemental slides, and no external runtime dependencies.")
# Confirm the presentation now contains JavaScript/React examples and their matching references.
deck_copy = json.dumps(data)
assert "Python" not in deck_copy
assert "sqlite" not in deck_copy.lower()
assert "JAVASCRIPT" in deck_copy
assert "node-postgres" in deck_copy
print("PASS: Code examples and supporting references consistently use React/JavaScript.")

