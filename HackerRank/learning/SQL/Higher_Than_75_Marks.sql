/* 
* ==================================== Higher Than 75 Marks =================================
* Query the Name of any student in STUDENTS who scored higher than 75 Marks. Order your output 
* by the last three characters of each name. If two or more students both have names ending in
* the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.
*
* INPUT FORMAT
*                                  -------------------------
*                                 |  Column   |    Type     |
*                                  -------------------------
*                                 |     Id    |   Integer   |
*                                  -------------------------
*                                 |    Name   |    String   |
*                                  ------------------------- 
*                                 |   Marks   |   Integer   |
*                                  -------------------------
* The STUDENTS table is described as follows: 
*  The Name column only contains uppercase (A-Z) and lowercase (a-z) letters.
*
*
* SAMPLE IMPUT
*
*                                  -------------------------------------
*                                 |     ID    |    NAME     |   MARKS   |
*                                  -------------------------------------
*                                 |     1     |   Ashley    |    81     |
*                                  -------------------------------------
*                                 |     2     |  Samantha   |    75     |
*                                  ------------------------------------- 
*                                 |     4     |   Julia     |    76     |
*                                  -------------------------------------
*                                 |     3     |   Belvet    |    84     |
*                                  -------------------------------------
*
* Sample output
*
*   Ashley
*   Julia
*   Belvet
*/
select name from students where marks > 75 order by RIGHT(Name, 3), ID;