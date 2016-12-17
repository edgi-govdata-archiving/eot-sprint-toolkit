# EIS scraping

## Stage one: get ID numbers (@wdenton, @freemoth)

A full listing of all Environmental Impact Statements is available at https://cdxnodengn.epa.gov/cdx-enepa-public/action/eis/search by doing an empty search. Unfortunately the CSV export there isn't useful because it doesn't include the ID numbers of the statements, so we need to go through all the pages of the results and scrape them to get the information out.

`scrape-eis.rb` does this.

Usage: `ruby scrape-eis.rb > eis-listing.csv`

The CSV file has these columns, all pulled from the database:

* eis_id
* title
* document
* epa_comment_letter_date
* federal_register_date
* agency
* state

The important field is the `eid_id`.

For example, [https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details?eisId=219321](219321), "Effects of Oil and Gas Activities in the Arctic Ocean."

At the bottom of the page there are links to several EIS documents and a comment letter.  On the search results page there are links to ZIP files for each.

* Documents: https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details/downloadEisDocuments?eisId=219321
* Comments: https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details/downloadCommentLetters?eisId=219321

Knowing the eis_id and those URL patterns means it's easy to download all the documents and comments (but make sure to rename the downloaded ZIP files, because they do not have unique names).

## Stage two: get the metadata

## Stage three: archive
