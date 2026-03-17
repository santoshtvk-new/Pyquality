# pyquality 🎈

A kid-friendly, yet exceptionally powerful automation framework for Python driven directly by the Chrome DevTools Protocol (CDP).

`pyquality` is designed to be as simple as possible. Want to close the browser? Just call `b.bye()`. Want to navigate? `b.go_to("https://...")`

Under the hood, it retains uncompromising power. Advanced users have **unfiltered access** to all 40+ raw Chromium DevTools domains (DOM, Network, Page, etc.) auto-generated from the official Google spec!

---

## 🚀 Installation (Source)
If you are developing locally:
```bash
git clone https://github.com/santoshtvk-new/Pyquality.git
cd pyquality
pip install -e .
```

## 🛠️ Installation (PIP)
*(When published to PyPi)*
```bash
pip install py4quality
```

---

## 📖 Quick Start

```python
from pyquality.browser import Browser

# 1. Start it up
b = Browser(headless=False)

# 2. Go somewhere
b.go_to("https://example.com")

# 3. Validation is easy
b.should_be_seen("h1")

# 4. Say goodbye
b.bye()
```

## ✨ The Kid-Friendly Aliases

`pyquality` dynamically binds methods defined in `METHOD_ALIASES.yml` so you can use vocabulary that makes sense to you.

### Navigation
- `navigate(url)` -> `go_to`, `open_website`
- `reload()` -> `refresh`, `reload_page`
- `close()` -> `close_browser`, `bye`
- `go_back()` -> `step_back`, `previous_page`
- `go_forward()` -> `step_forward`, `next_page`

### Interaction
- `click_element(selector)` -> `click_this`, `tap`
- `type_text(selector, text)` -> `type_in`, `write_this`
- `hover_element(selector)` -> `point_at`, `hover_over`

### APIs & Data
- `API.get(endpoint)` -> `fetch_data`, `grab`
- `API.post(endpoint, json)` -> `create_data`, `send_new`

---

## ⚡ Raw CDP Power (Advanced)

If you need capabilities beyond the simple wrappers, `pyquality` has raw auto-generated bindings for **EVERY** CDP Domain. They are attached natively to the browser instance:

```python
from pyquality.browser import Browser
b = Browser()

# Use raw 'Page' domain to capture a PDF
b.page.printToPDF()

# Use raw 'Network' domain to throttle connection
b.network.emulateNetworkConditions(
    offline=False, 
    latency=200, 
    downloadThroughput=1000, 
    uploadThroughput=1000
)

# Use raw 'DOM' domain to get node information
b.dom.getDocument(depth=-1)
```

## 📦 Deploying Initial PIP Package

To package this framework and upload it to PyPi:

1. **Install build tools:**
   ```bash
   pip install build twine
   ```

2. **Generate Native Wrappers:**
   Ensure your CDP protocol bindings are up-to-date:
   ```bash
   python src/pyquality/generate_cdp_wrappers.py
   ```

3. **Build wheels:**
   ```bash
   python -m build
   ```
   *This generates `.tar.gz` and `.whl` files in the `/dist` folder.*

4. **Upload to PyPi (Requires Account):**
   ```bash
   python -m twine upload dist/*
   ```

5. **Done!** Users can now run `pip install pyquality`.
