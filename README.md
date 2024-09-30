# fctutils
_fctutils_ is a Python package for manipulating and analyzing categorical data (factors), inspired by the R package fctutils. It provides a suite of functions for ordering, replacing, filtering, merging factors, and more. The package is designed to work seamlessly with pandas DataFrames and Series, and integrates well with other data manipulation libraries like dfply and plotnine.
### Installation
```
pip install fctutils
```
### Getting Started
```
import pandas as pd
from fctutils import fct_count, fct_replace

# Example usage
factor_series = pd.Series(['apple', 'banana', 'apple', 'cherry'], dtype='category')

# Reorder levels by decreasing count
new_series = fct_count(factor_series)
print(new_series.cat.categories)
```
### Ordering and Sorting Functions
_fct_count_ Reorder levels of a factor based on the count of each level. 
__Parameters:__
* data: pandas DataFrame or Series.
* column: Column name if data is a DataFrame.
* decreasing: bool, if True, sort in decreasing order.
* inplace: bool, if True, modify the data in place.
* Returns: Modified DataFrame or Series if inplace=False, else None.
```
import pandas as pd
from fctutils import fct_count

# Using a Series
factor_series = pd.Series(['apple', 'banana', 'apple', 'cherry'], dtype='category')

# Reorder levels by decreasing count
new_series = fct_count(factor_series, decreasing=True)
print(new_series.cat.categories)
# Output: Index(['apple', 'banana', 'cherry'], dtype='object')

# Modify in place
fct_count(factor_series, decreasing=True, inplace=True)
print(factor_series.cat.categories)
# Output: Index(['apple', 'banana', 'cherry'], dtype='object')

# Using a DataFrame
df = pd.DataFrame({'fruits': ['apple', 'banana', 'apple', 'cherry']})
df['fruits'] = df['fruits'].astype('category')

# Reorder levels by decreasing count in place
fct_count(df, column='fruits', decreasing=True, inplace=True)
print(df['fruits'].cat.categories)
# Output: Index(['apple', 'banana', 'cherry'], dtype='object')

```
_fct_pos_ Reorder levels based on characters at specified positions.
__Parameters:__
* data: pandas DataFrame or Series.
* column: Column name if data is a DataFrame.
* positions: List of integer positions to consider (1-based indexing).
* case: bool, if False, comparison is case-insensitive.
* decreasing: bool, if True, sort in decreasing order.
* inplace: bool, if True, modify the data in place.
* Returns: Modified DataFrame or Series if inplace=False, else None.
```
import pandas as pd
from fctutils import fct_pos

# Example factor vector
factor_series = pd.Series(['Apple', 'banana', 'Cherry', 'date', 'Fig', 'grape'], dtype='category')

# Reorder based on positions 1 and 3, case-insensitive
new_series = fct_pos(factor_series, positions=[1, 3], case=False)
print(new_series.cat.categories)
# Output: Index(['Apple', 'banana', 'Cherry', 'date', 'Fig', 'grape'], dtype='object')

# Reorder in decreasing order, case-sensitive
new_series_desc = fct_pos(factor_series, positions=[1, 2], case=True, decreasing=True)
print(new_series_desc.cat.categories)
# Output: Index(['grape', 'Fig', 'date', 'Cherry', 'banana', 'Apple'], dtype='object')

```
_fct_sub_ Reorder levels based on substrings extracted from the factor levels.
__Parameters:__
* data: pandas DataFrame or Series.
* column: Column name if data is a DataFrame.
* start_pos: Integer, starting position for substring (1-based indexing).
* end_pos: Integer, ending position for substring. If None, goes to the end.
* case: bool, if False, comparison is case-insensitive.
* decreasing: bool, if True, sort in decreasing order.
* inplace: bool, if True, modify the data in place.
* Returns: Modified DataFrame or Series if inplace=False, else None.
```
import pandas as pd
from fctutils import fct_sub

# Example factor vector
factor_series = pd.Series(['Apple', 'banana', 'Cherry', 'date', 'Fig', 'grape'], dtype='category')

# Reorder based on substring from position 2 to 4
new_series = fct_sub(factor_series, start_pos=2, end_pos=4)
print(new_series.cat.categories)
# Output: Index(['banana', 'Apple', 'Cherry', 'date', 'grape', 'Fig'], dtype='object')

# Reorder from position 3 to end, case-sensitive
new_series_case = fct_sub(factor_series, start_pos=3, case=True)
print(new_series_case.cat.categories)
# Output: Index(['Fig', 'grape', 'Apple', 'Cherry', 'banana', 'date'], dtype='object')

```
_fct_freq_ Reorder levels based on total character frequency.
__Parameters:__
* data: pandas DataFrame or Series.
* column: Column name if data is a DataFrame.
* case: bool, if False, comparison is case-insensitive.
* decreasing: bool, if True, sort in decreasing order.
* inplace: bool, if True, modify the data in place.
* Returns: Modified DataFrame or Series if inplace=False, else None.
```
import pandas as pd
from fctutils import fct_freq

# Example factor vector
factor_series = pd.Series(['apple', 'banana', 'cherry', 'date', 'banana', 'apple', 'fig'], dtype='category')

# Reorder levels based on total character frequency
new_series = fct_freq(factor_series)
print(new_series.cat.categories)
# Output: Index(['banana', 'apple', 'cherry', 'date', 'fig'], dtype='object')

```
_fct_char_freq_ Reorder levels based on the frequency of characters at specified positions within the data.
__Parameters:__
* data: pandas DataFrame or Series.
* column: Column name if data is a DataFrame.
* positions: List of integer positions to consider (1-based indexing).
* case: bool, if False, comparison is case-insensitive.
* decreasing: bool, if True, sort in decreasing order.
* inplace: bool, if True, modify the data in place.
* Returns: Modified DataFrame or Series if inplace=False, else None.
```
import pandas as pd
from fctutils import fct_char_freq

# Example factor vector
factor_series = pd.Series(['apple', 'banana', 'apricot', 'cherry', 'banana', 'banana', 'date'], dtype='category')

# Reorder based on characters at positions 1 and 2
new_series = fct_char_freq(factor_series, positions=[1, 2])
print(new_series.cat.categories)
# Output: Index(['banana', 'apple', 'apricot', 'cherry', 'date'], dtype='object')

```
_fct_substr_freq_ Reorder levels based on the frequency of substrings extracted from the data.
__Parameters:__
* data: pandas DataFrame or Series.
* column: Column name if data is a DataFrame.
* start_pos: Integer, starting position for substring (1-based indexing).
* end_pos: Integer, ending position for substring. If None, goes to the end.
* case: bool, if False, comparison is case-insensitive.
* decreasing: bool, if True, sort in decreasing order.
* inplace: bool, if True, modify the data in place.
* Returns: Modified DataFrame or Series if inplace=False, else None.
```
import pandas as pd
from fctutils import fct_substr_freq

# Example factor vector
factor_series = pd.Series(['apple', 'banana', 'apricot', 'cherry', 'banana', 'banana', 'date'], dtype='category')

# Reorder based on substrings from position 2 to 3
new_series = fct_substr_freq(factor_series, start_pos=2, end_pos=3)
print(new_series.cat.categories)
# Output: Index(['banana', 'apple', 'apricot', 'cherry', 'date'], dtype='object')

```
_fct_regex_freq_ Reorder levels based on the frequency of substrings matching a regular expression.
__Parameters:__
* data: pandas DataFrame or Series.
* column: Column name if data is a DataFrame.
* pattern: String or regex pattern to match.
* case: bool, if False, comparison is case-insensitive.
* decreasing: bool, if True, sort in decreasing order.
* inplace: bool, if True, modify the data in place.
* Returns: Modified DataFrame or Series if inplace=False, else None.
```
import pandas as pd
from fctutils import fct_regex_freq

# Example factor vector
factor_series = pd.Series(['apple', 'banana', 'apricot', 'cherry', 'blueberry', 'blackberry', 'date'], dtype='category')

# Reorder based on pattern matching 'a'
new_series = fct_regex_freq(factor_series, pattern='a')
print(new_series.cat.categories)
# Output: Index(['banana', 'apricot', 'apple', 'blackberry', 'blueberry', 'cherry', 'date'], dtype='object')

```
_fct_split_ Split and reorder levels based on specified patterns or positions.
__Parameters:__
* data: pandas DataFrame or Series.
* column: Column name if data is a DataFrame.
* split_pattern: String or list of patterns to split on.
* part: Integer, which part to use after splitting.
* use_pattern: Integer, specifies which pattern to use if multiple patterns are provided.
* char_freq: bool, if True, reorder based on character frequencies in the specified part.
* case: bool, if False, comparison is case-insensitive.
* decreasing: bool, if True, sort in decreasing order.
* inplace: bool, if True, modify the data in place.
* Returns: Modified DataFrame or Series if inplace=False, else None.
```
import pandas as pd
from fctutils import fct_split

# Example factor vector with patterns
factor_series = pd.Series(['item1-sub1', 'item2_sub2', 'item3|sub3', 'item1-sub4'], dtype='category')

# Split by patterns '-', '_', or '|' and reorder based on the first part
new_series = fct_split(factor_series, split_pattern=['-', '_', '\\|'], part=1)
print(new_series.cat.categories)
# Output: ['item1-sub1', 'item1-sub4', 'item2_sub2', 'item3|sub3']

```
_fct_len_  Reorder levels of a factor based on the character length of each level.
__Parameters:__
* data: pandas DataFrame or Series.
* column: Column name if data is a DataFrame.
* decreasing: bool, if True, sort in decreasing order.
* inplace: bool, if True, modify the data in place.
* Returns: Modified DataFrame or Series if inplace=False, else None.
```
import pandas as pd
from fctutils import fct_len

# Example factor vector
factor_series = pd.Series(['apple', 'banana', 'cherry', 'date'], dtype='category')

# Sort levels by length
new_series = fct_len(factor_series)
print(new_series.cat.categories)
# Output: Index(['date', 'apple', 'banana', 'cherry'], dtype='object')

```
_fct_sort_  Sort levels based on the values of another vector or a column from a DataFrame.
__Parameters:__
* data: pandas DataFrame or Series.
* column: Column name if data is a DataFrame.
* by: List or Series to sort by.
* na_position: 'first' or 'last', position of NA values.
* inplace: bool, if True, modify the data in place.
* Returns: Modified DataFrame or Series if inplace=False, else None.
```
import pandas as pd
from fctutils import fct_sort

# Example factor vector
factor_series = pd.Series(['apple', 'banana', 'cherry', 'date'], dtype='category')
by_vec = [2, 3, 1, None]

# Sort levels based on by_vec
new_series = fct_sort(factor_series, by=by_vec)
print(new_series.cat.categories)
# Output: Index(['cherry', 'apple', 'banana', 'date'], dtype='object')

```
_fct_sort_custom_  Reorder levels of a factor vector based on a custom function applied to each level.
__Parameters:__
* data: pandas DataFrame or Series.
* column: Column name if data is a DataFrame.
* sort_func: Function to apply to each level.
* inplace: bool, if True, modify the data in place.
* Returns: Modified DataFrame or Series if inplace=False, else None.
```
import pandas as pd
from fctutils import fct_sort_custom

# Example factor vector
factor_series = pd.Series(['apple', 'banana', 'cherry'], dtype='category')

# Sort levels by reverse alphabetical order
new_series = fct_sort_custom(factor_series, sort_func=lambda x: [-ord(c[0]) for c in x])
print(new_series.cat.categories)
# Output: Index(['cherry', 'banana', 'apple'], dtype='object')

```
_fct_inorder_ Order levels based on first appearance.
__Parameters:__
* data: pandas DataFrame or Series.
* column: Column name if data is a DataFrame.
* inplace: bool, if True, modify the data in place.
* Returns: Modified DataFrame or Series if inplace=False, else None.
```
import pandas as pd
from fctutils import fct_inorder

# Example factor vector
factor_series = pd.Series(['banana', 'apple', 'cherry', 'banana', 'date', 'apple'], dtype='category')

# Order levels based on first appearance
new_series = fct_inorder(factor_series)
print(new_series.cat.categories)
# Output: Index(['banana', 'apple', 'cherry', 'date'], dtype='object')

```
_fct_lump_ Lump together infrequent levels into a single 'Other' level.
__Parameters:__
* data: pandas DataFrame or Series.
* column: Column name if data is a DataFrame.
* n: Integer, number of most frequent levels to keep.
* prop: Float between 0 and 1, proportion threshold to keep levels.
* other_level: String, name of the lumped level.
* inplace: bool, if True, modify the data in place.
* Returns: Modified DataFrame or Series if inplace=False, else None.
```
import pandas as pd
from fctutils import fct_lump

# Example factor vector
factor_series = pd.Series(['apple', 'banana', 'cherry', 'date', 'banana', 'apple', 'fig', 'grape', 'apple'], dtype='category')

# Lump together all but the top 2 levels
lumped_series = fct_lump(factor_series, n=2)
print(lumped_series)
# Output:
# 0     apple
# 1    banana
# 2     Other
# 3     Other
# 4    banana
# 5     apple
# 6     Other
# 7     Other
# 8     apple
# dtype: category
# Categories (3, object): ['apple', 'banana', 'Other']

```
_fct_lump_min_ Lump levels that appear fewer than a specified number of times.
__Parameters:__
* data: pandas DataFrame or Series.
* column: Column name if data is a DataFrame.
* min_count: Integer, minimum count a level must have to be kept.
* other_level: String, name of the lumped level.
* inplace: bool, if True, modify the data in place.
* Returns: Modified DataFrame or Series if inplace=False, else None.
```
import pandas as pd
from fctutils import fct_lump_min

# Example factor vector
factor_series = pd.Series(['apple', 'banana', 'apple', 'cherry', 'banana', 'banana', 'date', 'fig'], dtype='category')

# Lump levels appearing fewer than 2 times
lumped_series = fct_lump_min(factor_series, min_count=2)
print(lumped_series)
# Output:
# 0     apple
# 1    banana
# 2     apple
# 3     Other
# 4    banana
# 5    banana
# 6     Other
# 7     Other
# dtype: category
# Categories (3, object): ['apple', 'banana', 'Other']

```
_fct_shift_
Shift factor levels by a specified number of positions.
```
import pandas as pd
from fctutils import fct_shift

# Example factor vector
factor_series = pd.Series(['low', 'medium', 'high'], dtype='category')

# Shift levels by 1 position
shifted_series = fct_shift(factor_series, positions=1)
print(shifted_series.cat.categories)
# Output: Index(['high', 'low', 'medium'], dtype='object')

```
_fct_reverse_ Reverse the order of factor levels.
```
import pandas as pd
from fctutils import fct_reverse

# Example factor vector
factor_series = pd.Series(['low', 'medium', 'high'], dtype='category')

# Reverse the order of factor levels
reversed_series = fct_reverse(factor_series)
print(reversed_series.cat.categories)
# Output: Index(['high', 'medium', 'low'], dtype='object')

```

