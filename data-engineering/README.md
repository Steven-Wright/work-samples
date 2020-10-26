# work-samples
work-samples

## Purpose
The following files have been made available to provide a fuller assessment of my skills than is typically available through technical interviews.

All this work is my own and I've redacted any proprietary information.

## schema.sql.txt
An Abridged schema of a database that tracks retailer promotions, with a view providing a "flat" representation of the data and a trigger function to decompose incoming rows into facts and attributes. Today this database contains ~21K rows, with new rows added weekly using a VBA macro (not included, but available upon request) I wrote to scrape Excel files created by our analysts.

## query.sql.txt
An SQL query against the above database which compiles quarter-to-date averages of promotional and other retailer history to provide comparison points to current performance.

## visit_canidates.py
A Python script used to select candidates from registered channel-checkers ("secret shoppers") to visit retailers based on the distance between their location and the location of targeted stores.
