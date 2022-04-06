import os
import random
import time

from PIL import Image
from psychopy import core
from screeninfo import get_monitors

from task_template import TaskTemplate


def size(no_trial, j):
    image = Image.open(f'img/img_{no_trial}_{j}.png')
    imgwidth, imgheight = image.size

    if imgwidth > get_monitors()[0].width:
        while imgwidth > get_monitors()[0].width:
            imgwidth = imgwidth * 0.9
            imgheight = imgheight * 0.9
    if imgheight > get_monitors()[0].height:
        while imgheight > get_monitors()[0].height:
            imgwidth = imgwidth * 0.9
            imgheight = imgheight * 0.9

    return imgwidth, imgheight


def get_nb_diff(no_trial):
    return len([filename for filename in os.listdir('img/diff') if filename.startswith(f"img_{no_trial}")]) - 1


class Symetry(TaskTemplate):
    trials = 30  # A CHANGER
    yes_key_name = "p"
    yes_key_code = "p"
    no_key_code = "a"
    no_key_name = "a"
    quit_code = "q"
    keys = ["space", yes_key_name, no_key_name, quit_code]

    next = f"Pour passer à l'instruction suivante, appuyez sur la touche {yes_key_name}"

    instructions = [
        f"Dans cette tâche cognitive, appuyez sur la touche '{yes_key_name}' pour répondre oui ou pour selectionner la réponse "
        f"de droite. \n\n Appuyez sur la touche '{no_key_name}' pour répondre non ou pour selectionner la réponse de "
        f"gauche."]

    csv_headers = ['id_candidate', 'no_trial', 'num_subtrial', 'ans_candidate',
                   'good_ans', 'correct', 'reaction_time', 'time_stamp']

    def task(self, no_trial, exp_start_timestamp, trial_start_timestamp, practice=False, count_image=1):

        index_list = [0, 1, 2, 3, 4]
        while True:
            j = index_list.pop(index_list.index(random.choice(index_list)))
            self.create_visual_image(image=f'img/img_{no_trial}_{j}.png', size=size(no_trial, j)).draw()
            self.win.flip()
            core.wait(2)
            self.create_visual_text("Les deux barres sont-elles parallèles ? \n\n Non / Oui").draw()
            self.win.flip()
            resp, rt = self.get_response_with_time()
            good_ans = ['p' if j != 4 else 'a'][0]
            self.update_csv(self.participant, no_trial, j, resp, good_ans, resp == good_ans, round(rt, 2),
                            round(time.time() - exp_start_timestamp, 2))
            if len(index_list) == 0:
                break


exp = Symetry(csv_folder="csv")
exp.start()
