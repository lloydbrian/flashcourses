"""
FlashCourses- Test cases for the deck model
Created By: Lloyd Dagoc  10/21/2018

Relative File Path:
/flash/src/flashcards/test_flashcards/test_flashcards_models.py
Modified Date:  10/21/2018
"""

from django.test import TestCase
from flashcards.models import Deck, Card
from accounts.models import User
from courses.models import Course


class ModelDeckCardTest(TestCase):

    """
    Tests API endpoint response status codes
    """

    def setUp(self):
        """
        Sets up test data for the deck model and run tests
        """
        user = User.objects.create_user(
            'Lloyd',
            'lloydbriantech@outlook.com',
            'imppwdswelloyd'
        )
        course_tbl = Course.objects.create(
            course_title='test',
            course_id='2',
            course_description='this is a test data'
        )

        deckA = Deck.objects.create(
            parent_user=user,
            title='Test DeckA',
            deck_description='This is a test DeckA'
        )
        deckB = Deck.objects.create(
            parent_user=user,
            title='Test DeckB',
            deck_description='This is a test DeckB'
        )
        cardA = Card.objects.create(
            parent_deck=deckA,
            front='testFrontA',
            back='testBackA'
        )
        cardB = Card.objects.create(
            parent_deck=deckA,
            front='testFrontB',
            back='testBackB'
        )
        card1 = Card.objects.create(
            parent_deck=deckB,
            front='testFront1',
            back='testBack1'
        )
        card2 = Card.objects.create(
            parent_deck=deckB,
            front='testFront1',
            back='testBack1'
        )

    def test_deck_string_value(self):
        """
        Test the owner of the deck
        """
        deck_objects = Deck.objects.all()
        for deck_item in deck_objects:
            deckLabel = deck_item.title
            deckLabel2 = deck_item.deck_description
            self.assertEqual(deckLabel, str(deck_item))
            self.assertNotEqual(deckLabel2, str(deck_item))

    def test_get_number_cards(self):
        """
        Test the number of cards in a deck
        """
        deck_objects = Deck.objects.all()
        for deck_item in deck_objects:
            deckLen = deck_item.card_set.count()
            self.assertEqual(deck_item.get_number_cards(), deckLen)

    def test_has_duplicates(self):
        """
        Test has_duplicates method
        """
        deck_objects = Deck.objects.all()
        for deck_item in deck_objects:
            cards = deck_item.card_set.all()
            for card in cards:
                qs = cards.filter(front=card.front)
                if qs.count() > 1:
                    self.assertTrue(deck_item.has_duplicates(card))
                else:
                    self.assertFalse(deck_item.has_duplicates(card))

    def test_is_owner(self):
        """
        Test the owner of the deck
        """
        deck_objects = Deck.objects.all()
        for deck_item in deck_objects:
            deckUser = deck_item.parent_user
            self.assertTrue(deck_item.is_owner(deckUser))

    def test_card_string_value(self):
        """
        Test the owner of the deck
        """
        card_objects = Card.objects.all()
        for card_item in card_objects:
            card_string_val = card_item.front + ' , ' + card_item.back
            self.assertEqual(card_string_val, str(card_item))
