# Pyquality - Task Tracker

Maintain completed and planned features here for open-source tracking.

## Phase 1: Core Architecture
- [x] Initial project scaffolding (`pyproject.toml`, `src/pyquality`)
- [ ] Direct Websocket connection manager (`cdp_driver.py`)
- [ ] Browser manipulation wrapper with alias support (`browser.py`)
- [ ] Alias mappings (`METHOD_ALIASES.yml`)

## Phase 2: Fundamental Actions
- [ ] Navigation (`go_to`, `refresh`, `back`, `forward`)
- [ ] Discovery (`find`, `wait_for`)
- [ ] Interaction (`click`, `type`, `hover`)

## Phase 3: Advanced Capabilities
- [x] Screenshots
- [x] Network log interception
- [x] REST API simple wrapper
- [x] Accessibility checks
- [x] Full CDP Protocol Methods (`.dom` and `.cdp_browser`) generated from official devtools-protocol JSON

## Phase 4: Validation & Kid-Friendly Exposes
- [x] Verification methods (`should_have_text`, `is_visible`)

## Phase 5: Documentation & Open-Source
- [x] Add basic test scripts to `.gitignore`
- [x] Create robust `README.md`
- [x] Document build and PIP deployment instructions
