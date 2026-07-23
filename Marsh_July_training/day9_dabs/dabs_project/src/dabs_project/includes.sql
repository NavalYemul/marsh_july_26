-- Databricks notebook source
create catalog if not exists dev;

create schema if not exists dev.bronze;
create schema if not exists dev.silver;
create schema if not exists dev.gold;

create volume if not exists dev.bronze.raw;

create catalog if not exists uat;

create schema if not exists uat.bronze;
create schema if not exists uat.silver;
create schema if not exists uat.gold;

create volume if not exists uat.bronze.raw;

create catalog if not exists prod;

create schema if not exists prod.bronze;
create schema if not exists prod.silver;
create schema if not exists prod.gold;

create volume if not exists prod.bronze.raw;