import argparse, fnmatch, json, subprocess
from pathlib import Path

RISKS={".env":"environment secrets","*.pem":"private key material","id_rsa":"SSH private key","*.pyc":"Python bytecode",".DS_Store":"macOS metadata","node_modules/*":"installed Node dependencies","dist/*":"build output","*.log":"runtime logs"}
def patterns(root):
 p=Path(root)/".gitignore"; return [x.strip() for x in p.read_text().splitlines() if x.strip() and not x.lstrip().startswith("#")] if p.exists() else []
def tracked(root):
 r=subprocess.run(["git","-C",str(root),"ls-files"],capture_output=True,text=True); return r.stdout.splitlines() if r.returncode==0 else []
def audit(root):
 root=Path(root); ignored=patterns(root); files=tracked(root); findings=[]
 for glob,reason in RISKS.items():
  matches=[x for x in files if fnmatch.fnmatch(x,glob) or fnmatch.fnmatch(Path(x).name,glob)]
  if matches: findings.append({"severity":"error","rule":"tracked-risk","pattern":glob,"reason":reason,"files":matches[:5]})
  if not any(fnmatch.fnmatch(glob,p) or p==glob for p in ignored): findings.append({"severity":"info","rule":"missing-rule","pattern":glob,"reason":reason,"files":[]})
 return findings
def markdown(rows): return "# Gitignore Audit\n\n"+("\n".join(f"- **{x['severity'].upper()}** `{x['pattern']}` — {x['rule']}: {x['reason']}" for x in rows) or "✅ No findings.")+"\n"
def main(argv=None):
 p=argparse.ArgumentParser(description="Audit tracked risks and missing gitignore rules"); p.add_argument("repo"); p.add_argument("--json",action="store_true"); p.add_argument("--output")
 a=p.parse_args(argv); rows=audit(a.repo); text=json.dumps(rows,indent=2) if a.json else markdown(rows); Path(a.output).write_text(text) if a.output else print(text); return 1 if any(x["severity"]=="error" for x in rows) else 0
if __name__=="__main__": raise SystemExit(main())
