\# KEV Power BI Dashboard



A Power BI dashboard analysing the CISA Known Exploited Vulnerabilities (KEV) catalog: which vendors appear most, how additions change over time, and how many entries are linked to ransomware.



\## Tools used

\- Python (pandas) for data cleaning

\- Power BI for the dashboard



\## Files

\- `known\_exploited\_vulnerabilities.csv`: raw KEV data

\- `load\_data.py`: loads and inspects the raw data

\- `clean\_data.py`: cleans the data and adds columns (days to fix, year added, ransomware flag)

\- `kev\_clean.csv`: cleaned data used in Power BI

\- `rasn.pbix`: Power BI dashboard file

\- `pdf.pdf`: exported dashboard



\## Dashboard pages

1\. \*\*KEV Overview:\*\* cards for Total CVEs, Ransomware CVEs, Ransomware Share and Avg Days to Fix, plus a line chart over time.

2\. \*\*Top 10 Vendors:\*\* bar chart of the vendors with the most known exploited vulnerabilities, with a year slicer.



\## Key insights

\- Microsoft has the most entries (about 400), followed by Cisco, Apple, Adobe and Google.

\- Additions peaked in 2022, fell in 2023-24, and have risen again since 2025.

\- About 20% of entries are linked to known ransomware campaigns.



\## How to run

1\. Install Python and pandas: `pip install pandas`

2\. Run `python clean\_data.py` in the project folder to create `kev\_clean.csv`.

3\. Open `rasn.pbix` in Power BI Desktop.

