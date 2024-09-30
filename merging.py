from difflib import SequenceMatcher

def fct_merge_similar(factor_series, max_distance=1):
    """
    Merge levels of a factor that are similar based on string distance.

    Parameters:
    - factor_series: pandas Series with categorical dtype.
    - max_distance: Maximum normalized string distance (0 to 1).

    Returns:
    - pandas Series with merged categories.
    """
    levels = factor_series.cat.categories.tolist()
    mapping = {}
    for i, level in enumerate(levels):
        for j in range(i + 1, len(levels)):
            other_level = levels[j]
            ratio = SequenceMatcher(None, level, other_level).ratio()
            if ratio >= (1 - max_distance):
                merged_level = min(level, other_level, key=len)
                mapping[other_level] = merged_level

    mapping = {**{lvl: lvl for lvl in levels}, **mapping}
    factor_series = factor_series.replace(mapping)
    factor_series = factor_series.astype('category')
    return factor_series
def fct_concat(*factor_series_list):
    """
    Combines multiple factor series into a single factor, unifying the levels.

    Parameters:
    - *factor_series_list: Variable number of pandas Series with categorical dtype.

    Returns:
    - Concatenated pandas Series with unified categories.
    """
    all_series = [fs.astype('category') for fs in factor_series_list]
    combined_categories = pd.api.types.union_categoricals(
        [fs.cat.categories for fs in all_series])

    concatenated_series = pd.concat(all_series).astype('category')
    concatenated_series = concatenated_series.cat.set_categories(
        combined_categories)
    return concatenated_series
# fctutils/merging.py

def fct_combine(vector1, vector2, sort_by=1):
    """
    Combines two vectors into a factor vector and sorts based on the levels of either the first or second vector.
    """
    combined_series = pd.Series(vector1 + vector2, dtype='category')
    if sort_by == 1:
        levels = pd.Series(vector1, dtype='category').cat.categories.tolist()
    elif sort_by == 2:
        levels = pd.Series(vector2, dtype='category').cat.categories.tolist()
    else:
        levels = combined_series.cat.categories.tolist()
    combined_series = combined_series.cat.set_categories(levels)
    return combined_series

# fctutils/merging.py

def fct_cross(factor_series1, factor_series2, sep='_'):
    """
    Create a new factor by combining levels from two factors.

    Parameters:
    - factor_series1: pandas Series with categorical dtype.
    - factor_series2: pandas Series with categorical dtype.
    - sep: String, separator to use between levels.

    Returns:
    - pandas Series with new combined categories.
    """
    if not pd.api.types.is_categorical_dtype(factor_series1):
        factor_series1 = factor_series1.astype('category')
    if not pd.api.types.is_categorical_dtype(factor_series2):
        factor_series2 = factor_series2.astype('category')

    combined = factor_series1.astype(str) + sep + factor_series2.astype(str)
    combined = combined.astype('category')
    return combined

# fctutils/merging.py

def fct_match(factor_series1, factor_series2):
    """
    Match levels of factor_series1 to factor_series2, aligning categories.

    Parameters:
    - factor_series1: pandas Series with categorical dtype.
    - factor_series2: pandas Series with categorical dtype.

    Returns:
    - pandas Series with levels matched to factor_series2.
    """
    if not pd.api.types.is_categorical_dtype(factor_series1):
        factor_series1 = factor_series1.astype('category')
    if not pd.api.types.is_categorical_dtype(factor_series2):
        factor_series2 = factor_series2.astype('category')

    matched_series = factor_series1.cat.set_categories(factor_series2.cat.categories)
    return matched_series

