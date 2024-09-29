Used Selenium and Beautiful Soup to scrap data from rotten tomatoes. Rotten tomato doesn’t allow users
to access pages greater than 5 directly
(https://www.rottentomatoes.com/browse/movies_at_home/?page='100
defaults back to page 5
https://www.rottentomatoes.com/browse/movies_at_home/?page='5)
To overcome this issue, I used selenium to manually click the “load more” button. After the program gets
to its desired page, selenium is used to save the page in html form. I can then access this information,
using BeautifulSoup and pick out the information that I want such as the title, scores, and stream date.
To scrap rotten tomato, I had to first find what information I needed from the page. Thankfully, each movie
only had a limited amount of information that was useful for me to scrap. These were the title, audience
score, critics score, and the stream date and I was able to access this data by accessing the html file in
developer mode within my browser. Since there is only a few scrapable information per movie, the
database schema cosistist of just those 4 values.
In this trial, I attempted to scrap 200 pages worth of movies from rotten tomato as shown in the image
below.
![image](https://github.com/user-attachments/assets/20250f8c-ce49-4712-b28f-330d4448bedc)

Below is a showcase of queries to the Mongo Database on my local system using the Mongo
Shell.

![image](https://github.com/user-attachments/assets/9184a201-8b7a-45f4-bbe3-f80ef7e73a10)

![webscrapermongodb-images-0](https://github.com/user-attachments/assets/3e9dfa48-97c0-4325-90d8-6c2e0c1d82a0)
![webscrapermongodb-images-1](https://github.com/user-attachments/assets/de8dc4dc-b04c-45d7-b090-3d2b3583e841)
![webscrapermongodb-images-2](https://github.com/user-attachments/assets/4899fbcd-2db4-438f-b8a2-2262db12ae4f)
![webscrapermongodb-images-3](https://github.com/user-attachments/assets/e05f926b-aa2f-4d8c-87fc-580910f3971a)
