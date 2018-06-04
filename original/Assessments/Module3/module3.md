Format:
Type: Multiple Choice (Single Correct Answer),  Multiple Choice (Multiple Correct Answers), Free Response (Text Answers, Code Expression)
Question: ...  
Answer: ...  
Choices: ...  

# Lesson 1

# Lesson 2

- Question: Which Unix command can be used to list the contents of a directory?
    - Type: Multiple Choice (Single Correct Answer) or Free Response Programming Question
    - Choices: list_contents; ls; list; content list

 - Question: Which Unix command can be used to list all files and directories?
    - Type: Multiple Choice (Single Correct Answer) or Free Response Programming Question
    - Choices: ls all; list -a; list all; ls -a

 - Question: Which Unix command can be used to change the current working directory to "/home"
    - Type: Multiple Choice (Single Correct Answer) or Free Response Programming Question
    - Choices: change /home; cd /home; change directory /home; go /home

 - Question: Which Unix command can be used to create an empty file called "empty_file"
    - Type: Multiple Choice (Single Correct Answer) or Free Response Programming Question
    - Choices: create empty_file; make empty_file; touch empty_file; mkdir empty_file

 - Question: Which Unix command can be used to create a new directory called "new_directory"
    - Type: Multiple Choice (Single Correct Answer) or Free Response Programming Question
    - Choices: mkdir new_directory; make new_directory; touch new_directory; create new_directory

  - Question: Which Unix command can be used to delete a file called "my_file" ?
    - Type: Multiple Choice (Single Correct Answer) or Free Response Programming Question
    - Choices: remove my_file; delete my_file; rm my_file; rmdir my_file

  - Question: Which Unix command can be used to download files from a website?
    - Type: Multiple Choice (Single Correct Answer)
    - Choices: website download; wget; websiteget; webget

  - Question: Which Unix command can be used to view the contents of a file called "my_file" ?
    - Type: Multiple Choice (Single Correct Answer) or Free Response Programming Question
    - Choices: view my_file; look my_file; cat my_file; peep my_file

  - Question: Which Unix command can be used to view the first 3 lines of a file called "my_file" ?
    - Type: Multiple Choice (Single Correct Answer) or Free Response Programming Question
    - Choices: head -3 my_file; cat my_file 3; 3 head my_file; cat my_file -3

# Lesson 3
- Question: What modes do I use to append to a file in binary mode?
  - Type: Multiple Choice (Single Answer)
  - Choices: ab; r; rb; x
- Question: Which one of the following code snippets will write to a file in Python?
  - Type: Multiple choice (Single Correct Answer)
  - Choices: with open('text.txt', 'w') as f: f.write('hi'); with open('text.txt', 'r') as f: f.write('hi'); with open('text.txt', 'b') as f: f.write('hi'); with open('text.txt', 'w') as f: f.read('hi')
- Question: Which library handles fast numerical arrays and matrices?
  - Type: Multiple choice (Single Correct Answer)
  - Choices:  numpy; seaborn; matplotlib ; csv
- Question: Which library handles writing and reading to CSV files
  - Type: Multiple choice (Single Correct Answer)
  - Choices: numpy; seaborn; matplotlib ; csv
- Question: If you want to save data to file, which of the following libraries should you use?
  - Type: Multiple choice (Single Correct Answer)
  - Choices: pickle; seaborn; matplotlib; scikit-learn
- Question: A file called 'data.p' how do I use pickle to load it into a variable called data?
  - Type: Multiple choice (Single Correct Answer)
  - Choices: import pickle\n\t with open('data.p', 'rb') as f:\n\t data = pickle.load(f); import pickle\n\t with open('data', 'rb') as f:\n\t data = pickle.load(f); import pickle\n\t with open('data.p', 'rb') as f:\n\t data = pickle.load(g); import pickle\n\t with open('data.p', 'r') as f:\n\t data = pickle.load(f)
- Question: While data persistence is useful, why is it not optimal?
  - Type: Multiple choice (Single Correct Answer)
  - Choices: All data is written and read as Python strings. Complex arrangements of heterogenous data thus require potentially complex (and costly in execution time) transformations; All concurrency is provided by the file system, thus we are not guaranteed consistent results if multiple writers work at the same time; Without extra effort, for example, to write to a binary file or to employ compression, this approach is costly in terms of storage space; We rely completely on the underlying file system for consistency and durability. Thus, persisted application state may have unintentional dependencies on the underlying file system.
# Lesson 4

- Question: Pandas primarily utilizes which data structures?
    - Type: Multiple Choice (Single Correct Answer)
    - Choices: Series; List; DataFrame; numpy array

- Question: Before using pandas which code must first be run to make the library available?
    - Type: Multiple Choice (Single Correct Answer) or Free Response Programming Question
    - Choices: import pd; import library pandas; import pandas as pd; import pandas library

- Question: How do you view the column names of a DataFrame called "df"?
    - Type: Multiple Choice (Single Correct Answer) or Free Response Programming Question
    - Choices: df(columns); columns(df); df.columns; columns.df

- Question: What will be the data type of the output of "df['A']" where "df" is a DataFrame and 'A' is one of the columns.
    - Type: Multiple Choice (Single Correct Answer)
    - Choices: Series; DataFrame; List; numpy array

- Question: How would you view summary statistics of a DataFrame called "df"?
    - Type: Multiple Choice (Single Correct Answer) or Free Response Programming Question
    - Choices: df.summary(); df.describe(); df.statistics(); df.description()   

- Question: What does the "iloc" method of a pandas data frame do?
    - Type: Multiple Choice (Single Correct Answer) 
    - Choices: Uses positional index to select a subset of the entire dataframe; Locks the dataframe so it can't be changed; Unlocks the dataframe so it can be changed; Uses explicit labels to select a subset of the entire dataframe 

- Question: What does the "loc" method of a pandas data frame do?
    - Type: Multiple Choice (Single Correct Answer) 
    - Choices: Uses positional index to select a subset of the entire dataframe; Locks the dataframe so it can't be changed; Unlocks the dataframe so it can be changed; Uses explicit labels to select a subset of the entire dataframe 
