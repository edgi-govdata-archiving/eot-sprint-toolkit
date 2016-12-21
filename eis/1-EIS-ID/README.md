# EIS ID scraping

A full listing of all Environmental Impact Statements is available at https://cdxnodengn.epa.gov/cdx-enepa-public/action/eis/search by doing an empty search. Unfortunately the CSV export there isn't useful because it doesn't include the ID numbers of the statements, so we need to go through all the pages of the results and scrape them to get the information out.

`scrape-eis.rb` does this.

## Usage

Usage: `ruby scrape-eis.rb > eis-listing.csv`

Before running you will need to get a valid jsessionid field and paste it into the script.  Without it, you will just get the same 20 results over and over because the paging isn't happening. Go to https://cdxnodengn.epa.gov/cdx-enepa-public/action/eis/search and do an empty search, and the URL of the results page will have a jsessionid field that will work.

## CSV output

The CSV file has these columns, all pulled from the database:

* eis_id
* title
* document
* epa_comment_letter_date
* federal_register_date
* agency
* state

The important field is the `eis_id`.

For example, [https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details?eisId=219321](219321), "Effects of Oil and Gas Activities in the Arctic Ocean."

At the bottom of the page there are links to several EIS documents and a comment letter.  On the search results page there are links to ZIP files for each.

* Documents: https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details/downloadEisDocuments?eisId=219321
* Comments: https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details/downloadCommentLetters?eisId=219321

Knowing the eis_id and those URL patterns means it's easy to download all the documents and comments (but make sure to rename the downloaded ZIP files, because they do not have unique names).

## Unique results

`cut -d, -f1 eis-listing.csv | sort | uniq -c | sort -rn | head -5` will tell you if there are any duplicated lines, which may happen if more queries are made than necessary just to be on the safe side.

    2 83709
    2 83553
    2 83301
    2 83232
    2 82975

Tidy things up by doing this:

    head -1 eis-listing.csv > tmp.csv
    grep -v eis_id eis-listing.csv | sort -rn | uniq >> tmp.csv
	mv tmp.csv eis-listing.csv

# License

GPL v3.  See LICENSE for details.
