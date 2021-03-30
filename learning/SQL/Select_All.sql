/*
 *============================================= Revising the Select Query I =====================================
 * Query all columns (attributes) for every row in the CITY table.
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
 select * from city where CountryCode = 'USA' and population > 100000;
