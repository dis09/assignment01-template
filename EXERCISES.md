## Exercise 1: Write your own statistical functions (40 + 10 points)

Implement the functions

- `my_range` (4)
- `my_mean` (6)
- `my_var` (8)
- `my_median` (10)
- `my_frequency_table` (12)

in the file [`ex1.py`](/exercises/ex1.py)

  - **Important**: To get any points, it is **not** allowed to import any external modules (i.e., no `import` statements). Use [built-in python functions](https://docs.python.org/3/library/functions.html) only.

  - Detailed descriptions of the functions are in [`ex1.py`](/exercises/ex1.py). Also look at the [test cases](/tests/test_ex1.py).

*Bonus*: For each of the functions think of how to properly implement the handling of missing values in the input (i.e., this is the case if the input array `x` contains some `None` values). For example, you could let the users of the function decide if missing values should be removed or not. Or you could throw an error in case of missing values *Explain your approach in the [report](/REPORT.md) (10)*.

---


## Exercise 2: Real data analysis with `pandas` and the `youtube` dataset ( [`ex2.py`](/exercises/ex2.py)) (60 + 20 points)

Read the data-set `./data/DEvideos.zip` into python. Use the `pandas.read_csv` function for that.

- How many videos are in the dataset? Save the result in the variable `n_rows` (5).

- What is the maximum number of likes and dislikes? Save the result in the variables `max_likes` (2.5) and `max_dislikes` (2.5).

- What is the `title` of the videos with the maximum number of likes and dislikes? Save the result *as a string* in the variables `max_likes_title` (7.5) and `max_dislikes_title` (7.5).

- What is the average number of `views` in the data-set: Calculate the arithmetic mean and the median and save the results in the variables `mean_views` (5), `median_views` (5). Why are the two numbers so different? *Answer this in your [report](/REPORT.md) (10)*.

- What is the Pearson correlation between `likes` and `views`. Save the result in the variable `corr_likes_views` (10). *In your [report](/REPORT.md) write about on how you interpret the value (10)*?

- Find the name of the channel that has the largest number of overall summed-up views for all its videos. Save the result in the string variable `max_views_channel` (15).

Hint: The following functions from the `pandas` library might be useful for solving the exercises: `pandas.DataFrame.loc`, `pandas.Series.item`, `pandas.DataFrame.groupby`, `pandas.DataFrame.idxmax`, `pandas.DataFrame.corr`, `pandas.DataFrame.sum`. Also look at the pandas cheatsheet and the [online reference](https://pandas.pydata.org/pandas-docs/stable/reference/index.html).
