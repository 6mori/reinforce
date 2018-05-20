import pygame as pg
from pygame.sprite import Group

import copy

from .. import tools, setup
from .. import constants as c
from .. components import brick
from .. components import props
from .. components import Darling
from .. components import guan_gong
from .. components import k


class Gaming(tools._State):
    def __init__(self):
        super(Gaming, self).__init__()

    #def get_event(self, event):

    def startup(self, current_time, persist):
        self.game_info = persist
        self.persist = self.game_info
        self.game_info[c.CURRENT_TIME] = current_time
        self.next = c.GAME_OVER

        self.setup_bricks()
        self.setup_characters()
        self.setup_killing_items()
        #self.setup_spritegroups()

        self.setup_props()

    def setup_props(self):
        self.props_group = Group()
        self.create_prop(self.props_group, 2, 1, 'red_prop')
        self.create_prop(self.props_group, 4, 4, 'blue_prop')


    def create_prop(self, props_group, row, col,prop_kind):
        x = row * c.BRICK_WIDTH
        y = col * c.BRICK_HEIGHT
        props_group.add(props.Prop(x, y, prop_kind))


    def setup_bricks(self):
        self.bricks_group = Group()
        self.create_bricks(self.bricks_group, 0, 10, 40, 1,'grass_surface')
        self.create_bricks(self.bricks_group, 18, 14, 2, 1,'grass_surface')
        self.create_bricks(self.bricks_group, 17, 0, 1, 7,'long_wood')
        self.create_bricks(self.bricks_group, 17, 11, 1, 4,'grass_soil')
        self.create_bricks(self.bricks_group, 10, 0, 3, 7,'long_wood')
        self.create_bricks(self.bricks_group, 0, 7, 7, 1,'grass_surface')
        self.create_bricks(self.bricks_group, 0, 8, 7, 1, 'grass_soil')
        self.create_bricks(self.bricks_group, 0, 9, 7, 1, 'grass_soil')
        self.create_bricks(self.bricks_group, 0, 10, 7, 1, 'grass_soil')


    def create_bricks(self, bricks, x, y, width, height, ground_kind):#ground_kind为表示什么砖块条的字符串
        for row in list(range(x, x+width)):
            for col in list(range(y, y+height)):
                if(row==x):
                    self.create_brick(bricks,row,col,tools.kindOfGround[ground_kind][0])
                elif(row==x+width-1):
                    self.create_brick(bricks, row, col, tools.kindOfGround[ground_kind][2])
                else:
                    self.create_brick(bricks, row, col, tools.kindOfGround[ground_kind][1])


    def create_brick(self, bricks, row, col,brick_kind):
        x = row * c.BRICK_WIDTH
        y = col * c.BRICK_HEIGHT
        bricks.add(brick.Brick(x, y, brick_kind))


    def setup_characters(self):
        characters = [
            {
                c.DARLING: Darling.Darling(),
                c.GUAN_GONG: guan_gong.Guan_gong(),
                c.K: k.K(),
            },
            {
                c.DARLING: Darling.Darling(),
                c.GUAN_GONG: guan_gong.Guan_gong(),
                c.K: k.K(),
            },
        ]

        player_1 = characters[0][self.game_info[c.P1_CHARACTER]]
        player_1.player_num = 0
        player_1.rect.x = 0
        player_1.rect.y = 0
        player_1.state = c.FALLING

        player_2 = characters[1][self.game_info[c.P2_CHARACTER]]
        player_2.player_num = 1
        player_2.rect.right = c.SCREEN_WIDTH
        player_2.rect.y = 0
        player_2.state = c.FALLING

        self.characters_group = Group(player_1, player_2)


    def setup_killing_items(self):
        self.setup_bullets()
        self.setup_swords()

        action_group = {
            c.DARLING: self.bullets_group,
            c.GUAN_GONG: self.swords_group,
            c.K: self.swords_group
        }

        self.killing_items = [
            action_group[self.game_info[c.P1_CHARACTER]],
            action_group[self.game_info[c.P2_CHARACTER]],
        ]


    def setup_bullets(self):
        self.bullets_group = Group()


    def setup_swords(self):
        self.swords_group = Group()


    def update(self, surface, keys, current_time):
        self.game_info[c.CURRENT_TIME] = self.current_time = current_time
        self.handle_state(keys)
        self.blit_everything(surface)


    def handle_state(self, keys):
        self.update_all_sprites(keys)


    def update_all_sprites(self, keys):
        for character in self.characters_group.sprites():
            character.update(keys, tools.keybinding[character.player_num],
                             self.game_info, self.killing_items[character.player_num])
        self.bullets_group.update()
        self.adjust_sprite_positions()


    def adjust_sprite_positions(self):
        self.adjust_characters_position()
        self.adjust_bullets_position()
        self.check_swords_collisions()


    def adjust_characters_position(self):
        for character in self.characters_group.sprites():
            character.rect.x += round(character.x_vel)
            self.check_character_x_edge(character)
            self.check_character_x_collisions(character)

            character.rect.y += round(character.y_vel)
            self.check_character_y_collisions(character)
            self.check_character_under_bottom(character)


    def check_character_x_edge(self, character):
        if character.rect.left < 0:
            character.rect.left = 0
        if character.rect.right > c.SCREEN_WIDTH:
            character.rect.right = c.SCREEN_WIDTH


    def check_character_x_collisions(self, character):
        brick = pg.sprite.spritecollideany(character, self.bricks_group)
        prop = pg.sprite.spritecollideany(character, self.props_group)

        if brick:
            self.adjust_character_for_x_collisions(character, brick)

        if prop:
            prop.ActOnCharacters(character)
            prop.kill()


    def adjust_character_for_x_collisions(self, character, collider):
        if character.rect.x < collider.rect.x:
            character.rect.right = collider.rect.left
        else:
            character.rect.left = collider.rect.right

        character.x_vel = 0


    def check_character_y_collisions(self, character):
        brick = pg.sprite.spritecollideany(character, self.bricks_group)
        prop = pg.sprite.spritecollideany(character, self.props_group)

        if brick:
            self.adjust_character_for_y_collisions(character, brick)

        if prop:
            prop.ActOnCharacters(character)
            prop.kill()

        self.check_if_character_is_falling(character)


    def adjust_character_for_y_collisions(self, character, collider):
        if character.rect.y < collider.rect.y:
            character.rect.bottom = collider.rect.top
            character.state = c.WALKING
        else:
            character.rect.top = collider.rect.bottom

        character.y_vel = 0


    def check_character_under_bottom(self, character):
        if character.rect.top >= c.SCREEN_HEIGHT:
            character.HP = 0
            self.set_result()


    def check_if_character_is_falling(self, character):
        character.rect.y += 1
        test_collide_group = pg.sprite.Group(self.bricks_group)

        if pg.sprite.spritecollideany(character, test_collide_group) is None:
                if character.state != c.JUMPING and character.state != c.SKILLING:        #飞起来
                    character.state = c.FALLING
        character.rect.y -= 1


    def adjust_bullets_position(self):
        for bullet in self.bullets_group:
            if bullet.rect.right < 0:
                bullet.kill()
            if bullet.rect.left > c.SCREEN_WIDTH:
                bullet.kill()
            if bullet.rect.bottom < 0:
                bullet.kill()
            self.check_bullet_x_collisions(bullet)


    def check_bullet_x_collisions(self, bullet):
        character = pg.sprite.spritecollideany(bullet, self.characters_group)
        brick = pg.sprite.spritecollideany(bullet, self.bricks_group)

        if character:
            if bullet.owner != character.player_num:
                character.HP -= bullet.damage
                if character.HP <= 0:
                    character.HP = 0
                    self.set_result()
                bullet.kill()

        if brick:
            brick.HP -= bullet.damage
            if brick.HP <= 0:
                brick.kill()
            bullet.kill()


    def check_swords_collisions(self):
        bricks = pg.sprite.groupcollide(self.swords_group, self.bricks_group, False, False)
        bullets = pg.sprite.groupcollide(self.swords_group, self.bullets_group, False, False)
        characters = pg.sprite.groupcollide(self.swords_group, self.characters_group, False, False)

        if bricks:
            self.apply_swords_damage(bricks)

        if bullets:
            self.apply_swords_damage(bullets)

        if characters:
            self.apply_swords_damage(characters)

        self.swords_group.empty()


    def apply_swords_damage(self, coll_dict):
        for sword in coll_dict.keys():
            for collider in coll_dict[sword][:]:
                collider.HP -= sword.damage
                if collider.HP <= 0:
                    collider.kill()


    def blit_everything(self, surface):
        surface.fill(c.BG_COLOR)
        for character in self.characters_group.sprites():
            surface.blit(character.image, character.rect)
        for brick in self.bricks_group.sprites():
            surface.blit(brick.image, brick.rect)
        for bullet in self.bullets_group.sprites():
            surface.blit(bullet.image, bullet.rect)
        for prop_item in self.props_group.sprites():
            surface.blit(prop_item.image, prop_item.rect)
        # For test
        #for sw in self.swords_group.sprites():
        #    pg.draw.rect(surface, sw.color, sw.rect)


    def set_result(self):
        for character in self.characters_group.sprites():
            if character.player_num == 0:
                self.game_info[c.P1_HP] = character.HP
            else:
                self.game_info[c.P2_HP] = character.HP
        self.done = True