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
    #
    def test_topic_can_insert(self):
        res = self.client().post('/topic', json={ "topic": "Test Topic" })
        self.assertEqual(res.status_code, 201, 'Cek insert status')

        data = json.loads(res.data)['data']
        self.__class__.topic_input_id = data['topic_id']

        res = self.client().get('/topic/' + str(data['topic_id']))
        data = json.loads(res.data)['data']

        self.assertEqual(data['topic'], 'Test Topic', 'Cek topic yang berhasil terinput')

    def test_topic_can_update(self):
        id = self.__class__.topic_input_id

        res = self.client().put('/topic', json={"topic_id": id, "topic": "Test Update Topic nih"})
        self.assertEqual(res.status_code, 200, 'Cek update status')

        res = self.client().get('/topic/' + str(id))
        data = json.loads(res.data)['data']

        self.assertIn('Test Update Topic nih', data['topic'], 'Cek isi topik yang terupdate')
        self.assertNotEqual(data['modified_date'], None, 'Cek kolom modified date sudah terisi tanggal')

    def test_topic_can_updelete(self):
        id = self.__class__.topic_input_id

        res = self.client().delete('/topic/' + str(id))
        self.assertEqual(res.status_code, 204)

        res = self.client().get('/topic/' + str(id))
        self.assertEqual(res.status_code, 404, 'Cek topic jika sudah terhapus')

    # -------------------------------------------------------------
    # -------------------------------------------------------------

    def test_api_can_get_all_news(self):
        #case 1
        res = self.client().get('/news')
        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data)['data']
        self.assertLessEqual(len(data), 5, 'cek pagination kurang dari samadengan 5')

        pages = json.loads(res.data)['pages']

        if len(data) >= 5:
            self.assertIsNotNone(pages['next'], 'cek pagination next tersedia jika data lebih samadengan 5')
            self.assertIsNone(pages['prev'], 'cek pagination prev tidak tersedia jika data lebih samadengan 5')
        if len(data) < 5:
            self.assertIsNone(pages['next'], 'cek pagination next tidak tersedia jika data kurang dari 5')
            self.assertIsNotNone(pages['prev'], 'cek pagination prev tidak tersedia jika data kurang dari 5')

        # case 2
        res = self.client().get('/news?page=2')
        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data)['data']
        self.assertLessEqual(len(data), 5, 'cek pagination kurang dari samadengan 5')

        pages = json.loads(res.data)['pages']

        if len(data) >= 5:
            self.assertIsNotNone(pages['next'], 'cek pagination next tersedia jika data lebih samadengan 5')
            self.assertIsNone(pages['prev'], 'cek pagination prev tidak tersedia jika data lebih samadengan 5')
        if len(data) < 5:
            self.assertIsNone(pages['next'], 'cek pagination next tidak tersedia jika data kurang dari 5')
            self.assertIsNotNone(pages['prev'], 'cek pagination prev tidak tersedia jika data kurang dari 5')

    def test_api_can_get_by_news_status(self):
        res = self.client().get('/news?status=1')
        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data)['data']
        for row in data:
            self.assertEqual(row['status_id'], 1, 'cek status id harus 1')


        res = self.client().get('/news?status=2')
        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data)['data']
        for row in data:
            self.assertEqual(row['status_id'], 2, 'cek status id harus 2')


        res = self.client().get('/news?status=3')
        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data)['data']
        for row in data:
            self.assertEqual(row['status_id'], 3, 'cek status id harus 3')

    def test_api_can_get_by_news_topic(self):
        res = self.client().get('/news?topic=2')
        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data)['data']
        for row in data:
            self.assertIn({"topic_id": 2, "topic": "Bisnis"}, row['topic_list'], 'cek topic id memiliki id 2 Bisnis')

    def test_news_can_insert(self):
        res = self.client().post('/news',
                                 json={
                                     "status_id": 1,
                                     "title": "Tes Article",
                                     "content": "Lorem Ipsum Lorem Ipsum Lorem Ipsum",
                                     "topic_list": [
                                         { "topic_id": 1 },
                                         { "topic_id": 2 }
                                     ]
                                 })
        self.assertEqual(res.status_code, 201)

        data = json.loads(res.data)['data']
        self.__class__.news_input_id = data['news_id']

        res = self.client().get('/news/' + str(data['news_id']))
        data = json.loads(res.data)['data']

        self.assertEqual(data['title'], 'Tes Article', 'Cek title')
        self.assertEqual(data['content'], 'Lorem Ipsum Lorem Ipsum Lorem Ipsum', 'Cek content yang berhasil terinput')
        self.assertEqual(len(data['topic_list']), 2, 'Cek jumlah topic yang terinput')
        self.assertEqual(data['status_id'], 1, 'Cek status id yang terinput')

    def test_news_can_update(self):
        id = self.__class__.news_input_id

        res = self.client().put('/news',
                                json={
                                    "news_id": id,
                                    "status_id": 2,
                                    "title": "Tes Title Update",
                                    "content": "Tes Update Isi Konten Berita"
                                })

        self.assertEqual(res.status_code, 200)

        res = self.client().get('/news/' + str(id))
        data = json.loads(res.data)['data']

        self.assertEqual(data['title'], 'Tes Title Update', 'Cek title yang terupdate')
        self.assertEqual(data['content'], 'Tes Update Isi Konten Berita', 'Cek konten yang terupdate')
        self.assertEqual(data['status_id'], 2, 'Cek perubahan status dari 1 ke 2')

    def test_news_can_updelete(self):
        id = self.__class__.news_input_id

        res = self.client().delete('/news/' + str(id))
        self.assertEqual(res.status_code, 204)

        res = self.client().get('/news/' + str(id))
        self.assertEqual(res.status_code, 404, 'Cek news jika sudah terhapus')

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()

if __name__ == '__main__':
    unittest.main()
