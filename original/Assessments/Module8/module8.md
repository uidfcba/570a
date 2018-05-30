Format:
Question: ...  
Type: Multiple Choice (Single Correct Answer),  Multiple Choice (Multiple Correct Answers), Free Response (Text Answers, Code Expression)
Answer: ...  
Choices: ...  

# Lesson 1

# Lesson 2

- Question: What is a violin plot?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: A box plot with a KDE
    - Choices: A box plot with a KDE; A plot of Mozart's life; A box plot, A KDE

- Question: What is a rug plot?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: A plot of short lines at each point
    - Choices: A plot of a rug; A plot of circles at each datapoint; A plot of short lines at each datapoint; A histogram

- Question: What can be added to aid in visualization for a rug plot if too many values are the same?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: jitter
    - Choices: derek jeter; jitter; jatter; jutter

- Question: What type of plot counts the number of datapoints in bins?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: Histogram
    - Choices: Histogram; Binogram; Scatter plot; Countergram

- Question: We can interpret normalized histogram as:
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: a probability mass distribution
    - Choices: a probability mass distribution; a scatter plot; a rug plot; a jitter plot

- Question: KDE works by replacing each discrete point with:
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: an approximating continuous function
    - Choices: a scatter plot; a circle; an exact continuous function; an approximating continuous function

- Question: What is another name for the function used in KDE?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: Kernel
    - Choices: Kernel; Colonel; Gaussian; Seaborn

- Question: What is the most common choice of kernel in KDE?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: Gaussian
    - Choices: Poisson; Gaussian; Histogram; Seaborn

# Lesson 3
- Question: What function or class do you use to perform KDE in Scikit Learn?
  - Type: Multiple Choice (Single Response)
  - Answer: sklearn.neighbors.KernelDensity
  - Choices: sklearn.neighbors.KernelDensity, sklearn.neighbors.Kernel_Density, sklearn.neighbors.kernel_density, sklearn.neighbors.kd
- Question: How do you create a Gaussiann KDE with sklearn imported?
  - Type:
  - Answer: sklearn.neighbors.KernelDensity(kernel='gaussian')
  - Choices: sklearn.neighbors.KernelDensity(kernel='gaussian'), sklearn.neighbors.Kernel_Density(kernel='gaussian'), sklearn.neighbors.kernel_density(kernel='gaussian'), sklearn.neighbors.kd(kernel='gaussian')
- Question:I have created a sklearn.neighbors.KernelDensity() object named kde. How do I fit kde to a column of a pandas dataframe called X?
  - Type:Multiple Choice (Single Correct Answer)
  - Answer: kde.fit(X)
  - Choices: kde.fit(X); kde.fit_pandas(X); kde.fit_pd(X); kde.fitPD()
- Question: I have imported seaborn as sns. How do I create a mult-variate KDE?
  - Type:Multiple choice (Single Correct Answer)
  - Answer: sns.joinplot()
  - Choices: sns.joinplot(); sns.mv_kde(); sns.kde(2); sns.plotkde()
- Question: I have created a sklearn.neighbors.KernelDensity() object named kde and fit it to data. How I sample and generate 50 new instances of data from kde?
  - Type: Multiple choice (Single Correct Answer)
  - Answer: kde.sample(50)
  - Choices: kde.sample(); kde.sample(50); kde.generate(50); kde.generate(); kde.make_new_data(50)
- Question: Given the information presented in Module 8 Lesson 3 readings which libraries can be used to create multi dimensional arrays in Python?
  - Type: Multiple Choice (Multiple Correct Response)
  - Answer: sci-kit learn; seaborn
  - Choices: sci-kit learn; seaborn; math; random; numpy
- Question: Is it possible to generate new data if you have a kernel density estimate?
  - Type: Multiple Choice (Single Correct Response)
  - Answer: Yes
  - Choices: Yes; No; Yes only if it is done in seaborn; Yes only if it is done in sci-kit learn
