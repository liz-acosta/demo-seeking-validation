import requests
import unittest
from unittest.mock import patch, Mock
import get_dog_facts as dog_facts


class GetDogFacts(unittest.TestCase):

    @patch("get_dog_facts.requests")
    def test_get_dog_breed_id_with_mock(self, mock_requests):

        test_data = {
            "data": [
                {
                    "id": "036feed0-da8a-42c9-ab9a-57449b530b13",
                    "type": "breed",
                    "attributes": {
                        "name": "Affenpinscher",
                    },
                },
                {
                    "id": "a6ea38ed-f692-478e-af29-378d0e2cc270",
                    "type": "breed",
                    "attributes": {
                        "name": "Pug",
                    },
                },
            ]
        }

        mock_response = Mock()
        mock_response.json.return_value = test_data
        mock_requests.get.return_value = mock_response

        expected_result = ["a6ea38ed-f692-478e-af29-378d0e2cc270"]
        test_result = dog_facts.get_breed_id("pug")

        self.assertEqual(expected_result, test_result)

    @patch("get_dog_facts.requests")
    def test_get_dog_breed_info(self, mock_requests):

        mock_dog_breed_id = Mock(return_value=["a6ea38ed-f692-478e-af29-378d0e2cc270"])

        test_data = {
            "data": {
                "attributes": {
                    "name": "Pug",
                    "description": "The Pug is the best dog breed.",
                    "life": {
                        "max": 15,
                    },
                    "male_weight": {
                        "max": 8,
                    },
                },
                "relationships": {
                    "group": {
                        "data": {
                            "id": "f56dc4b1-ba1a-4454-8ce2-bd5d41404a0c",
                        }
                    }
                },
            }
        }

        mock_requests.get.return_value.json.return_value = test_data

        with patch.object(dog_facts, "get_breed_id", mock_dog_breed_id):

            test_result = dog_facts.get_dog_breed_info("pug")

            self.assertEqual(test_result["name"], "Pug")
            mock_dog_breed_id.assert_called_once_with("pug")
            mock_requests.get.assert_called_with(
                "https://dogapi.dog/api/v2/breeds/a6ea38ed-f692-478e-af29-378d0e2cc270"
            )
