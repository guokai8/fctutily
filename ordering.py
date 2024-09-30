# fctutils/ordering.py

import pandas as pd

def fct_pos(factor_series, positions, case=False, decreasing=False):
    """
    Reorder the levels of a factor (categorical series) based on characters at specified positions.
    """
    if not pd.api.types.is_categorical_dtype(factor_series):
        factor_series = factor_series.astype('category')

    levels = factor_series.cat.categories.tolist()

    # Function to extract characters at specified positions
    def extract_chars(s):
        return ''.join([s[i - 1] if i - 1 < len(s) else '' for i in positions])

    # Create a DataFrame for sorting
    df_levels = pd.DataFrame({'level': levels})
    df_levels['sort_key'] = df_levels['level'].apply(extract_chars)

    # Handle case sensitivity
    if not case:
        df_levels['sort_key'] = df_levels['sort_key'].str.lower()

    # Sort levels
    df_levels = df_levels.sort_values('sort_key', ascending=not decreasing)
    new_categories = df_levels['level'].tolist()

    # Update factor_series with new category order
    factor_series = factor_series.cat.reorder_categories(new_categories, ordered=True)
    return factor_series


def fct_count(data, column=None, decreasing=True):
    """
    Reorder levels of a factor based on the count of each level.

    Parameters:
    - data: pandas DataFrame or Series.
    - column: Column name if data is a DataFrame.
    - decreasing: Boolean, if True, sort in decreasing order.

    Returns:
    - pandas DataFrame or Series with updated categories.
    """
    if isinstance(data, pd.DataFrame):
        factor_series = data[column]
    else:
        factor_series = data

    if not pd.api.types.is_categorical_dtype(factor_series):
        factor_series = factor_series.astype('category')

    counts = factor_series.value_counts().sort_values(ascending=not decreasing)
    new_categories = counts.index.tolist()
    factor_series = factor_series.cat.reorder_categories(new_categories, ordered=True)

    if isinstance(data, pd.DataFrame):
        data[column] = factor_series
        return data
    else:
        return factor_series


def fct_sub(factor_series, start_pos, end_pos=None, case=False, decreasing=False):
    """
    Reorder levels based on substrings extracted from the factor levels.
    """
    levels = factor_series.cat.categories.tolist()
    start_idx = start_pos - 1
    end_idx = end_pos if end_pos is not None else None

    # Extract substrings
    substrings = [s[start_idx:end_idx] for s in levels]

    # Handle case sensitivity
    if not case:
        substrings = [s.lower() for s in substrings]

    # Create DataFrame for sorting
    df_levels = pd.DataFrame({'level': levels, 'substring': substrings})
    df_levels = df_levels.sort_values('substring', ascending=not decreasing)
    new_categories = df_levels['level'].tolist()

    factor_series = factor_series.cat.reorder_categories(new_categories, ordered=True)
    return factor_series
# fctutils/ordering.py

from collections import Counter

def fct_freq(factor_series, case=False, decreasing=True):
    """
    Reorder levels of a factor based on the total frequency of characters appearing in the vector.
    """
    levels = factor_series.cat.categories.tolist()
    text = ''.join(levels)
    if not case:
        text = text.lower()
    char_freq = Counter(text)

    # Calculate frequency score for each level
    def level_score(s):
        if not case:
            s = s.lower()
        return sum(char_freq.get(char, 0) for char in s)

    df_levels = pd.DataFrame({'level': levels})
    df_levels['freq_score'] = df_levels['level'].apply(level_score)

    df_levels = df_levels.sort_values('freq_score', ascending=not decreasing)
    new_categories = df_levels['level'].tolist()

    factor_series = factor_series.cat.reorder_categories(new_categories, ordered=True)
    return factor_series

def fct_char_freq(factor_series, positions, case=False, decreasing=True):
    """
    Reorder levels of a factor based on the frequency of characters at specified positions within the data.
    """
    # Extract characters at specified positions
    levels = factor_series.cat.categories.tolist()
    chars_at_positions = []

    for level in levels:
        chars = [level[i - 1] if i - 1 < len(level) else '' for i in positions]
        chars_at_positions.extend(chars)

    if not case:
        chars_at_positions = [char.lower() for char in chars_at_positions]

    char_freq = Counter(chars_at_positions)

    # Calculate frequency score for each level
    def level_score(s):
        chars = [s[i - 1] if i - 1 < len(s) else '' for i in positions]
        if not case:
            chars = [char.lower() for char in chars]
        return sum(char_freq.get(char, 0) for char in chars)

    df_levels = pd.DataFrame({'level': levels})
    df_levels['freq_score'] = df_levels['level'].apply(level_score)

    df_levels = df_levels.sort_values('freq_score', ascending=not decreasing)
    new_categories = df_levels['level'].tolist()

    factor_series = factor_series.cat.reorder_categories(new_categories, ordered=True)
    return factor_series

