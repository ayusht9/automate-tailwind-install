# Tailwind CSS Project Setup

The script will:

1. Initialize a new npm project
2. Install TailwindCSS and CLI
3. Create `src/input.css` and `src/index.html`
4. Write a custom `package.json` with a start script
5. Start the Tailwind watcher (`npx @tailwindcss/cli -i ./src/input.css -o ./src/output.css --watch`)
6. Wait for `output.css` to be generated
7. Open `src/index.html` in your default browser
8. Open VS Code or VS Codium if installed

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

## Run directly using curl

```bash
curl -sSL https://raw.githubusercontent.com/ayusht9/automate-tailwind-install/main/setup-tailwind.py | python
```

## Run locally

1. Place the Python script in an empty project folder.
2. Run the script:

```bash
python tailwind_setup.py
```


