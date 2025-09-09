# Package shim to avoid import-time failures and allow submodule imports under your_application/
# This module exposes a lazy create_app() for compatibility and makes this name behave like a package.

import os as _os

# Make this module behave like a package by providing a search path for submodules
__path__ = [_os.path.join(_os.path.dirname(__file__), 'your_application')]


def create_app():
    """Compatibility factory returning the main Flask app.
    This avoids import-time side effects during build and works for deployments
    that reference `your_application.wsgi:application`.
    """
    from app import app as flask_app
    return flask_app
