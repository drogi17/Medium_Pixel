from PIL import Image
import pygame
import collections

print('made by @drogi17')




def get_arr(source_name):
    source = Image.open(source_name).convert('RGB')
    cost_d = collections.Counter(source.getdata())
    return cost_d.most_common()

def takeelement_1(elem):
    return elem[1]


arr = get_arr('image.jpg')
arr.sort(key=takeelement_1)

dil = int(input('Number of parts: '))




pygame.init()
 
sc = pygame.display.set_mode((400, dil*70+20))


dog_surf = pygame.image.load('image.jpg').convert()

height_1 = (400*dog_surf.get_height())//(dil*70+20)
scale = pygame.transform.scale(dog_surf, (400, height_1))#(dog_surf.get_width() // 2, dog_surf.get_height() // 2))

scale_rect = scale.get_rect(center=(200, 250))

sc.blit(scale, scale_rect)


sch = 0
ch0 = round(len(arr)/dil)-1
while sch <= dil-1:
    ch = round(len(arr)/dil)-1
    m1 = arr[ch0*sch + round(ch/2)-1][0]
    print(m1)
    pygame.draw.rect(sc, m1, (120, 20+sch*70, 150, 50))
    sch += 1


pygame.display.update()

while 1:
    pygame.time.delay(1000)
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()