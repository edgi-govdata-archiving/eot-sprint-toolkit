var request = require( 'request' );
var cheerio = require( 'cheerio' );
var fs = require( 'fs' );
var pageData = {
  metaData: {
    'EIS Title': '',
    'EIS Number': '',
    'Document Type': '',
    'Federal Register Date': '',
    'EIS Comment Due/ Review Period Date': '',
    'Amended Notice Date': '',
    'Amended Notice': '',
    'Supplemental Information': '',
    'Website': '',
    'EPA Comment Letter Date': '',
    'State or Territory': '',
    'Lead Agency': '',
    'Contact Name': '',
    'Contact Phone': '',
    'Rating (if Draft EIS)': ''
  },
  pdfLinks: []
};

request( 'https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details?eisId=222951', function( err, res, html ) {
  if ( !err && res.statusCode == 200 ) {
    var $ = cheerio.load( html );
    $( '.form-item' ).each( function( i, element ) {
      var formItem = $( element );
      var text = formItem.text().trim().replace( /\s\s+/g, ' ' );
      for ( var prop in pageData.metaData ) {
        if ( text.indexOf( prop ) !== -1 ) {
          pageData.metaData[ prop ] = text.replace( prop, '' );
        }
      }
    } );
    $( '.node.node-page div:last-child div:last-child p a' ).each( function( i, element ) {
      var linkElement = $( element );
      var linkHref = 'https://cdxnodengn.epa.gov' + linkElement.attr( 'href' );
      var linkText = linkElement.text();
      pageData.pdfLinks.push( {
        'pdf-link': linkHref,
        'pdf-filename': linkText
      } );
    } );

    fs.writeFileSync( 'page-metadata.json', JSON.stringify( pageData ), 'utf8' );
  }
} );
