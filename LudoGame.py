# Author: Brittaney Nicole Davis (Nico)
# GitHub username: baedirin
# Date: 07/29/2022
# Description: A program that simulates the
#              board game Ludo, with classes to
#              represent the player and the game itself.
#              These two classes interact with one another,
#              and each contains methods which further simulate
#              both the actions of the player(s) (up to 4)
#              and the functionality of the board game
#              while in play.


class Player:
    """
    A class which represents the players of
    the Ludo board game, with one to four
    players, listed A through D. Included in
    this class are methods for tracking the
    player tokens and game spaces, as well as
    other methods to interact with the board.

    The private data members reflect the details
    of a player and their tokens, including number,
    current position, start and end space.

    This class will
    communicate with the LudoGame class, in order
    to access the game playing methods for each
    player.
    """

    def __init__(self, position):

        self._current_position_p = "H"
        self._current_position_q = "H"
        self._current_state = "Ongoing"
        self._completed = False
        self._token_p_step_count = -1
        self._token_q_step_count = -1
        self._stacked_tokens = False
        self._token_name = ["p", "q"]
        self._position = position
        if position == "A":
            self._start_space = 1
            self._end_space = 50
        if position == "B":
            self._start_space = 15
            self._end_space = 8
        if position == "C":
            self._start_space = 29
            self._end_space = 22
        if position == "D":
            self._start_space = 43
            self._end_space = 36
        else:
            self._position = position

    def get_position(self):
        """
        A method that takes no parameters and
        returns the position of the player,
        which can be A, B, C or D
        """

        return self._position

    def get_start_space(self):
        """
        A method that takes no parameters and
        returns the start space of a token
        depending upon the player
        """

        return self._start_space

    def get_current_state(self):
        """
        A method that takes no parameters and
        returns the current state of the
        player
        """

        return self._current_state

    def get_token_name(self):
        """
        A method that takes no parameters and
        returns the name of a token, p or q
        """

        return self._token_name

    def get_token_p_step_count(self):
        """
        A method that takes no parameters,
        and returns the total steps that token
        p has taken on the board
        """

        return self._token_p_step_count

    def get_token_q_step_count(self):
        """
        A method that takes no parameters, and
        returns the total steps that token
        q has taken on the board
        """

        return self._token_q_step_count

    def get_current_position_p(self):
        """
        A method that takes no parameters and
        returns the current position of the
        player's p token
        """

        return self._current_position_p

    def get_current_position_q(self):
        """
        A method that takes no parameters and
        returns the current position of the
        player's q token
        """

        return self._current_position_q

    def get_stacked(self):
        """
        A method that takes no parameters and
        returns whether a token is stacked
        or not
        """

        return self._stacked_tokens

    def get_completed(self):
        """
        A method that takes no parameters, and returns
        whether the player has finished the game
        or not as True or False
        """

        return self._completed

    def get_space_name(self, total_token_steps):
        """
        A method that takes as a parameter the
        total steps taken by the token, and returns
        the name of the space that the token has landed
        on the board as a string. It will also return
        the home yard position "H" and the ready to
        go position "R"
        """

        if total_token_steps == -1:
            return "H"
        if total_token_steps == 0:
            return "R"
        if total_token_steps == 57:
            return "E"

        # Player A Squares
        if self._position == "A":
            if 0 < total_token_steps <= 50:
                return str(total_token_steps)
            else:
                # Player A Home Squares
                if total_token_steps > 50:
                    if total_token_steps == 51:
                        return "A1"
                    if total_token_steps == 52:
                        return "A2"
                    if total_token_steps == 53:
                        return "A3"
                    if total_token_steps == 54:
                        return "A4"
                    if total_token_steps == 55:
                        return "A5"
                    if total_token_steps == 56:
                        return "A6"
                    elif total_token_steps == 57:
                        return "E"

        # Player B Squares
        if self._position == "B":
            if 0 < total_token_steps <= 50:
                player_b_steps = total_token_steps + 14
                if player_b_steps <= 56:
                    return str(player_b_steps)
                else:
                    player_b_steps = player_b_steps - 56
                    return str(player_b_steps)
            else:
                # Player B Home Squares
                if total_token_steps > 50:
                    if total_token_steps == 51:
                        return "B1"
                    if total_token_steps == 52:
                        return "B2"
                    if total_token_steps == 53:
                        return "B3"
                    if total_token_steps == 54:
                        return "B4"
                    if total_token_steps == 55:
                        return "B5"
                    if total_token_steps == 56:
                        return "B6"
                    elif total_token_steps == 57:
                        return "E"

        # Player C Squares
        if self._position == "C":
            if 0 < total_token_steps <= 50:
                player_c_steps = total_token_steps + 28
                if player_c_steps <= 56:
                    return str(player_c_steps)
                else:
                    player_c_steps = player_c_steps - 56
                    return str(player_c_steps)

            else:
                # Player C Home Squares
                if total_token_steps > 50:
                    if total_token_steps == 51:
                        return "C1"
                    if total_token_steps == 52:
                        return "C2"
                    if total_token_steps == 53:
                        return "C3"
                    if total_token_steps == 54:
                        return "C4"
                    if total_token_steps == 55:
                        return "C5"
                    if total_token_steps == 56:
                        return "C6"
                    elif total_token_steps == 57:
                        return "E"

        # Player D Squares
        if self._position == "D":
            if 0 < total_token_steps <= 50:
                player_d_steps = total_token_steps + 42
                if player_d_steps <= 56:
                    return str(player_d_steps)
                else:
                    player_d_steps = player_d_steps - 56
                    return str(player_d_steps)

            else:
                # Player D Home Squares
                if total_token_steps > 50:
                    if total_token_steps == 51:
                        return "D1"
                    if total_token_steps == 52:
                        return "D2"
                    if total_token_steps == 53:
                        return "D3"
                    if total_token_steps == 54:
                        return "D4"
                    if total_token_steps == 55:
                        return "D5"
                    if total_token_steps == 56:
                        return "D6"
                    elif total_token_steps == 57:
                        return "E"

    def set_p_token_steps(self, total_token_p_steps):
        """
        A method that takes one parameter,
        the updated total token p steps
        and resets them
        """

        self._token_p_step_count = total_token_p_steps

    def set_q_token_steps(self, total_token_q_steps):
        """
        A method that takes one parameter,
        the updated total token q steps
        and resets them
        """

        self._token_q_step_count = total_token_q_steps

    def set_current_position_p(self, new_position_p):
        """
        A method that takes one parameter,
        which is a new token p position and
        sets the new position of the player's
        token p
        """

        self._current_position_p = new_position_p

    def set_current_position_q(self, new_position_q):
        """
        A method that takes one parameter,
        which is a new token q position and
        sets the new position of the player's
        token q
        """

        self._current_position_q = new_position_q

    def set_current_state(self, updated_game_state):
        """
        A method that takes one parameter,
        which is a new game state, and
        sets the game state to reflect the
        status of the player
        """

        self._current_state = updated_game_state

    def set_stacked(self, stacked_boolean):
        """
        A method that takes one parameter, a
        boolean, and sets the stacked
        token data member to True or False,
        depending upon whether two tokens
        of the same player share the same
        space
        """

        self._stacked_tokens = stacked_boolean

    def set_completed(self, completed_boolean):
        """
        A method that takes one parameter, a
        boolean, and sets the completed data
        member to True or False, depending upon
        whether the game is finished
        """

        if self._current_position_p == "E" and self._current_position_q == "E":
            self._completed = completed_boolean
        else:
            return False


