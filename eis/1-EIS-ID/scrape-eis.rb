#!/usr/bin/env ruby

require "csv"
require "nokogiri"
require "open-uri"

# Note: annoying jsessionid field is required or you will just
# get the same 20 results because the paging isn't happening.
# Go to
# https://cdxnodengn.epa.gov/cdx-enepa-public/action/eis/search
# and do an empty search, and the URL of the results page
# will have a jsessionid field. Paste it in below.

results_page_url = "https://cdxnodengn.epa.gov/" \
                   "cdx-enepa-II/public/action/eis/search/search" \
                   ";jsessionid=::JSESSIONID::?d-446779-p=::PAGE::"

jsessionid = "161419A50BD99AC9A7D90C19ADE84559"

results_page_url.gsub!("::JSESSIONID::", jsessionid)

puts %w(eis_id title document epa_comment_letter_date federal_register_date agency state).to_csv

# "14,633 items found, displaying 1 to 20"
# # 14633 / 20 = 731, so go up to 732

page = 1
page_end = 733

while page <= page_end
  warn page
  results_page = results_page_url.gsub("::PAGE::", page.to_s)
  # warn results_page
  begin
    open(results_page) do |f|
      if f.status[0] == "200"
        doc = Nokogiri::HTML(f.read)
        begin
          doc.xpath("//table/tbody/tr").each do |row|
            title_link = row.xpath("td")[0].xpath("a")
            title = title_link.text
            eis_id = title_link.xpath("@href").text.split("?")[1].split("=")[1]
            document = row.xpath("td")[1].text
            epa_comment_letter_date = row.xpath("td")[2].text
            federal_register_date = row.xpath("td")[3].text
            agency = row.xpath("td")[4].text
            state = row.xpath("td")[5].text
            puts [eis_id, title, document, epa_comment_letter_date,
                  federal_register_date, agency, state].to_csv
          end
        rescue StandardError => e
          warn "Error parsing row: #{e}"
        end
      else
        warn "Cannot load spreadsheet: #{f.status}"
      end
    end
  rescue StandardError => open_error
    warn "ERROR on #{page}: #{open_error}"
  end
  page += 1
  # sleep 1 # If you want to be nice, but it's slow as it is.
end