def fct_substr_freq(factor_series, start_pos, end_pos=None, case=False, decreasing=True):
    """
    Reorder levels based on the frequency of substrings extracted from the data.
    """
    levels = factor_series.cat.categories.tolist()
    substrings = []

    start_idx = start_pos - 1
    end_idx = end_pos if end_pos is not None else None

    for level in levels:
        substr = level[start_idx:end_idx]
        if not case:
            substr = substr.lower()
        substrings.append(substr)

    substr_freq = Counter(substrings)

    # Calculate frequency score for each level
    def level_score(s):
        substr = s[start_idx:end_idx]
        if not case:
            substr = substr.lower()
        return substr_freq.get(substr, 0)

    df_levels = pd.DataFrame({'level': levels})
    df_levels['freq_score'] = df_levels['level'].apply(level_score)

    df_levels = df_levels.sort_values('freq_score', ascending=not decreasing)
    new_categories = df_levels['level'].tolist()

    factor_series = factor_series.cat.reorder_categories(new_categories, ordered=True)
    return factor_series
# fctutils/ordering.py

import re

def fct_regex_freq(factor_series, pattern, case=False, decreasing=True):
    """
    Reorder levels based on the frequency of substrings matching a regular expression.
    """
    levels = factor_series.cat.categories.tolist()
    regex_flags = 0 if case else re.IGNORECASE

    matches = []

    for level in levels:
        matches_in_level = re.findall(pattern, level, flags=regex_flags)
        matches.extend(matches_in_level)

    match_freq = Counter(matches)

    # Calculate frequency score for each level
    def level_score(s):
        matches_in_s = re.findall(pattern, s, flags=regex_flags)
        return sum(match_freq.get(m, 0) for m in matches_in_s)

    df_levels = pd.DataFrame({'level': levels})
    df_levels['freq_score'] = df_levels['level'].apply(level_score)

    df_levels = df_levels.sort_values('freq_score', ascending=not decreasing)
    new_categories = df_levels['level'].tolist()

    factor_series = factor_series.cat.reorder_categories(new_categories, ordered=True)
    return factor_series
# fctutils/ordering.py

def fct_split(factor_series, split_pattern, part=1, use_pattern=None, char_freq=False, case=False, decreasing=True):
    """
    Splits the levels of a factor vector using specified patterns or positions and reorders based on specified parts or criteria.
    """
    levels = factor_series.cat.categories.tolist()

    if isinstance(split_pattern, list):
        # Combine patterns into a single regex pattern
        split_pattern = '|'.join(split_pattern)

    # Split levels
    split_levels = [re.split(split_pattern, level) for level in levels]

    # Use specified pattern for splitting
    if use_pattern is not None:
        pattern = split_pattern[use_pattern - 1]
        split_levels = [re.split(pattern, level) for level in levels]

    # Extract the part to use for ordering
    def get_part(splits):
        if len(splits) >= part:
            return splits[part - 1]
        else:
            return ''

    parts = [get_part(splits) for splits in split_levels]

    if not case:
        parts = [part.lower() for part in parts]

    if char_freq:
        # Reorder based on character frequencies in the specified part
        char_counts = Counter(''.join(parts))
        def freq_score(s):
            return sum(char_counts.get(c, 0) for c in s)
        scores = [freq_score(part) for part in parts]
    else:
        scores = parts

    df_levels = pd.DataFrame({'level': levels, 'score': scores})
    df_levels = df_levels.sort_values('score', ascending=not decreasing)
    new_categories = df_levels['level'].tolist()

    factor_series = factor_series.cat.reorder_categories(new_categories, ordered=True)
    return factor_series
def fct_len(factor_series, decreasing=False):
    """
    Reorder levels of a factor based on the character length of each level.

    Parameters:
    - factor_series: pandas Series with categorical dtype.
    - decreasing: Boolean, sort in decreasing order if True.

    Returns:
    - pandas Series with updated categories.
    """
    levels = factor_series.cat.categories
    lengths = levels.str.len()
    sorted_levels = levels[lengths.argsort()]
    if decreasing:
        sorted_levels = sorted_levels[::-1]
    return factor_series.cat.reorder_categories(sorted_levels, ordered=True)
# fctutils/ordering.py

def fct_sort(factor_series, by, na_position='last'):
    """
    Sorts the levels of a factor vector based on the values of another vector or a column from a data frame.
    Handles cases where the sorting vector may contain NAs.
    """
    levels = factor_series.cat.categories.tolist()
    sort_values = pd.Series(by, index=levels)

    # Handle NA positions
    if na_position == 'last':
        sort_values = sort_values.fillna(sort_values.max() + 1)
    elif na_position == 'first':
        sort_values = sort_values.fillna(sort_values.min() - 1)

    sorted_levels = sort_values.sort_values().index.tolist()
    factor_series = factor_series.cat.reorder_categories(sorted_levels, ordered=True)
    return factor_series
