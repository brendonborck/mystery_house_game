import pygame

pygame.init()
scr = pygame.display.set_mode((700,600))
pygame.display.set_caption("Escapes")
font = pygame.font.SysFont("impact", 80)
text = font.render("Can you escape?", True, (255, 255, 255))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    scr.fill((0,0,0))
    scr.blit(text, (int(350 - text.get_width()/2), int(270 - text.get_height()/2)))
    pygame.display.flip()
