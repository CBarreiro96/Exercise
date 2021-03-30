/*
 *============================================= Revising the Select Query II =====================================
 * Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.
 * The CITY table is described as follows:
 *
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
 select NAME from CITY WHERE POPULATION >= 120000 AND COUNTRYCODE = 'USA';
