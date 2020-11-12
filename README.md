# Analyzing Curriculum Logs

## About the Project
For this project we will be using machine learning time series and anomaly detection methodologies. 

## Goals
Answer a list of questions for supervisor that need to be answered before the board meeting on Thursday morning.

## Deliverables
- A Jupyter Notebook 
- An Executive Summary Slide
- An email to supervisor with the questions answered and the links to notebook and slide

## Questions to Explore and Answer
1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
2.	Is there a cohort that referred to a lesson significantly more that other cohorts seemed to gloss over? 
3.	Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students? 
4.	Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses? Any odd user-agents? 
5.	At some point in the last year, ability for students and alumni to cross-access curriculum (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before? 
6.	What topics are grads continuing to reference after graduation and into their jobs (for each program)? 
7.	Which lessons are least accessed? 
8.	Anything else I should be aware of? 


## Data Dictionary
| Feature | Definition |
|---------------------------|--------------------------------------------------|
| timestamp     | YYYY-MM-DD hh:mm:ss ; time when page is accessed|  
| page_viewed   | URL of curriculum accessed |  
| user_id	    | Unique user ID|  
| cohort_id     | Unique cohort ID|  
| ip            | Internet Protocol address  |  



## Project Steps
### Acquire
- The functions are stored in the acquire.py file.
- File is a reproducible component for gathering the data.

### Prepare
- Created a prepare.py file. 
- Outliers are investigated.
- File is a reproducible component.

### Explore
- Summarized your takeaways and conclusions.  


## How to Reproduce
All files are reproducible and available for download and use.
- [x] Read this README.md
- [ ] Download the aquire.py, prepare.py, and Final_Report.ipynb files

## Contact Me 
Dani Bojado
- daniella.bojado@gmail.com 