# Google Sheets to Obsidian markdown conversion

The following script allows us to convert a Google Sheet file to Obsidian markdown including `dataview`/`dataviewjs` syntax to query files and plot charts and tables.

## Requirements

It needs the configuration of `gspread` module and to set the path of the `.json` key in `/src/helpers/check.py` in `giveServicePath()` function. 

## Usage

```bash
/python3 /path/to/folder/main.py
```

Or filtering data with the starting date:

```bash
/python3 /path/to/folder/main.py dd/mm/yyyy
```

## Descriptions

For a complete description see [Google Sheets and Obsidian integration](https://alessandromastrofini.it/en/google-sheets-obsidian-integration/). 


 
