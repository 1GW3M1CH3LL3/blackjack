from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''
        output = run_test([11, 2, 5, 11], ['k', 'y', 'y'], [1, 11], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Jack\n" \
                   "Drew a 2\n" \
                   "You have 12. Hit (y/n)? k\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 12. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew a Jack\n" \
                   "Final hand: 27.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a Jack\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_and_dealer_push(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with equal hand value.
        They both push.
        '''
        output = run_test([12, 10], ['n'], [5, 1, 4], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 10\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew an Ace\n" \
                   "Dealer has 16.\n" \
                   "Drew a 4\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_blackjacks_and_wins_while_user_is_less_than_twentyone(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards and the dealer ends up with a handvalue equal to 21 while the user has a handvalue less than 21.
        Dealer wins by having blackjack.
        '''
        output = run_test([4, 1, 3], ['y', 'n'], [4, 7, 13], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew an Ace\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 7\n" \
                   "Dealer has 11.\n" \
                   "Drew a King\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins_when_user_busts(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards and the user ends up with handvalue greater  than 21.
        Dealer wins because user busts
        '''
        output = run_test([1,3, 6, 13], ['y', 'y'], [12, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 3\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "You have 20. Hit (y/n)? y\n" \
                   "Drew a King\n" \
                   "Final hand: 30.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 10\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins_when_both_bust(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards and end up with handvalue greater  than 21.
        Dealer wins because user busts
        '''
        output = run_test([10,13,  9], ['y'], [12, 5 , 8], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a King\n" \
                   "You have 20. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "Final hand: 29.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 5\n" \
                   "Dealer has 15.\n" \
                   "Drew an 8\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_blackjacks_while_user_busts(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards and the dealer has a hand of 21 while the user has a hand greater than 21.
        Dealer wins because of blackjack.
        '''
        output = run_test([11,13,  9], ['y'], [12, 5 , 8], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Jack\n" \
                   "Drew a King\n" \
                   "You have 20. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "Final hand: 29.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 5\n" \
                   "Dealer has 15.\n" \
                   "Drew an 8\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_when_dealer_busts(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards and the dealer has a hand greater than 21 while user has a hand less than 21.
        User wins because dealer busts.
        '''
        output = run_test([3,7], ['n'], [4, 2, 5, 5, 13], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 7\n" \
                   "You have 10. Hit (y/n)? n\n" \
                   "Final hand: 10.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 2\n" \
                   "Dealer has 6.\n" \
                   "Drew a 5\n" \
                   "Dealer has 11.\n" \
                   "Drew a 5\n" \
                   "Dealer has 16.\n" \
                   "Drew a King\n" \
                   "Final hand: 26.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_by_having_lower_handvalue(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards and have hand values less than 21 and the user has a hand greater than that of the  user
        User wins by having greater hand value than dealer.
        '''
        output = run_test([10, 12], ['n'], [10, 7], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a Queen\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 7\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)  

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_when_only_dealer_busts(self, input_mock, randint_mock):
        '''Both the dealer and user receive cards and dealer has a has a handvalue greater than 21 while the user does not.
        User wins because it has a hand value less than 21 and dealer busts.'''
        output = run_test([11, 8, 2], ['y', 'n'], [3, 13, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Jack\n" \
                   "Drew an 8\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a King\n" \
                   "Dealer has 13.\n" \
                   "Drew a 9\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_with_blackjack_while_dealer_busts(self, input_mock, randint_mock):
        '''Both the dealer and user receive cards and user has a has a handvalue equal to  21 while the dealer has a hand greater than 21.
        User wins because it has a hand value equal 21 and dealer busts.'''
        output = run_test([1, 10], [], [3, 13, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 10\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a King\n" \
                   "Dealer has 13.\n" \
                   "Drew a 9\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected) 
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_with_blackjack_while_user_has_a_hand_less_than_it(self, input_mock, randint_mock):
        '''Both the dealer and user receive cards and user has a has a handvalue equal to 21 while the dealer has a hand less than 21.
        User wins because it has a hand value equal to 21 and dealer has a hand less than 21.'''
        output = run_test([1, 5, 5], ['r', 'y' ], [1, 5, 4], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 5\n" \
                   "You have 16. Hit (y/n)? r\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 16. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 5\n" \
                   "Dealer has 16.\n" \
                   "Drew a 4\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)                                                   
    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()
