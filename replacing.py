# fctutils/replacing.py

def fct_replace(data, column=None, old_level=None, new_level=None, position=None):
    """
    Replace a specified level in a factor vector with a new level.

    Parameters:
    - data: pandas DataFrame or Series.
    - column: Column name if data is a DataFrame.
    - old_level: String, the level to replace.
    - new_level: String, the new level to insert.
    - position: Integer, position to place the new level among categories.

    Returns:
    - pandas DataFrame or Series with updated categories.
    """
    if isinstance(data, pd.DataFrame):
        factor_series = data[column]
    else:
        factor_series = data

    if not pd.api.types.is_categorical_dtype(factor_series):
        factor_series = factor_series.astype('category')

    factor_series = factor_series.cat.add_categories(new_level)
    factor_series = factor_series.replace(old_level, new_level)
    factor_series = factor_series.cat.remove_categories(old_level)

    if position is not None:
        categories = factor_series.cat.categories.tolist()
        categories.insert(position - 1, categories.pop(categories.index(new_level)))
        factor_series = factor_series.cat.reorder_categories(categories, ordered=True)

    if isinstance(data, pd.DataFrame):
        data[column] = factor_series
        return data
    else:
        return factor_series



import re

def fct_replace_pattern(data, column=None, pattern=None, replacement=None, regex=True, inplace=False):
    """
    Replace parts of the factor levels that match a specified pattern with a new string.

    Parameters:
    - data: pandas DataFrame or Series.
    - column: Column name if data is a DataFrame.
    - pattern: String or regex pattern to match.
    - replacement: String to replace the matched pattern.
    - regex: Boolean, if True, uses regex matching.
    - inplace: Boolean, if True, modify the data in place.

    Returns:
    - pandas DataFrame or Series with updated categories.
    """
    if isinstance(data, pd.DataFrame):
        factor_series = data[column]
    else:
        factor_series = data

    levels = factor_series.cat.categories.tolist()

    if regex:
        new_levels = [re.sub(pattern, replacement, level) for level in levels]
    else:
        new_levels = [level.replace(pattern, replacement) for level in levels]

    mapping = dict(zip(levels, new_levels))
    factor_series = factor_series.cat.rename_categories(mapping)

    if inplace:
        if isinstance(data, pd.DataFrame):
            data[column] = factor_series
            return None
        else:
            data[:] = factor_series
            return None
    else:
        if isinstance(data, pd.DataFrame):
            new_data = data.copy()
            new_data[column] = factor_series
            return new_data
        else:
            return factor_series


def fct_anon(factor_series, prefix='Level'):
    """
    Anonymize factor levels by replacing them with numeric codes.

    Parameters:
    - factor_series: pandas Series with categorical dtype.
    - prefix: String, prefix for the anonymized levels.

    Returns:
    - pandas Series with anonymized categories.
    """
    if not pd.api.types.is_categorical_dtype(factor_series):
        factor_series = factor_series.astype('category')

    levels = factor_series.cat.categories
    new_levels = [f"{prefix}{i+1}" for i in range(len(levels))]
    mapping = dict(zip(levels, new_levels))
    factor_series = factor_series.cat.rename_categories(mapping)
    return factor_series

# fctutils/replacing.py

def fct_collapse(factor_series, levels_to_collapse, new_level):
    """
    Collapse specified levels of a factor into a single new level.

    Parameters:
    - factor_series: pandas Series with categorical dtype.
    - levels_to_collapse: List of levels to collapse.
    - new_level: String, name of the new level.

    Returns:
    - pandas Series with updated categories.
    """
    if not pd.api.types.is_categorical_dtype(factor_series):
        factor_series = factor_series.astype('category')

    factor_series = factor_series.cat.add_categories(new_level)
    factor_series = factor_series.replace(levels_to_collapse, new_level)
    factor_series = factor_series.cat.remove_categories(levels_to_collapse)
    return factor_series

