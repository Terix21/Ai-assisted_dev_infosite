from pathlib import Path
from html.parser import HTMLParser
import json, re
p = Path(__file__).parent.parent / "ai-assisted-development.html"
s = p.read_text(encoding="utf-8")
data = json.loads(re.search(r'<script id="slide-data" type="application/json">(.*?)</script>',s,re.S).group(1))
assert len(data) == 41
assert all(x["notes"] for x in data)
assert data[30]["title"] == "Q&A"
assert len([x for x in data if x["kind"]=="deep"]) == 6
class ExternalRuntime(HTMLParser):
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag in ["script","img","iframe","audio","video","source"] and a.get("src"):
            raise AssertionError((tag,a))
        if tag=="link" and a.get("rel") in ["stylesheet","preload","modulepreload"]:
            raise AssertionError((tag,a))
ExternalRuntime().feed(s)
assert not re.search(r'fetch\(|XMLHttpRequest|WebSocket|@import|url\(\s*https?://',s)
script=re.findall(r"<script>(.*?)</script>",s,re.S)[0]
(p.parent/".qa"/"runtime.js").write_text(script,encoding="utf-8")
print("PASS: 41 slides, complete notes, Q&A boundary, six supplemental slides, no external runtime dependencies.")
# A print-layout proof using exactly the checklist's print rules.
css=re.search(r"<style>(.*?)</style>",s,re.S).group(1)
print_css=css.split("@media print{",1)[1].rstrip()[:-1]
check=re.search(r'(<dialog id="checklist".*?</dialog>)',s,re.S).group(1).replace('<dialog id="checklist"','<section id="printChecklist"').replace('</dialog>','</section>')
proof='<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Checklist print proof</title><style>'+css+'\n'+print_css+'\nbody{width:725px;margin:24px auto!important}#printChecklist{overflow:visible!important}</style></head><body class="print-check">'+check+'</body></html>'
(p.parent/".qa"/"checklist-print-proof.html").write_text(proof,encoding="utf-8")
# Confirm the presentation now contains JavaScript/React examples and their matching references.
deck_copy = json.dumps(data)
assert "Python" not in deck_copy
assert "sqlite" not in deck_copy.lower()
assert "JAVASCRIPT" in deck_copy
assert "node-postgres" in deck_copy
print("PASS: Code examples and supporting references consistently use React/JavaScript.")

