# game.py
import pygame


class Game:
    def __init__(self):
        pygame.init()

        self.WIDTH = 900
        self.HEIGHT = 600

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Kniffel")

        self.font = pygame.font.SysFont("Arial", 26)
        self.small_font = pygame.font.SysFont("Arial", 18)

        self.WHITE = (245, 245, 245)
        self.BLACK = (20, 20, 20)
        self.GRAY = (210, 210, 210)
        self.DARK_GRAY = (80, 80, 80)
        self.GREEN = (30, 120, 60)
        self.BLUE = (80, 160, 255)

        self.roll_count = 1
        self.max_rolls = 3

        self.rules = [
            "Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser",
            "Dreierpasch", "Viererpasch", "Full House", "Kleine Straße",
            "Große Straße", "Kniffel", "Chance"
        ]

    def draw_dices(self, pDiceValues):
        dice_size = 70
        spacing = 20
        start_x = 390
        dice_y = 180

        for i in range(5):
            dice_rect = pygame.Rect(
                start_x + i * (dice_size + spacing),
                dice_y,
                dice_size,
                dice_size
            )

            pygame.draw.rect(self.screen, self.DARK_GRAY, dice_rect, border_radius=10)
            pygame.draw.rect(self.screen, self.BLACK, dice_rect, 3, border_radius=10)

            value = str(pDiceValues[i])
            text_surface = self.font.render(value, True, self.WHITE)
            text_rect = text_surface.get_rect(center=dice_rect.center)

            self.screen.blit(text_surface, text_rect)

    def build_field(self, pCup):
        rule_text = ""
        keep_text = ""

        active_rule = False
        active_keep = False

        running = True

        while running:
            rule_input_rect = pygame.Rect(390, 350, 250, 35)
            keep_input_rect = pygame.Rect(390, 450, 250, 35)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if rule_input_rect.collidepoint(event.pos):
                        active_rule = True
                        active_keep = False
                    elif keep_input_rect.collidepoint(event.pos):
                        active_keep = True
                        active_rule = False
                    else:
                        active_rule = False
                        active_keep = False

                if event.type == pygame.KEYDOWN:
                    if active_rule:
                        if event.key == pygame.K_BACKSPACE:
                            rule_text = rule_text[:-1]

                        elif event.key == pygame.K_RETURN:
                            print("Regel:", rule_text)

                            # später hier Regel berechnen / Punkte speichern
                            # danach neue Runde starten
                            self.roll_count = 1
                            pCup.throw_all()

                            rule_text = ""

                        else:
                            rule_text += event.unicode.upper()

                    elif active_keep:
                        if event.key == pygame.K_BACKSPACE:
                            keep_text = keep_text[:-1]

                        elif event.key == pygame.K_RETURN:
                            if self.roll_count < self.max_rolls:
                                if keep_text != "":
                                    dices_to_keep = [
                                        int(x.strip())
                                        for x in keep_text.split(",")
                                    ]

                                    pCup.change_dices(dices_to_keep)
                                    self.roll_count += 1

                                keep_text = ""
                            else:
                                print("Du hast bereits 3x gewürfelt.")
                                keep_text = ""

                        else:
                            keep_text += event.unicode

            self.screen.fill(self.GREEN)

            pygame.draw.line(
                self.screen,
                self.BLACK,
                (320, 0),
                (320, self.HEIGHT),
                3
            )

            title = self.font.render("Regeln", True, self.WHITE)
            self.screen.blit(title, (40, 20))

            y = 70

            for rule in self.rules:
                rule_rect = pygame.Rect(40, y, 220, 28)

                pygame.draw.rect(self.screen, self.GRAY, rule_rect, border_radius=5)
                pygame.draw.rect(self.screen, self.BLACK, rule_rect, 2, border_radius=5)

                text = self.small_font.render(rule, True, self.BLACK)
                self.screen.blit(text, (50, y + 5))

                y += 35

            dice_title = self.font.render("Würfel", True, self.WHITE)
            self.screen.blit(dice_title, (500, 60))

            dice_values = pCup.get_values()
            self.draw_dices(dice_values)

            roll_info = self.small_font.render(
                f"Wurf: {self.roll_count} / {self.max_rolls}",
                True,
                self.WHITE
            )
            self.screen.blit(roll_info, (390, 270))

            rule_input_label = self.small_font.render(
                "Kürzel eingeben (z.B. FH):",
                True,
                self.WHITE
            )
            self.screen.blit(rule_input_label, (390, 320))

            border_color_rule = self.BLUE if active_rule else self.BLACK

            pygame.draw.rect(self.screen, self.WHITE, rule_input_rect, border_radius=5)
            pygame.draw.rect(
                self.screen,
                border_color_rule,
                rule_input_rect,
                2,
                border_radius=5
            )

            rule_surface = self.small_font.render(rule_text, True, self.BLACK)
            self.screen.blit(rule_surface, (400, 357))

            keep_input_label = self.small_font.render(
                "Würfel behalten (z.B. 1,3,5):",
                True,
                self.WHITE
            )
            self.screen.blit(keep_input_label, (390, 420))

            border_color_keep = self.BLUE if active_keep else self.BLACK

            pygame.draw.rect(self.screen, self.WHITE, keep_input_rect, border_radius=5)
            pygame.draw.rect(
                self.screen,
                border_color_keep,
                keep_input_rect,
                2,
                border_radius=5
            )

            keep_surface = self.small_font.render(keep_text, True, self.BLACK)
            self.screen.blit(keep_surface, (400, 457))

            pygame.display.flip()

        pygame.quit()