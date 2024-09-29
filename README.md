# pythonWebScraper

Selenium and Beautiful Soup were used to scrape data from Rotten Tomatoes. Rotten Tomatoes does not allow users to access pages beyond page 5 directly (for example, attempting to access https://www.rottentomatoes.com/browse/movies_at_home/?page=100 defaults back to page 5 at https://www.rottentomatoes.com/browse/movies_at_home/?page=5). To overcome this limitation, Selenium was employed to manually click the "Load More" button. Once the desired page was reached, Selenium saved the page in HTML form.

Afterward, the saved page was accessed using Beautiful Soup to extract the relevant information, such as the title, scores, and stream date. To scrape Rotten Tomatoes, it was necessary to first identify which data from the page was required. Fortunately, each movie had a limited amount of useful information for scraping. These data points included the title, audience score, critics score, and stream date. This data was accessed by examining the HTML file in developer mode within the browser. Since only a few pieces of information were scrapable per movie, the database schema consisted of these four values.

In this trial, an attempt was made to scrape data from 200 pages of movies from Rotten Tomatoes, as shown in the accompanying image. Each entry was subsequently inserted into a local MongoDB database.

Below is a demonstration of queries made to the MongoDB database on the local system using the Mongo Shell.

![image](https://github.com/user-attachments/assets/9184a201-8b7a-45f4-bbe3-f80ef7e73a10)

![webscrapermongodb-images-0](https://github.com/user-attachments/assets/3e9dfa48-97c0-4325-90d8-6c2e0c1d82a0)
![webscrapermongodb-images-1](https://github.com/user-attachments/assets/de8dc4dc-b04c-45d7-b090-3d2b3583e841)
![webscrapermongodb-images-2](https://github.com/user-attachments/assets/4899fbcd-2db4-438f-b8a2-2262db12ae4f)
![webscrapermongodb-images-3](https://github.com/user-attachments/assets/e05f926b-aa2f-4d8c-87fc-580910f3971a)

