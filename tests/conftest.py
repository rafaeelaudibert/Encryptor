import os
import tempfile

import pytest

from encryptor import create_app


@pytest.fixture
def client():
    """Create and configure a new app instance for each test, with a test client for the app."""
    # create the app with common test config
    app = create_app({"TESTING": True})

    return app.test_client()
