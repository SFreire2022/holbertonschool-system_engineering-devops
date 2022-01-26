# Basic tools from shell
0. Show current working directory.
1. List current directory content.
2. Move from current directory to user home directory (must run as source ./script).
3. Display current directory contents in a long format.
4. Display current directory contents, including hidden files (starting with .). Use the long format.
5. Display current directory contents.
   * Long format
   * With user and group IDs displayed numerically
   * And hidden files (starting with .)
6. Creates a directory named my_first_directory in the /tmp/ directory.
7. Move the file betty from /tmp/ to /tmp/my_first_directory.
8. Delete the file betty.
9. Delete the directory my_first_directory that is in the /tmp directory.
10. Write a script that changes the working directory to the previous one.
11. List all files (even ones with hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
12. Prints the type of the file named iamafile. The file iamafile will be in the /tmp directory.
13. Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.
14. Copy all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
-------------------------------------------------------------------------------------------------------------------------------------------
100. Script that moves all files beginning with an uppercase letter to the directory /tmp/u.
101. Script that deletes all files in the current working directory that end with the character ~.
102. Script that creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory (in 2 lines).
103. Command that lists all the files and directories of the current directory, separated by commas (,).
    * Directory names end with a slash (/).
    * Files and directories starting with a dot (.) will be listed.
    * The listing will be alpha ordered, except for the directories . and .. which will be listed at the very beginning.
    * Only digits and letters are used to sort; Digits will come first.
    * You can assume that all the files we will test with will have at least one letter or one digit.
    * The listing ends with a new line.
104. Create a magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.