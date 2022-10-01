library(worldfootballR)
library(magrittr)
results <- fotmob_get_matches_by_date(date = c("20220619", "20220723"))
dplyr::glimpse(results)

filtered_results <- results %>%
  dplyr::select(primary_id ccode, league_name = name, matches) %>%
  dplyr::filter(league_name == "Major League Soccer", ccode == "USA")

fotmob_matches <- c(3900346)
match_details <- fotmob_get_match_details(fotmob_matches)
dplyr::glimpse(match_details)
write.csv(match_details[[15]][[1]],"groningenvolendam.csv")
