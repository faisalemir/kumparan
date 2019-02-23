# Kumparan Simple RESTful API with Python

## Installation
Restore database using `kumparan.sql`

Run this command to terminal
```
python run.py
```
To run unit testing use command bellow
```
python src/test/unittest.py
```
## Usage
### 1. News
    Url:  http://127.0.0.1:5000/news
  - Get All News

    Method: `GET`
    
    **Url Parameters:**

    ```
    Filter by News status:  status=<news_id>

    Filer by News topics:   topic=<topic_id>
    ```
    Example:
    ```
    http://127.0.0.1:5000/new?status=<news_id>&topic=<topic_id>
    ```
  - Insert News
    
    Method: `POST`

    JSON Parameters:
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

    Method: `PUT`

    JSON Parameters:
    ```
    {
          "news_id": <int: data>,
          "title": <string: data>,
          "content": <string: data>,
          "status_id": <int: data>
    }
    ```
  - Delete News

    Method: `DELETE`

    Url Parameter:
    ```
    http://127.0.0.1:5000/news/<int: news_id>
    ```

### 2. Topics
    Url:  http://127.0.0.1:5000/topic
  - Get All Topics

    Method: `GET`

  - Insert new Topic

    Method: `POST`

    JSON Parameters:
    ```
    {
          "topic": <string: data>
    }
    ```
  - Update News Information

    Method: `PUT`

    JSON Parameters:
    ```
    {
          "topic_id": <int: data>,
          "topic": <string: data>
    }
    ```
  - Delete News

    Method: `DELETE`

    Url Parameter:
    ```
    http://127.0.0.1:5000/news/<int: news_id>
    ```
