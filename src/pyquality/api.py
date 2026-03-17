import requests

class API:
    """
    Kid-friendly wrapper for REST API calls.
    """
    def __init__(self, base_url=""):
        self.base_url = base_url
        self.session = requests.Session()
        self._apply_aliases()

    def _apply_aliases(self):
        """Bind kid-friendly aliases to instance methods dynamically."""
        from .__init__ import ALIASES
        if "api" in ALIASES:
            for method_name, aliases in ALIASES["api"].items():
                if hasattr(self, method_name):
                    func = getattr(self, method_name)
                    for alias in aliases:
                        setattr(self, alias, func)

    def _build_url(self, endpoint):
        if endpoint.startswith("http"):
            return endpoint
        return f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"

    def set_header(self, key, value):
        """Set a header for subsequent requests."""
        self.session.headers.update({key: value})

    def use_token(self, token):
        """Authenticate with a Bearer token."""
        self.set_header("Authorization", f"Bearer {token}")

    def get(self, endpoint, **kwargs):
        """Send a GET request."""
        return self.session.get(self._build_url(endpoint), **kwargs)

    def post(self, endpoint, json=None, data=None, **kwargs):
        """Send a POST request."""
        return self.session.post(self._build_url(endpoint), json=json, data=data, **kwargs)

    def put(self, endpoint, json=None, data=None, **kwargs):
        """Send a PUT request."""
        return self.session.put(self._build_url(endpoint), json=json, data=data, **kwargs)

    def delete(self, endpoint, **kwargs):
        """Send a DELETE request."""
        return self.session.delete(self._build_url(endpoint), **kwargs)

    def patch(self, endpoint, json=None, data=None, **kwargs):
        """Send a PATCH request."""
        return self.session.patch(self._build_url(endpoint), json=json, data=data, **kwargs)

    def should_be_status(self, response, expected_status):
        """Kid-friendly assertion for status codes."""
        if response.status_code != expected_status:
            raise AssertionError(f"Expected status {expected_status}, but got {response.status_code}.")
        return True
