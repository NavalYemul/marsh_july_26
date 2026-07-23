-- Databricks notebook source
-- DBTITLE 1,Std View
create or replace view IDENTIFIER(concat(:catalog, '.', 'gold.total_amount')) as  
select customer_id, round(sum(total_amount)) as total_amount from IDENTIFIER(concat(:catalog, '.', 'silver.sales_cleaned')) group by customer_id order by total_amount desc