### Replacing Factor Levels
_fct_replace_ Replace a specified level in a factor vector with a new level.
* data: pandas DataFrame or Series.
* column: Column name if data is a DataFrame.
* old_level: String, the level to replace.
* new_level: String, the new level to insert.
* position: Integer, position to place the new level among categories.
* inplace: bool, if True, modify the data in place.
```
import pandas as pd
from fctutils import fct_replace

# Using a Series
factor_series = pd.Series(['apple', 'banana', 'cherry', 'date', 'fig', 'grape'], dtype='category')

# Replace 'banana' with 'blueberry', and keep original order
new_series = fct_replace(factor_series, old_level='banana', new_level='blueberry')
print(new_series.cat.categories)
# Output: Index(['apple', 'blueberry', 'cherry', 'date', 'fig', 'grape'], dtype='object')

# Replace 'banana' with 'blueberry' at position 2
new_series_pos = fct_replace(factor_series, old_level='banana', new_level='blueberry', position=2)
print(new_series_pos.cat.categories)
# Output: Index(['apple', 'blueberry', 'cherry', 'date', 'fig', 'grape'], dtype='object')

# Modify in place
fct_replace(factor_series, old_level='banana', new_level='blueberry', inplace=True)
print(factor_series.cat.categories)
# Output: Index(['apple', 'blueberry', 'cherry', 'date', 'fig', 'grape'], dtype='object')

```
_fct_replace_pattern_ Replace parts of the factor levels that match a specified pattern with a new string.
```
import pandas as pd
from fctutils import fct_replace_pattern

# Example factor vector
factor_series = pd.Series(['apple_pie', 'banana_bread', 'cherry_cake'], dtype='category')

# Replace '_pie', '_bread', '_cake' with '_dessert'
new_series = fct_replace_pattern(factor_series, pattern='_.*', replacement='_dessert')
print(new_series.cat.categories)
# Output: Index(['apple_dessert', 'banana_dessert', 'cherry_dessert'], dtype='object')

# Modify in place
fct_replace_pattern(factor_series, pattern='_.*', replacement='_dessert', inplace=True)
print(factor_series.cat.categories)
# Output: Index(['apple_dessert', 'banana_dessert', 'cherry_dessert'], dtype='object')

```
_fct_relabel_ Apply a function to relabel factor levels.
```
import pandas as pd
from fctutils import fct_relabel

# Example factor vector
factor_series = pd.Series(['apple', 'banana', 'cherry'], dtype='category')

# Convert levels to uppercase
relabelled_series = fct_relabel(factor_series, relabel_func=lambda x: x.upper())
print(relabelled_series.cat.categories)
# Output: Index(['APPLE', 'BANANA', 'CHERRY'], dtype='object')

```
_fct_anon_ Anonymize factor levels by replacing them with numeric codes.
* data: pandas DataFrame or Series.
* column: Column name if data is a DataFrame.
* prefix: String, prefix for the anonymized levels.
* inplace: bool, if True, modify the data in place.
```
import pandas as pd
from fctutils import fct_anon

# Example factor vector
factor_series = pd.Series(['apple', 'banana', 'cherry', 'date'], dtype='category')

# Anonymize factor levels
anon_series = fct_anon(factor_series)
print(anon_series.cat.categories)
# Output: Index(['Level1', 'Level2', 'Level3', 'Level4'], dtype='object')

```
_fct_collapse_ Collapse specified levels of a factor into a single new level.
* data: pandas DataFrame or Series.
* column: Column name if data is a DataFrame.
* levels_to_collapse: List of levels to collapse.
* new_level: String, name of the new level.
* inplace: bool, if True, modify the data in place.
```
import pandas as pd
from fctutils import fct_collapse

# Example factor vector
factor_series = pd.Series(['apple', 'banana', 'cherry', 'date', 'fig', 'grape'], dtype='category')

# Collapse 'fig' and 'grape' into 'other_fruits'
collapsed_series = fct_collapse(factor_series, levels_to_collapse=['fig', 'grape'], new_level='other_fruits')
print(collapsed_series)
# Output:
# 0            apple
# 1           banana
# 2           cherry
# 3             date
# 4     other_fruits
# 5     other_fruits
# dtype: category
# Categories (4, object): ['apple', 'banana', 'cherry', 'other_fruits']

```
### Filtering and Removing Factor Levels
_fct_filter_freq_ Filters out factor levels that occur less than a specified frequency threshold.
* data: pandas DataFrame or Series.
* column: Column name if data is a DataFrame.
* min_freq: Integer, minimum frequency threshold.
* na_rm: bool, if True, removes NA values.
* inplace: bool, if True, modify the data in place.
* return_info: bool, if True, returns additional information.
* Returns: Modified DataFrame or Series if return_info=False and inplace=False, else None. If return_info=True, returns a dictionary with keys: 'filtered_factor': The modified factor series or DataFrame. 'removed_levels': List of removed levels. 'char_freq_table': Character frequency table.
 ```
import pandas as pd
from fctutils import fct_filter_freq

# Example factor vector
factor_series = pd.Series(['apple', 'banana', 'cherry', 'date', 'banana', 'apple', 'fig', None], dtype='category')

# Filter levels occurring less than 2 times and reorder by character frequency
filtered_series = fct_filter_freq(factor_series, min_freq=2)
print(filtered_series.cat.categories)
# Output: Index(['apple', 'banana'], dtype='object')

# Filter levels, remove NA values, and return additional information
result = fct_filter_freq(factor_series, min_freq=2, na_rm=True, return_info=True)
print(result['filtered_factor'].cat.categories)
# Output: Index(['apple', 'banana'], dtype='object')
print('Removed levels:', result['removed_levels'])
# Output: Removed levels: ['cherry', 'date', 'fig']
print('Character frequency table:', result['char_freq_table'])
# Output: Character frequency table: Counter({'a': 4, 'p': 2, 'l': 2, 'e': 2, 'b': 2, 'n': 2})

```
_fct_filter_pos_ Removes factor levels where a specified character appears at specified positions within the levels.
```
import pandas as pd
from fctutils import fct_filter_pos

# Example factor vector
factor_series = pd.Series(['apple', 'banana', 'apricot', 'cherry', 'date', 'fig', 'grape'], dtype='category')

# Remove levels where 'a' appears at position 1
new_series = fct_filter_pos(factor_series, positions=[1], char='a')
print(new_series.cat.categories)
# Output: Index(['cherry', 'date', 'fig', 'grape'], dtype='object')

```
_fct_remove_levels_ Removes specified levels from a factor vector, keeping the remaining levels and their order unchanged.
```
import pandas as pd
from fctutils import fct_remove_levels

# Example factor vector
factor_series = pd.Series(['apple', 'banana', 'cherry', 'date', 'fig', 'grape'], dtype='category')

# Remove levels 'banana' and 'date'
new_series = fct_remove_levels(factor_series, levels_to_remove=['banana', 'date'])
print(new_series.cat.categories)
# Output: Index(['apple', 'cherry', 'fig', 'grape'], dtype='object')

```
_fct_filter_func_ Removes levels from a factor vector based on a user-defined function.
```
import pandas as pd
from fctutils import fct_filter_func

# Example factor vector
factor_series = pd.Series(['apple', 'banana', 'cherry', 'date'], dtype='category')

# Remove levels that start with 'b'
new_series = fct_filter_func(factor_series, filter_func=lambda x: not x.startswith('b'))
print(new_series.cat.categories)
# Output: Index(['apple', 'cherry', 'date'], dtype='object')

```