# fctutils/ordering.py

def fct_sort_custom(factor_series, sort_func):
    """
    Reorders the levels of a factor vector based on a custom function applied to each level.
    """
    levels = factor_series.cat.categories.tolist()
    sort_keys = sort_func(levels)

    df_levels = pd.DataFrame({'level': levels, 'sort_key': sort_keys})
    df_levels = df_levels.sort_values('sort_key')
    new_categories = df_levels['level'].tolist()

    factor_series = factor_series.cat.reorder_categories(new_categories, ordered=True)
    return factor_series

# fctutils/ordering.py

import pandas as pd

def fct_lump_min(factor_series, min_count, other_level='Other'):
    """
    Lump levels that appear fewer than a specified number of times.

    Parameters:
    - factor_series: pandas Series with categorical dtype.
    - min_count: Integer, minimum count a level must have to be kept.
    - other_level: String, name of the lumped level.

    Returns:
    - pandas Series with updated categories.
    """
    if not pd.api.types.is_categorical_dtype(factor_series):
        factor_series = factor_series.astype('category')

    value_counts = factor_series.value_counts()
    levels_to_keep = value_counts[value_counts >= min_count].index.tolist()

    new_categories = levels_to_keep + [other_level]
    factor_series = factor_series.cat.add_categories(other_level)
    factor_series = factor_series.where(factor_series.isin(levels_to_keep), other_level)
    factor_series = factor_series.cat.set_categories(new_categories)
    return factor_series

# fctutils/ordering.py

def fct_shift(factor_series, positions=1):
    """
    Shift factor levels by a specified number of positions.

    Parameters:
    - factor_series: pandas Series with categorical dtype.
    - positions: Integer, number of positions to shift. Positive values shift to the right.

    Returns:
    - pandas Series with shifted categories.
    """
    if not pd.api.types.is_categorical_dtype(factor_series):
        factor_series = factor_series.astype('category')

    levels = factor_series.cat.categories.tolist()
    shifted_levels = levels[-positions:] + levels[:-positions]
    factor_series = factor_series.cat.reorder_categories(shifted_levels, ordered=True)
    return factor_series

# fctutils/ordering.py

def fct_inorder(factor_series):
    """
    Set factor levels based on the order they appear in the data.

    Parameters:
    - factor_series: pandas Series.

    Returns:
    - pandas Series with ordered categories.
    """
    seen = []
    for item in factor_series:
        if pd.notna(item) and item not in seen:
            seen.append(item)

    factor_series = factor_series.astype('category')
    factor_series = factor_series.cat.reorder_categories(seen, ordered=True)
    return factor_series

# fctutils/ordering.py

def fct_reverse(factor_series):
    """
    Reverse the order of factor levels.

    Parameters:
    - factor_series: pandas Series with categorical dtype.

    Returns:
    - pandas Series with reversed categories.
    """
    if not pd.api.types.is_categorical_dtype(factor_series):
        factor_series = factor_series.astype('category')

    reversed_categories = factor_series.cat.categories[::-1]
    factor_series = factor_series.cat.reorder_categories(reversed_categories, ordered=True)
    return factor_series

# fctutils/ordering.py
def fct_lump_min(factor_series, min_count, other_level='Other'):
    """
    Lump levels that appear fewer than a specified number of times.

    Parameters:
    - factor_series: pandas Series with categorical dtype.
    - min_count: Integer, minimum count a level must have to be kept.
    - other_level: String, name of the lumped level.

    Returns:
    - pandas Series with updated categories.
    """
    if not pd.api.types.is_categorical_dtype(factor_series):
        factor_series = factor_series.astype('category')

    value_counts = factor_series.value_counts()
    levels_to_keep = value_counts[value_counts >= min_count].index.tolist()

    new_categories = levels_to_keep + [other_level]
    factor_series = factor_series.cat.add_categories(other_level)
    factor_series = factor_series.where(factor_series.isin(levels_to_keep), other_level)
    factor_series = factor_series.cat.set_categories(new_categories)
    return factor_series



# fctutils/ordering.py

def fct_shift(factor_series, positions=1):
    """
    Shift factor levels by a specified number of positions.

    Parameters:
    - factor_series: pandas Series with categorical dtype.
    - positions: Integer, number of positions to shift. Positive values shift to the right.

    Returns:
    - pandas Series with shifted categories.
    """
    if not pd.api.types.is_categorical_dtype(factor_series):
        factor_series = factor_series.astype('category')

    levels = factor_series.cat.categories.tolist()
    shifted_levels = levels[-positions:] + levels[:-positions]
    factor_series = factor_series.cat.reorder_categories(shifted_levels, ordered=True)
    return factor_series

