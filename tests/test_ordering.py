
---

## **Example Unit Test for `fct_lump_min`**

**File**: `tests/test_ordering.py`

```python
# tests/test_ordering.py

import unittest
import pandas as pd
from fctutils.ordering import fct_lump_min

class TestOrderingFunctions(unittest.TestCase):

    def test_fct_lump_min(self):
        factor_series = pd.Series(['apple', 'banana', 'apple', 'cherry',
                                   'banana', 'banana', 'date', 'fig'], dtype='category')
        lumped_series = fct_lump_min(factor_series, min_count=2)
        expected_categories = ['apple', 'banana', 'Other']
        self.assertEqual(list(lumped_series.cat.categories), expected_categories)
        self.assertTrue(all(lumped_series.isin(expected_categories)))

if __name__ == '__main__':
    unittest.main()

