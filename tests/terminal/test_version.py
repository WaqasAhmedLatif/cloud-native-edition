import contextlib
import os

import pytest


def test_version_no_prompt(settings):
    from pygluu.kubernetes.terminal.version import PromptVersion

    prompt = PromptVersion(settings, version="4.3")
    prompt.prompt_version()
    assert settings.get("GLUU_VERSION") == "4.3"


@pytest.mark.parametrize("given, expected", [
    ("", "4.3.0_01"),  # default if empty
    ("4.3.0_dev", "4.3.0_dev"),  # non-empty shouldn't be overriden
])
def test_version_merge_names_tags(settings, given, expected):
    import json
    from pygluu.kubernetes.terminal.version import PromptVersion

    with open("./gluu_versions.json", "w") as f:
        json.dump({"4.3": {"LDAP_IMAGE_TAG": "4.3.0_01"}}, f)

    settings.set("GLUU_VERSION", "4.3")
    settings.set("LDAP_IMAGE_TAG", given)

    PromptVersion(settings)
    assert settings.get("LDAP_IMAGE_TAG") == expected

    with contextlib.suppress(FileNotFoundError):
        os.unlink("./gluu_versions.json")


@pytest.mark.parametrize("given, expected", [
    ("", "4.3"),
    ("4.3", "4.3"),
])
def test_version(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.version import PromptVersion

    monkeypatch.setattr("click.prompt", lambda x, default: given or expected)

    prompt = PromptVersion(settings)

    # unset GLUU_VERSION in order to prompt user-input
    settings.set("GLUU_VERSION", "")

    prompt.prompt_version()
    assert settings.get("GLUU_VERSION") == expected
