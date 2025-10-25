# Tailwind CSS Project Setup

This project contains a Python script that automates the setup of a Tailwind CSS project. It initializes a Node.js project, installs Tailwind, creates the necessary files, starts a live watcher for CSS changes, opens the HTML in a browser, and optionally opens your code editor.

---

## Prerequisites

Before running the script, make sure you have:

- **Python 3.7+** installed and available in PATH
- **Node.js & npm** installed and available in PATH
- (Optional) **VS Code or VS Codium** installed if you want the project to open automatically

You can verify installations:

```bash
python --version
node --version
npm --version
````

---

## Files Created by the Script

* `package.json` – Customized with Tailwind dependencies and start script
* `src/input.css` – Entry CSS file for Tailwind
* `src/output.css` – Generated CSS file by Tailwind
* `src/index.html` – Example HTML file that uses Tailwind classes

---

## How to Use

1. Place the Python script in an empty project folder.
2. Run the script:

```bash
python tailwind_setup.py
```

3. The script will:

   1. Initialize a new npm project
   2. Install TailwindCSS and CLI
   3. Create `src/input.css` and `src/index.html`
   4. Write a custom `package.json` with a start script
   5. Start the Tailwind watcher (`npx @tailwindcss/cli -i ./src/input.css -o ./src/output.css --watch`)
   6. Wait for `output.css` to be generated
   7. Open `src/index.html` in your default browser
   8. Open VS Code or VS Codium if installed
