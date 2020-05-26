<title>Welcome to the MVP Leveler Python Package!</title>

<h1>WELCOME!</h1>

<body>Thank you for downloading the MVP Leveler Python Package. You should have received five total files: mvpleveler.py; KindergartenList.txt; G1List.txt; READEME.md (this file); and about.md </body>

<h2>The MVP Leveler assists writers and editors in determining the grade-level of certain words.</h2>

<body>The purpose of this instrument is to eventually provide practitioners of grade-level writing a simple way to cross reference the appropriate grade level for a given word. This program is merely a minimal viable product and contains word lists for Kindergarten and Grade 1 leveling.</body>

<h2>Installation</h2>

<body>To install the package, download the five files to a single directory on your computer. Make sure that all of the files live in the same place.</body>

<h2>Execution</h2>

<body>To execute the program, you must first install Python 3 to your command line. From there, run: </body>

<code>python mvpleveler.py</code>

<body>This should launch the program within your command line.</body>

<h2>How to Operate</h2>

<body>The MVP Leveler is straightforward. The program will greet you, then ask you which grade you would like to test reading levels for. You can select K or G1, which respectively represent Kindergarten and Grade 1.</body>

<body>After selecting the grade you want to level within, you will be asked to input a word to level. For example, if you select Kindergarten, you will be prompted: </body>
<code>Please input word for Kindergarten leveling</code>

<body>From here, you can enter any word that comes to mind. If the word is appropriate for a Kindergarten audience, the program will inform you as such: </body>

<code>This word is appropriate for a Kindergarten reading audience!</code>

<body>If the word is *NOT* appropriate for a Kindergarten audience, you will be informed: </body>

<code>I am sorry, this word is not appropriate for a Kindergarten reading audience.</code>
<h2>Further Uses</h2>

<body>The MVP Leveler can be expanded upon to contain other lists. To create a new list to be compared against, start a text document and sort your words in any order you wish. However, the words should be set between single quotes and divided by commas.</body>

<body><br>The list should be saved in the same location on your computer as the MVP Leveler package.</body></br>

<body><br>The Python code will need to be amended to import your list. You will need to open the mvpleveler.py file in VS Code or another program editor. </body></br>

<body><br>First, you must tell Python to open the list along with the other two lists. Let's call the new list G2List.txt. Create a new line below line two and type: </body></br>

<code>G2_file = open("G2List.txt", "r")</code>

<body>This will import your list as G2_file.</body>

<body><br>Next, we want to define the file as a data file. Below the code that reads: <body></br>
<code>k_data = Kindergarten_file.readlines()</code>
<code>g1_data = G1_file.readlines()</code>

<body>Add a new line and write: </body>
<code>g2_data = G2_file.readlines()</code>

<body>Then, tell Python to close the file.</body>
<code>G1_file.close()</code>

<body>Now the file will need to be cleaned up a bit for easier reading in Python. To clean up the commas and quotes, first enter this code: </body>
<code>g2_data_splitted = g2_data[0].split(',')</code>
<body>This will split the commas from the elements in the list.</body>

<body><br>Now, define the data as a new list: </body></br>
<code>grade2_list = []</code>

<body>Now Python will want to clean up the quotes and added syntax in your txt file. To do this, enter the following block of code: <body>
<code>for elem in g2_data_splitted:</code>
<code>elem = elem.strip()</code>
<code> elem = elem.strip('\'')</code>
<code>grade2_list.append(elem)</code>

<body>Next, you will want to combine your list with the other two existing lists in a new set. This will allow the program to build your list into the previous grade levels.</body>
<body><br>To do this, create a new line of code below the existing line reading: </body><br>
<code>grade2_set = set(grade2_list + grade1_list + kindergarten_list)</code>

<body>Finally, you will want to amend the prompts to include the option of your new list.</body>