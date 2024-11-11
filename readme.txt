This Weather App is a valuable tool for gaining insights on the expected weather for a particular date. This knowledge will help our team in choosing the best equipment to use when planning events at our Augusta, MO location. 

To use:

1. Run the Main.py file

2. When prompted, enter the number for the month, day and year. It will look like this, but with your chosen values:
			

			Enter the month number 1-12: 8
			Enter the day of the month 1-31: 19
			Enter the 4 digit year (ex 2024): 2025
	

3. Program will provide you with the average, highest and lowest temperature, wind speed and precipitation for that date over the previous 5 years. Expected output will be:


		    	ID: 8
                    	Latitude: 38.5726
                    	Longitude: -90.8821
                    	Date: 08-19-2025
                    	Average Temperature: 84.58°F
                    	Min Temperature: 78.00°F
                    	Max Temperature: 89.80°F
                    	Average Wind Speed: 11.98 mph
                    	Min Wind Speed: 8.40 mph
                    	Max Wind Speed: 14.20 mph
                    	Average Precipitation: 0.00 inches
                    	Min Precipitation: 0.00 inches
                    	Max Precipitation: 0.00 inches


4. After providing the information for the chosen date, the program will ask if you would like to try another date. You may type y for yes and n for no. 


			Try another date? (y or n): 


The information will also be stored in the Weather_data database and may be looked up there as well after the initial request is made. This will be a faster option during the continued planning of the event. 




For questions or technical issues, please contact Shanna Siebert at ssieb13@myfakecompany.com or call 123-555-4567.




Technical Info: This program was written in Python and uses SQLAlchemy and SQLite for database creation and management. Weather data is pulled from the open-meteo historical weather API. Please see the requirements.txt for additional information. 

