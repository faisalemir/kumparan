import unittest
import json
from run import create_app
from src import db

getMsg = lambda res: json.loads(res.data)['data']['message']

class KumparanTestCase(unittest.TestCase):
    topic_input_id = -1
    news_input_id = -1

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client

    def test_topic_can_insert(self):
        res = self.client().post('/topic', json={ "topic": "Test Topic" })
        self.assertEqual(res.status_code, 201)

        data = json.loads(res.data)['data']
        self.__class__.topic_input_id = data['topic_id']

    def test_topic_can_update(self):
        id = self.__class__.topic_input_id

        res = self.client().put('/topic', json={"topic_id": id, "topic": "Test Update Topic"})

        self.assertEqual(res.status_code, 200)

        res = self.client().get('/topic/' + str(id))
        self.assertIn('Test Update Topic', str(res.data))

    def test_topic_can_updelete(self):
        id = self.__class__.topic_input_id

        res = self.client().delete('/topic/' + str(id))
        self.assertEqual(res.status_code, 204)

    # -------------------------------------------------------------
    # -------------------------------------------------------------

    def test_api_can_get_all_news(self):
        res = self.client().get('/news')
        self.assertEqual(res.status_code, 200)

    def test_api_can_get_by_news_status(self):
        res = self.client().get('/news?status=1')
        self.assertEqual(res.status_code, 200)

    def test_api_can_get_by_news_topic(self):
        res = self.client().get('/news?topic=2')
        self.assertEqual(res.status_code, 200)

    def test_news_can_insert(self):
        res = self.client().post('/news',
                                 json={
                                     "status_id": 1,
                                     "title": "Tes Article",
                                     "content": "aaaaaaaaaaaaaaaaaaaaaaaa",
                                     "topic_list": [
                                         { "topic_id": 1 },
                                         { "topic_id": 2 }
                                     ]
                                 })
        self.assertEqual(res.status_code, 201)

        data = json.loads(res.data)['data']
        self.__class__.news_input_id = data['news_id']

    def test_news_can_update(self):
        id = self.__class__.news_input_id

        res = self.client().put('/news',
                                json={
                                    "news_id": id,
                                    "status_id": 2,
                                    "title": "Tes Title Update",
                                    "content": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
                                })

        self.assertEqual(res.status_code, 200)

    def test_news_can_updelete(self):
        id = self.__class__.news_input_id

        res = self.client().delete('/news/' + str(id))
        self.assertEqual(res.status_code, 204)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()

if __name__ == '__main__':
    unittest.main()
