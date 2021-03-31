/*
 *============================================= Revising the Select Query I =====================================
 * Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.
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
select *from city where COUNTRYCODE = 'JPN';
