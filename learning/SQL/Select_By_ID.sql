/*
 *============================================= Revising the Select Query I =====================================
 * Query all columns for a city in CITY with the ID 1661.
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
select  * from city where ID = 1661;
