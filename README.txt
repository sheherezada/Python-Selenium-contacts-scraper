Example of Python/Selenium scraper:
Driver: Chrome
URL : Public german website with job offers for architects
Search : List of different key words Example : Revit - > software; BIM -> job position
Result : csv file containing Title and Content


Logic:
	Make a search for each keyword and gather the results from the resulting page/s. 
	3 differents scenarios for each keyword search: Results: None, Results: One page, Results: multiple pages
	Save the results and pass on the next keyword.


Installation:
	1.Download and Install python: https://www.python.org/downloads/
	2.Download Chrome driver: https://chromedriver.chromium.org/downloads
	2.Open the project in IDE and make all the installations from requirements.txt
	3.Add the absolute path of the chromedriver.exe to the PATH variable
	4.Run the code
	
	


