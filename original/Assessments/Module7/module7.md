Format:
Question: ...  
Type: Multiple Choice (Single Correct Answer),  Multiple Choice (Multiple Correct Answers), Free Response (Text Answers, Code Expression)
Answer: ...  
Choices: ...  

# Lesson 1

- Question: Which of the below code could be used to create a scatter plot of two sets of data called "x" and "y"?
    - Type: Multiple Choice (Single Correct Answer) or Free Response Code Expression
    - Answer: ax.scatter(x,y)
    - Choices: scatter.ax(x,y); ax.scatter(x,y); ax.histogram(x,y); xy.scatter

- Question: What type of correlation shows no obvious trend between the two variables being plotted?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: null correlation
    - Choices: joint correlation; negative correlation; positive correlation; null correlation

- Question: What type of correlation has vertical values that tend to decrease as horizontal values increase?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: negative correlation
    - Choices: joint correlation; negative correlation; positive correlation; null correlation

- Question: What type of correlation has vertical values that tend to increase as horizontal values increase?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: positive correlation
    - Choices: joint correlation; negative correlation; positive correlation; null correlation

- Question: A Pair Plot can be created using which Python module using the .pairplot method?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: seaborn
    - Choices: numpy; seaborn; matplotlib; pandas


# Lesson 2
- Question: I have created a numpy array that has the length of 100 called a. How do I reshape a to the shape of a 10 x 10 multi dimensional array?
  - Type: Multiple Choice (Single Correct Response)
  - Answer: a.reshape(10,10)
  - Choices: a.reshape(10,10); a.change_shape(10,10); a.shape(10,10); a.c_shape(10,10)
- Question: What is an identity matrix?
  - Type: Multiple Choice (Single Correct Response)
  - Answer:A Matrix where the diagonal elements are all 1 and other elements in the matrix are 0
  - Choices:A Matrix where the diagonal elements are all 1 and other elements in the matrix are 0; matrix where the diagonal elements are all 0 and other elements in the matrix are 1; A Matrix containing eyes; An matrix that identifies other matrices.
- Question: How do I create a 25 x 25 identity matrix in numpy? I have imported numpy as np.
  - Type: Multiple Choice (Single Correct Response)
  - Answer: np.eye(25)
  - Choices: np.eye(25); np.diag(5,5); np.c_identity(25); np.eye(5)
- Question: I have created a 5x5 numpy multidimensional array called x. How do you access elements in the first row?
  - Type: Multiple Choice (Single Correct Response)
  - Answer: x[0]
  - Choices: x[0]; x[:0]; x[0][0]; x.get_row(0)
- Question: I have created a 5x5 numpy multidimensional array called x. How do you access elements in the first column?
  - Type: Multiple Choice (Single Correct Response)
  - Answer: x[:,0]
  - Choices: x[:,0];x[0]; x[:0]; x.get_col(0)
- Question: I have created a 5x5 numpy multidimensional array called x. How do you you add scalar b to the matrix?
  - Type: Multiple Choice (Single Correct Response)
  - Answer: x + b
  - Choices: x+b ;x[0:0]+b; x.add_all(0); x.get_all(b, 'add')
- Question:How do I find the mean of a multi dimensional numpy array called x in Python?
  - Type: Multiple choice (Single Correct Response)
  - Answer: np.mean(x)
  - Choices: np.mean(x), np.std(x), np.get_mean(x), np.whatis('mean', x)
- Question:How do I find the min value of a multi dimensional numpy array called x in Python?
  - Type: Multiple choice (Single Correct Response)
  - Answer: np.min(x)
  - Choices: np.min(x), np.std(x), np.get_min(x), np.whatis('min', x)

# Lesson 3

- Question: What is Simpson's Paradox?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: Trends within different groups dissapear when data are combined
    - Choices: Trends within different groups dissapear when data are combined; The Simpsons keeps getting worse but people keep watching; It looks like there's an association between two independent variables when there really isn't; Moving something from one group to another increases both averages even though no values actually increase

- Question: What is Will Rogers Paradox?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: Moving something from one group to another increases both averages even though no values actually increase
    - Choices: Trends within different groups dissapear when data are combined; Too many people named Will have the last name Rogers; It looks like there's an association between two independent variables when there really isn't; Moving something from one group to another increases both averages even though no values actually increase

- Question: What is Berkson's Paradox?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: It looks like there's an association between two independent variables when there really isn't
    - Choices: Trends within different groups dissapear when data are combined; Berkshire Hathaway's relatively poor performance since 1999; It looks like there's an association between two independent variables when there really isn't; Moving something from one group to another increases both averages even though no values actually increase

- Question: What is the Multiple Comparison Fallacy?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: Unexpected trends occur just by chance
    - Choices: Trends within different groups dissapear when data are combined; Unexpected trends occur just by chance; It looks like there's an association between two independent variables when there really isn't; Disregarding important information when making a judgement of how likely something is

- Question: What is the Base Rate Fallacy?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: Disregarding important information when making a judgement of how likely something is
    - Choices: Trends within different groups dissapear when data are combined; Unexpected trends occur just by chance; It looks like there's an association between two independent variables when there really isn't; Disregarding important information when making a judgement of how likely something is


# Lesson 4

- Question: What does OLS try to minimize?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: The sum of squared errors
    - Choices: The sum of errors; The sum of squared errors; The sum of cubed errors; The sum of predictions


- Question: In the context of OLS, how is error defined?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: The difference between prediction and reality
    - Choices: The difference between prediction and reality; The number of data points; The number of squares; The sum of predictions

- Question: For the OLS equation $$y = \alpha + \beta x + \epsilon$$ which variable is the dependent variable?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: $$y$$
    - Choices: $$\epsilon$$; $$\beta$$; $$x$$; $$y$$

- Question: For the OLS equation $$y = \alpha + \beta x + \epsilon$$ which variable is the independent variable?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: $$x$$
    - Choices: $$\epsilon$$; $$\beta$$; $$x$$; $$y$$

- Question: For the OLS equation $$y = \alpha + \beta x + \epsilon$$ which variable represents the error?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: $$\epsilon$$
    - Choices: $$\epsilon$$; $$\beta$$; $$x$$; $$y$$

- Question: For the OLS equation $$y = \alpha + \beta x + \epsilon$$ which variable represents the intercept?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: $$\alpha$$
    - Choices: $$\epsilon$$; $$\beta$$; $$x$$; $$y$$
