import pygame

pygame.init()

# Defining the border for the field
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kniffel")

font = pygame.font.SysFont("Arial", 26)
small_font = pygame.font.SysFont("Arial", 18)

#preDefining Colors
WHITE = (245, 245, 245)
BLACK = (20, 20, 20)
GRAY = (210, 210, 210)
DARK_GRAY = (80, 80, 80)
GREEN = (30, 120, 60)
BLUE = (80, 160, 255)

#preDefining the rules for the list
rules = [
    "Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser",
    "Dreierpasch", "Viererpasch", "Full House", "Kleine Straße",
    "Große Straße", "Kniffel", "Chance"
]

rule_text = ""
keep_text = ""

active_rule = False
active_keep = False

running = True

while running:
    # Eingabefelder müssen vor dem Event-Check existieren
    rule_input_rect = pygame.Rect(390, 350, 250, 35)
    keep_input_rect = pygame.Rect(390, 450, 250, 35)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            #wurde das Regelfeld geklickt => Feld wird auf aktiv geschalten
            if rule_input_rect.collidepoint(event.pos):
                active_rule = True
                active_keep = False
            #wurde das behaltenfeld geklickt => Feld wird auf aktiv geschalten
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
                    print("Regel-Kürzel:", rule_text)
                else:
                    rule_text += event.unicode.upper()

            elif active_keep:
                if event.key == pygame.K_BACKSPACE:
                    keep_text = keep_text[:-1]
                elif event.key == pygame.K_RETURN:
                    print("Behaltene Würfel:", keep_text)
                else:
                    keep_text += event.unicode

    screen.fill(GREEN)

    pygame.draw.line(screen, BLACK, (320, 0), (320, HEIGHT), 3)

    # Regeln links
    title = font.render("Regeln", True, WHITE)
    screen.blit(title, (40, 20))

    y = 70
    for rule in rules:
        rule_rect = pygame.Rect(40, y, 220, 28)
        pygame.draw.rect(screen, GRAY, rule_rect, border_radius=5)
        pygame.draw.rect(screen, BLACK, rule_rect, 2, border_radius=5)

        text = small_font.render(rule, True, BLACK)
        screen.blit(text, (50, y + 5))

        y += 35

    # Würfel rechts
    dice_title = font.render("Würfel", True, WHITE)
    screen.blit(dice_title, (500, 60))

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

        pygame.draw.rect(screen, DARK_GRAY, dice_rect, border_radius=10)
        pygame.draw.rect(screen, BLACK, dice_rect, 3, border_radius=10)

    # Eingabefeld 1: Regel-Kürzel
    rule_input_label = small_font.render(
        "Kürzel eingeben (z.B. FH):",
        True,
        WHITE
    )
    screen.blit(rule_input_label, (390, 320))

    border_color_rule = BLUE if active_rule else BLACK
    pygame.draw.rect(screen, WHITE, rule_input_rect, border_radius=5)
    pygame.draw.rect(screen, border_color_rule, rule_input_rect, 2, border_radius=5)

    rule_surface = small_font.render(rule_text, True, BLACK)
    screen.blit(rule_surface, (400, 357))

    # Eingabefeld 2: Würfel behalten
    keep_input_label = small_font.render(
        "Würfel behalten (z.B. 1,3,5):",
        True,
        WHITE
    )
    screen.blit(keep_input_label, (390, 420))

    border_color_keep = BLUE if active_keep else BLACK
    pygame.draw.rect(screen, WHITE, keep_input_rect, border_radius=5)
    pygame.draw.rect(screen, border_color_keep, keep_input_rect, 2, border_radius=5)

    keep_surface = small_font.render(keep_text, True, BLACK)
    screen.blit(keep_surface, (400, 457))

    pygame.display.flip()

pygame.quit()