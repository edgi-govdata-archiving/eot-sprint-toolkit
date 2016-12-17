#!/usr/bin/env ruby

require 'csv'
require 'nokogiri'
require 'open-uri'

# "14,633 items found, displaying 1 to 20"

big_listing_url = "https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/search/search?searchCriteria.endCommentLetterDate=&d-446779-p=::PAGE::&searchCriteria.title=&searchRecords=Search&searchCritera.primaryStates=&searchCriteria.endFRDate=&searchCriteria.startCommentLetterDate=&searchCriteria.startFRDate=#results"

puts %w(eid_id title document epa_comment_letter_date federal_register_date agency state).to_csv

page = 1 # 14633 / 20 = 731, so go up to 732
page_end = page + 732 # Could go by hundreds if you want

while page < page_end
  warn page
  results_page = big_listing_url.gsub("::PAGE::", page.to_s)
  begin
    open(results_page) do |f|
      if f.status[0] == "200"
        doc = Nokogiri::HTML(f.read)
        begin
          doc.xpath("//table/tbody/tr").each do |row|
            title_link = row.xpath("td")[0].xpath("a")
            title = title_link.text
            eid_id = title_link.xpath("@href").text.split("?")[1].split("=")[1]
            document = row.xpath("td")[1].text
            epa_comment_letter_date = row.xpath("td")[2].text
            federal_register_date = row.xpath("td")[3].text
            agency = row.xpath("td")[4].text
            state = row.xpath("td")[5].text
            puts [eid_id, title, document, epa_comment_letter_date, federal_register_date, agency, state].to_csv
          end
          # rescue StandardError => e
          #   warn "Error parsing row: #{e}"
        end
      else
        logger.warn "Cannot load spreadsheet: #{f.status}"
      end
    end
  rescue StandardError => open_error
    warn "ERROR on #{page}: #{open_error}"
  end
  page += 1
  sleep 2 # Be nice
end
