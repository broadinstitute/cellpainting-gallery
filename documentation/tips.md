# Tips and Tricks

## Working with load_data.csv

- Because .csv's do not have explicit typing, when working programatically with load_data.csv's we recommend casting all `Metadata_` columns as strings to prevent conflicting dtypes.
e.g. An all numeric `Metadata_Plate` like `1053597806` may be read in as int or float, depending on the program.
