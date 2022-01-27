# Sell permissions
0. Switch to user betty in 8 chars line.
1. Print the effective username of the current user.
2. Print all the groups the current user is part of.
3. Change the owner of the file hello to the user betty.
4. Create an empty file called hello.
5. Add execute permission to the owner of the file hello.
6. Add execute permission to the owner and the group owner, and read permission to other users, to the file hello.
7. Add execution permission to the owner, the group owner and the other users, to the file hello:
   * The file hello will be in the working directory.
   * Not allowed to use commas for this script.
8. Set the permission to the file hello as follows:
   * Owner: no permission at all.
   * Group: no permission at all.
   * Other users: all the permissions.
9. sets the mode of the file hello to this:
   -rwxr-x-wx
   * The file hello will be in the working directory.
   * Not allowed to use commas for this script.
10. Set the mode of the file hello the same as olleh’s mode (-rw-rw-r--):
    * The mode of olleh will not always be 664. Make sure your script works for any mode.
11. Add execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
12. Create a directory called my_dir with permissions 751 in the working directory.
13. Change the group owner to school for the file hello.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
100. changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.
101. changes the owner and the group owner of _hello to vincent and staff respectively.
     * The file _hello is in the working directory.
     * The file _hello is a symbolic link.
102. Script that changes the owner of the file hello to vincent only if it is owned by the user guillaume.
103. Play the StarWars IV episode in the terminal.
