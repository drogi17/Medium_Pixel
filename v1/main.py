from PIL import Image
import pygame

print('made by @drogi17')

def Selection(array):
    nomber = 0
    while nomber <= len(array)-1:
        z = nomber
        min = z
        while z <= len(array)-1:
            if array[z][1] < array[min][1]:
                min = z
            z += 1
        array[nomber], array[min] = array[min], array[nomber]
        nomber += 1
    return array



def gray_scale(source_name):
	cost_d = {}
	source = Image.open(source_name).convert('RGB')
	for x in range(source.size[0]):
		for y in range(source.size[1]):
			r, g, b = source.getpixel((x, y))
			if not str(r) + ';' + str(g) + ';' + str(b) in cost_d:
				cost_d[str(r) + ';' + str(g) + ';' + str(b)] = 1
			else:
				cost_d[str(r) + ';' + str(g) + ';' + str(b)] += 1
	return cost_d


pix_les = gray_scale('image.jpg')

arr = []
for pix in pix_les:
	arr.append([pix, pix_les[pix]])
pix_les = {}

arr = Selection(arr)

#print(arr)

dil = int(input('Number of parts: '))




pygame.init()
 
sc = pygame.display.set_mode((400, 500))
sch = 0
ch0 = round(len(arr)/dil)-1
while sch <= dil-1:
	ch = round(len(arr)/dil)-1
	m1 = arr[ch0*sch + round(ch/2)-1][0].split(';')
	print(m1)
	pygame.draw.rect(sc, (int(m1[0]), int(m1[1]), int(m1[2])), (20, 20+sch*70, 150, 50))
	sch += 1


pygame.display.update()

while 1:
    pygame.time.delay(1000)
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()