Format:
Question: ...  
Type: Multiple Choice (Single Correct Answer),  Multiple Choice (Multiple Correct Answers), Free Response (Text Answers, Code Expression)
Answer: ...  
Choices: ...  

# Lesson 1

- Question: Why are pie charts difficult to interpret?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: It's difficult to reliably compare the 2-D areas
    - Choices: It's difficult to reliably compare the 2-D areas; It's hard to not think about pie when looking at one; It doesn't show percentages; It's circular

- Question: What effect can truncating the axis of a bar plot have on the perception of the plot?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: Makes differences between bars more dramatic
    - Choices: Makes differences between bars more dramatic; Makes differences between bars less dramatic; It has no effect; It becomes a histogram

- Question: Which of following values should be used when comparing across categories or groups?
    - Type: Multiple Choice (MUltiple Correct Answers)
    - Answer: Percentages; Rates
    - Choices: Percentages; Absolute values; Rates; None of the above

- Question: Which of following values should be used when comparing across categories or groups?
    - Type: Multiple Choice (MUltiple Correct Answers)
    - Answer: Percentages; Rates
    - Choices: Percentages; Absolute values; Rates; None of the above


# Lesson 2

- Question: What type of variable describes how much there is of something?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: Quantitative
    - Choices: Qualitative; Categorical; Quantitative; Descriptive

- Question: What type of variable describes what something is?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: Categorical
    - Choices: Illustrative; Categorical; Quantitative; Descriptive

- Question: What type of variable should hue be used for in order to make distinctions?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: Categorical
    - Choices: Illustrative; Categorical; Quantitative; Descriptive

- Question: What type of graph makes it easy to see overall changes over time?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: Line graph
    - Choices: Time graph; Bar graph; Pie graph; Line graph

- Question: Which attributes are useful for encoding categorical values?
    - Type: Multiple Choice (Multiple Correct Answers)
    - Answer: Shape; Hue
    - Choices: Hue; Area; Lightness; Shape

- Question: Which attributes are useful for encoding quantitative values?
    - Type: Multiple Choice (Multiple Correct Answers)
    - Answer: Saturation; 2-D position
    - Choices: Spatial grouping; Saturation; 2-D position; Enclosure

# Lesson 3

- Question: How would you import the matplotlib module?
    - Type: Multiple Choice (Single Correct Answer) or Free Response Code Expression
    - Answer: import matplotlib.pyplot as plt
    - Choices: import matplotlib.pyplot as plt; from pyplot import matplotlib.plt, load matplotlib.plt as pyplot, library matplotlib.pyplot as plt

- Question: What effect would adding the option "figsize(5,5)" have on a resulting figure from plt.subplots()?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: Make the figure 5 units wide and 5 units tall
    - Choices: Make the figure 5 units wide and 5 units tall; Make the figure 25 units wide, Make the figure 25 units tall, Make the figure 5 units taller and 5 units wider

- Question: Which below code will save a plot titled "my_plot.pdf"?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: plt.savefig("my_plot.pdf")
    - Choices: plt.figsave("my_plot.pdf"); plt.savefig(my_plot.pdf); plt.savefig("my_plot.pdf"); plt.save("my_plot.pdf")

- Question: How would you import the seaborn module?
    - Type: Multiple Choice (Single Correct Answer) or Free Response Code Expression
    - Answer: import seaborn as sns
    - Choices: import seaborn sns; import seaborn as sns; load seaborn as sns; library seaborn as sns

- Question: Which of the below code will add the label "x-axis" to the x-axis of a plot?
    - Type: Multiple Choice (Single Correct Answer) or Free Response Code Expression
    - Answer: ax.set_xlabel("x-axis")
    - Choices: ax.xlabel("x-axis"); ax.set_ylabel("x-axis"); ax.set_xlabel("x-axis"); ax.set_xlabel(x-axis)

- Question: Which of the below code will add the title "my plot" to a plot?
    - Type: Multiple Choice (Single Correct Answer) or Free Response Code Expression
    - Answer: ax.set_title("my plot")
    - Choices: ax.set_label("my plot"); ax.title("x-axis"); ax.set_title(my plot); ax.set_title("my plot")

- Question: Which below code will change the y-axis limits of a plot to between 10 and 20?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: ax.set_ylim(10,20)
    - Choices: ax.set_ylim(10,20); ax.ylim(10,20); ax.y_lim(10,20); ax.change_ylim(10,20)


# Lesson 4
- Question: Which of these types of plots can be used to display 1D distribution of data?
  - Type: Multiple Choice (multiple correct answers)
  - Answer:rugplot, boxplot, histogram
  - Choices: rugplot, boxplot, histogram, 3d scatter plot
- Question:I have imported seaborn. What function or class would I use to make a rugplot?
  - Type: Multiple Choice (Single correct answer)
  - Answer: rugplot
  - Choices: rugplot, Rugplot, RUGPLOT, pyplot, pandas
- Question: I have imported **seaborn as sns**, and loaded data to a dataframe call **x** with a column named **"A"**. Which of following code snippets creates a boxplot using seaborn?
  - Type: Multiple Choice (Single correct answer)
  - Answer: sns.boxplot(x=x['A'])
  - Choices: sns.boxplot(x=x['A']), boxplot(x=x['A']), sns.boxplot(x=x[A]), sns.boxplot(x=x['a'])
- Question: matplotlib.pyplot is imported as plt.  We then create a figure and axes object from plt.subplots as fig and ax respectively. Which function or class would I use to create histogram from pyplot?
  - Type: Multiple Choice (Single Correct Answer)
  - Answer: ax.hist()
  - Choices: ax.hist(), ax.hist, sns.hist, sns.hist()
- Question: If I have N data points how bins should I have?
  - Type: Multiple Choice (Single Correct Response)
  - Answer: root-three N bins
  - Choices:root-three N bins; N bins; N/2 bins; N+1 bins
- Question: Which plot type can be used to explore how data are distributed in a binned representation?
  - Type: Multiple Choice (Single Correct Response)
  - Answer: Histogram
  - Choices: Histogram; Plot; 3D Scatter Plot; Box Plot
- Question: What happens if you use too many bins in a Histogram?
  - Type: Multiple Choice (Single Correct Response)
  - Answer: More bins capture more detail however it may also capture noise.
  - Choices: More bins capture more detail however it may also capture noise; More bins capture less detail however it may also capture noise; More bins capture more detail; It will not look nice
