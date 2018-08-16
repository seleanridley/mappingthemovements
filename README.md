# mappingthemovements
Welcome to Mapping the Movements (MTM), a web application design to plot social media and news activity on data visualizations. This readme will walk you through the content of the app and how to effectively use Mapping the Movements.
----------------------------------------------------------------------------------------------------------------------------
TABLE OF CONTENTS

I. BEFORE USING THE APP
II. RUNNING THE APP
III. THE SEARCH PAGE
IV. RESULTS PAGE
----------------------------------------------------------------------------------------------------------------------------

I. BEFORE USING THE APP

Mapping the Movements requires the user to be running on Google Chrome on any operating system. You must also have a stable internet connection.

To run the app from a computer, you must have all of the various python libraries installed. To do this, type the following commands into a terminal window:

pip install Django==2.0.8

pip install django-bootstrap-datepicker
pip install django-widget-tweaks
pip install django-extensions
Pip install django-datetimepicker

pip install newsapi-python
pip install twitter
pip install praw

II. RUNNING THE APP

To run the app, navigate to the mappingthemovements folder, and then input the following command on the terminal:

python manage.py runserver

Then, open your browser and go to http://127.0.0.1:8000/. Mapping the Movements should display the search page.

III. THE SEARCH PAGE

When opening up Mapping the Movements, you will be introduced to the app’s search page. From here, you will be able to search a keyword along with a the date range and which social media platform to search through. There are important rules to follow when search:

- You must enter a keyword, a date range, and select a social media platform to start a search
- You cannot select both Reddit and Twitter as social media platforms to search through. Only one social media platform can be searched through at a time.
- When entering a date, make sure that the end date is more recent than the start date.
- If Twitter is the selected social media platform, the date range cannot be before seven days from the current date.

The app will check if these conditions appear but it’s good practice to follow the guidelines. When all the information is filled out, you can press the search button to start the search.


IV. THE RESULTS PAGE

If you have started a search and have not encountered any errors, you will reach the results page. On this page, you will be able to see the data visualization on the left along with top headlines relating to the keyword on the right. It’s important to note when starting a search, a default data visualization is picked and displayed on the results page. 

From this page, you can change the data visualization from the drop-down menu. If you would like to keep an image of the data visualization, the download visualization button is available and will provide a JPEG image file. For the reddit bar graph, click the three lines in the top right-hand corner of the visualization to save it. If you would like to perform a new search, you can click on the Mapping the Movements logo (On the top left of the page) and you will be redirected to the search page. From here, you can start a new search.
