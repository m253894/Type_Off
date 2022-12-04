import pygame
import sys
import game
import operations
key = []


def keydown():
    # make a blank key list
    key = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                key.append('a')
            if event.key == pygame.K_b:
                key.append('b')
            if event.key == pygame.K_c:
                key.append('c')
            if event.key == pygame.K_d:
                key.append('d')
            if event.key == pygame.K_e:
                key.append('e')
            if event.key == pygame.K_f:
                key.append('f')
            if event.key == pygame.K_g:
                key.append('g')
            if event.key == pygame.K_h:
                key.append('h')
            if event.key == pygame.K_i:
                key.append('i')
            if event.key == pygame.K_j:
                key.append('j')
            if event.key == pygame.K_k:
                key.append('k')
            if event.key == pygame.K_l:
                key.append('l')
            if event.key == pygame.K_m:
                key.append('m')
            if event.key == pygame.K_n:
                key.append('n')
            if event.key == pygame.K_o:
                key.append('o')
            if event.key == pygame.K_p:
                key.append('p')
            if event.key == pygame.K_q:
                key.append('q')
            if event.key == pygame.K_r:
                key.append('r')
            if event.key == pygame.K_s:
                key.append('s')
            if event.key == pygame.K_t:
                key.append('t')
            if event.key == pygame.K_u:
                key.append('u')
            if event.key == pygame.K_v:
                key.append('v')
            if event.key == pygame.K_w:
                key.append('w')
            if event.key == pygame.K_x:
                key.append('x')
            if event.key == pygame.K_y:
                key.append('y')
            if event.key == pygame.K_z:
                key.append('z')
    return key