class LudoGame:
    """
    A class representing the game of
    Ludo in action, which contains
    information about the players and board
    as well as methods for playing the game,
    obtaining player information, and interacting
    with player tokens. This class will
    interact with the Player class.
    """

    def __init__(self):

        self._players_list = []
        self._turns_list = []

    def add_player(self, player_object):
        """
        A method that takes a player object as
        a parameter and adds it to the players_list
        dictionary
        """

        self._players_list.append(player_object)

    def get_player_by_position(self, position):
        """
        A method which takes one parameter,
        a string representing the player's
        position. If the string is an
        invalid parameter, the method will
        return "Player not found!"
        """

        for player in self._players_list:
            if position == player.get_position():
                return player
        return "Player not found!"

    def move_token(self, player_object, token_name, token_steps):
        """
        A method that takes three parameters:
        player object, token name (p or q),
        and token steps (the amount the token
        will move on the board, which will
        be an integer)
        """

        has_moved = False

        # Priority Rule 1
        if token_steps == 6:

            if player_object.get_current_position_p() == "H" and player_object.get_token_p_step_count() == -1 \
                    and has_moved is False:
                player_object.set_current_position_p("R")
                player_object.set_p_token_steps(0)
                has_moved = True

            elif player_object.get_current_position_q() == "H" and player_object.get_token_q_step_count() == -1 \
                    and has_moved is False:
                player_object.set_current_position_q("R")
                player_object.set_q_token_steps(0)
                has_moved = True

        # Priority Rule #2
        if player_object.get_token_p_step_count() + token_steps == 57 and has_moved is False:
            player_object.set_p_token_steps(57)
            player_object.set_current_position_p("E")
            has_moved = True

        if player_object.get_token_q_step_count() + token_steps == 57 and has_moved is False:
            player_object.set_q_token_steps(57)
            player_object.set_current_position_q("E")
            has_moved = True

        if player_object.get_token_p_step_count() == 57 and \
                player_object.get_token_q_step_count() == 57 and has_moved is False:
            player_object.set_current_position_p("E")
            player_object.set_current_position_q("E")
            has_moved = True
            player_object.set_current_state("Finished")

        # Priority Rule 3
        for player in self._players_list:

            if player_object == player:
                pass
            else:
                if player_object.get_token_q_step_count() > 0:
                    if player_object.get_space_name(player_object.get_token_q_step_count() + token_steps) == \
                            player.get_space_name(player.get_token_q_step_count()):
                        if not has_moved:
                            player_object.set_q_token_steps(player_object.get_token_q_step_count() + token_steps)
                            has_moved = True
                        player.set_q_token_steps(0)
                        player.set_stacked(False)
                        player.set_current_position_q("H")

                    if player_object.get_space_name(player_object.get_token_q_step_count() + token_steps) == \
                            player.get_space_name(player.get_token_p_step_count()):
                        if not has_moved:
                            player_object.set_q_token_steps(player_object.get_token_q_step_count() + token_steps)
                            has_moved = True
                        player.set_p_token_steps(0)
                        player.set_stacked(False)
                        player.set_current_position_p("H")

                if player_object.get_token_p_step_count() > 0:
                    if player_object.get_space_name(player_object.get_token_p_step_count() + token_steps) == \
                            player.get_space_name(player.get_token_p_step_count()):
                        if not has_moved:
                            player_object.set_p_token_steps(player_object.get_token_p_step_count() + token_steps)
                            has_moved = True
                        player.set_p_token_steps(0)
                        player.set_stacked(False)
                        player.set_current_position_p("H")

                    if player_object.get_space_name(player_object.get_token_p_step_count() + token_steps) == \
                            player.get_space_name(player.get_token_q_step_count()):
                        if not has_moved:
                            player_object.set_p_token_steps(player_object.get_token_p_step_count() + token_steps)
                            has_moved = True
                        player.set_q_token_steps(0)
                        player.set_stacked(False)
                        player.set_current_position_q("H")

        # Priority Rule 4
        if player_object.get_token_p_step_count() == -1 and player_object.get_token_q_step_count() == -1:
            return

        if player_object.get_token_p_step_count() == 0 and player_object.get_token_q_step_count() == 0 \
                and has_moved is False:
            has_moved = True

        if player_object.get_token_p_step_count() >= 0 and player_object.get_token_q_step_count() == -1 \
                and has_moved is False:
            player_object.set_p_token_steps(player_object.get_token_p_step_count() + token_steps)
            has_moved = True

        if player_object.get_token_q_step_count() >= 0 and player_object.get_token_p_step_count() == -1 \
                and has_moved is False:
            player_object.set_q_token_steps(player_object.get_token_q_step_count() + token_steps)
            has_moved = True

        if player_object.get_token_p_step_count() == player_object.get_token_q_step_count() \
                and has_moved is False:
            player_object.set_p_token_steps(player_object.get_token_p_step_count() + token_steps)
            has_moved = True

        if player_object.get_token_p_step_count() > player_object.get_token_q_step_count() \
                and has_moved is False:
            player_object.set_q_token_steps(player_object.get_token_q_step_count() + token_steps)
            has_moved = True

        else:
            if player_object.get_token_p_step_count() < player_object.get_token_q_step_count() \
                    and has_moved is False:
                player_object.set_p_token_steps(player_object.get_token_p_step_count() + token_steps)
            has_moved = True

        # Bounce Back
        if player_object.get_token_p_step_count() > 50 or player_object.get_token_q_step_count() > 50:
            if player_object.get_token_p_step_count() > 57:
                total_steps = player_object.get_token_p_step_count()
                player_object.set_p_token_steps(57 - (total_steps - 57))

            if player_object.get_token_q_step_count() > 57:
                total_steps = player_object.get_token_q_step_count()
                player_object.set_q_token_steps(57 - (total_steps - 57))

        # Stacking tokens
        if player_object.get_token_p_step_count() != 0 and \
                player_object.get_token_q_step_count() != 0:
            if player_object.get_token_p_step_count() != -1 and \
                    player_object.get_token_q_step_count() != -1:
                if player_object.get_token_p_step_count() == player_object.get_token_q_step_count():
                    player_object.set_stacked(True)
                if player_object.get_token_q_step_count() == player_object.get_token_p_step_count():
                    player_object.set_stacked(True)

        # Already stacked
        if player_object.get_stacked():
            player_object.set_q_token_steps(player_object.get_token_p_step_count())

        # Player wins game
        if player_object.get_completed():
            player_object.set_current_state("Finished")

    def play_game(self, list_of_players_strings, turns_list):
        """
        A method that takes two parameters, the
        players list and the turns list. This method
        will create the player list first using the
        players list pass in, and then move the tokens
        according to the turns list following the
        priority rule and update the tokens position
        and the player’s game state (whether
        finished the game or not). After all the moving
        is done in the turns list, the method will
        return a list of strings representing the
        current spaces of all the tokens for each
        player in the list after moving the tokens
        following the rules described above
        """

        movement_list = []

        for player in list_of_players_strings:
            player_object = Player(player)
            self._players_list.append(player_object)

        for turns in turns_list:
            player_letter = turns[0]
            token_steps = turns[1]
            player_object = self.get_player_by_position(player_letter)
            token_name = self.priority_rule(token_steps, player_object)
            self.move_token(player_object, token_name, token_steps)

            movement_list = []

            for player_letter in self._players_list:
                movement_list.append(player_letter.get_space_name(player_letter.get_token_p_step_count()))
                movement_list.append(player_letter.get_space_name(player_letter.get_token_q_step_count()))
        return movement_list

    def priority_rule(self, die_roll, player_object):
        """
        A method that functions as a
        decision-making algorithm for a
        player to choose a certain token
        to move.
        """

        # Priority Rule 1
        if die_roll == 6:

            if player_object.get_current_position_p() == "H" and player_object.get_token_p_step_count() == -1:
                return "p"
            if player_object.get_current_position_q() == "H" and player_object.get_token_q_step_count() == -1:
                return "q"

        # Priority Rule #2
        if player_object.get_token_p_step_count() + die_roll == 57:
            return "p"
        if player_object.get_token_q_step_count() + die_roll == 57:
            return "q"
        if player_object.get_token_p_step_count() == 57 and player_object.get_token_q_step_count() == 57:
            player_object.set_current_state("Finished")

        # Priority Rule 3
        for player in self._players_list:

            if player_object.get_space_name(player_object.get_token_q_step_count() + die_roll) == \
                    player.get_space_name(player.get_token_q_step_count()):
                return "q"
            if player_object.get_space_name(player_object.get_token_p_step_count() + die_roll) == \
                    player.get_space_name(player.get_token_p_step_count()):
                return "p"
            if player_object.get_space_name(player_object.get_token_p_step_count() + die_roll) == \
                    player.get_space_name(player.get_token_q_step_count()):
                return "p"
            if player_object.get_space_name(player_object.get_token_q_step_count() + die_roll) == \
                    player.get_space_name(player.get_token_p_step_count()):
                return "q"

        # Priority Rule 4
        if player_object.get_token_p_step_count() == -1 and player_object.get_token_q_step_count() == -1:
            pass

        if player_object.get_token_p_step_count() >= 0 and player_object.get_token_q_step_count() == -1:
            return "q"

        if player_object.get_token_q_step_count() >= 0 and player_object.get_token_p_step_count() == -1:
            return "p"

        if player_object.get_token_p_step_count() > player_object.get_token_q_step_count():
            return "q"
        else:
            if player_object.get_token_p_step_count() < player_object.get_token_q_step_count():
                return "p"
