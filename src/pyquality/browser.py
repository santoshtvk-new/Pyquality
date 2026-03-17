from .cdp_driver import CDPDriver
from .__init__ import ALIASES
from . import domains

class Browser:
    """
    Kid-friendly wrapper around CDPDriver.
    This class can dynamically expose methods mapped by aliases.
    """
    def __init__(self, headless=False):
        self.driver = CDPDriver()
        self.driver.start_chrome(headless=headless)
        self.driver.connect()
        # Enable network tracking
        self.driver.execute_and_wait("Network.enable")
        
        # Initialize native CDP domains dynamically
        for attr_name in dir(domains):
            if attr_name.endswith("Domain"):
                domain_class = getattr(domains, attr_name)
                # Ensure the property name doesn't collide with existing class/instance vars like `browser` -> `cdp_browser`
                prop_name = attr_name[:-6].lower()
                if prop_name == "browser":
                    prop_name = "cdp_browser"
                    
                setattr(self, prop_name, domain_class(self.driver))
                
        self._apply_aliases()

    def _apply_aliases(self):
        """Bind kid-friendly aliases to instance methods dynamically."""
        for category, methods in ALIASES.items():
            for method_name, aliases in methods.items():
                if hasattr(self, method_name):
                    func = getattr(self, method_name)
                    for alias in aliases:
                        setattr(self, alias, func)

    # ===============
    # CORE METHODS
    # ===============
    def navigate(self, url):
        """Navigate to a URL."""
        response = self.driver.execute_and_wait("Page.navigate", {"url": url})
        return response
        
    def reload(self):
        """Reload the current page using raw CDP."""
        return self.page.reload()

    def go_back(self):
        """Navigate backward in history."""
        return self.evaluate_js("window.history.back()")

    def go_forward(self):
        """Navigate forward in history."""
        return self.evaluate_js("window.history.forward()")

    def get_title(self):
        """Get page title."""
        res = self.evaluate_js("document.title")
        return res.get('result', {}).get('result', {}).get('value', '')

    def get_url(self):
        """Get current URL."""
        res = self.evaluate_js("window.location.href")
        return res.get('result', {}).get('result', {}).get('value', '')

    def evaluate_js(self, expression):
        """Evaluate JS in the browser."""
        response = self.driver.execute_and_wait("Runtime.evaluate", {
            "expression": expression,
            "returnByValue": True
        })
        return response

    def find_element(self, selector):
        """Check if element exists."""
        res = self.evaluate_js(f"document.querySelector('{selector}') !== null")
        return res.get('result', {}).get('result', {}).get('value', False)

    def click_element(self, selector):
        """Click an element using JS."""
        return self.evaluate_js(f"document.querySelector('{selector}').click()")

    def type_text(self, selector, text):
        """Type text into an input."""
        # Escape quotes in text
        safe_text = text.replace("'", "\\'").replace('"', '\\"')
        return self.evaluate_js(
            f"document.querySelector('{selector}').value = '{safe_text}';"
            f"document.querySelector('{selector}').dispatchEvent(new Event('input'));"
        )

    def hover_element(self, selector):
        """Hover over an element (dispatches mouseover/mouseenter events)."""
        return self.evaluate_js(
            f"var el = document.querySelector('{selector}');"
            f"if (el) {{ el.dispatchEvent(new MouseEvent('mouseenter', {{bubbles: true}}));"
            f"el.dispatchEvent(new MouseEvent('mouseover', {{bubbles: true}})); }}"
        )

    # ===============
    # DISCOVERY & VALIDATION
    # ===============
    def wait_for_selector(self, selector, timeout=10):
        """Wait until an element appears in the DOM."""
        import time
        start = time.time()
        while time.time() - start < timeout:
            if self.find_element(selector):
                return True
            time.sleep(0.5)
        raise Exception(f"Timeout waiting for selector: {selector}")

    def assert_visible(self, selector):
        """Check if an element is visible (naive check for presence and display structure)."""
        res = self.evaluate_js(
            f"var el = document.querySelector('{selector}');"
            f"el ? (el.offsetWidth > 0 && el.offsetHeight > 0 && getComputedStyle(el).display !== 'none') : false"
        )
        is_vis = res.get('result', {}).get('result', {}).get('value', False)
        if not is_vis:
            raise AssertionError(f"Element {selector} is not visible.")
        return True

    def assert_text(self, selector, expected_text):
        """Check if an element contains expected text."""
        res = self.evaluate_js(f"var el = document.querySelector('{selector}'); el ? el.innerText : ''")
        actual_text = res.get('result', {}).get('result', {}).get('value', '')
        if expected_text not in actual_text:
            raise AssertionError(f"Expected text '{expected_text}' not found in '{actual_text}'.")
        return True

    # ===============
    # ADVANCED
    # ===============
    def take_screenshot(self, filename="screenshot.png"):
        """Take a full page screenshot."""
        import base64
        response = self.driver.execute_and_wait("Page.captureScreenshot")
        data = response.get('result', {}).get('data', '')
        if data:
            with open(filename, "wb") as f:
                f.write(base64.b64decode(data))
        return filename

    def get_network_logs(self):
        """Return all network events captured."""
        return self.driver.events

    def get_accessibility_tree(self):
        """Fetch the accessibility tree for the page."""
        response = self.driver.execute_and_wait("Accessibility.getFullAXTree")
        return response.get('result', {}).get('nodes', [])
        
    def get_cookies(self):
        """Get all browser cookies via Network domain."""
        return self.network.getCookies().get('result', {}).get('cookies', [])

    def clear_cookies(self):
        """Clear all browser cookies via Network domain."""
        return self.network.clearBrowserCookies()

    def set_viewport(self, width, height, is_mobile=False):
        """Emulate device metrics / viewport."""
        return self.emulation.setDeviceMetricsOverride(width=width, height=height, deviceScaleFactor=3 if is_mobile else 1, mobile=is_mobile)

    def act_like_phone(self):
        """Emulate a generic phone viewport."""
        return self.set_viewport(375, 812, is_mobile=True)

    def set_location(self, latitude, longitude, accuracy=100):
        """Emulate geographical location."""
        return self.emulation.setGeolocationOverride(latitude=latitude, longitude=longitude, accuracy=accuracy)

    def close(self):
        """Close the browser."""
        self.driver.stop_chrome()
