# Part 2: Scraper

This takes in a csv (i.e. `../1-EIS-ID/eis-listing.csv`) with a unique ID of each EIS page, and outputs a JSON with the metadata and PDF links.

For example, if one of the links in the CSV document includes [this link](https://cdxnodengn.epa.gov/cdx-enepa-II/public/act
ion/eis/details?eisId=222951) with ID `222951`, then it will output this metadata JSON called `output/page-metadata-222951.json`:

```js
{
  "metaData": {
    "EIS Title": " Nexus Gas Transmission Project and Texas Eastern Appalachian Lease Project",
    "EIS Number": " 20160289",
    "Document Type": " Final",
    "Federal Register Date": " 2016-12-09 00:00:00.0",
    "EIS Comment Due/ Review Period Date": " 2017-01-09 00:00:00.0",
    "Amended Notice Date": "",
    "Amended Notice": "",
    "Supplemental Information": "",
    "Website": "",
    "EPA Comment Letter Date": "",
    "State or Territory": " MI - OH",
    "Lead Agency": " Federal Energy Regulatory Commission",
    "Contact Name": " Joanne Wachholder",
    "Contact Phone": " 202-502-8056",
    "Rating (if Draft EIS)": ""
  },
  "pdfLinks": [ {
    "pdf-link": "https://cdxnodengn.epa.gov#links",
    "pdf-filename": "EPA's PDF page"
  }, {
    "pdf-link": "https://cdxnodengn.epa.gov#links",
    "pdf-filename": "NEPAdatabasesupport"
  }, {
    "pdf-link": "https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details;jsessionid=DACBBEC17397AF888EDC4C8470BB17A1?downloadAttachment=&attachmentId=223102",
    "pdf-filename": "1 Final Environmental Impact Statement.pdf"
  }, {
    "pdf-link": "https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details;jsessionid=DACBBEC17397AF888EDC4C8470BB17A1?downloadAttachment=&attachmentId=223104",
    "pdf-filename": "2 Appendices A-D.pdf"
  }, {
    "pdf-link": "https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details;jsessionid=DACBBEC17397AF888EDC4C8470BB17A1?downloadAttachment=&attachmentId=223106",
    "pdf-filename": "3 Appendices E1-E4.pdf"
  }, {
    "pdf-link": "https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details;jsessionid=DACBBEC17397AF888EDC4C8470BB17A1?downloadAttachment=&attachmentId=223108",
    "pdf-filename": "4 Appendix E5 Part 1.pdf"
  }, {
    "pdf-link": "https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details;jsessionid=DACBBEC17397AF888EDC4C8470BB17A1?downloadAttachment=&attachmentId=223110",
    "pdf-filename": "5 Appendix E5 Part 2.pdf"
  }, {
    "pdf-link": "https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details;jsessionid=DACBBEC17397AF888EDC4C8470BB17A1?downloadAttachment=&attachmentId=223112",
    "pdf-filename": "6 Appendices F-Q.pdf"
  }, {
    "pdf-link": "https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details;jsessionid=DACBBEC17397AF888EDC4C8470BB17A1?downloadAttachment=&attachmentId=223114",
    "pdf-filename": "7 Appendix R Part 1.pdf"
  }, {
    "pdf-link": "https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details;jsessionid=DACBBEC17397AF888EDC4C8470BB17A1?downloadAttachment=&attachmentId=223116",
    "pdf-filename": "8 Appendix R Part 2.pdf"
  }, {
    "pdf-link": "https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details;jsessionid=DACBBEC17397AF888EDC4C8470BB17A1?downloadAttachment=&attachmentId=223118",
    "pdf-filename": "9 Appendix R Part 3.pdf"
  }, {
    "pdf-link": "https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details;jsessionid=DACBBEC17397AF888EDC4C8470BB17A1?downloadAttachment=&attachmentId=223120",
    "pdf-filename": "10 Appendix R Part 4.pdf"
  } ]
}

```

## Getting started

To get started, run

```sh
# navigate to the epa-eis-collection directory
cd epa-eis-collection/2-scraper
# install node modules
npm install
# start the scraper
npm start
```

