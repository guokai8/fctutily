def fct_filter_freq(factor_series, min_freq=1, na_rm=False, return_info=False):
    """
    Filters out factor levels that occur less than a specified frequency threshold.
    
    Parameters:
    - factor_series: pandas Series with categorical dtype.
    - min_freq: Integer, minimum frequency threshold.
    - na_rm: Boolean, if True, removes NA values.
    - return_info: Boolean, if True, returns additional information.
    
    Returns:
    - If return_info is False: pandas Series with filtered levels.
    - If return_info is True: Dictionary with 'filtered_series', 'removed_levels', and 'char_freq_table'.
    """
    if na_rm:
        factor_series = factor_series.dropna()
    
    counts = factor_series.value_counts()
    levels_to_keep = counts[counts >= min_freq].index.tolist()
    levels_to_remove = counts[counts < min_freq].index.tolist()
    
    filtered_series = factor_series.where(factor_series.isin(levels_to_keep))
    filtered_series = filtered_series.cat.remove_categories(levels_to_remove)
    
    # Calculate character frequencies
    char_freq = filtered_series.dropna().str.cat().lower()
    from collections import Counter
    char_freq_table = Counter(char_freq)
    
    if return_info:
        return {
            'filtered_factor': filtered_series,
            'removed_levels': levels_to_remove,
            'char_freq_table': char_freq_table
        }
    else:
        return filtered_series


def fct_filter_pos(factor_series, positions, char, case=False):
    """
    Removes factor levels where a specified character appears at specified positions within the levels.
    """
    levels = factor_series.cat.categories.tolist()

    def char_at_positions(s):
        return [s[i - 1] if i - 1 < len(s) else '' for i in positions]

    if not case:
        char = char.lower()

    levels_to_remove = []
    for level in levels:
        chars = char_at_positions(level)
        if not case:
            chars = [c.lower() for c in chars]
        if char in chars:
            levels_to_remove.append(level)

    filtered_series = factor_series[~factor_series.isin(levels_to_remove)]
    filtered_series = filtered_series.cat.remove_categories(levels_to_remove)
    return filtered_series
# fctutils/filtering.py

def fct_remove_levels(factor_series, levels_to_remove):
    """
    Removes specified levels from a factor vector, keeping the remaining levels and their order unchanged.
    """
    filtered_series = factor_series[~factor_series.isin(levels_to_remove)]
    filtered_series = filtered_series.cat.remove_categories(levels_to_remove)
    return filtered_series
# fctutils/filtering.py

def fct_filter_func(factor_series, filter_func):
    """
    Removes levels from a factor vector based on a user-defined function.
    """
    levels = factor_series.cat.categories.tolist()
    levels_to_keep = [level for level in levels if filter_func(level)]
    filtered_series = factor_series[factor_series.isin(levels_to_keep)]
    filtered_series = filtered_series.cat.set_categories(levels_to_keep)
    return filtered_series

# fctutils/filtering.py

def fct_drop_na(factor_series):
    """
    Remove NA levels from a factor.

    Parameters:
    - factor_series: pandas Series with categorical dtype.

    Returns:
    - pandas Series with NA levels removed.
    """
    factor_series = factor_series.cat.remove_unused_categories()
    return factor_series