### Merging Factor Vectors
_fct_merge_similar_ Merge levels of a factor that are similar based on string distance.
```
import pandas as pd
from fctutils import fct_merge_similar

# Example factor vector
factor_series = pd.Series(['apple', 'appel', 'banana', 'bananna', 'cherry'], dtype='category')

# Merge similar levels
merged_series = fct_merge_similar(factor_series, max_distance=0.2)
print(merged_series.cat.categories)
# Output: Index(['apple', 'banana', 'cherry'], dtype='object')

```
_fct_concat_ Combines multiple factor vectors into a single factor, unifying the levels.
```
import pandas as pd
from fctutils import fct_concat

factor_vec1 = pd.Series(['apple', 'banana'], dtype='category')
factor_vec2 = pd.Series(['cherry', 'date'], dtype='category')

# Concatenate factors
concatenated_factor = fct_concat(factor_vec1, factor_vec2)
print(concatenated_factor.cat.categories)
# Output: Index(['apple', 'banana', 'cherry', 'date'], dtype='object')
```
_fct_combine_ Combines two vectors into a factor vector and sorts based on the levels of either the first or second vector.
```
import pandas as pd
from fctutils import fct_combine

vector1 = ['apple', 'banana', 'cherry']
vector2 = ['date', 'fig', 'grape', 'honeydew']

# Combine and sort based on vector1 levels
combined_series = fct_combine(vector1, vector2, sort_by=1)
print(combined_series.cat.categories)
# Output: Index(['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'honeydew'], dtype='object')
```
_fct_union_ Combines multiple factor vectors and returns a factor vector containing all unique levels.
```
import pandas as pd
from fctutils import fct_union

factor_vec1 = pd.Series(['apple', 'banana'], dtype='category')
factor_vec2 = pd.Series(['banana', 'cherry'], dtype='category')
factor_vec3 = pd.Series(['date', 'fig'], dtype='category')

# Get union of levels
union_series = fct_union(factor_vec1, factor_vec2, factor_vec3)
print(union_series.cat.categories)
# Output: Index(['apple', 'banana', 'cherry', 'date', 'fig'], dtype='object')
```
_fct_cross_ Create a new factor by combining levels from two factors.
```
import pandas as pd
from fctutils import fct_cross

# Example factor vectors
factor_series1 = pd.Series(['red', 'green', 'blue'], dtype='category')
factor_series2 = pd.Series(['circle', 'square', 'triangle'], dtype='category')

# Create cross product factor
crossed_series = fct_cross(factor_series1, factor_series2)
print(crossed_series)
# Output:
# 0       red_circle
# 1      green_square
# 2    blue_triangle
# dtype: category
# Categories (3, object): ['blue_triangle', 'green_square', 'red_circle']
```
_fct_match_ Match levels of one factor to another, aligning categories.
```
import pandas as pd
from fctutils import fct_match

# Example factor vectors
factor_series1 = pd.Series(['apple', 'banana', 'cherry'], dtype='category')
factor_series2 = pd.Series(['banana', 'date', 'cherry', 'apple'], dtype='category')

# Match levels of factor_series1 to factor_series2
matched_series = fct_match(factor_series1, factor_series2)
print(matched_series.cat.categories)
# Output: Index(['banana', 'date', 'cherry', 'apple'], dtype='object'
```
### Other Useful Functions
_fct_insert_ Inserts one or more new levels into a factor vector immediately after specified target levels.
* data: pandas DataFrame or Series.
* column: Column name if data is a DataFrame.
* insert: Level(s) to insert.
* target: Target level(s) after which to insert.
* position: 'after' or 'before'.
* allow_duplicates: bool, if True, allows duplicate levels.
* inplace: bool, if True, modify the data in place.
```
import pandas as pd
from fctutils import fct_insert

# Using a Series
factor_series = pd.Series(['apple', 'banana', 'cherry'], dtype='category')

# Insert 'date' after 'banana' in place
fct_insert(factor_series, insert='date', target='banana', inplace=True)
print(factor_series.cat.categories)
# Output: Index(['apple', 'banana', 'date', 'cherry'], dtype='object')
```
_fct_pairs_ Creates all unique pairwise combinations between elements of a vector.
* elements: List or pandas Series.
* ref: Optional list or pandas Series of reference elements.
* symmetric: bool, if True, unique unordered pairs are returned.
* include_na: bool, if True, includes NA values.
* include_self: bool, if True, includes pairs where Var1 == Var2.
* filter_fn: Function to filter the pairs.
* pre_process_fn: Function to preprocess elements.
* inplace: bool, if True, modify the data in place (if applicable).
```
import pandas as pd
from fctutils import fct_pairs

# Example vector with extra spaces
vec = [' A', 'b ', ' C ', 'D']

# Generate pairwise comparisons within vec
pairs = fct_pairs(vec, pre_process_fn=lambda x: x.strip())
print(pairs)
# Output:
#   Var1 Var2
# 0    A    b
# 1    A    C
# 2    A    D
# 3    b    C
# 4    b    D
# 5    C    D
```

