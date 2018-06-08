from . import bullet
import pygame as pg
class Skill_attack(bullet.Bullet):
    def __init__(self, owner, damage, direction, skill_style,owner_name):
        super().__init__(owner,damage,direction,skill_style)

        self.skill_style = skill_style
        self.owner_name = owner_name
        if self.skill_style == 'skull' and self.owner_name == 'Spider_prince':
            self.passed_distance = 0
            self.animation_speed = 8
            self.skill_size = (178//6,709//6)
            self.image = pg.transform.scale(pg.image.load('images/bullet/' + skill_style + '/0.png'), self.skill_size)
            self.rect = self.image.get_rect()
            self.frame_numbers = 6
            self.decay_distance = [40,80,120,160,200,300]
            self.decay_range = 1.2

    def update(self):
        super().update()
        if self.skill_style == 'skull' and self.owner_name == 'Spider_prince':
            self.passed_distance += abs(self.x_vel)
            for dis in self.decay_distance:
                if self.passed_distance == dis :
                    if dis == 300:
                        self.kill()
                    else:
                        tmp = self.rect.bottom
                        self.skill_size = (
                        int(self.skill_size[0] / self.decay_range), int(self.skill_size[1] / self.decay_range))
                        self.counter += 1
                        self.counter %= self.frame_numbers * self.animation_speed
                        self.image = pg.transform.scale(
                            pg.image.load(
                                'images/bullet/%s/%s.png' % (self.skill_style, self.counter // self.animation_speed)),
                            self.skill_size)
                        self.rect.size = self.skill_size
                        self.rect.bottom = tmp
            else:
                self.counter += 1
                self.counter %= self.frame_numbers * self.animation_speed
                self.image = pg.transform.scale(pg.image.load('images/bullet/%s/%s.png'%(self.skill_style, self.counter// self.animation_speed)), self.skill_size)