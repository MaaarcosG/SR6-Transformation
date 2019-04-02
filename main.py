from bitmap import *
from obj import *
# Universidad del Valle de Guatemala
# Grafica por Computadora
# Nombre: Marcos Gutierrez
# Carne: 17909

def reyBoo():
	renderizando = Bitmap(1000,1000)
	glViewPort(0,0,800,800)
	#renderizando.renderer(./modelos/test3.obj, scale=(0,0,0), translate=(0,0,0))
	#renderizando.texture_render('./modelos/reyBoo.obj',(200,200,200),(3,3,3))
	#renderizando.renderer('./modelos/reyBoo.obj',(200,200,200),(3,3,3))
	renderizando.loadMatriz('./modelos/reyBoo.obj', scale=(0.03,0.03,0.03), rotate=(0.4,-0.4,0), translate=(0,0,0))
	renderizando.archivo('RENDERER.bmp')

print("Renderizando los modelos obj")

print("Renderizando Modelo de blender")
print(reyBoo())
