# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class MessageInteractionTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.proxy.v1.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .sessions(sid="KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .participants(sid="KPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .message_interactions.create()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://proxy.twilio.com/v1/Services/KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Sessions/KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Participants/KPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/MessageInteractions',
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "service_sid": "KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "data": "body",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "participant_sid": "KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "inbound_participant_sid": null,
                "inbound_resource_sid": null,
                "inbound_resource_status": null,
                "inbound_resource_type": null,
                "inbound_resource_url": null,
                "outbound_participant_sid": "KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "outbound_resource_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "outbound_resource_status": "sent",
                "outbound_resource_type": "Message",
                "outbound_resource_url": null,
                "sid": "KIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "type": "message",
                "url": "https://proxy.twilio.com/v1/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/MessageInteractions/KIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "session_sid": "KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.proxy.v1.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .sessions(sid="KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .participants(sid="KPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .message_interactions.create()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.proxy.v1.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .sessions(sid="KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .participants(sid="KPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .message_interactions(sid="KIXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://proxy.twilio.com/v1/Services/KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Sessions/KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Participants/KPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/MessageInteractions/KIXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "service_sid": "KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "data": "data",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "participant_sid": "KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "inbound_participant_sid": null,
                "inbound_resource_sid": null,
                "inbound_resource_status": null,
                "inbound_resource_type": null,
                "inbound_resource_url": null,
                "outbound_participant_sid": "KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "outbound_resource_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "outbound_resource_status": "sent",
                "outbound_resource_type": "Message",
                "outbound_resource_url": null,
                "sid": "KIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "type": "message",
                "url": "https://proxy.twilio.com/v1/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/MessageInteractions/KIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "session_sid": "KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.proxy.v1.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .sessions(sid="KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .participants(sid="KPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .message_interactions(sid="KIXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.proxy.v1.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .sessions(sid="KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .participants(sid="KPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .message_interactions.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://proxy.twilio.com/v1/Services/KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Sessions/KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Participants/KPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/MessageInteractions',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "interactions": [],
                "meta": {
                    "previous_page_url": null,
                    "next_page_url": null,
                    "url": "https://proxy.twilio.com/v1/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/MessageInteractions?PageSize=50&Page=0",
                    "page": 0,
                    "first_page_url": "https://proxy.twilio.com/v1/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/KPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/MessageInteractions?PageSize=50&Page=0",
                    "page_size": 50,
                    "key": "interactions"
                }
            }
            '''
        ))

        actual = self.client.proxy.v1.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .sessions(sid="KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .participants(sid="KPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .message_interactions.list()

        self.assertIsNotNone(actual)
