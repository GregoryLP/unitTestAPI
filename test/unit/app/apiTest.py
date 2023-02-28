import unittest
import requests

    # URL de l'API
url = 'http://127.0.0.1:8000/classeDestiny'

data_classeDestiny = {
    "name": "Titan Test",
    "doctrine": "Solaire test",
    "element": "Feu test"
}

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.classeDestiny_data = data_classeDestiny

    def test_ajout(self):
        response = requests.post(url, json=data_classeDestiny)
        self.assertEqual(response.status_code, 200)
        classeDestiny = response.json()
        self.assertIsInstance(classeDestiny, dict)
        self.assertEqual(classeDestiny['data_classeDestiny'][0]["name"], self.classeDestiny_data["name"])
        self.assertEqual(classeDestiny['data_classeDestiny'][0]["doctrine"], self.classeDestiny_data["name"])
        self.assertEqual(classeDestiny['data_classeDestiny'][0]["element"], self.classeDestiny_data["name"])
    
    def test_update(self):
        self.classeDestiny_data['name'] = 'Chasseur_modifier'
        response = requests.get(url)
        old_classeDestiny = response.json()
        for i in range(0, len(old_classeDestiny['data'][0])):
            if old_classeDestiny['data_classeDestiny'][i]['name'] == 'Titan Test':
                id_classeDestiny = old_classeDestiny['data_classeDestiny'][i]['id']
            break
        response = requests.put(f"{url}/{id_classeDestiny}", json=data_classeDestiny)
        self.assertEqual(response.status_code, 200)
        classeDestiny = response.json()
        self.assertIsInstance(classeDestiny, dict)
        self.assertEqual(classeDestiny['data_classeDestiny'][0], f"Classe Destiny {id_classeDestiny} modifié avec succès")
    
    def test_suppression(self):
        
        response = requests.get(url)
        old_classeDestiny = response.json()
        for i in range(0, len(old_classeDestiny['data_classeDestiny'][0])):
            if old_classeDestiny['data_classeDestiny'][i]['name'] == 'Titan Test':
                id_classeDestiny = old_classeDestiny['data_classeDestiny'][i]['id']
            break
        response = requests.delete(f"{url}/{id_classeDestiny}")
        self.assertEqual(response.status_code, 200)
        classeDestiny = response.json()
        self.assertIsInstance(classeDestiny, dict)
        self.assertEqual(classeDestiny['data'][0], f"Classe Destiny {id_classeDestiny} supprimé avec succès")

if __name__ == '__main__':
    unittest.main()
