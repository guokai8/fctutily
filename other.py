def fct_insert(data, column=None, insert=None, target=None, position='after', allow_duplicates=False, inplace=False):
    """
    Inserts one or more new levels into a factor vector immediately after specified target levels.

    Parameters:
    - data: pandas DataFrame or Series.
    - column: Column name if data is a DataFrame.
    - insert: Level(s) to insert.
    - target: Target level(s) after which to insert.
    - position: 'after' or 'before'.
    - allow_duplicates: Boolean, if True, allows duplicate levels.
    - inplace: Boolean, if True, modify the data in place.

    Returns:
    - pandas DataFrame or Series with updated categories.
    """
    if isinstance(data, pd.DataFrame):
        factor_series = data[column]
    else:
        factor_series = data

    levels = factor_series.cat.categories.tolist()

    if not isinstance(insert, list):
        insert = [insert]
    if not isinstance(target, list):
        target = [target]

    for t, ins in zip(target, insert):
        if ins in levels and not allow_duplicates:
            levels.remove(ins)
        try:
            idx = levels.index(t)
        except ValueError:
            continue  # Target not found
        insert_pos = idx + 1 if position == 'after' else idx
        levels.insert(insert_pos, ins)

    factor_series = factor_series.cat.set_categories(levels, ordered=True)

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

def fct_pairs(elements, ref=None, symmetric=True, include_na=False,
              include_self=False, filter_fn=None, pre_process_fn=None):
    """
    Creates all unique pairwise combinations between elements of a vector.

    Parameters:
    - elements: List or pandas Series.
    - ref: Optional list or pandas Series of reference elements.
    - symmetric: Boolean, if True, unique unordered pairs are returned.
    - include_na: Boolean, if True, includes NA values.
    - include_self: Boolean, if True, includes pairs where Var1 == Var2.
    - filter_fn: Function to filter the pairs.
    - pre_process_fn: Function to preprocess elements.

    Returns:
    - DataFrame containing pairwise combinations.
    """
    import pandas as pd
    elements = pd.Series(elements).drop_duplicates()
    if not include_na:
        elements = elements.dropna()
    if pre_process_fn:
        elements = elements.apply(pre_process_fn)

    if ref is None:
        ref = elements
    else:
        ref = pd.Series(ref).drop_duplicates()
        if not include_na:
            ref = ref.dropna()
        if pre_process_fn:
            ref = ref.apply(pre_process_fn)

    combinations = pd.MultiIndex.from_product([elements, ref]).to_frame(
        index=False, name=['Var1', 'Var2'])

    if not include_self:
        combinations = combinations[combinations['Var1'] != combinations['Var2']]

    if symmetric:
        combinations['key'] = combinations.apply(
            lambda row: tuple(sorted((row['Var1'], row['Var2']))), axis=1)
        combinations = combinations.drop_duplicates('key').drop('key', axis=1)

    if filter_fn:
        combinations = combinations[filter_fn(combinations)]

    return combinations.reset_index(drop=True)
