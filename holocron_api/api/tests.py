from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from api.models import Source, Medium, Tactic, Creative, \
    LOB, Intent, LifeCycle, Audience, Ad_Network, Program, Campaign
from rest_framework import status
import factory


class SourceFactory(factory.DjangoModelFactory):
    class Meta:
        model = Source
    source_name = "Testing Source"
    source_key = "TestingSource"


class MediumFactory(factory.DjangoModelFactory):
    class Meta:
        model = Medium
    medium_name = "Testing Medium"
    medium_key = "Test_Medium"


class TacticFactory(factory.DjangoModelFactory):
    class Meta:
        model = Tactic

    tactic_id = 1
    tactic_name = "Testing tactic"
    tactic_description = "This is a Test"
    tactic_key = "tacticTest"
    created_by = "Test User"
    tactic_notes = "This is a note"
    start_date = None
    end_date = None
    campaign = Campaign.objects.get(campaign_id=1)


class CreativeFactory(factory.DjangoModelFactory):
    class Meta:
        model = Creative
    creative_name = "Testing Content"
    creative_description = "This is a test for Content"
    creative_id = 1


class LOBFactory(factory.DjangoModelFactory):
    class Meta:
        model = LOB
    lob_key = "Test"
    lob_description = "This is a test Line of Business"


class IntentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Intent
    intent_key = "Test_Intent"
    intent_description = "To make a test"


class LifeCycleFactory(factory.DjangoModelFactory):
    class Meta:
        model = LifeCycle
    lifecycle_key = "TestLC"
    lifecycle_description = "Test LC"


class AudienceFactory(factory.DjangoModelFactory):
    class Meta:
        model = Audience
    audience_key = "Test_Audience"
    audience_description = "Everyone"


class AdNetworkFactory(factory.DjangoModelFactory):
    class Meta:
        model = Ad_Network
    network_key = "Ad Network A"
    network_description = "Test Network"


class SourceTest(APITestCase):

    @staticmethod
    def create_test(source_name="Test Source",
                    source_key="TestS"):
        return Source.objects.create(source_name=source_name,
                                     source_key=source_key)

    def test_was_created(self):
        s = self.create_test()
        self.assertTrue(isinstance(s, Source))


class MediumTest(APITestCase):

    @staticmethod
    def create_test(medium_name="Test Medium",
                    medium_key="TestM"):
        return Medium.objects.create(medium_name=medium_name,
                                     medium_key=medium_key)

    def test_was_created(self):
        m = self.create_test()
        self.assertTrue(isinstance(m, Medium))


class CreativeTest(APITestCase):

    @staticmethod
    def create_test(creative_name="Test Content",
                    creative_desc="I am a piece of Content!"):
        return Creative.objects.create(creative_name=creative_name,
                                       creative_description=creative_desc)

    def test_was_created(self):
        cr = self.create_test()
        self.assertTrue(isinstance(cr, Creative))


class TacticTest(APITestCase):

    @staticmethod
    def create_test(tactic_name="Test tactic",
                    tactic_desc="I am a test tactic",
                    end_date="2020-09-20",
                    tactic_key="TestT",
                    created_by="Test User"):
        return Tactic.objects.create(tactic_name=tactic_name,
                                     tactic_description=tactic_desc,
                                     end_date=end_date,
                                     tactic_key=tactic_key,
                                     created_by=created_by,
                                     campaign=Campaign.objects.get(campaign_id=1))

    def test_was_created(self):
        ca = self.create_test()
        self.assertTrue(isinstance(ca, Tactic))


class CampaignTest(APITestCase):
    @staticmethod
    def create_test(campaign_name="My Test Campaign",
                    campaign_description="This is a test Campagin",
                    created_by="system"):
        return Campaign.objects.create(campaign_name=campaign_name,
                                       campaign_description=campaign_description,
                                       created_by=created_by,
                                       program=Program.objects.get(program_id=1))

    def test_was_created(self):
        camp = self.create_test()
        self.assertTrue(isinstance(camp, Campaign))


