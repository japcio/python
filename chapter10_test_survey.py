import unittest
from chapter10_survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    def test_store_single_reponse(self):
        """Test that a single response is stored properly."""
        question="What language?"
        my_survey=AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English',my_survey.responses)
    def test_store_three_responses(self):
        """"Test that three responses are stored properly"""
        question="What language?"
        my_survey=AnonymousSurvey(question)
        responses=["English","Polish","French"]
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)

    def setUp(self):
        """Create a survey and a set of responses for use in all test methods """

if __name__=='__main__':
    unittest.main()