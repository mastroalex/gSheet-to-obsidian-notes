# Google Sheets to Obsidian markdown conversion

The following script allows us to convert a Google Sheet file to Obsidian markdown including `dataview`/`dataviewjs` syntax to query files and plot charts and tables.

## Requirements

It needs the configuration of [gspread](https://docs.gspread.org) module and to set the path of the `.json` key in `/src/helpers/check.py` in `giveServicePath()` function. 

## Usage

```bash
python3 /path/to/folder/main.py
```

Or filtering data with the starting date:

```bash
python3 /path/to/folder/main.py dd/mm/yyyy
```

## Description

For a complete description see [Google Sheets and Obsidian integration](https://alessandromastrofini.it/en/google-sheets-obsidian-integration/). 


It create an Obsidian markdown note for each training exercise and then another notes for the overall training day.
The training day contains also charts and summary table.

For the different notes the templates are defined into the `template.py` module. 


