import os
import json
import subprocess
import shutil
import sys
import webbrowser
import time

print("============================================")
print("Tailwind CSS Project Setup (Python version)")
print("============================================")

# --- Step 0: Locate npm command ---
npm_path = shutil.which("npm")
if npm_path is None:
    default_path = r"C:\Program Files\nodejs\npm.cmd"
    if os.path.exists(default_path):
        npm_path = default_path
    else:
        print("Could not find npm. Make sure Node.js is installed and in PATH.")
        sys.exit(1)
print(f"Found npm at: {npm_path}")

# --- Step 1: Initialize npm project ---
print("\n[1/8] Initializing npm project...")
subprocess.run([npm_path, "init", "-y"], check=True)

# --- Step 2: Install TailwindCSS and CLI ---
print("\n[2/8] Installing TailwindCSS and CLI...")
subprocess.run([npm_path, "install", "tailwindcss", "@tailwindcss/cli"], check=True)

# --- Step 3: Create src/input.css ---
print("\n[3/8] Creating src/input.css...")
os.makedirs("src", exist_ok=True)
with open("src/input.css", "w", encoding="utf-8") as f:
    f.write('@import "tailwindcss";\n')

# --- Step 4: Write custom package.json ---
print("\n[4/8] Writing package.json...")
package_json = {
    "name": "tailwind5",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1",
        "start": "npx @tailwindcss/cli -i ./src/input.css -o ./src/output.css --watch"
    },
    "keywords": [],
    "author": "",
    "license": "ISC",
    "type": "commonjs",
    "dependencies": {
        "@tailwindcss/cli": "^4.1.16",
        "tailwindcss": "^4.1.16"
    }
}
with open("package.json", "w", encoding="utf-8") as f:
    json.dump(package_json, f, indent=2)

# --- Step 5: Create src/index.html ---
print("\n[5/8] Creating src/index.html...")
html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Document</title>
  <link href="./output.css" rel="stylesheet">
</head>
<body>
  <h1 class="text-3xl font-bold underline text-blue-600">Hello Tailwind!</h1>
</body>
</html>
"""
with open("src/index.html", "w", encoding="utf-8") as f:
    f.write(html)

# --- Step 6: Start Tailwind watcher ---
print("\n[6/8] Starting Tailwind watcher...")
try:
    subprocess.Popen([npm_path, "start"], shell=True)
    print("Tailwind watcher started! Watching src/input.css -> src/output.css")
except Exception as e:
    print(f"Failed to start Tailwind watcher: {e}")

# --- Step 7: Open index.html in browser ---
print("\n[7/8] Opening src/index.html in your default browser...")

# Wait until output.css exists
output_path = os.path.abspath("src/output.css")
print("\nWaiting for Tailwind to generate output.css...")

while not os.path.exists(output_path):
    time.sleep(0.5)

print("output.css generated, opening browser now.")
webbrowser.open(f"file:///{os.path.abspath('src/index.html').replace(os.sep, '/')}")

# --- Step 8: Open VS Codium or VS Code ---
print("\n[8/8] Opening project in Code Editor")
ide_cmd = None
if shutil.which("codium"):
    ide_cmd = "codium"
elif shutil.which("code"):
    ide_cmd = "code"

if ide_cmd:
    try:
        subprocess.Popen([ide_cmd, "."], shell=True)
        print(f"{ide_cmd} opened successfully!")
    except Exception as e:
        print(f"Failed to open {ide_cmd}: {e}")
else:
    print("Neither VS Codium nor VS Code found in PATH.")

print("\n============================================")
print("Setup complete!")
print("============================================")
