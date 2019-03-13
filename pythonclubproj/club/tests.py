from django.test import TestCase
from .models import Resource, Meeting, Minutes
from django.urls import reverse

# Create your tests here.
class ResourceTest(TestCase):
    def test_stringOutput(self):
       resource = Resource(resourcename='laptop')
       self.assertEqual(str(resource), resource.resourcename)
    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class MinutesTest(TestCase):
    def test_stringOutput(self):
        meet=Meeting(meetingtitle="new meeting")
        minutes = Minutes(minutestitle='holidays', meeting=meet)
        self.assertEqual(str(minutes), minutes.meeting)
    def test_tablename(self):
        self.assertEqual(str(Minutes._meta.db_table), 'minutes')

class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting = Meeting(meetingtitle='holidays')
        self.assertEqual(str(meeting),meeting.meetingtitle)
    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')                        

class TestIndex(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'club/index.html')     

class TestResources(TestCase):
    def test_view_url_accesible_by_name(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('resources'))
        self.assertTemplateUsed(response, 'club/resources.html') 

class TestMeetings(TestCase):
    def test_view_url_accesible_by_name(self):
        response = self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('meetings'))
        self.assertTemplateUsed(response, 'club/meetings.html')

# here we are testing minutes: this one creates errors even if the class name is TestMeetingDetail
class TestDetails(TestCase):
    def test_view_url_accesible_by_name(self):
        #response = self.client.get(reverse('meetingdetail/1'))
        response = self.client.get(reverse('details'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('meetingdetail/'))
        self.assertTemplateUsed(response, 'club/details.html')        