class ProgramTest(APITestCase):
    @staticmethod
    def create_test(program_name="My Test Program",
                    program_description="This is a test Program",
                    created_by="system"):
        return Program.objects.create(program_name=program_name,
                                      program_description=program_description,
                                      created_by=created_by)

    def test_was_created(self):
        prog = self.create_test()
        self.assertTrue(isinstance(prog, Program))


class AdNetworkTest(APITestCase):

    @staticmethod
    def create_test(network_key="Test Network",
                    network_description="This is a test Network"):
        return Ad_Network.objects.create(network_key=network_key,
                                         network_description=network_description)

    def test_was_created(self):
        a = self.create_test()
        self.assertTrue(isinstance(a, Ad_Network))


class SourceAPITest(APITestCase):
    def test_post_source_api(self):
        data = {'source_name': 'My Source',
                'source_key': 'TestSource'}
        response = self.client.post('/source/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Testing sql injection is cast to String
    def test_post_sql_source_api(self):
        data = {'source_name': 'DROP TABLE *',
                'source_key': 'TestSource'}
        response = self.client.post('/source/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_source_api(self):
        client = APIClient()
        response = client.get("/source/")
        self.assertEqual(response.status_code, 200)

    def test_empty_post_source_api(self):
        data = {'source_name': '',
                'source_key': ''}
        response = self.client.post('/source/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_data_post_source_api(self):
        data = {}
        response = self.client.post('/source/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_bad_param_post_source_api(self):
        data = {'name': 'test',
                'source_key': 'TestSource'}
        response = self.client.post('/source/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_too_long_post_source_api(self):
        data = {'source_name': 'Random o85y9384ytoerty3849yroehg '
                               'yhvytvytoa8y4tyv8ytoeryto8y34o8ythiua48y'
                               'tlai4ytai47tyiow4t8orghowiy4toi4ehtoweit',
                'source_key': 'TestSource'}
        response = self.client.post('/source/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class MediumAPITest(APITestCase):
    def test_post_medium_api(self):
        data = {'medium_name': 'My Meduim',
                'medium_key': 'Medium1'}
        response = self.client.post('/medium/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_sql_medium_api(self):
        data = {'medium_name': 'DROP TABLE *',
                'medium_key': 'Medium1'}
        response = self.client.post('/medium/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_medium_api(self):
        client = APIClient()
        response = client.get("/medium/")
        self.assertEqual(response.status_code, 200)

    def test_empty_post_medium_api(self):
        data = {'medium_name': '',
                'medium_key': 'Medium1'}
        response = self.client.post('/medium/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_data_post_medium_api(self):
        data = {}
        response = self.client.post('/medium/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_bad_param_post_medium_api(self):
        data = {'name': 'Test',
                'medium_key': 'Medium1'}
        response = self.client.post('/medium/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_too_long_post_medium_api(self):
        data = {'medium_name': 'Random o85y9384ytoerty3849yroehg '
                               'yhvytvytoa8y4tyv8ytoeryto8y34o8ythiu'
                               'a48ytlai4ytai47tyiow4t8orghowiy4toi4ehtoweit',
                'medium_key': 'Medium1'}
        response = self.client.post('/medium/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TacticAPITest(APITestCase):

    def test_post_tactic_api(self):
        data = {'tactic_name': 'My tactic',
                'tactic_description': 'This one is mine',
                'end_date': '2020-12-12',
                'tactic_key': 'tacticTest',
                'created_by': 'Test User',
                'campaign': 1}
        response = self.client.post('/tactic/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_sql_tactic_api(self):
        data = {'tactic_name': 'DROP TABLE *',
                'tactic_description': 'DROP TABLE *',
                'end_date': '2020-12-12',
                'tactic_key': 'tacticTest',
                'created_by': 'Test User',
                'campaign': 1}
        response = self.client.post('/tactic/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_tactic_api(self):
        client = APIClient()
        response = client.get("/tactic/")
        self.assertEqual(response.status_code, 200)

    def test_empty_name_tactic_api(self):
        data = {'tactic_name': '',
                'tactic_description': 'This one is mine',
                'end_date': '2020-12-12',
                'tactic_key': 'tacticTest',
                'created_by': 'Test User',
                'campaign': 1}
        response = self.client.post('/tactic/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_empty_description_tactic_api(self):
        data = {'tactic_name': 'Test',
                'tactic_description': '',
                'end_date': '2020-12-12',
                'tactic_key': 'tacticTest',
                'created_by': 'Test User',
                'campaign': 1}
        response = self.client.post('/tactic/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_empty_date_tactic_api(self):
        data = {'tactic_name': 'Test',
                'tactic_description': 'This one is mine',
                'end_date': '',
                'tactic_key': 'tacticTest',
                'created_by': 'Test User',
                'campaign': 1}
        response = self.client.post('/tactic/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_name_tactic_api(self):
        data = {'tactic_description': 'This one is mine',
                'end_date': '2020-12-12',
                'tactic_key': 'tacticTest',
                'created_by': 'Test User',
                'campaign': 1}
        response = self.client.post('/tactic/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_description_tactic_api(self):
        data = {'tactic_name': 'Test',
                'end_date': '2020-12-12',
                'tactic_key': 'tacticTest',
                'created_by': 'Test User',
                'campaign': 1}
        response = self.client.post('/tactic/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_bad_date_tactic_api(self):
        data = {'tactic_name': 'Test',
                'tactic_description': 'This one is mine',
                'end_date': 'Nov. 2, 2018',
                'tactic_key': 'tacticTest',
                'created_by': 'Test User',
                'campaign': 1}
        response = self.client.post('/tactic/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_data_post_tactic_api(self):
        data = {}
        response = self.client.post('/tactic/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_bad_param_post_tactic_api(self):
        data = {'name': 'Test',
                'tactic_description': 'This one is mine',
                'end_date': '2020-12-12',
                'tactic_key': 'tacticTest',
                'created_by': 'Test User',
                'campaign': 1}
        response = self.client.post('/tactic/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_name_too_long_post_tactic_api(self):
        data = {'tactic_name': 'Random o85y9384ytoerty3849yroehg yhvytvyto'
                               'a8y4tyv8ytoeryto8y34o8ythiua48ytlai4ytai47t'
                               'yiow4t8orghowiy4toi4ehtoweit',
                'tactic_description': 'This one is mine',
                'end_date': '2020-12-12',
                'tactic_key': 'tacticTest',
                'created_by': 'Test User',
                'campaign': 1}
        response = self.client.post('/tactic/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_description_too_long_post_tactic_api(self):
        data = {'tactic_name': 'Long Description',
                'tactic_description': 'What happens if this is too long '
                                      'srihgoityow aiytowierhtohirgoirytiors'
                                      'hgoheao4yhtoaghrihat;oeirhtahlhghe sf'
                                      'sifghoirhgeoirhgeilrgherigheirfklnvh',
                'end_date': '2020-12-12',
                'tactic_key': 'tacticTest',
                'created_by': 'Test User',
                'campaign': 1}
        response = self.client.post('/tactic/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CreativeAPITest(APITestCase):
    def test_post_creative_api(self):
        data = {'creative_name': 'My Content',
                'creative_description': 'This is my content'}
        response = self.client.post('/creative/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_sql_creative_api(self):
        data = {'creative_name': 'DROP TABLE *',
                'creative_description': 'This is my content'}
        response = self.client.post('/creative/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_creative_api(self):
        client = APIClient()
        response = client.get("/creative/")
        self.assertEqual(response.status_code, 200)

    def test_empty_name_creative_api(self):
        data = {'creative_name': '',
                'creative_description': 'This one is mine'}
        response = self.client.post('/creative/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_empty_description_creative_api(self):
        data = {'creative_name': 'Test',
                'creative_description': ''}
        response = self.client.post('/creative/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_data_post_creative_api(self):
        data = {}
        response = self.client.post('/creative/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_bad_param_post_creative_api(self):
        data = {'name': 'Test',
                'creative_description': 'This one is mine'}
        response = self.client.post('/creative/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_name_too_long_post_creative_api(self):
        data = {'creative_name': 'Random o85y9384ytoerty3849yroehg '
                                 'yhvytvytoa8y4tyv8ytoeryto8y34o8ythi'
                                 'ua48ytlai4ytai47tyiow4t8orghowiy4toi4ehto',
                'creative_description': 'Name is too long'}
        response = self.client.post('/creative/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_description_too_long_post_creative_api(self):
        data = {'creative_name': 'Description is too long',
                'creative_description': 'This is too long. '
                                        'lsirghotyeiyrtoeirhgtoeitoeuto94uti '
                                        'ioeartoeirhto eheoihteoit'
                                        'hoeihtaoeirhteoirhtoei heoirt '
                                        'woirygoeirfhgvoeirshgeoishgsjdfhskjd'}
        response = self.client.post('/creative/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class AdNetworkAPITest(APITestCase):
    def test_post_network_api(self):
        data = {'network_key': 'My Ad Network',
                'network_description': 'Test Network'}
        response = self.client.post('/ad-network/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Testing sql injection is cast to String
    def test_post_sql_network_api(self):
        data = {'network_key': 'DROP TABLE *',
                'network_description': 'SQL Ad'}
        response = self.client.post('/ad-network/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_network_api(self):
        client = APIClient()
        response = client.get("/source/")
        self.assertEqual(response.status_code, 200)

    def test_empty_post_network_api(self):
        data = {'network_key': '',
                'network_description': ''}
        response = self.client.post('/ad-network/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_data_post_network_api(self):
        data = {}
        response = self.client.post('/ad-network/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_bad_param_post_network_api(self):
        data = {'name': 'test',
                'network_description': 'New Ad'}
        response = self.client.post('/ad-network/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_too_long_post_network_api(self):
        data = {'network_key': 'Random o85y9384ytoerty3849yroehg '
                               'yhvytvytoa8y4tyv8ytoeryto8y34o8ythiua48y'
                               'tlai4ytai47tyiow4t8orghowiy4toi4ehtoweit',
                'network_description': 'New Ad'}
        response = self.client.post('/ad-network/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_too_long_desc_post_network_api(self):
        data = {'network_key': 'Ad Network A',
                'network_description': 'Random o85y9384ytoerty3849yroehg '
                               'yhvytvytoa8y4tyv8ytoeryto8y34o8ythiua48y'
                               'tlai4ytai47tyiow4t8orghowiy4toi4ehtoweit sdhg'
                               'skughksrughsk gskshgksghskghskeuhgkdjghvsdkjgh'
                               'sughksughksuhfgksdfhskdjhvgksjutg'}
        response = self.client.post('/ad-network/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PlacementAPITest(APITestCase):

    @staticmethod
    def make_pks():
        SourceFactory.create()
        MediumFactory.create()
        TacticFactory.create()
        CreativeFactory.create()
        AdNetworkFactory.create()

    def test_get_placement_api(self):
        client = APIClient()
        response = client.get("/placement/")
        self.assertEqual(response.status_code, 200)

    def test_post_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test Placement",
                "placement_url": "www.test.com/pricing",
                "catid": 94835,
                "page_cat": "",
                "page_id": "",
                "jira_ticket": "",
                "start_date": None,
                "end_date": None,
                "tactic": 1,
                "medium": "Test_Medium",
                "source": "TestingSource",
                "creative": 1}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_placement_api_optional_fields(self):
        self.make_pks()
        data = {"placement_name": "Test Placement 2",
                "placement_url": "www.test.com/pricing",
                "catid": 94835,
                "page_cat": "Test",
                "page_id": "Still Test",
                "jira_ticket": "Ticket-234",
                "start_date": "2015-07-07",
                "end_date": "2040-07-07",
                "tactic": 1,
                "medium": "Test_Medium",
                "source": "TestingSource",
                "creative": 1,
                "ad_network": "Ad Network A"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_missing_name_placement_api(self):
        self.make_pks()
        data = {"placement_name": "",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "tactic": "Testtactic",
                "medium": "Test_Medium",
                "source": "TestingSource",
                "creative": 1,
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_url_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "",
                "end_date": "2040-01-01",
                "tactic": "Testtactic",
                "medium": "Test_Medium",
                "source": "TestingSource",
                "creative": 1,
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_date_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "",
                "tactic": "Testtactic",
                "medium": "Test_Medium",
                "source": "TestingSource",
                "creative": 1,
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_date_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "1-1-2010",
                "tactic": "Testtactic",
                "medium": "Test_Medium",
                "source": "TestingSource",
                "creative": 1,
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_string_date_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "January 1, 2020",
                "tactic": "Testtactic",
                "medium": "Test_Medium",
                "source": "TestingSource",
                "creative": 1,
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_tactic_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "tactic": "",
                "medium": "Test_Medium",
                "source": "TestingSource",
                "creative": 1,
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_medium_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "tactic": "Testtactic",
                "medium": "",
                "source": "TestingSource",
                "creative": 1,
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_source_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "tactic": "Testtactic",
                "medium": "Test_Medium",
                "source": "",
                "creative": 1,
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_creative_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "tactic": "Testtactic",
                "medium": "Test_Medium",
                "source": "TestingSource",
                "creative": "",
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_tactic_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "tactic": 0,
                "medium": "Test_Medium",
                "source": "TestingSource",
                "creative": 1,
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_medium_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "tactic": "Testtactic",
                "medium": 0,
                "source": "TestingSource",
                "creative": 1,
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_source_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "tactic": "Testtactic",
                "medium": "Test_Medium",
                "source": 0,
                "creative": 1,
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_creative_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "tactic": "Testtactic",
                "medium": "Test_Medium",
                "source": "TestingSource",
                "creative": 0,
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_tactic_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "tactic": -1,
                "medium": "Test_Medium",
                "source": "TestingSource",
                "creative": 1,
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_medium_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "tactic": "Testtactic",
                "medium": -1,
                "source": "TestingSource",
                "creative": 1,
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_source_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "tactic": "Testtactic",
                "medium": "Test_Medium",
                "source": -1,
                "creative": 1,
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_creative_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "tactic": "Testtactic",
                "medium": "Test_Medium",
                "source": "TestingSource",
                "creative": -1,
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_non_int_tactic_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "tactic": "test",
                "medium": "Test_Medium",
                "source": "TestingSource",
                "creative": 1,
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_int_medium_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "tactic": "Testtactic",
                "medium": 1,
                "source": "TestingSource",
                "creative": 1,
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_int_source_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "tactic": "Testtactic",
                "medium": "Test_Medium",
                "source": 1,
                "creative": 1,
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_string_creative_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "tactic": "Testtactic",
                "medium": "Test_Medium",
                "source": "TestingSource",
                "creative": "My Content",
                "catid": 12345,
                "jira_ticket": "AN-154"}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_network_placement_api(self):
        self.make_pks()
        data = {"placement_name": "Test",
                "placement_url": "www.testurl.com",
                "end_date": "2040-01-01",
                "tactic": "Testtactic",
                "medium": "Test_Medium",
                "source": "TestingSource",
                "creative": 1,
                "catid": 12345,
                "jira_ticket": "AN-154",
                "ad_network": 0}
        response = self.client.post('/placement/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ExportTests(APITestCase):
    def test_JSONExport_exists(self):
        client = APIClient()
        response = client.get("/export/json/")
        self.assertEqual(response.status_code, 200)

    def test_CSVExport_exists(self):
        client = APIClient()
        response = client.get("/export/csv/")
        self.assertEqual(response.status_code, 200)
