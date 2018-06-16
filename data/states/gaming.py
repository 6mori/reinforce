import pygame as pg
from pygame.sprite import Group


from .. import tools
from .. import constants as c
from .. components import brick
from .. components import props
from .. components import Darling
from .. components import guan_gong
from .. components import k
from .. components import Archer
from .. components import spider_prince
from .. components import poena

class Gaming(tools._State):
    def __init__(self):
        super(Gaming, self).__init__()


    def startup(self, current_time, persist):
        self.game_info = persist
        self.persist = self.game_info
        self.game_info[c.CURRENT_TIME] = current_time
        self.next = c.GAME_OVER

        self.setup_bricks()
        self.setup_characters()
        #self.setup_killing_items()
        self.setup_action_group()
        #self.setup_spritegroups()

        self.setup_props()
        self.setup_splines()
        self.setup_MPsphere()

    def setup_MPsphere(self):
        self.MPgroup1MAX = Group()
        self.MPgroup2MAX = Group()
        for i in range(0, 6):
            c.P1MPPOS = (c.P1MPPOS[0] + 20, c.P1MPPOS[1])
            self.MPgroup1MAX.add(props.MPsphere(c.P1MPPOS[0], c.P1MPPOS[1]))
        for i in range(0, 6):
            c.P2MPPOS = (c.P2MPPOS[0] + 20, c.P2MPPOS[1])
            self.MPgroup2MAX.add(props.MPsphere(c.P2MPPOS[0], c.P2MPPOS[1]))

    def setup_splines(self):
        self.MaxHP = []
        for character in self.characters_group.sprites():
            self.MaxHP.append(character.HP)
        self.HPSplinesSpace = Group()
        self.HPSplinesSpace.add(props.Spline_Space(0, 0, 6))
        self.HPSplinesSpace.add(props.Spline_Space(650, 0, 6))
        self.HPSplines = Group()
        self.HPSplines.add(props.Spline(0, 0, self.MaxHP[0], 6))
        self.HPSplines.add(props.Spline(650, 0, self.MaxHP[1], 6))

    def setup_props(self):
        self.props_group = Group()
        self.create_prop(self.props_group, 2, 1, 'Prop_MP_potion')
        self.create_prop(self.props_group, 3, 1, 'Prop_HP_potion')
        # self.create_prop(self.props_group, 4, 1, 'Prop_HP_Apple')
        # self.create_prop(self.props_group, 2, 2, 'Prop_HP_Ginseng')


    def create_prop(self, props_group, row, col,prop_kind):
        x = row * c.BRICK_WIDTH
        y = col * c.BRICK_HEIGHT
        props_group.add(props.Prop(x, y, prop_kind))


    def setup_bricks(self):
        map = "images/map.txt"
        self.bricks_group = Group()
        with open(map) as file_object:
            lines=file_object.readlines()
            for line in lines:
                line=line.strip().split(',')
                self.create_bricks(self.bricks_group,int(line[0]),int(line[1]),int(line[2]),int(line[3]),eval(line[4]))


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
                c.ARCHER: Archer.Archer(),
                c.SPIDER_PRINCE:spider_prince.Spider_prince(),
                c.POENA:poena.Poena()
            },
            {
                c.DARLING: Darling.Darling(),
                c.GUAN_GONG: guan_gong.Guan_gong(),
                c.K: k.K(),
                c.ARCHER: Archer.Archer(),
                c.SPIDER_PRINCE: spider_prince.Spider_prince(),
                c.POENA: poena.Poena()
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


    def setup_action_group(self):
        self.action_group = Group()


    def setup_killing_items(self):
        self.setup_bullets()
        self.setup_swords()

        action_group = {
            c.DARLING: self.bullets_group,
            c.GUAN_GONG: self.swords_group,
            c.K: self.swords_group,
            c.ARCHER: self.bullets_group,
            c.SPIDER_PRINCE:self.bullets_group,
            c.POENA:self.bullets_group
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
        self.blit_everything(surface)
        self.handle_state(keys)
        self.check_if_finish()

    def handle_state(self, keys):
        self.update_all_sprites(keys)

    def update_all_sprites(self, keys):
        for character in self.characters_group.sprites():
            character.update(keys, tools.keybinding[character.player_num],
                             self.game_info, self.action_group)
        self.adjust_sprite_positions()
        self.action_group.update()
        self.props_group.update()

    def adjust_sprite_positions(self):
        self.adjust_characters_position()
        #self.adjust_bullets_position()
        self.adjust_action_item_position()
        self.adjust_props_position()
        #self.check_swords_collisions()

    def adjust_characters_position(self):
        for character in self.characters_group.sprites():
            character.rect.x += round(character.x_vel)
            self.check_character_x_edge(character)
            self.check_character_x_collisions(character)

            character.rect.y += round(character.y_vel)
            self.check_character_y_collisions(character)
            self.check_collider_under_bottom(character)

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

        self.check_if_collider_is_falling(character)

    def adjust_character_for_y_collisions(self, character, collider):
        if character.rect.y < collider.rect.y:
            character.rect.bottom = collider.rect.top
            character.state = c.WALKING
        else:
            character.rect.top = collider.rect.bottom

        character.y_vel = 0

    def check_collider_under_bottom(self, collider):
        if collider.rect.top >= c.SCREEN_HEIGHT:
            collider.kill()

    def check_if_collider_is_falling(self, collider):
        collider.rect.y += 1
        test_collide_group = pg.sprite.Group(self.bricks_group)

        if pg.sprite.spritecollideany(collider, test_collide_group) is None:
            if collider.state != c.JUMPING and collider.state != c.SKILLING:        #飞起来
                collider.state = c.FALLING

        collider.rect.y -= 1


    def adjust_action_item_position(self):
        for action_item in self.action_group.sprites():
            if action_item.type == c.BULLET:
                self.adjust_bullet_position(action_item)
            elif action_item.type == c.SWORD:
                self.check_sword_collisions(action_item)


    def adjust_bullet_position(self, bullet):
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
                    character.kill()
                bullet.kill()

        if brick:
            brick.HP -= bullet.damage
            if brick.HP <= 0:
                brick.kill()
            bullet.kill()

    def adjust_props_position(self):
        for prop in self.props_group:
            self.check_and_adjust_prop_for_y_collisions(prop)
            self.check_collider_under_bottom(prop)
            self.check_if_collider_is_falling(prop)

    def check_and_adjust_prop_for_y_collisions(self, prop):
        brick = pg.sprite.spritecollideany(prop, self.bricks_group)
        if brick:
            prop.state = c.STANDING
            prop.rect.bottom = brick.rect.top

    def check_sword_collisions(self, sword):
        bricks = pg.sprite.spritecollide(sword, self.bricks_group, False)
        action_items = pg.sprite.spritecollide(sword, self.action_group, True)
        characters = pg.sprite.spritecollide(sword, self.characters_group, False)

        if bricks:
            self.apply_swords_damage(sword, bricks)

        #if bullets:
        #    self.apply_swords_damage(bullets)

        if characters:
            self.apply_swords_damage(sword, characters)


    def apply_swords_damage(self, sword, coll_dict):
        for collider in coll_dict:
            collider.HP -= sword.damage
            if collider.HP <= 0:
                collider.kill()


    def blit_everything(self, surface):
        surface.fill(c.BG_COLOR)
        for character in self.characters_group.sprites():
            surface.blit(character.image, character.rect)
        for brick in self.bricks_group.sprites():
            surface.blit(brick.image, brick.rect)
        for action_item in self.action_group.sprites():
            if action_item.type == c.BULLET:
                surface.blit(action_item.image, action_item.rect)
        for prop_item in self.props_group.sprites():
            surface.blit(prop_item.image, prop_item.rect)
        # MP
        self.PlayerMP = []
        for character in self.characters_group.sprites():
            self.PlayerMP.append(character.MP)
        i = 0
        for mpsphere in self.MPgroup1MAX.sprites():
            if i == self.PlayerMP[0]:
                break
            else:
                surface.blit(mpsphere.image, mpsphere.rect)
                i = i + 1
        i = 0
        for mpsphere in self.MPgroup2MAX.sprites():
            if i == self.PlayerMP[1]:
                break
            else:
                surface.blit(mpsphere.image, mpsphere.rect)
                i = i + 1
        # HP
        for spline_space_item in self.HPSplinesSpace.sprites():
            surface.blit(spline_space_item.image, spline_space_item.rect)
        self.PlayerHP = []
        for character in self.characters_group.sprites():
            self.PlayerHP.append(character.HP)
        i = 0
        for spline_item in self.HPSplines.sprites():
            try:
                spline_item.scale_change(self.PlayerHP[i])
                i = (i + 1) % 2
                surface.blit(spline_item.image, spline_item.rect)
            except:
                pass

    def check_if_finish(self):
        if len(self.characters_group) < 2:
            for character in self.characters_group.sprites():
                if character.player_num == 0:
                    self.game_info[c.P1_HP] = character.HP
                else:
                    self.game_info[c.P2_HP] = character.HP
            self.done = True