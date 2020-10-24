import numpy as np
import pandas as pd
import pytest

from entity_disambiguation.preprocessing import normalize_text


def test_normer_works():
    assert normalize_text("United States ") == "united states"
