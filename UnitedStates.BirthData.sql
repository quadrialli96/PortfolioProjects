-- United states birth data collected by the CDC ranging from year 2016-2018. Data was collected by counties and it was analyzed using Google Cloud Platform.

-- Link to the data => https://console.cloud.google.com/bigquery(cameo:product/center-disease-control/wonder-births)?project=portfolio-project-342104

-- Skills used: Temp Tables, Windows Functions, Aggregate Functions, Wild cards, Self-ish Joins & INNER JOINS, Case Statements.

-- What is the sum of all births in Florida (2016-2018)?
SELECT SUM(Births) AS total_num_birth
FROM `bigquery-public-data.sdoh_cdc_wonder_natality.county_natality`
WHERE County_of_Residence LIKE "%FL%"



--What is the sum of all birth in California in 2018?
SELECT sum(Births) AS new_column
FROM `bigquery-public-data.sdoh_cdc_wonder_natality.county_natality`
WHERE County_of_Residence like "%CA%"
AND Year = '2018-01-01'



--What county in NY has the highest Average Number of Prenatal Visits (descending order).
Select County_of_Residence, max(Ave_Number_of_Prenatal_Wks) AS highest_num_prenat
FROM `bigquery-public-data.sdoh_cdc_wonder_natality.county_natality`
WHERE County_of_Residence like "%NY%"
GROUP BY County_of_Residence
ORDER BY highest_num_prenat DESC



-- What county had the highest average age of mother in the overall table?
SELECT County_of_Residence, max(Ave_Age_of_Mother) AS highest_age_mom
FROM `bigquery-public-data.sdoh_cdc_wonder_natality.county_natality`
GROUP BY County_of_Residence
ORDER BY highest_age_mom desc



-- What is the count of all average birth weight in grams in the counties that has "GA"
SELECT COUNT(Ave_Birth_Weight_gms) AS count_ave_birth_weight
FROM `bigquery-public-data.sdoh_cdc_wonder_natality.county_natality`
WHERE County_of_Residence LIKE "%GA%"



-- What county has the lowest Average number of prenatal weeks?
SELECT County_of_Residence, min(Ave_Number_of_Prenatal_Wks) AS lowest_prenat_wks
FROM `bigquery-public-data.sdoh_cdc_wonder_natality.county_natality`
GROUP BY County_of_Residence
ORDER BY lowest_prenat_wks



--- This gives us county of residence when we input the code.
SELECT County_of_Residence, County_of_Residence_FIPS
    CASE WHEN County_of_Residence_FIPS = 39049 THEN 'Franklin County, OH'
         WHEN County_of_Residence_FIPS = 13113 THEN 'Fayette County GA'
         ELSE 'other' END
         AS new_colom
FROM `bigquery-public-data.sdoh_cdc_wonder_natality.county_natality`
ORDER BY new_colom


--- This gives us the first 10 counties with births lower than 1000 in all the states throughout the year 2016-2018.
SELECT County_of_Residence, Births, Year
FROM `bigquery-public-data.sdoh_cdc_wonder_natality.county_natality`
WHERE births < 1000
ORDER BY Births desc
LIMIT 10


-- This helps us compare the same table with eachother using Self-ish Joins.
-- This also helps us filter out rows with unidentified counties.

SELECT b1.Ave_Age_of_Mother, b2.Ave_Age_of_Mother, b1.County_of_Residence as county_res
FROM `bigquery-public-data.sdoh_cdc_wonder_natality.county_natality` AS b1
INNER JOIN `bigquery-public-data.sdoh_cdc_wonder_natality.county_natality` AS b2
ON b1.Ave_Age_of_Mother = b2.Ave_Age_of_Mother
WHERE b1.County_of_Residence is not null
ORDER BY b1.Ave_Age_of_Mother