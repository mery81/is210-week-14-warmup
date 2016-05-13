#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides the Dog class."""

import pet


class Dog(pet.Pet):
    """Dog Class"""

    def __init__(self, has_shots, **kwargs):
        pet.Pet.__init__(self, **kwargs)
        self.has_shots = has_shots
