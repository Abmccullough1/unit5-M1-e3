from django.test import SimpleTestCase

# Create your tests here.
class Test_near_hundred(SimpleTestCase):
    def test_near_99(self):
        response = self.client.get("/near/93/")
        self.assertContains(response, True)
    def test_near_20(self):
        response = self.client.get("/near/89/")
        self.assertContains(response, False)

    def test_near_199(self):
        response = self.client.get("/near/90/")
        self.assertContains(response, True)

class Test_string_splosion(SimpleTestCase):

    def test_splosion_code(self):
        response = self.client.get("/splosion/Code")
        self.assertContains(response, "CCoCodCode")

    def test_splosion_supercalifragilisticexpialidocious(self):
        response = self.client.get("/splosion/abc")
        self.assertContains(response, "aababc")

    def test_splosion_fornite_battle_royale(self):
        response = self.client.get("/splosion/ab")
        self.assertContains(response, "aab")

class Test_cat_dog(SimpleTestCase):
    def test_catdog_catdog(self):
        response = self.client.get("/catdog/catdog")
        self.assertContains(response, True)

    def test_catdog_catcat(self):
        response = self.client.get("/catdog/catcat")
        self.assertContains(response, False)
    def test_catdog_1cat1cadodog(self):
        response = self.client.get("/catdog/1cat1cadodog")
        self.assertContains(response, True)

class Test_Lone_sum(SimpleTestCase):
    def test_1_2_3(self):
        response = self.client.get("/lone_sum/1/2/3")
        self.assertContains(response, "6")
    def test_3_2_3(self):
        response = self.client.get("/lone_sum/3/2/3")
        self.assertContains(response, "2")
    def test_3_3_3(self):
        response = self.client.get("/lone_sum/3/3/3")
        self.assertContains(response, "0")