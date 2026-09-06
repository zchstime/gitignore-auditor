import tempfile, unittest, subprocess
from pathlib import Path
from gitignore_auditor.__main__ import audit
class Tests(unittest.TestCase):
 def test_tracked_env(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d); subprocess.run(["git","init","-q",p],check=True); (p/".env").write_text("DEMO=synthetic"); subprocess.run(["git","-C",p,"add","-f",".env"],check=True)
   rows=audit(p); self.assertIn("tracked-risk",{x["rule"] for x in rows})
if __name__=="__main__": unittest.main()
