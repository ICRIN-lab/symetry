import os
import random
import time

from psychopy import core
from Template_Task_Psychopy.task_template import TaskTemplate


class Symetry(TaskTemplate):
    # IMPORTANT ! To MODIFY IF NEEDED
    nb_ans = 2
    response_pad = True  # has to be set on "True" on production.
    # END OF IMPORTANT
    trials = 30
    yes_key_name = "verte"
    yes_key_code = "6"
    no_key_code = "rouge"
    no_key_name = "0"
    quit_code = "3"
    keys = ["space", yes_key_code, no_key_code, quit_code]

    next = f"Pour passer à l'instruction suivante, appuyez sur la touche {yes_key_name}"

    instructions = [
        f"Dans cette expérience : \n\n - appuyez sur la touche '{yes_key_name}' pour répondre oui ou pour "
        f"selectionner la réponse de droite. \n\n - appuyez sur la touche '{no_key_name}' pour répondre non ou pour "
        f"selectionner la réponse de gauche.", "N'appuyez sur les touches que lorsqu'on vous le demande.",
        "Placez vos index sur les touches 'a' et 'p'."]

    csv_headers = ['id_candidate', 'no_trial', 'num_subtrial', 'ans_candidate',
                   'good_ans', 'correct', 'reaction_time', 'time_stamp']

    def task(self, no_trial, exp_start_timestamp, trial_start_timestamp, practice=False, count_image=1):

        index_list = [0, 1, 2, 3, 4]
        while True:
            j = index_list.pop(index_list.index(random.choice(index_list)))
            self.create_visual_image(image=f'img/img_{no_trial}_{j}.png',
                                     size=self.size(f'img_{no_trial}_{j}.png')).draw()
            self.win.flip()
            core.wait(2)
            self.create_visual_text("Les deux barres sont-elles parallèles ? \n\n Non / Oui").draw()
            self.win.flip()
            time_stamp = time.time() - exp_start_timestamp
            resp, rt = self.get_response_with_time(self.response_pad)
            good_ans = [self.yes_key_code if j != 4 else self.no_key_code][0]
            if self.response_pad:
                self.update_csv(self.participant, no_trial, j, resp, good_ans, resp == good_ans,
                                round(rt - time_stamp, 2), round(rt, 2))
            else:
                self.update_csv(self.participant, no_trial, j, resp, good_ans, resp == good_ans, round(rt, 2),
                                round(time.time() - exp_start_timestamp, 2))
            if len(index_list) == 0:
                break


exp = Symetry(csv_folder="csv")
exp.start()
