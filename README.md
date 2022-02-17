# Search and filter Athens Courses in one place!

As you may know, page [https://register.athensnetwork.eu/courses](https://register.athensnetwork.eu/courses) is not too user-friendly. It does not allow to filter available courses by the year of study or language for example. That's exactly why I scrapped all course description pages and gathered them in one place. Have a look [here](https://mstaczek.github.io/athens_courses/)!
  
## Athens Exchange Courses March 2022:  
Unofficial pages (mine):

- [Nice webpage with filters etc](https://mstaczek.github.io/athens_courses/)  
- [Simple tabular view of data](https://mstaczek.github.io/athens_courses/table)  

[Official webpage](https://register.athensnetwork.eu/courses)  

## Features:  
- all courses information gathered in a single webpage!
- filtering,
- sorting,
- no filtering by tags (but we all know, that course descriptions are more important).

Link: https://mstaczek.github.io/athens_courses/

Last updated: January 2022

### Disclaimer

I did [this webpage](https://mstaczek.github.io/athens_courses/) to facilitate looking for courses offered at the next session of Athens Network students exchange. However, data gathered and presented there is by no means official, might be outdated and is not to be used as the only factor when selecting courses. 

Remember to always use the official data available at https://register.athensnetwork.eu/courses when planning your trip!

## Historical data   
From 2006 until today (March 2022) there were more than 2500 courses in total. Scrapped data is available:  
- as csv in [`results_all.csv`](https://raw.githubusercontent.com/mstaczek/athens_courses/main/results_all.csv)
- in [a nice looking webpage](https://mstaczek.github.io/athens_courses/web_big) (WIP, long loading time)
- in [a single html table](https://mstaczek.github.io/athens_courses/table_big) (laggy, long loading time)

### How to run locally

Gather links to course pages and run `run.py`. To get all links to courses currently listed at `https://register.athensnetwork.eu/courses` you may run script `js_scrapper.js` in web browser terminal. Note, that downloading all data uses selenium and in my case [chromedriver.exe](https://sites.google.com/chromium.org/driver/) which is not included in this repo.
