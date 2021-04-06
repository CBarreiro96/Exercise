/*
 *============================================= Revising the Select Query I =====================================
 * Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
 * The CITY table is described as follows:  
 *            CITY
 *  -------------------------
 * | Field     |    Type     |
 *  -------------------------
 * |  Id       |   Number    |
 *  -------------------------
 * |  Name     | VARCHAR2(17)|
 *  ------------------------- 
 * |COUNTRYCODE| VARCHAR2(3) |
 *  -------------------------
 * | District  | VARCHAR2(20 |
 *  -------------------------
 * | Population|   NUMBER    |
 *  -------------------------
 */
select name from city where COUNTRYCODE = 'JPN';
