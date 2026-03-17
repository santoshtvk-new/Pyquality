# IDEOLOGY

## Core Philosophy

1. **Kid-Friendly & Accessible**: The API should be so intuitive that a kid could use it. Complex underlying operations are abstracted behind simple, clear method names.
2. **Flexible Naming**: We use `METHOD_ALIASES.yml` to map internal technical names to front-facing aliases. This allows users to customize the SDK to language that resonates with them (e.g., `click_this` instead of `click_element`).
3. **No Unnecessary Dependencies**: We interact directly with the Chrome DevTools Protocol (CDP) using websockets where possible. This improves portability and reduces dependency bloat.
4. **Built-in Power**: While simple on the surface, the framework includes advanced capabilities by default:
   - Network interception and logging
   - Easy full-page screenshots and activity tracing
   - Native accessibility checks built-in
   - Friendly validation rules (e.g., checking if text is present)

## Future Plans

- Expand alias support to multiple human languages.
- Create an integrated visual DOM explorer that generates pyquality scripts.
- Portability to non-Chromium browsers if applicable, while retaining the CDP-like interface.
