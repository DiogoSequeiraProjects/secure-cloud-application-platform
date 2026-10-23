
import importlib

import config


def test_debug_disabled_by_default(monkeypatch):
    monkeypatch.delenv("FLASK_DEBUG", raising=False)
    importlib.reload(config)

    assert config.Config.DEBUG is False


def test_debug_enabled_explicitly(monkeypatch):
    monkeypatch.setenv("FLASK_DEBUG", "true")
    importlib.reload(config)

    assert config.Config.DEBUG is True


def test_debug_disabled_explicitly(monkeypatch):
    monkeypatch.setenv("FLASK_DEBUG", "false")
    importlib.reload(config)

    assert config.Config.DEBUG is False
