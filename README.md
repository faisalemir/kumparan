# Simple RESTful API with Python
Selesai juga percobaan pertama kali di python bikin RESTful API. Perjalanan 4 malam untuk convert syntax, konsep OOP dan pola si python didalam kepala.
## Installation
Restore MySQL database using `kumparan.sql`

Run this command to terminal
```
python run.py
```
To run unit testing use this command bellow
```
python src/test/unittest.py
```
## Usage
### 1. News
  - Get All News
    ```
    GET /news
    ```    
    Option Parameters:

    Pagination:   
    `page=<page number>`
    
    Filter by News status:  
    `status=<status_id>`

    Filter by News topics:   
    `topic=<topic_id>`
    
    Example:
    ```
    GET /news?page=<page number>&status=<status_id>&topic=<topic_id>
    ```
  - Get News by id
    ```
    GET /news/<int: news_id>
    ```
  - Insert News
    ```
    POST /news
    ```
    JSON Request Parameters:
    ```
    {
          "title": <string: data>,
          "content": <string: data>,
          "status_id": <int: data>,
          "topic_list": [
              {
                  "topic_id": <int: data>
              },
              {
                  "topic_id": <int: data>
              }
          ]
    }
    ```
  - Update News Information
    ```
    PUT /news
    ```
    JSON Request Parameters:
    ```
    {
          "news_id": <int: data>,
          "title": <string: data>,
          "content": <string: data>,
          "status_id": <int: data>
    }
    ```
  - Delete News
    ```
    DELETE /news/<int: news_id>
    ```

### 2. Topics
  - Get All Topics
    ```
    GET /topic
    ```    
    Option Parameters:

    Pagination:   
    `page=<page number>`
    
    Example:
    ```
    GET /topic?page=<page number>
    ```
  - Get Topic by id
    ```
    GET /topic/<int: news_id>
    ```    
  - Insert Topic
    ```
    POST /topic
    ```    
    JSON Request Parameters:
    ```
    {
          "topic": <string: data>
    }
    ```
  - Update Topic Information
    ```
    PUT /topic
    ```    
    JSON Request Parameters:
    ```
    {
          "topic_id": <int: data>,
          "topic": <string: data>
    }
    ```
  - Delete Topic
    ```
    DELETE /topic/<int: news_id>
    ```    
