# Databricks notebook source
# Creating widgets for leveraging parameters, and printing the parameters

dbutils.widgets.text("input", "","")
y = dbutils.widgets.get("input")
print ("Param -\'input':")
print ("bbbbbbbb1111111111111111111111111111111111111111111111111bbbbbbbbbbbbb -\'input':")
print (y)