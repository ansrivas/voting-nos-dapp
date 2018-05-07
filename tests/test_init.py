# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test modules."""


def test_init(hello_world):
    """Run a test."""
    import voting_smartcontract

    # Test __init__
    assert hasattr(voting_smartcontract, '__version__')

    # Test pytest fixtures
    assert(hello_world == "Hello World!")
